# Drone Swarm Optimization Prototype

This repository contains a Python prototype for optimizing autonomous drone swarm behaviors. It implements a particle-based simulation where interaction rules—attraction, alignment, and repulsion—are tuned using a Genetic Algorithm (GA).

The project provides two mathematically equivalent implementations:
1. **CPU Baseline (`Mk1`)**: Uses NumPy and multiprocessing.
2. **GPU Accelerator (`Mk2`)**: Uses CuPy for massive parallelization of the population evaluation.

## Architecture

The system is designed to ensure strict consistency between CPU and GPU results by centralizing the physics and evaluation logic.

### Core Modules
* `config.py`: Defines global constants for the environment (timestep, arena size, drone count) and optimization weights.
* `dynamics.py`: Implements the physics engine and cost function. It handles:
    * **Forces**: Lennard-Jones style attraction/repulsion and heading alignment.
    * **Constraints**: Soft-boundary wall repulsion.
    * **Metrics**: Calculation of Dispersion, Control Effort, Polarization, and Collisions.

### Solvers
* `Mk1_CPU_Full.py`: Executes the GA on the CPU. It utilizes `multiprocessing.Pool` to parallelize the evaluation of swarm candidates across available cores.
* `Mk2_GPU_Full.py`: Executes the GA on the GPU. It vectorizes the entire population (e.g., 2000 swarms) into a single batch operation using CuPy, significantly reducing computation time.

## Technical Details

### Physics Model
Agents follow first-order unicycle dynamics. The angular velocity command $\dot{\phi}$ is derived from the weighted sum of social forces:

$$
\dot{\phi}_{cmd} = \sum_{j \neq i} \left( F_{att}(d_{ij}) \sin(\psi_{ij}) + F_{ali}(d_{ij}) \sin(\Delta \phi_{ij}) \right) + F_{wall}
$$

Where interactions decay based on Lorentzian functions defined by the optimization parameters.

### Optimization Objective
The Genetic Algorithm minimizes a composite cost function defined in `dynamics.py`:

$$
J = w_{disp} | \bar{r} - r_{target} | + w_{effort} \sum |\dot{\phi}| + w_{pol} (1 - \Psi) + w_{coll} N_{coll}
$$

* **Dispersion**: Maintains a specific swarm radius ($r_{target} = 5.0m$).
* **Effort**: Penalizes high turn rates to ensure smooth trajectories.
* **Polarization ($\Psi$)**: Maximizes velocity alignment (0 to 1).
* **Collision**: Heavily penalizes inter-agent distances below 0.6m.

To ensure convergence, the evaluation phase uses **Frozen Noise** (fixed random seed), guaranteeing that score improvements are due to better parameters rather than stochastic variance.

## Usage

### Dependencies
* Python 3.8+
* NumPy
* Matplotlib
* CuPy (Required for `Mk2`)
* NVIDIA GPU + CUDA Toolkit (Required for `Mk2`)

### Execution

**CPU Mode:**
```bash
python Mk1_CPU_Full.py'''

**GPU Mode:**
```bash
python Mk2_GPU_Full.py'''

## Configuration
Simulation parameters and cost function weights can be modified in config.py:

'''python
W_EFFORT 
W_DISP 
W_POL 
W_COLL'''
