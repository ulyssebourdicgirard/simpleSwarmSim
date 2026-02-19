import os
import sys

# Windows CUDA Fix
cuda_bin = r"C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\bin"
if os.path.exists(cuda_bin):
    os.add_dll_directory(cuda_bin)
    os.environ['PATH'] = cuda_bin + os.pathsep + os.environ['PATH']

import time
import numpy as np
import config

from config import NB_DRONES, ARENA_RADIUS, DT, SIM_STEPS, VISU_STEPS, POP_SIZE_GPU, GEN_GPU
from dynamics import SwarmParams, compute_derivatives, get_deterministic_initial_state, compute_metrics
from logger import ExperimentLogger
from visualization import generate_gif_from_log

try:
    import cupy as cp
except ImportError:
    raise RuntimeError("Mk2 requires CuPy + NVIDIA GPU")

def run_batch_gpu(genes):
    # FROZEN NOISE
    cp.random.seed(42)
    
    pos, phi, v = get_deterministic_initial_state(genes['y_att'].shape[0], NB_DRONES, xp=cp)
    
    params = SwarmParams(**genes)
    
    n_batch = genes['y_att'].shape[0]
    cost_total = cp.zeros(n_batch)

    for t in range(SIM_STEPS):
        acc, phi_dot = compute_derivatives(pos, phi, v, params, xp=cp)
        
        # Integration
        v   += acc * DT
        phi += phi_dot * DT
        pos[..., 0] += v * cp.cos(phi) * DT
        pos[..., 1] += v * cp.sin(phi) * DT
        
        # Accumulate metrics (Post-Transient)
        if t > 50:
            c_disp, c_effort, c_coll, c_pol, c_mill = compute_metrics(pos, phi, phi_dot, v, xp=cp)
            cost_total += c_disp + c_effort + c_coll + c_pol + c_mill

    return cost_total

def optimize_gpu():
    logger = ExperimentLogger(mode="GPU")
    logger.log_config(config)
    
    print(f"--- GPU GA (Pop: {POP_SIZE_GPU}) | Log: {logger.log_dir} ---")
    
    genes = {
        'y_att':  cp.random.uniform(0.5, 5.0, (POP_SIZE_GPU, 1)),
        'd0_att': cp.random.uniform(1.0, 4.0, (POP_SIZE_GPU, 1)),
        'l_att':  cp.random.uniform(1.0, 5.0, (POP_SIZE_GPU, 1)),
        'y_ali':  cp.random.uniform(0.0, 4.0, (POP_SIZE_GPU, 1)),
        'l_ali':  cp.random.uniform(1.0, 5.0, (POP_SIZE_GPU, 1)),
        'y_f':    cp.random.uniform(0.5, 2.0, (POP_SIZE_GPU, 1)),
        'alpha_att': cp.full((POP_SIZE_GPU, 1), 1.0),
        'alpha_ali': cp.full((POP_SIZE_GPU, 1), 0.0),
    }

    n_keep = int(0.2 * POP_SIZE_GPU)
    
    sorted_idx = cp.arange(POP_SIZE_GPU)
    
    for gen in range(GEN_GPU):
        t0 = time.time()
        
        costs = run_batch_gpu(genes)
        cp.cuda.Stream.null.synchronize()
        dt = time.time() - t0
        
        sorted_idx = cp.argsort(costs)
        best_idx = sorted_idx[0]
        best_cost = float(costs[best_idx])
        
        print(f"Gen {gen:02d} | Cost: {best_cost:.2f} | T: {dt:.2f}s")
        
        best_gene_values = {k: genes[k][best_idx].item() for k in genes}
        current_best = SwarmParams(**best_gene_values)
        logger.log_generation(gen, best_cost, dt, current_best)

        if gen < GEN_GPU - 1:
            cp.random.seed(int(time.time() * 1000) % 2**32)
            
            survivors = sorted_idx[:n_keep]
            best_idx_arr = sorted_idx[:1]
            parents = survivors[cp.random.randint(0, n_keep, POP_SIZE_GPU - 1)]
            fill_idx = cp.concatenate((best_idx_arr, parents))
            
            for k in genes:
                if 'alpha' in k: continue
                genes[k] = genes[k][fill_idx]
                
                mask = cp.random.rand(*genes[k].shape) < 0.25 
                noise = cp.random.normal(1.0, 0.25, genes[k].shape)
                genes[k][1:] = cp.where(mask[1:], genes[k][1:] * noise[1:], genes[k][1:])
                
                genes[k] = cp.maximum(0.1, genes[k])
                if k == 'd0_att': genes[k] = cp.maximum(0.5, genes[k])

    final_params = SwarmParams(**{k: genes[k][sorted_idx[0]].item() for k in genes})
    
    logger.close()
    return final_params, logger

def generate_final_data_gpu(params, logger):
    print("\n[GPU] Generating final trajectory...")
    cp.random.seed(42)
    
    # Dynamics returns (N, 2) when Batch=1, not (1, N, 2)
    pos, phi, v = get_deterministic_initial_state(1, NB_DRONES, xp=cp)
    
    history_pos = []
    history_phi = []
    history_v = []
    
    for _ in range(VISU_STEPS): 
        history_pos.append(pos.get())
        history_phi.append(phi.get())
        history_v.append(v.get())

        acc, phi_dot = compute_derivatives(pos, phi, v, params, xp=cp)
        
        v   += acc * DT
        phi += phi_dot * DT
        pos[..., 0] += v * cp.cos(phi) * DT
        pos[..., 1] += v * cp.sin(phi) * DT
        
    # Arrays are (Time, N, 2) or (Time, N) directly
    full_pos = np.array(history_pos)
    full_phi = np.array(history_phi)
    full_v   = np.array(history_v)
    
    logger.save_trajectory(full_pos, full_phi, full_v, params)

if __name__ == "__main__":
    best_p, logger = optimize_gpu()
    generate_final_data_gpu(best_p, logger)
    generate_gif_from_log(logger.log_dir)