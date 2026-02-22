import multiprocessing
import os
import time
import numpy as np
import matplotlib.pyplot as plt
import config
from matplotlib.patches import Circle
from matplotlib.animation import FuncAnimation

from logger import ExperimentLogger
from visualization import generate_gif_from_log

from config import NB_DRONES, ARENA_RADIUS, DT, SIM_STEPS, VISU_STEPS, POP_SIZE_CPU, GEN_CPU
from dynamics import SwarmParams, compute_derivatives, get_deterministic_initial_state, compute_metrics

def run_simulation(params, steps=SIM_STEPS):
    # Deterministic Seed (Frozen Noise)
    np.random.seed(42)
    
    pos, phi, v, vz = get_deterministic_initial_state(1, NB_DRONES, xp=np)
    
    cost_total = 0.0

    for t in range(steps):
        acc, phi_dot, vz_dot = compute_derivatives(pos, phi, v, params, vz=vz, xp=np)
        
        v   += acc * DT
        phi += phi_dot * DT
        pos[:, 0] += v * np.cos(phi) * DT
        pos[:, 1] += v * np.sin(phi) * DT
        
        if vz is not None and vz_dot is not None:
            vz += vz_dot * DT
            pos[:, 2] += vz * DT
        
        # Accumulate metrics (Post-Transient)
        if t > 50:
            c_disp, c_effort, c_coll, c_pol, c_mill = compute_metrics(pos, phi, phi_dot, v, xp=np)
            cost_total += c_disp + c_effort + c_coll + c_pol + c_mill
            
    return cost_total

def optimize():
    # Logger initialisation
    logger = ExperimentLogger(mode="CPU")
    logger.log_config(config)
    
    # Detect cores (Safe margin -2)
    n_workers = max(1, (os.cpu_count() or 1) - 2)
    print(f"--- CPU GA (Pop: {POP_SIZE_CPU}) | Workers: {n_workers} | Log: {logger.log_dir} ---")
    
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
            
            duration = time.time() - t0
            print(f"Gen {gen:02d} | Cost: {costs[best_idx]:.2f} | T: {time.time()-t0:.2f}s")
            logger.log_generation(gen, costs[best_idx], duration, pop[best_idx])
            
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
    logger.close()
    return pop[0], logger # Returning logger for path

def generate_final_data(params, logger):
    """
    Runs the final simulation to feed into logs and visualization
    """
    print("\nGénération de la trajectoire finale (Machine Data)...")
    # Seed reset
    np.random.seed(42)
    
    pos, phi, v, vz = get_deterministic_initial_state(1, NB_DRONES, xp=np)
    
    history_pos = []
    history_phi = []
    history_v = []
    history_vz = []
    
    for _ in range(VISU_STEPS):
        # Current state
        history_pos.append(pos.copy())
        history_phi.append(phi.copy())
        history_v.append(v.copy())
        if vz is not None:
            history_vz.append(vz.copy())
        
        acc, phi_dot, vz_dot = compute_derivatives(pos, phi, v, params, vz=vz, xp=np)
            
        v   += acc * DT
        phi += phi_dot * DT
        pos[:, 0] += v * np.cos(phi) * DT
        pos[:, 1] += v * np.sin(phi) * DT
        
        if vz is not None and vz_dot is not None:
            vz += vz_dot * DT
            pos[:, 2] += vz * DT
        
    # Conversion to numpy arrays
    full_pos = np.array(history_pos)
    full_phi = np.array(history_phi)
    full_v   = np.array(history_v)
    full_vz  = np.array(history_vz) if vz is not None else None
    
    # Logging
    logger.save_trajectory(full_pos, full_phi, full_v, params, vz=full_vz)

if __name__ == "__main__":
    best_params, logger = optimize()
    
    generate_final_data(best_params, logger)
    
    generate_gif_from_log(logger.log_dir)