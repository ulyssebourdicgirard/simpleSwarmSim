import os

# Env / Physics
ENABLE_3D = True    # True: 3D, False: 2D
DT = 0.1                
ARENA_RADIUS = 50.0
NB_DRONES = 20          
MAX_SPEED = 2.0   
NEIGHBORS = None   # Number of closest neighbors taken into account for interactions  
# NEIGHBORS = None for no limit (bypasses partition for better performance)
COLLISION_DIST = 0.4

# Optimization
POP_SIZE_CPU = 150        
GEN_CPU = 20              

POP_SIZE_GPU = 5000      
GEN_GPU = 20             

SIM_STEPS = 500          
VISU_STEPS = 1000      

# Cost Function Weights
W_EFFORT = 1   
W_DISP =0.0
W_POL = -0.0
W_COLL = 500.0
W_MILL = -20.0

# Hardware
try:
    import cupy as cp
    GPU_AVAILABLE = True
except ImportError:
    GPU_AVAILABLE = False
    
    
    