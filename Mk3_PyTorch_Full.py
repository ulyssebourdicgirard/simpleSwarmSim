import time
import torch
import config
import concurrent.futures
import numpy as np

from config import NB_DRONES, ARENA_RADIUS, DT, SIM_STEPS, VISU_STEPS, POP_SIZE_GPU, GEN_GPU
from dynamics_pytorch import SwarmParams, TensorExplorationGrid, compute_derivatives, get_deterministic_initial_state, compute_metrics
from logger import ExperimentLogger
from visualization import generate_gif_from_log

# Hardware routing
devices = []
if torch.cuda.is_available():
    n_gpus = torch.cuda.device_count()
    print(f"[Hardware] Found {n_gpus} CUDA device(s).")
    devices = [torch.device(f"cuda:{i}") for i in range(n_gpus)]
elif torch.backends.mps.is_available():
    print("[Hardware] Using Apple MPS.")
    devices = [torch.device("mps")]
else:
    print("[Hardware] Using CPU.")
    devices = [torch.device("cpu")]
    
primary_device = devices[0]

def run_batch_pytorch(genes, device):
    # Frozen noise
    torch.manual_seed(42)
    
    n_batch = genes['y_att'].shape[0]
    n_envs = getattr(config, 'N_INIT_CONDITIONS', 4)
    total_envs = n_batch * n_envs
    
    pos, phi, v, vz = get_deterministic_initial_state(n_batch, NB_DRONES, device=device)
    
    expanded_genes = {}
    for k, val in genes.items():
        expanded_genes[k] = val.unsqueeze(1).expand(-1, n_envs, -1).reshape(total_envs, 1)
        
    params = SwarmParams(**expanded_genes)
    cost_total = torch.zeros(total_envs, device=device) 
    
    grid = None 
    if config.SCENARIO == "exploration":
        grid = TensorExplorationGrid(total_envs, NB_DRONES, config.ARENA_RADIUS, config.GRID_RES, device=device)
    
    eye_mask_batch = torch.eye(NB_DRONES, dtype=torch.bool, device=device).expand(total_envs, NB_DRONES, NB_DRONES)
    noise_buffer = torch.empty_like(phi)
    
    # Integration loop
    for t in range(SIM_STEPS):
        acc, phi_dot, vz_dot = compute_derivatives(
            pos, phi, v, params, vz=vz, grid=grid, 
            eye_mask=eye_mask_batch, noise_buffer=noise_buffer
        )
        
        v += acc * DT
        phi += phi_dot * DT
        pos[..., 0] += v * torch.cos(phi) * DT
        pos[..., 1] += v * torch.sin(phi) * DT
        
        if vz is not None and vz_dot is not None:
            vz += vz_dot * DT
            pos[..., 2] += vz * DT
            
        if grid:
            grid.update(pos)
            
            if t % getattr(config, 'REFRESH_MAP_TICKS', 50) == 0:
                grid.share_maps(pos, getattr(config, 'NEIGHBORS', 2)) # Sharing maps with neighbors
        
        # Post-transient metrics
        if t > 50:
            c_disp, c_effort, c_coll, c_pol, c_mill = compute_metrics(
                pos, phi, phi_dot, v, eye_mask = eye_mask_batch )
            cost_total += c_disp + c_effort + c_coll + c_pol + c_mill

            if grid:
                cost_total += grid.get_score() * config.W_EXPLO

    # --- MIN-MAX ---
    cost_total = cost_total.view(n_batch, n_envs)
    
    worst_costs, _ = torch.max(cost_total, dim=1) # keeping the worst costs to favor robustness

    final_covs = None
    if grid:
        covs = grid.get_coverage() 
        covs = covs.view(n_batch, n_envs)
        final_covs = torch.mean(covs, dim=1) # Average genome coverage
        
    return worst_costs, final_covs



