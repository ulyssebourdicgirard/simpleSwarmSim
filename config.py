import os

# Env / Physics
ENABLE_3D = False    # True: 3D, False: 2D
Z_MIN = 1.0     
Z_MAX = 10.0 
DT = 0.1             # for 3D simulations, use 0.01 max   
ARENA_RADIUS = 100.0
NB_DRONES = int(os.getenv('NB_DRONES_OVERRIDE', 30))         
MAX_SPEED = 20.0     
                    # NEIGHBORS = None for no limit (bypasses partition for better performance)
NEIGHBORS = 3       # Number of closest neighbors taken into account for interactions
COLLISION_DIST = 0.4
SCENARIO = "exploration"  # "default" | "exploration"
FULL_MILLING_MODE = True # Enables the no-arena milling scenario
GRID_RES = 5.0        # Spatial resolution (m)

# Dynamics Control
ALPHA_LPF = 0.2          # Low-pass filter gain for yaw rate
MAX_YAW_RATE = 3.14      # Max rotational speed (rad/s)

# Exploration
SPOIL_MULT = 1.01
SPOIL_ADD = 0.05

# Optimization
POP_SIZE_CPU = 150        
GEN_CPU = 20              

POP_SIZE_GPU = 5000   # PyTorch uses this one   
GEN_GPU = 20             

SIM_STEPS = 500         
VISU_STEPS = 1000      

# Cost Function Weights
if FULL_MILLING_MODE:
    SCENARIO = "default" # No grid exploration
    W_EFFORT = 1.0       # To avoid shaking
    W_DISP = 0.0         
    W_POL = 0.0          # No reward for flying in a straight line
    W_COLL = 500.0       
    W_MILL = -100.0      # NEGATIVE VALUE to reward milling
    W_EXPLO = 0.0
else:
    W_EFFORT = 1   
    W_DISP = 0.0
    W_POL = -0.0
    W_COLL = 500.0
    W_MILL = 20.0
    W_EXPLO = -50.0