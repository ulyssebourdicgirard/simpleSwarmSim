import os
import subprocess
import sys 
import datetime

# Configurations to test
map_strategy = ["global", "local_individual", "local_shared"]
explo_strategy = ["local_gradient", "global_best"]

timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_dir = os.path.join("logs", f"{timestamp}_explo_sweep")
os.makedirs(log_dir, exist_ok=True)
os.environ['LOG_DIR_OVERRIDE'] = log_dir

log_file = os.path.join(log_dir, "execution.log")
error_file = os.path.join(log_dir, "errors.log")

with open(log_file, 'w') as out_file, open(error_file, 'w') as err_file:
    for m_strat in map_strategy:
        for e_strat in explo_strategy:
            os.environ['MAP_STRATEGY_OVERRIDE'] = m_strat
            os.environ['EXPLO_STRATEGY_OVERRIDE'] = e_strat
            
            print(f"\n>>> Stratégie de partage de la carte: {m_strat}", file=out_file)
            print(f"\n>>> Stratégie d'exploration: {e_strat}", file=out_file)

            try:
                subprocess.run(
                [sys.executable, "Mk3_PyTorch_Full.py"],
                stdout=out_file,
                stderr=err_file,
                text=True,
                check=True
                )
            except subprocess.CalledProcessError:
                print("Une erreur s'est produite, consultez le fichier pour plus de détails...")

    print("\n>>> Balayage terminé.", file=out_file)