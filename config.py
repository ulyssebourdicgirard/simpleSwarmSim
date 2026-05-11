import os

# Env / Physics
ENABLE_3D = False    # True: 3D, False: 2D
Z_MIN = 1.0     
Z_MAX = 10.0 
DT = 0.1             # ADVICE : for 3D simulations, use less than 0.1   
ARENA_RADIUS = 50.0
NB_DRONES = int(os.getenv('NB_DRONES_OVERRIDE', 10))         
MAX_SPEED = 20.0     
                    # NEIGHBORS = None for no limit (bypasses partition for better performance)
NEIGHBORS = 2       # Number of closest neighbors taken into account for interactions
COLLISION_DIST = 0.4
SCENARIO = "exploration"  # "default" | "exploration"
FULL_MILLING_MODE = True # Enables the no-arena milling scenario
GRID_RES = 5.0        # Spatial resolution (m)

# Dynamics Control
ALPHA_LPF = 0.2          # Low-pass filter gain for yaw rate
MAX_YAW_RATE = 3.14      # Max rotational speed (rad/s)

# Exploration
SPOIL_MULT = 1.002
SPOIL_ADD = 0.02

# Optimization
POP_SIZE_CPU = 150        
GEN_CPU = 20              

POP_SIZE_GPU = 5000   # PyTorch uses this one   
GEN_GPU = 20             

SIM_STEPS = 3000         
VISU_STEPS = 6000     

# Initial Conditions & Robustness
N_INIT_CONDITIONS = 4     # Nombre de situations initiales différentes
MIN_SPAWN_DIST = 2.0      # Distance minimale entre les drones à l'apparition
EVAL_STRATEGY = "average"  # Stratégie d'évaluation : "minmax" | "average" | "best"

# Distributed Memory & Exploration
MAP_STRATEGY = os.getenv('MAP_STRATEGY_OVERRIDE', "local_shared")       # "global" | "local_individual" | "local_shared"
EXPLO_STRATEGY = os.getenv('EXPLO_STRATEGY_OVERRIDE', "global_best")  # "local_gradient" | "global_best"
REFRESH_MAP_TICKS = 100             # Fréquence de partage (en nombre de dt)
FOV_FACTOR = 0.9                    # Tangente du demi-angle du cône de vision (1.0 = angle de 45°)

# Cost Function Weights
if FULL_MILLING_MODE:
    SCENARIO = "default" # No grid exploration
    W_EFFORT = 0       
    W_DISP = 10.0        
    W_POL = 250.0          # No reward for flying in a straight line
    W_COLL = 50.0       
    W_MILL = -600.0      # NEGATIVE VALUE to reward milling
    W_EXPLO = 0.0
    W_STATIONARY = 50       # To keep the barycenter from moving for exploits, POSITIVE -> rewards being stationary
else:
    W_EFFORT = 1.0  # To avoid shaking
    W_DISP = 0.0
    W_POL = -0.0
    W_COLL = 500.0
    W_MILL = 0
    W_EXPLO = -50.0
    W_STATIONARY = 0
