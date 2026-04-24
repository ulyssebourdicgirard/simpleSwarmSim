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
        'y_att':  torch.empty((POP_SIZE_GPU, 1), device=device).uniform_(0.001, 5.0),
        'd0_att': torch.empty((POP_SIZE_GPU, 1), device=device).uniform_(1.0, 4.0), # Augmenter distances pour permettre plus longue attraction
        'l_att':  torch.empty((POP_SIZE_GPU, 1), device=device).uniform_(1.0, 5.0), # l_att >>> d0_att
        'y_ali':  torch.empty((POP_SIZE_GPU, 1), device=device).uniform_(0.0, 4.0),
        'l_ali':  torch.empty((POP_SIZE_GPU, 1), device=device).uniform_(1.0, 5.0),
        'y_f':    torch.empty((POP_SIZE_GPU, 1), device=device).uniform_(0.001, 2.0), # Pas forcément variable
        'a_att':  torch.zeros((POP_SIZE_GPU, 1), device=device),
        'b1_att': torch.zeros((POP_SIZE_GPU, 1), device=device),
        'b2_att': torch.zeros((POP_SIZE_GPU, 1), device=device),
        'd0_ali': torch.ones((POP_SIZE_GPU, 1), device=device),
        'a_ali':  torch.zeros((POP_SIZE_GPU, 1), device=device),
        'b1_ali': torch.zeros((POP_SIZE_GPU, 1), device=device),
        'b2_ali': torch.zeros((POP_SIZE_GPU, 1), device=device),
        'target_altitude': torch.empty((POP_SIZE_GPU, 1), device=device).uniform_(config.Z_MIN + 1.0, config.Z_MAX - 1.0),
        'y_acc': torch.empty((POP_SIZE_GPU, 1), device=device).uniform_(0.001, 2.0),
        'l_acc': torch.empty((POP_SIZE_GPU, 1), device=device).uniform_(0.5, 4.0),
        'd0_v':  torch.empty((POP_SIZE_GPU, 1), device=device).uniform_(0.5, 3.0),
    }

    sorted_idx = torch.arange(POP_SIZE_GPU, device=device)
    global_best_cost = float('inf')
    global_best_params = {}
    
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
        
        if best_cost < global_best_cost:
            global_best_cost = best_cost
            global_best_params = {k: genes[k][best_idx].clone() for k in genes}
            
        print(f"Gen {gen:02d} | Cost: {global_best_cost:.2f} | T: {dt:.2f}s")
        
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