import os
import re
from pathlib import Path
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

LOGS_DIR = "./logs"

CURRENT_TIME = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
OUTPUT_DIR = f"./analyses/analysis_{CURRENT_TIME}"

ENABLE_TIME_FILTER = True 

START_DATETIME = "2026-05-10 00:00:00"
END_DATETIME = "2026-05-10 23:59:59"

sns.set_theme(style="whitegrid", context="paper", font_scale=1.2)
plt.rcParams['font.family'] = 'serif' 

def extract_metrics_from_text(text):
    f_val, c_val = None, None
    
    cost_match = re.search(r'(?:Fitness|Cost|Score|Coût|Cout).{0,30}?([-+]?\d*\.\d+|\d+)', text, re.IGNORECASE)
    if cost_match:
        f_val = float(cost_match.group(1))
        
    coverage_match = re.search(r'(?:Coverage|Couverture).{0,30}?([-+]?\d*\.\d+|\d+)', text, re.IGNORECASE)
    if coverage_match:
        c_val = float(coverage_match.group(1))
        
    return f_val, c_val

def parse_markdown_report(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()

    data = {'file_path': str(filepath), 'run_name': filepath.parent.name}

    time_match = re.search(r'(\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2})', filepath.parent.name)
    if time_match:
        data['Timestamp'] = datetime.strptime(time_match.group(1), "%Y-%m-%d_%H-%M-%S")
    else:
        data['Timestamp'] = datetime.fromtimestamp(os.path.getmtime(filepath))

    map_match = re.search(r'MAP_STRATEGY[^\w]*([a-zA-Z0-9_]+)', content, re.IGNORECASE)
    explo_match = re.search(r'EXPLO_STRATEGY[^\w]*([a-zA-Z0-9_]+)', content, re.IGNORECASE)
    
    if map_match and explo_match:
        data['Map Strategy'] = map_match.group(1)
        data['Explo Strategy'] = explo_match.group(1)
    else:
        print(f"   [X] Ignored (Strategies missing) : {filepath.parent.name}")
        return None

    data['Cost'], data['Coverage (%)'] = None, None
    source_trouvee = "Not found"

    f_val, c_val = extract_metrics_from_text(content)
    if f_val is not None: data['Cost'] = f_val
    if c_val is not None: data['Coverage (%)'] = c_val
    if f_val is not None or c_val is not None:
        source_trouvee = "report_3D.md"

    if data['Cost'] is None or data['Coverage (%)'] is None:
        local_log_path = filepath.parent / "execution.log"
        if local_log_path.exists():
            with open(local_log_path, 'r', encoding='utf-8', errors='replace') as f_log:
                f_val, c_val = extract_metrics_from_text(f_log.read())
                if f_val is not None: data['Cost'] = f_val
                if c_val is not None: data['Coverage (%)'] = c_val
                if f_val is not None or c_val is not None:
                    source_trouvee = "execution.log (Local)"

    if data['Cost'] is None or data['Coverage (%)'] is None:
        sweep_log_path = filepath.parent.parent / "execution.log"
        if sweep_log_path.exists():
            with open(sweep_log_path, 'r', encoding='utf-8', errors='replace') as f_sweep:
                sweep_content = f_sweep.read()
                
                m_strat = re.escape(data['Map Strategy'])
                e_strat = re.escape(data['Explo Strategy'])
                
                pattern = f"carte:\\s*{m_strat}.*?exploration:\\s*{e_strat}(.*?)(?:\n>>>|\\Z)"
                block_match = re.search(pattern, sweep_content, re.DOTALL | re.IGNORECASE)
                
                if block_match:
                    f_val, c_val = extract_metrics_from_text(block_match.group(1))
                    if f_val is not None: data['Cost'] = f_val
                    if c_val is not None: data['Coverage (%)'] = c_val
                    if f_val is not None or c_val is not None:
                        source_trouvee = "execution.log (Sweep Parent)"

    if data['Cost'] is None and data['Coverage (%)'] is None:
         print(f"   [!] Strategies OK, but metrics missing : {filepath.parent.name}")
    else:
         print(f"   [V] Success : {filepath.parent.name} (Source: {source_trouvee})")
         
    return data

def build_dataset(base_dir):
    all_data = []
    base_path = Path(base_dir)
    print(f"Searching for 'report_3D.md' in {base_path.resolve()} ...")
    
    for file_path in base_path.rglob("report_3D.md"):
        run_data = parse_markdown_report(file_path)
        if run_data:
            all_data.append(run_data)

    df = pd.DataFrame(all_data)
    return df

def filter_dataset_by_time(df):
    if df.empty or 'Timestamp' not in df.columns:
        return df

    start_dt = pd.to_datetime(START_DATETIME)
    end_dt = pd.to_datetime(END_DATETIME)

    mask = (df['Timestamp'] >= start_dt) & (df['Timestamp'] <= end_dt)
    filtered_df = df.loc[mask].copy()

    print(f"\nTime filter applied ({START_DATETIME} -> {END_DATETIME}) :")
    print(f"  - Runs before filtering : {len(df)}")
    print(f"  - Runs after filtering : {len(filtered_df)}")

    return filtered_df

def plot_bar_metrics(df, metric, output_dir):
    if metric not in df.columns or df[metric].dropna().empty:
        print(f"   -> Bar chart ignored : missing data '{metric}'.")
        return
        
    plt.figure(figsize=(10, 6))
    ax = sns.barplot(
        data=df, x='Map Strategy', y=metric, hue='Explo Strategy',
        capsize=.1, err_kws={'linewidth': 1.5}, palette="viridis"
    )
    plt.title(f'Exploration Strategy Comparison: {metric}', pad=15, fontweight='bold')
    plt.xlabel('Information Sharing Topology')
    plt.ylabel(metric)
    plt.legend(title='Decision Strategy', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    filename = Path(output_dir) / f'bar_comparison_{metric.replace(" ", "_").replace("%", "pct")}.png'
    plt.savefig(filename, dpi=300)
    plt.close()

def plot_box_metrics(df, metric, output_dir):
    if metric not in df.columns or df[metric].dropna().empty:
        print(f"   -> Boxplot ignored : missing data '{metric}'.")
        return
        
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x='Map Strategy', y=metric, hue='Explo Strategy', palette="Set2")
    sns.stripplot(data=df, x='Map Strategy', y=metric, hue='Explo Strategy', dodge=True, color='black', alpha=0.4, size=4)
    handles, labels = plt.gca().get_legend_handles_labels()
    if len(handles) >= 2:
        plt.legend(handles[:2], labels[:2], title='Decision Strategy', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.title(f'Robustness and Distribution: {metric}', pad=15, fontweight='bold')
    plt.xlabel('Information Sharing Topology')
    plt.ylabel(metric)
    plt.tight_layout()
    filename = Path(output_dir) / f'boxplot_{metric.replace(" ", "_").replace("%", "pct")}.png'
    plt.savefig(filename, dpi=300)
    plt.close()

if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    dataset = build_dataset(LOGS_DIR)
    
    if dataset.empty:
        print("\n[!] No valid data could be extracted.")
    else:
        if ENABLE_TIME_FILTER:
            dataset = filter_dataset_by_time(dataset)

        if not dataset.empty:
            print("\n--- Final Data Overview ---")
            print(dataset[['Timestamp', 'Map Strategy', 'Explo Strategy', 'Cost', 'Coverage (%)']].head())
            
            dataset.to_csv(Path(OUTPUT_DIR) / "aggregated_results.csv", index=False)
            
            plot_bar_metrics(dataset, 'Cost', OUTPUT_DIR)
            plot_bar_metrics(dataset, 'Coverage (%)', OUTPUT_DIR)
            plot_box_metrics(dataset, 'Cost', OUTPUT_DIR)
            plot_box_metrics(dataset, 'Coverage (%)', OUTPUT_DIR)
            
            print(f"\nAnalysis complete. Results and graphs in : {OUTPUT_DIR}/")
        else:
            print("\nAll runs were excluded by the time filter.")