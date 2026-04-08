import os
import re
from datetime import datetime
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def parse_reports(log_dir: str, start_date: str, end_date: str) -> pd.DataFrame:
    """Extraie paramètres GA sur période."""
    start_dt = datetime.strptime(start_date, "%Y-%m-%d")
    end_dt = datetime.strptime(end_date, "%Y-%m-%d").replace(hour=23, minute=59, second=59)
    
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
    """Génère et sauvegarde heatmap corrélation."""
    df_params = df.drop(columns=['Generation', 'Cost', 'Session'], errors='ignore')
    
    plt.figure(figsize=(14, 12))
    sns.heatmap(df_params.corr(), annot=True, cmap='coolwarm', fmt=".2f")
    plt.title("Parameter Correlation Matrix")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

if __name__ == "__main__":
    LOGS_DIR = "logs"
    OUT_DIR = "analyses"
    START_DATE = "2025-04-01" 
    END_DATE = "2026-04-08"   

    os.makedirs(OUT_DIR, exist_ok=True)

    df_res = parse_reports(LOGS_DIR, START_DATE, END_DATE)
    
    if not df_res.empty:
        df_top = df_res.nsmallest(max(1, int(len(df_res) * 0.1)), 'Cost')
        
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"corr_matrix_{timestamp}.png"
        out_path = os.path.join(OUT_DIR, filename)
        
        plot_patterns(df_top, out_path)
        print(f"[Analyse] Sauvegarde : {out_path} ({len(df_res)} individus).")
    else:
        print("[Analyse] Aucune donnée trouvée.")