def optimize_pytorch(devices):
    device = devices[0] # Master GPU
    
    mode_str = f"PyTorch_MULTI_{len(devices)}xGPU" if len(devices) > 1 else f"PyTorch_{device.type.upper()}"
    logger = ExperimentLogger(mode=mode_str)
    logger.log_config(config)
    
    print(f"--- PyTorch GA (Pop: {POP_SIZE_GPU}) | Devices: {[d.type + (str(d.index) if d.index is not None else '') for d in devices]} | Log: {logger.log_dir} ---")
    
    # Init pop
    genes = {
        'y_att':  torch.empty((POP_SIZE_GPU, 1), device=device).uniform_(0.001, 5.0),
        'd0_att': torch.empty((POP_SIZE_GPU, 1), device=device).uniform_(1.0, 8.0), # Augmenter distances pour permettre plus longue attraction
        'l_att':  torch.empty((POP_SIZE_GPU, 1), device=device).uniform_(1.0, 12.0), # l_att >>> d0_att
        'y_ali':  torch.empty((POP_SIZE_GPU, 1), device=device).uniform_(0.0, 4.0),
        'l_ali':  torch.empty((POP_SIZE_GPU, 1), device=device).uniform_(1.0, 5.0),
        'y_f':    torch.empty((POP_SIZE_GPU, 1), device=device).uniform_(0.001, 2.0), # Pas forcément variable
        'a_att':  torch.zeros((POP_SIZE_GPU, 1), device=device),
        'b1_att': torch.zeros((POP_SIZE_GPU, 1), device=device),
        'b2_att': torch.zeros((POP_SIZE_GPU, 1), device=device),
        'd0_ali': torch.empty((POP_SIZE_GPU, 1), device=device).uniform_(0.5, 3.0),
        'a_ali':  torch.zeros((POP_SIZE_GPU, 1), device=device),
        'b1_ali': torch.zeros((POP_SIZE_GPU, 1), device=device),
        'b2_ali': torch.zeros((POP_SIZE_GPU, 1), device=device),
        'target_altitude': torch.empty((POP_SIZE_GPU, 1), device=device).uniform_(config.Z_MIN + 1.0, config.Z_MAX - 1.0),
        'y_acc': torch.empty((POP_SIZE_GPU, 1), device=device).uniform_(0.001, 2.0),
        'l_acc': torch.empty((POP_SIZE_GPU, 1), device=device).uniform_(0.5, 4.0),
        'd0_v':  torch.empty((POP_SIZE_GPU, 1), device=device).uniform_(0.5, 3.0),
        'y_explo': torch.empty((POP_SIZE_GPU, 1), device=device).uniform_(0.0, 5.0), # exploration influence
    }

    sorted_idx = torch.arange(POP_SIZE_GPU, device=device)
    global_best_cost = float('inf')
    global_best_params = {}
    global_best_cov = 0.0
    
    for gen in range(GEN_GPU):
        t0 = time.time()
        
        # Eval
        if len(devices) > 1:
            chunks = [{} for _ in range(len(devices))]
            for k, v in genes.items():
                split_v = torch.tensor_split(v, len(devices))
                for i, dev in enumerate(devices):
                    chunks[i][k] = split_v[i].to(dev)
            
            with concurrent.futures.ThreadPoolExecutor(max_workers=len(devices)) as executor:
                futures = [executor.submit(run_batch_pytorch, chunks[i], devices[i]) for i in range(len(devices))]
                results = [f.result() for f in futures]
                costs_chunks = [r[0] for r in results]
                covs_chunks = [r[1] for r in results]
                
            costs = torch.cat([c.to(device) for c in costs_chunks])
            if covs_chunks[0] is not None:
                covs = torch.cat([c.to(device) for c in covs_chunks if c is not None])
            else:
                covs = None
            
            # Sync multi-GPU
            for dev in devices:
                if dev.type == 'cuda':
                    torch.cuda.synchronize(dev)
        else:
            costs, covs = run_batch_pytorch(genes, device)
            # Sync single-GPU
            if device.type == 'cuda':
                torch.cuda.synchronize(device)
            elif device.type == 'mps':
                torch.mps.synchronize()
                
        dt = time.time() - t0
        
        # Sort
        sorted_idx = torch.argsort(costs)
        best_idx = sorted_idx[0]
        best_cost = costs[best_idx].item()
        best_cov_val = covs[best_idx].item() * 100 if covs is not None else 0.0
        
        if best_cost < global_best_cost:
            global_best_cost = best_cost
            global_best_params = {k: genes[k][best_idx].clone() for k in genes}
            global_best_cov = best_cov_val
            
        print(f"Gen {gen:02d} | Cost: {global_best_cost:.2f} | T: {dt:.2f}s | Best exploration rate : {global_best_cov:.1f}%")        
        # Log
        current_best = SwarmParams(**{k: v.item() for k, v in global_best_params.items()})
        logger.log_generation(gen, global_best_cost, dt, current_best)

        # Mutate
        if gen < GEN_GPU - 1:
            torch.manual_seed(int(time.time() * 1000) % (2**32 - 1))
            
            # Selection
            tournament_size = 3 
            tournaments = torch.randint(0, POP_SIZE_GPU, (POP_SIZE_GPU - 1, tournament_size), device=device)
            winners_idx = tournaments[torch.arange(POP_SIZE_GPU - 1).unsqueeze(1), torch.argmin(costs[tournaments], dim=1, keepdim=True)].squeeze()
            parent1_idx = winners_idx

            tournaments2 = torch.randint(0, POP_SIZE_GPU, (POP_SIZE_GPU - 1, tournament_size), device=device)
            winners2_idx = tournaments2[torch.arange(POP_SIZE_GPU - 1).unsqueeze(1), torch.argmin(costs[tournaments2], dim=1, keepdim=True)].squeeze()
            parent2_idx = winners2_idx
            
            mutation_rate = 0.35 - (0.20 * (gen / GEN_GPU))
            
            for k in genes:
                # Genes excluded from training
                if k in ['a_att', 'b1_att', 'b2_att', 'd0_ali', 'a_ali', 'b1_ali', 'b2_ali']: continue
                
                crossover_mask = torch.rand((POP_SIZE_GPU - 1, 1), device=device) < 0.5
                children_genes = torch.where(crossover_mask, genes[k][parent1_idx], genes[k][parent2_idx])
                
                # Noise mask
                mask = torch.rand(children_genes.shape, device=device) < mutation_rate
                noise = torch.normal(mean=1.0, std=0.3, size=children_genes.shape, device=device)
                children_genes = torch.where(mask, children_genes * noise, children_genes)
                
                genes[k][1:] = children_genes
                genes[k][0] = global_best_params[k]
                
                # Bounds
                if k == 'target_altitude':
                    genes[k].clamp_(min=config.Z_MIN, max=config.Z_MAX)
                elif 'ali' in k or k == 'y_acc':
                    genes[k].clamp_(min=0.0)
                elif k == 'd0_att': 
                    genes[k].clamp_(min=0.5)
                else:
                    genes[k].clamp_(min=0.1)

    # Final extraction
    final_params = SwarmParams(**{k: genes[k][0].item() for k in genes})
    
    logger.close()
    return final_params, logger

