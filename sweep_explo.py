import os
import subprocess
import sys 

# Configurations to test
map_strategy = ["global", "local_individual", "local_shared"]
explo_strategy = ["local_gradient", "global_closest"]

for m_strat in map_strategy:
    for e_strat in explo_strategy:
        print(f"\n>>> Stratégie de partage de la carte: {m_strat}")
        print(f"\n>>> Stratégie d'exploration: {e_strat}")
        
        os.environ['MAP_STRATEGY_OVERRIDE'] = m_strat
        os.environ['EXPLO_STRATEGY_OVERRIDE'] = e_strat
        
        # Calling main script
        subprocess.run([sys.executable, "Mk3_PyTorch_Full.py"], check=True)

print("\n>>> Balayage terminé.")
