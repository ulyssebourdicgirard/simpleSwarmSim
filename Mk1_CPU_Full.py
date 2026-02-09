import multiprocessing
import os
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.animation import FuncAnimation

from config import NB_DRONES, ARENA_RADIUS, DT, SIM_STEPS, VISU_STEPS, POP_SIZE_CPU, GEN_CPU
from dynamics import SwarmParams, compute_derivatives, get_deterministic_initial_state, compute_metrics

def run_simulation(params, steps=SIM_STEPS):
    # Deterministic Seed (Frozen Noise)
    np.random.seed(42)
    
    pos, phi, v = get_deterministic_initial_state(1, NB_DRONES, xp=np)
    
    cost_total = 0.0

    for t in range(steps):
        acc, phi_dot = compute_derivatives(pos, phi, v, params, xp=np)
        
        v   += acc * DT
        phi += phi_dot * DT
        pos[:, 0] += v * np.cos(phi) * DT
        pos[:, 1] += v * np.sin(phi) * DT
        
        # Accumulate metrics (Post-Transient)
        if t > 50:
            c_disp, c_effort, c_coll, c_pol = compute_metrics(pos, phi, phi_dot, xp=np)
            cost_total += c_disp + c_effort + c_coll + c_pol
            
    return cost_total

def optimize():
    # Detect cores (Safe margin -2)
    n_workers = max(1, (os.cpu_count() or 1) - 2)
    print(f"--- CPU GA (Pop: {POP_SIZE_CPU}) | Workers: {n_workers} ---")
    
    # Init Pop
    pop = []
    for _ in range(POP_SIZE_CPU):
        pop.append(SwarmParams(
            y_att=np.random.uniform(0.5, 4.0),
            d0_att=np.random.uniform(1.0, 3.0),
            l_att=np.random.uniform(1.0, 5.0),
            y_ali=np.random.uniform(0.5, 3.0),
            l_ali=np.random.uniform(1.0, 5.0),
            y_f=np.random.uniform(0.5, 2.0)
        ))

    # Parallel Pool
    with multiprocessing.Pool(n_workers) as pool:
        for gen in range(GEN_CPU):
            t0 = time.time()
            
            costs = pool.map(run_simulation, pop)
            sorted_idx = np.argsort(costs)
            best_idx = sorted_idx[0]
            
            print(f"Gen {gen:02d} | Cost: {costs[best_idx]:.2f} | T: {time.time()-t0:.2f}s")
            
            # Restore randomness for mutation
            np.random.seed(int(time.time() * 1000) % 2**32)

            survivors = [pop[i] for i in sorted_idx[:int(POP_SIZE_CPU*0.2)]]
            new_pop = [pop[best_idx]] 
            
            while len(new_pop) < POP_SIZE_CPU:
                parent = np.random.choice(survivors)
                child = SwarmParams(**parent.__dict__)
                
                if np.random.rand() < 0.2: child.y_att *= np.random.normal(1.0, 0.2)
                if np.random.rand() < 0.2: child.d0_att *= np.random.normal(1.0, 0.2)
                if np.random.rand() < 0.2: child.y_ali *= np.random.normal(1.0, 0.2)
                
                child.d0_att = max(0.5, child.d0_att)
                child.y_att = max(0.1, child.y_att)
                new_pop.append(child)
                
            pop = new_pop

    return pop[0]

def visualize(params):
    print("\nVisualizing...")
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
    
    title = f"CPU Result\nAtt: {params.y_att:.2f}, D0: {params.d0_att:.2f}"
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
    best = optimize()
    visualize(best)