def generate_final_data_pytorch(params, logger, device):
    print("\n[PyTorch] Generating final trajectory...")
    torch.manual_seed(42)
    
    # Init state
    pos, phi, v, vz = get_deterministic_initial_state(1, NB_DRONES, device=device)
    
    pos = pos[0:1]
    phi = phi[0:1]
    v = v[0:1]
    if vz is not None:
        vz = vz[0:1]
    
    history_pos, history_phi, history_v, history_vz = [], [], [], []
    history_cov = []
    
    grid = None
    if config.SCENARIO == "exploration":
        grid = TensorExplorationGrid(1, NB_DRONES, config.ARENA_RADIUS, config.GRID_RES, device=device)
    
    eye_mask_single = torch.eye(NB_DRONES, dtype=torch.bool, device=device).expand(1, NB_DRONES, NB_DRONES)
    noise_buffer = torch.empty_like(phi)
    
    # Visu loop
    for t in range(VISU_STEPS): 
        history_pos.append(pos.clone())
        history_phi.append(phi.clone())
        history_v.append(v.clone())
        if vz is not None:
            history_vz.append(vz.clone())

        acc, phi_dot, vz_dot = compute_derivatives(
            pos, phi, v, params, vz=vz, grid=grid,
            eye_mask=eye_mask_single, noise_buffer=noise_buffer
        )
        
        v += acc * DT
        phi += phi_dot * DT
        pos[..., 0] += v * torch.cos(phi) * DT
        pos[..., 1] += v * torch.sin(phi) * DT
        
        if vz is not None and vz_dot is not None:
            vz += vz_dot * DT
            pos[..., 2] += vz * DT
            
        if grid:
            grid.update(pos)
            
            if t % getattr(config, 'REFRESH_MAP_TICKS', 50) == 0:
                grid.share_maps(pos, getattr(config, 'NEIGHBORS', 2))
                
            # Snapshot of the map on each frame
            if grid.strategy == "global":
                explored = (grid.spoilage[0] < grid.MAX_SPOIL * 0.9).float()
            else:
                global_spoilage, _ = torch.min(grid.spoilage[0], dim=0)
                explored = (global_spoilage < grid.MAX_SPOIL * 0.9).float()
            history_cov.append(explored.cpu().numpy())
            
    # Host transfer
    final_cov = None
    if grid:
        score = grid.get_coverage().item()
        print(f"[PyTorch] Final Exploration Coverage: {score * 100:.2f}%")
        final_cov = np.stack(history_cov) # Temporal tensor of the map
        
    full_pos = torch.stack(history_pos).squeeze(1).cpu().numpy()
    full_phi = torch.stack(history_phi).squeeze(1).cpu().numpy()
    full_v   = torch.stack(history_v).squeeze(1).cpu().numpy()
    full_vz  = torch.stack(history_vz).squeeze(1).cpu().numpy() if vz is not None else None
    
    # Log
    logger.save_trajectory(full_pos, full_phi, full_v, params, vz=full_vz, coverage=final_cov)

if __name__ == "__main__":
    best_p, logger = optimize_pytorch(devices)
    generate_final_data_pytorch(best_p, logger, primary_device)
    generate_gif_from_log(logger.log_dir)
