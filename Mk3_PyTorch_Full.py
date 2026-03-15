import time
import torch
import config

from config import NB_DRONES, ARENA_RADIUS, DT, SIM_STEPS, VISU_STEPS, POP_SIZE_GPU, GEN_GPU
from dynamics_pytorch import SwarmParams, TensorExplorationGrid, compute_derivatives, get_deterministic_initial_state, compute_metrics
from logger import ExperimentLogger
from visualization import generate_gif_from_log

# Hardware routing
if torch.cuda.is_available():
    device = torch.device("cuda")
elif torch.backends.mps.is_available():
    device = torch.device("mps")
else:
    device = torch.device("cpu")

def run_batch_pytorch(genes, device):
    # Frozen noise
    torch.manual_seed(42)
    
    n_batch = genes['y_att'].shape[0]
    pos, phi, v, vz = get_deterministic_initial_state(n_batch, NB_DRONES, device=device)
    
    params = SwarmParams(**genes)
    cost_total = torch.zeros(n_batch, device=device) # Init tensor for all costs in all swarms
    
    grid = None 
    if config.SCENARIO == "exploration":
        grid = TensorExplorationGrid(n_batch, config.ARENA_RADIUS, config.GRID_RES, device=device)
    
    # Integration loop
    for t in range(SIM_STEPS):
        acc, phi_dot, vz_dot = compute_derivatives(pos, phi, v, params, vz=vz)
        
        v += acc * DT
        phi += phi_dot * DT
        pos[..., 0] += v * torch.cos(phi) * DT
        pos[..., 1] += v * torch.sin(phi) * DT
        
        if vz is not None and vz_dot is not None:
            vz += vz_dot * DT
            pos[..., 2] += vz * DT
            
        if grid:
            grid.update(pos)
        
        # Post-transient metrics
        if t > 50:
            c_disp, c_effort, c_coll, c_pol, c_mill = compute_metrics(pos, phi, phi_dot, v)
            cost_total += c_disp + c_effort + c_coll + c_pol + c_mill

            if grid:
                cost_total += grid.get_score() * config.W_EXPLO

    return cost_total



def optimize_pytorch(device):
    logger = ExperimentLogger(mode=f"PyTorch_{device.type.upper()}")
    logger.log_config(config)
    
    print(f"--- PyTorch GA (Pop: {POP_SIZE_GPU}) | Device: {device} | Log: {logger.log_dir} ---")
    
    # Init pop
    genes = {
        'y_att':  torch.empty((POP_SIZE_GPU, 1), device=device).uniform_(0.5, 5.0),
        'd0_att': torch.empty((POP_SIZE_GPU, 1), device=device).uniform_(1.0, 4.0),
        'l_att':  torch.empty((POP_SIZE_GPU, 1), device=device).uniform_(1.0, 5.0),
        'y_ali':  torch.empty((POP_SIZE_GPU, 1), device=device).uniform_(0.0, 4.0),
        'l_ali':  torch.empty((POP_SIZE_GPU, 1), device=device).uniform_(1.0, 5.0),
        'y_f':    torch.empty((POP_SIZE_GPU, 1), device=device).uniform_(0.5, 2.0),
        'a_att':  torch.zeros((POP_SIZE_GPU, 1), device=device),
        'b1_att': torch.zeros((POP_SIZE_GPU, 1), device=device),
        'b2_att': torch.zeros((POP_SIZE_GPU, 1), device=device),
        'd0_ali': torch.ones((POP_SIZE_GPU, 1), device=device),
        'a_ali':  torch.zeros((POP_SIZE_GPU, 1), device=device),
        'b1_ali': torch.zeros((POP_SIZE_GPU, 1), device=device),
        'b2_ali': torch.zeros((POP_SIZE_GPU, 1), device=device),
    }

    n_keep = int(0.2 * POP_SIZE_GPU)
    sorted_idx = torch.arange(POP_SIZE_GPU, device=device)
    
    for gen in range(GEN_GPU):
        t0 = time.time()
        
        # Eval
        costs = run_batch_pytorch(genes, device)
        
        # Sync
        if device.type == 'cuda':
            torch.cuda.synchronize()
        elif device.type == 'mps':
            torch.mps.synchronize()
            
        dt = time.time() - t0
        
        # Sort
        sorted_idx = torch.argsort(costs)
        best_idx = sorted_idx[0]
        best_cost = costs[best_idx].item()
        
        print(f"Gen {gen:02d} | Cost: {best_cost:.2f} | T: {dt:.2f}s")
        
        # Log
        best_gene_values = {k: genes[k][best_idx].item() for k in genes}
        current_best = SwarmParams(**best_gene_values)
        logger.log_generation(gen, best_cost, dt, current_best)

        # Mutate
        if gen < GEN_GPU - 1:
            torch.manual_seed(int(time.time() * 1000) % (2**32 - 1))
            
            survivors = sorted_idx[:n_keep]
            best_idx_arr = sorted_idx[:1]
            
            # Selection
            parents = survivors[torch.randint(0, n_keep, (POP_SIZE_GPU - 1,), device=device)]
            fill_idx = torch.cat((best_idx_arr, parents))
            
            for k in genes:
                # Genes excluded from training
                if k in ['a_att', 'b1_att', 'b2_att', 'd0_ali', 'a_ali', 'b1_ali', 'b2_ali']: continue
                genes[k] = genes[k][fill_idx]
                
                # Noise mask
                mask = torch.rand(genes[k].shape, device=device) < 0.25 
                noise = torch.normal(mean=1.0, std=0.25, size=genes[k].shape, device=device)
                genes[k][1:] = torch.where(mask[1:], genes[k][1:] * noise[1:], genes[k][1:])
                
                # Bounds
                if 'ali' in k:
                    genes[k].clamp_(min=0.0)
                elif k == 'd0_att': 
                    genes[k].clamp_(min=0.5)
                else:
                    genes[k].clamp_(min=0.1)

    # Final extraction
    final_params = SwarmParams(**{k: genes[k][sorted_idx[0]].item() for k in genes})
    
    logger.close()
    return final_params, logger

