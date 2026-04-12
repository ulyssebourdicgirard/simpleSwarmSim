import os
import subprocess
import sys 

# Configurations to test
drones_to_test = [5, 10, 15, 20, 25, 30]

for nb in drones_to_test:
    print(f"\n>>> Lancement de la simulation avec {nb} drones...")
    
    os.environ['NB_DRONES_OVERRIDE'] = str(nb)
    
    # Calling main script
    subprocess.run([sys.executable, "Mk3_PyTorch_Full.py"], check=True)

print("\nBalayage terminé.")