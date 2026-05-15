import os
import re
from datetime import datetime
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def parse_reports(log_dir: str, start_date: str, end_date: str) -> pd.DataFrame:
    """Extraie paramètres GA sur période."""
    start_dt = datetime.strptime(start_date, "%Y-%m-%d %H:%M:%S")
    end_dt = datetime.strptime(end_date, "%Y-%m-%d %H:%M:%S")
    
    data = []
    pattern = re.compile(r"\| (\d+)\s+\| ([\d\.\-]+)\s+\| [\d\.\-]+\s+\| (.*) \|")
    
    if not os.path.exists(log_dir):
        return pd.DataFrame()

    for folder in os.listdir(log_dir):
        folder_path = os.path.join(log_dir, folder)
        if not os.path.isdir(folder_path):
            continue
            
        try:
            folder_dt = datetime.strptime(folder[:19], "%Y-%m-%d_%H-%M-%S")
            if not (start_dt <= folder_dt <= end_dt):
                continue
        except ValueError:
            continue

        for file in os.listdir(folder_path):
            if file.startswith("report") and file.endswith(".md"):
                with open(os.path.join(folder_path, file), 'r', encoding='utf-8') as f:
                    for line in f:
                        match = pattern.search(line)
                        if match:
                            gen, cost, params_str = match.groups()
                            row = {'Generation': int(gen), 'Cost': float(cost), 'Session': folder_dt}
                            
                            pairs = re.findall(r"([a-zA-Z0-9_]+)=([\d\.\-]+)", params_str)
                            for k, v in pairs:
                                row[k] = float(v)
                            data.append(row)
                            
    return pd.DataFrame(data)

def plot_patterns(df: pd.DataFrame, output_path: str):
    """Génère et sauvegarde heatmap corrélation propre."""
    df_params = df.drop(columns=['Generation', 'Cost', 'Session'], errors='ignore')
    df_params = df_params.loc[:, df_params.std() > 0]
    # Calcul de la matrice de corrélation
    corr = df_params.corr()
    mask = np.triu(np.ones_like(corr, dtype=bool))
    
    # Configuration de la figure
    plt.figure(figsize=(12, 10))
    
    sns.heatmap(corr, mask=mask, annot=True, cmap='RdYlGn', fmt=".2f",
                square=True, linewidths=.5, cbar_kws={"shrink": .8},
                annot_kws={"size": 9})
    
    plt.title("Parameter Correlation Matrix", pad=20, fontsize=16)
    plt.tight_layout()
    
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    LOGS_DIR = "logs"
    OUT_DIR = "analyses"
    
    START_DATE = "2026-05-14 13:55:00" 
    END_DATE = "2026-05-14 18:45:00"   

    os.makedirs(OUT_DIR, exist_ok=True)

    df_res = parse_reports(LOGS_DIR, START_DATE, END_DATE)
    
    if not df_res.empty:
        df_best_per_run = df_res.loc[df_res.groupby('Session')['Cost'].idxmin()]
        
        df_top = df_best_per_run 
        
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"corr_matrix_{timestamp}.png"
        out_path = os.path.join(OUT_DIR, filename)
        
        plot_patterns(df_top, out_path)
        print(f"[Analyse] Sauvegarde : {out_path} ({len(df_top)} individus uniques analysés).")
    else:
        print("[Analyse] Aucune donnée trouvée.")