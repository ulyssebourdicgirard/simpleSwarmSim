import os
import time
import datetime
import numpy as np

class ExperimentLogger:
    def __init__(self, mode="CPU"):
        # Timestamp
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        self.log_dir = os.path.join("logs", f"{timestamp}_{mode}")
        os.makedirs(self.log_dir, exist_ok=True)
        
        # Files
        self.report_path = os.path.join(self.log_dir, "report.md")
        self.trajectory_path = os.path.join(self.log_dir, "trajectory.npz")
        
        # Init Markdown Header
        with open(self.report_path, 'w', encoding='utf-8') as f:
            f.write(f"# Experiment Report - {mode}\n")
            f.write(f"**Date:** {timestamp}\n\n")
            f.write("## 1. Initial Configuration\n")
            f.write("| Parameter | Value |\n")
            f.write("| :--- | :--- |\n") 
            
    def log_config(self, config_module):
        """Log constants from config.py"""
        with open(self.report_path, 'a', encoding='utf-8') as f:
            for key in dir(config_module):
                if key.isupper():
                    val = getattr(config_module, key)
                    f.write(f"| {key:<20} | {str(val):<10} |\n")
            
            f.write("\n## 2. Optimization Evolution\n")
            
            header = f"| {'Gen':^4} | {'Best Cost':^12} | {'Time (s)':^10} | {'All Parameters':^140} |"
            separator = f"| :--: | :{'':-^10}: | :{'':-^8}: | :{'':-^138} |"
            
            f.write(header + "\n")
            f.write(separator + "\n")

    def log_generation(self, gen, cost, duration, best_params):
        """
        Adds a line to the Markdown table for each generation.
        Now uses fixed-width formatting to ensure perfect alignment in raw text.
        """
        with open(self.report_path, 'a', encoding='utf-8') as f:
            params_list = []
            for k, v in best_params.__dict__.items():
                if isinstance(v, float):
                    params_list.append(f"{k}={v:.2f}")
                else:
                    params_list.append(f"{k}={v}")
            
            params_str = ", ".join(params_list)
            
            
            line = f"| {gen:02d}   | {cost:<12.4f} | {duration:<10.2f} | {params_str:<140} |\n"
            f.write(line)
    
    def save_trajectory(self, pos, phi, v, params):
        """
        C (NPZ Format): Saves the complete trajectory for replay.
        Data must be numpy arrays (not lists, not cupy).
        """
        # We also save the final parameters in the npz for machine reference
        param_dict = params.__dict__
        
        np.savez_compressed(
            self.trajectory_path,
            pos=pos,
            phi=phi,
            v=v,
            params=param_dict
        )
        print(f"\n[Logger] Trajectory saved: {self.trajectory_path}")
        return self.trajectory_path

    def close(self):
        with open(self.report_path, 'a', encoding='utf-8') as f:
            f.write("\n**End of experiment.**\n")