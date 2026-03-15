# Drone Swarm Optimization Prototype

This repository contains a Python prototype for optimizing autonomous drone swarm behaviors. It implements a particle-based simulation where interaction rules (attraction, alignment, repulsion) are tuned using a Genetic Algorithm (GA). The system natively supports both **2D and 3D simulations** and integrates a spatial hashing module for exploration scenarios.

The project provides three mathematically equivalent implementations:
1. **CPU Baseline (`Mk1`)**: Uses NumPy and the `multiprocessing` module.
2. **GPU Accelerator (`Mk2`)**: Uses CuPy for massive parallelization on NVIDIA hardware.
3. **PyTorch Engine (`Mk3`)**: Full vectorization compatible with CPU, CUDA (NVIDIA), and MPS (Apple Silicon), running without a gradient graph (`@torch.no_grad()`) for maximum performance.

## Architecture

The system centralizes the physics logic to ensure strict consistency of results across execution environments.

### Core Modules
* `config.py`: Defines global constants (timestep, arena, population), the simulation mode (`ENABLE_3D`), the scenario (`SCENARIO`), and optimization weights.
* `dynamics.py` / `dynamics_pytorch.py`: Physics engines and cost functions. They handle:
    * **Forces**: Attraction/repulsion and heading alignment.
    * **Vertical Dynamics**: Altitude alignment and social distance coupling (3D mode).
    * **Constraints**: Exponential repulsion from the arena walls.
    * **Exploration Grid**: Aging/freshening tensor to measure spatial coverage (`TensorExplorationGrid`).
* `logger.py`: Saves simulation states (`.npz` format) and automatically generates Markdown reports.
* `visualization.py`: Generates 2D vector fields, 3D GIF animations, and interactive 3D HTML exports via Plotly.

## Technical Details

### Physics Model
Agents follow first-order unicycle dynamics on the horizontal plane, with optional vertical dynamics.

The horizontal angular velocity command is derived from the weighted sum of social forces, modulated by viewing angles and heading differences to simulate sensory blind spots:
phi_dot_cmd = sum( F_att(d_ij) * O_att(psi) * E_att(dphi) + F_ali(d_ij) * O_ali(dphi) * E_ali(psi) ) + F_wall

When `ENABLE_3D` is active, the vertical velocity command is governed by a hyperbolic tangent function for altitude alignment and an exponential decay for social distance.

### Cost Function (Optimization)
The Genetic Algorithm minimizes a composite cost function:
J = w_disp * |r_mean - r_target| + w_effort * sum(|phi_dot|) + w_pol * (1 - Psi) + w_coll * N_coll + w_mill * M + w_explo * S_grid

* **Dispersion**: Maintains the target swarm radius (r_target = 5.0m).
* **Effort**: Penalizes high turn rates.
* **Polarization (Psi)**: Maximizes velocity vector alignment.
* **Collision**: Strictly penalizes inter-agent distances below 0.4m.
* **Milling (M)**: Rewards collective circular motion.
* **Exploration (S_grid)**: Maximizes the covered area via freshness grid analysis.

To guarantee convergence, the evaluation uses **Frozen Noise** (fixed random seed during the batch), ensuring that score improvements come from the parameters and not stochastic variance.

## Usage

### Dependencies
* Python 3.8+
* NumPy, Matplotlib
* PyTorch (Required for `Mk3`)
* Plotly (Required for interactive 3D HTML rendering)
* CuPy / CUDA Toolkit (Optional, required only for `Mk2`)

### Execution

**PyTorch Mode (Recommended - CPU/CUDA/MPS):**
python Mk3_PyTorch_Full.py

**CPU Baseline Mode:**
python Mk1_CPU_Full.py

**GPU CuPy Mode:**
python Mk2_GPU_Full.py

## Configuration
Simulation parameters, the scenario (e.g., "exploration"), and cost function weights can be adjusted in `config.py`.