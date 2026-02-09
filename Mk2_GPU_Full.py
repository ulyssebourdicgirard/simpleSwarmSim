import os
import sys

# Windows CUDA Fix
cuda_bin = r"C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\bin"
if os.path.exists(cuda_bin):
    os.add_dll_directory(cuda_bin)
    os.environ['PATH'] = cuda_bin + os.pathsep + os.environ['PATH']

import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.animation import FuncAnimation

from config import NB_DRONES, ARENA_RADIUS, DT, SIM_STEPS, VISU_STEPS, POP_SIZE_GPU, GEN_GPU
from dynamics import SwarmParams, compute_derivatives, get_deterministic_initial_state, compute_metrics

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
            c_disp, c_effort, c_coll, c_pol = compute_metrics(pos, phi, phi_dot, xp=cp)
            cost_total += c_disp + c_effort + c_coll + c_pol

    return cost_total

def optimize_gpu():
    print(f"--- GPU GA (Pop: {POP_SIZE_GPU}) | Minimizing Cost (Frozen Noise) ---")
    
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
    
    # Init Eval
    costs = run_batch_gpu(genes)
    sorted_idx = cp.argsort(costs)
    
    for gen in range(GEN_GPU):
        t0 = time.time()
        
        if gen < GEN_GPU:
            # Randomness for mutation
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

        # Eval
        costs = run_batch_gpu(genes)
        cp.cuda.Stream.null.synchronize()
        dt = time.time() - t0
        
        sorted_idx = cp.argsort(costs)
        best_idx = sorted_idx[0]
        
        print(f"Gen {gen:02d} | Cost: {float(costs[best_idx]):.2f} | T: {dt:.2f}s")

    best_idx = sorted_idx[0]
    return SwarmParams(
        y_att  = genes['y_att'][best_idx].item(),
        d0_att = genes['d0_att'][best_idx].item(),
        l_att  = genes['l_att'][best_idx].item(),
        y_ali  = genes['y_ali'][best_idx].item(),
        l_ali  = genes['l_ali'][best_idx].item(),
        y_f    = genes['y_f'][best_idx].item()
    )

def visualize_result(params):
    print("\nVisualizing (CPU)...")
    
    # Deterministic init matching training
    pos, phi, v = get_deterministic_initial_state(1, NB_DRONES, xp=np)
    history = []
    
    for _ in range(VISU_STEPS): 
        history.append((pos.copy(), phi.copy()))
        acc, phi_dot = compute_derivatives(pos, phi, v, params, xp=np)
        
        v   += acc * DT
        phi += phi_dot * DT
        pos[:, 0] += v * np.cos(phi) * DT
        pos[:, 1] += v * np.sin(phi) * DT
        
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_xlim(-ARENA_RADIUS-1, ARENA_RADIUS+1)
    ax.set_ylim(-ARENA_RADIUS-1, ARENA_RADIUS+1)
    ax.add_patch(Circle((0, 0), ARENA_RADIUS, color='r', fill=False, ls='--'))
    
    title = (f"Optimized Result\n"
             f"Att: {params.y_att:.2f}, Ali: {params.y_ali:.2f}, D0: {params.d0_att:.2f}")
    ax.set_title(title)

    pos0, phi0 = history[0]
    quiver = ax.quiver(pos0[:, 0], pos0[:, 1], np.cos(phi0), np.sin(phi0), 
                       color='dodgerblue', scale=25, width=0.005)

    def update(frame):
        p, h = history[frame]
        quiver.set_offsets(p)
        quiver.set_UVC(np.cos(h), np.sin(h))
        return quiver,

    ani = FuncAnimation(fig, update, frames=range(0, len(history), 3), interval=30, blit=True)
    plt.show()

if __name__ == "__main__":
    best_p = optimize_gpu()
    visualize_result(best_p)