def generate_final_data_pytorch(params, logger, device):
    print("\n[PyTorch] Generating final trajectory...")
    torch.manual_seed(42)
    
    # Init state
    pos, phi, v, vz = get_deterministic_initial_state(1, NB_DRONES, device=device)
    
    history_pos, history_phi, history_v, history_vz = [], [], [], []
    
    grid = None
    if config.SCENARIO == "exploration":
        grid = TensorExplorationGrid(1, config.ARENA_RADIUS, config.GRID_RES, device=device)
    
    # Visu loop
    for _ in range(VISU_STEPS): 
        history_pos.append(pos.clone())
        history_phi.append(phi.clone())
        history_v.append(v.clone())
        if vz is not None:
            history_vz.append(vz.clone())

        acc, phi_dot, vz_dot = compute_derivatives(pos, phi, v, params, vz=vz)
        
        v += acc * DT
        phi += phi_dot * DT
        pos[..., 0] += v * torch.cos(phi) * DT
        pos[..., 1] += v * torch.sin(phi) * DT
        
        if vz is not None and vz_dot is not None:
            vz += vz_dot * DT
            pos[..., 2] += vz * DT
            
        if grid:
            grid.update(pos)
            
    # Host transfer
    final_cov = None
    if grid:
        score = grid.get_score().item()
        print(f"[PyTorch] Final Exploration Coverage: {score * 100:.2f}%")
        final_cov = (1.0 - (grid.spoilage[0] / grid.MAX_SPOIL)).cpu().numpy()
        
    full_pos = torch.stack(history_pos).cpu().numpy()
    full_phi = torch.stack(history_phi).cpu().numpy()
    full_v   = torch.stack(history_v).cpu().numpy()
    full_vz  = torch.stack(history_vz).cpu().numpy() if vz is not None else None
    
    # Log
    logger.save_trajectory(full_pos, full_phi, full_v, params, vz=full_vz, coverage=final_cov)

if __name__ == "__main__":
    best_p, logger = optimize_pytorch(device)
    generate_final_data_pytorch(best_p, logger, device)
    generate_gif_from_log(logger.log_dir)