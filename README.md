# Drone Swarm Optimization Prototype

This repository contains a Python prototype for optimizing autonomous drone swarm behaviors. It implements a particle-based simulation where interaction rules (attraction, alignment, repulsion) are tuned using a Genetic Algorithm (GA). The system natively supports both **2D and 3D simulations** and integrates advanced spatial hashing modules for distributed exploration scenarios.

The project provides three mathematically equivalent implementations:
1. **CPU Baseline (`Mk1`)**: Uses NumPy and the `multiprocessing` module for CPU-bound optimization *(Legacy/Deprecated)*.
2. **GPU Accelerator (`Mk2`)**: Uses CuPy for massive parallelization on NVIDIA hardware *(Legacy/Deprecated)*.
3. **PyTorch Engine (`Mk3`)**: Full vectorization compatible with CPU, CUDA (NVIDIA, with **multi-GPU support**), and MPS (Apple Silicon). It runs without a gradient graph (`@torch.no_grad()`) for maximum performance and highly parallelized environment evaluation *(Active Engine)*.

---

## Architecture

The system centralizes the physics logic to ensure strict consistency of results across execution environments.

### Core Modules
* `config.py`: Defines global constants, the simulation mode (`ENABLE_3D`), the scenario (`SCENARIO` / `FULL_MILLING_MODE`), distributed mapping strategies, and GA cost function weights.
* `dynamics.py` *(Legacy)* / `dynamics_pytorch.py` *(Active)*: Physics engines and cost functions handling social forces (attraction/repulsion, KNN), vertical dynamics (altitude navigation, floor/ceiling avoidance), and aging/freshening exploration tensors.
* `logger.py`: Saves simulation states (`.npz` format) and automatically generates formatted Markdown reports.
* `visualization.py`: Generates 2D vector fields, 3D GIF animations, and interactive 3D HTML exports (via Plotly) with playback controls.
* `analysis.py`: Parses the markdown reports from optimization sessions over a specified date range to generate parameter correlation heatmaps.
* `sweep_parameters.py`: Automates batch running of the `Mk3` optimization across varying drone population sizes.
* `sweep_explo.py`: Automates batch running to test combinations of map sharing strategies (`global`, `local_individual`, `local_shared`) and exploration logic (`local_gradient`, `global_best`).

---

## Technical Details

### Physics Model
Agents follow first-order unicycle dynamics on the horizontal plane, with optional vertical dynamics.

The horizontal angular velocity command is derived from the weighted sum of social forces, modulated by viewing angles and heading differences to simulate sensory blind spots:

$$\dot{\phi}_{cmd} = \sum \left( F_{att}(d_{ij}) O_{att}(\psi) E_{att}(\Delta\phi) + F_{ali}(d_{ij}) O_{ali}(\Delta\phi) E_{ali}(\psi) \right) + F_{wall}$$

When `ENABLE_3D` is active, the vertical velocity command is governed by a hyperbolic tangent function for altitude navigation, exponential decay for collision avoidance on the Z-axis, and floor/ceiling repulsion.

### Distributed Exploration & Mapping
The exploration scenario simulates terrain coverage using a grid-based approach.

**Field of View (FOV)** logic allows drones to clear "spoilage" in the grid using a Gaussian splat based on an Inverse Square Law relative to their altitude ($Z$). Memory retention is governed by `MAP_STRATEGY`, where drones can share a `global` map, retain `local_individual` maps, or use `local_shared` maps that are asynchronously merged with nearby neighbors. Finally, the `EXPLO_STRATEGY` defines the routing logic, allowing drones to either steer towards the `local_gradient` of freshness or target the `global_best` unexplored coordinates.

### Cost Function (Optimization)
The Genetic Algorithm minimizes a composite cost function:

$$J = W_{disp} |\bar{r} - r_{target}| + W_{effort} \sum|\dot{\phi}| + W_{pol}(1 - \Psi) + W_{coll} N_{coll} + W_{mill} M + W_{explo} S_{grid} + W_{stationary} V_{bary}$$

* **Dispersion**: Maintains the target swarm radius (e.g., $r_{target} = 5.0m$).
* **Effort**: Penalizes high turn rates and erratic behavior.
* **Polarization ($\Psi$)**: Maximizes velocity vector alignment.
* **Collision**: Strictly penalizes inter-agent distances below the safety threshold.
* **Milling ($M$)**: Rewards collective circular motion (can be inverted depending on the scenario).
* **Exploration ($S_{grid}$)**: Maximizes the covered area via freshness grid analysis.
* **Stationary ($V_{bary}$)**: Penalizes barycenter movement to keep the swarm anchored during specific scenarios.

To guarantee convergence, the evaluation uses **Frozen Noise** (fixed random seeds during the batch), ensuring that score improvements come from the parameters and not stochastic variance. The PyTorch engine also utilizes multi-environment evaluation (`minmax`, `average`, `best`) across various initial conditions to favor robust parameter sets.

---

## Usage

### Dependencies
* Python 3.8+
* `numpy`, `matplotlib`
* `torch` (Required for `Mk3`)
* `plotly` (Required for interactive 3D HTML rendering)
* `pandas`, `seaborn` (Required for `analysis.py`)
* CuPy / CUDA Toolkit (Optional, required only for legacy `Mk2`)

### Execution

**PyTorch Mode (Recommended - CPU / CUDA / Multi-GPU / MPS):**
```bash
python Mk3_PyTorch_Full.py
```

**Automated Parameter Sweep:**
Run optimizations consecutively for varying swarm sizes (5 to 30 drones).
```bash
python sweep_parameters.py
```

**Automated Exploration Strategies Sweep:**
Test combinations of mapping and exploration modes.
```bash
python sweep_explo.py
```

**Post-Optimization Analysis:**
Generate parameter correlation heatmaps from your logs.
```bash
python analysis.py
```

**CPU Baseline Mode (Legacy):**
```bash
python Mk1_CPU_Full.py
```

**GPU CuPy Mode (Legacy):**
```bash
python Mk2_GPU_Full.py
```

### Configuration
Simulation constraints, scaling rules, and scenario toggles (exploration vs default, `FULL_MILLING_MODE`) must be adjusted in `config.py` prior to execution. Graphical outputs and logs will be automatically sorted into the `logs/` directory.