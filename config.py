import os

# Env / Physics
DT = 0.1                
ARENA_RADIUS = 50.0
NB_DRONES = 40          
MAX_SPEED = 2.0   
NEIGHBORS = 3   # Number of closest neighbors taken into account for interactions      

# Optimization
POP_SIZE_CPU = 150        
GEN_CPU = 20              

POP_SIZE_GPU = 100      
GEN_GPU = 20             

SIM_STEPS = 500          
VISU_STEPS = 1000      

# Cost Function Weights
W_EFFORT = 0.05   
W_DISP = 1.0
W_POL = -2.0
W_COLL = 5000.0 

# Hardware
try:
    import cupy as cp
    GPU_AVAILABLE = True
except ImportError:
    GPU_AVAILABLE = False
    
    
    