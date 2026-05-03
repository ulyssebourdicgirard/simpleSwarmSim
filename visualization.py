import os
import tempfile
import shutil
import concurrent.futures
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from PIL import Image

import config
from config import ARENA_RADIUS, NEIGHBORS

def generate_interactive_html(log_path, pos, phi, vz, params):
    """
    [Unchanged] Interactive 3D HTML export via Plotly.
    """
    import sys
    try:
        import plotly.graph_objects as go
    except ImportError:
        print(f"\n[Visu] Avertissement : Plotly n'est pas installé dans cet environnement.")
        print(f"[Visu] Interpréteur utilisé : {sys.executable}")
        print(f"[Visu] Le rendu HTML interactif a été ignoré, mais votre GIF est prêt.")
        return

    suffix = "3D"
    output_html = os.path.join(log_path, f"animation_{suffix}_interactive.html")
    
    step = 4    # Divides number of frames by 4
    pos_sub = pos[::step]
    phi_sub = phi[::step]
    vz_sub = vz[::step]

    u_raw = np.cos(phi_sub[0])
    v_raw = np.sin(phi_sub[0])
    w_raw = vz_sub[0]
    
    mag_init = np.sqrt(u_raw**2 + v_raw**2 + w_raw**2)
    u_init = u_raw / mag_init
    v_init = v_raw / mag_init
    w_init = w_raw / mag_init

    fig = go.Figure(
        data=[go.Cone(
            x=pos_sub[0, :, 0],
            y=pos_sub[0, :, 1],
            z=pos_sub[0, :, 2],
            u=u_init,
            v=v_init,
            w=w_init,
            sizemode="absolute",
            sizeref=2.0,
            anchor="tail",
            colorscale="Blues",
            showscale=False
        )]
    )

    frames = []
    for t in range(len(pos_sub)):
        u_t_raw = np.cos(phi_sub[t])
        v_t_raw = np.sin(phi_sub[t])
        w_t_raw = vz_sub[t]
        
        mag_t = np.sqrt(u_t_raw**2 + v_t_raw**2 + w_t_raw**2)
        
        frames.append(go.Frame(
            data=[go.Cone(
                x=pos_sub[t, :, 0],
                y=pos_sub[t, :, 1],
                z=pos_sub[t, :, 2],
                u=u_t_raw / mag_t,
                v=v_t_raw / mag_t,
                w=w_t_raw / mag_t,
                sizemode="absolute",
                sizeref=2.0,
                anchor="tail"
            )],
            name=str(t)
        ))
    
    fig.frames = frames

    sliders = [dict(
        active=0,
        yanchor="top",
        xanchor="left",
        currentvalue=dict(font=dict(size=14), prefix="Frame : ", visible=True, xanchor="right"),
        transition=dict(duration=0), 
        pad=dict(b=10, t=50),
        len=0.9,
        x=0.1,
        y=0,
        steps=[dict(
            args=[[str(k)], dict(frame=dict(duration=0, redraw=True), transition=dict(duration=0), mode="immediate")],
            label=str(k * step), 
            method="animate"
        ) for k in range(len(pos_sub))]
    )]

    fig.update_layout(
        title=f"Replay Interactif 3D : y_att={params.get('y_att', 0):.2f}",
        uirevision='constant', 
        scene=dict(
            xaxis=dict(range=[-ARENA_RADIUS, ARENA_RADIUS]),
            yaxis=dict(range=[-ARENA_RADIUS, ARENA_RADIUS]),
            zaxis=dict(range=[0, 15]),
            aspectmode='manual',
            aspectratio=dict(x=1, y=1, z=0.5)
        ),
        updatemenus=[dict(
            type="buttons",
            showactive=False,
            y=0,
            x=0.05,
            xanchor="right",
            yanchor="top",
            pad=dict(t=50, r=10),
            buttons=[
                dict(
                    label="Play (Normale)",
                    method="animate",
                    args=[None, dict(frame=dict(duration=100, redraw=True), transition=dict(duration=0), fromcurrent=True, mode="immediate")]
                ),
                dict(
                    label="Play (Rapide)",
                    method="animate",
                    args=[None, dict(frame=dict(duration=20, redraw=True), transition=dict(duration=0), fromcurrent=True, mode="immediate")]
                ),
                dict(
                    label="Pause",
                    method="animate",
                    args=[[None], dict(frame=dict(duration=0, redraw=False), mode="immediate", transition=dict(duration=0))]
                )
            ]
        )],
        sliders=sliders
    )

    fig.write_html(output_html)


def render_single_frame(args):
    """
    Worker function to render an isolated frame in parallel.
    Uses its own plot instance to ensure thread safety.
    """
    frame_idx, pos_f, phi_f, vz_f, cov_f, title, is_3d, full_milling, arena_radius, temp_dir = args
    
    # Strictly enforce Agg backend for worker process
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    
    fig = plt.figure(figsize=(8, 8))
    
    if is_3d:
        ax = fig.add_subplot(111, projection='3d')
        theta_circle = np.linspace(0, 2*np.pi, 100)
        
        if full_milling:
            barycenter = np.mean(pos_f, axis=0)
            max_dist = np.max(np.linalg.norm(pos_f[:, 0:2] - barycenter[0:2], axis=-1))
            margin = max(5.0, max_dist * 1.5)
            
            ax.set_xlim(barycenter[0] - margin, barycenter[0] + margin)
            ax.set_ylim(barycenter[1] - margin, barycenter[1] + margin)
            
            z_margin = max(5.0, np.max(np.abs(pos_f[:, 2] - barycenter[2])) * 1.5)
            ax.set_zlim(max(0, barycenter[2] - z_margin), barycenter[2] + z_margin)
        else:
            ax.set_xlim(-arena_radius-1, arena_radius+1)
            ax.set_ylim(-arena_radius-1, arena_radius+1)
            ax.set_zlim(0, 10)
            
        ax.set_title(title)
        ax.plot(arena_radius * np.cos(theta_circle), arena_radius * np.sin(theta_circle), 0, color='r', ls='--', alpha=0.5)
        
        if cov_f is not None:
            x_grid = np.linspace(-arena_radius, arena_radius, cov_f.shape[0])
            y_grid = np.linspace(-arena_radius, arena_radius, cov_f.shape[1])
            X, Y = np.meshgrid(x_grid, y_grid)
            ax.contourf(X, Y, cov_f.T, zdir='z', offset=0, cmap='YlGn', alpha=0.3, levels=[0.5, 1.0])
        
        px, py, pz = pos_f[:, 0], pos_f[:, 1], pos_f[:, 2]
        dx, dy = np.cos(phi_f), np.sin(phi_f)
        dz = vz_f if vz_f is not None else np.zeros_like(dx)
        
        ax.quiver(px, py, pz, dx, dy, dz, length=2, normalize=True, color='dodgerblue')
        
    else:
        ax = fig.add_subplot(111)
        if full_milling:
            ax.autoscale(False)
            barycenter = np.mean(pos_f, axis=0)
            max_dist = np.max(np.linalg.norm(pos_f - barycenter, axis=-1))
            margin = max(5.0, max_dist * 1.5)
            ax.set_xlim(barycenter[0] - margin, barycenter[0] + margin)
            ax.set_ylim(barycenter[1] - margin, barycenter[1] + margin)
        else:
            ax.set_xlim(-arena_radius-1, arena_radius+1)
            ax.set_ylim(-arena_radius-1, arena_radius+1)
            ax.add_patch(Circle((0, 0), arena_radius, color='r', fill=False, ls='--', alpha=0.5))
            
        if cov_f is not None:
            extent = (-arena_radius, arena_radius, -arena_radius, arena_radius)
            ax.imshow(cov_f.T, extent=extent, origin='lower', cmap='YlGn', alpha=0.3, zorder=0, vmin=0, vmax=1)
        
        ax.set_title(title)
        ax.set_aspect('equal')
        ax.grid(True, alpha=0.2)
        ax.quiver(pos_f[:, 0], pos_f[:, 1], 
                  np.cos(phi_f), np.sin(phi_f), 
                  color='dodgerblue', scale=25, width=0.005)

    # Save to dedicated temporary file
    out_path = os.path.join(temp_dir, f"frame_{frame_idx:05d}.png")
    plt.savefig(out_path, dpi=80, bbox_inches='tight') # Reduced DPI slightly for faster I/O
    plt.close(fig)
    return out_path


def generate_gif_from_log(log_path):
    """
    Visualization bridge.
    Reads the trajectory.npz file generated by the Logger and creates a GIF using all CPU cores.
    """
    import config
    suffix = "3D" if config.ENABLE_3D else "2D"
    trajectory_file = os.path.join(log_path, f"trajectory_{suffix}.npz")
    
    if not os.path.exists(trajectory_file):
        trajectory_file = os.path.join(log_path, "trajectory.npz")
        
    if not os.path.exists(trajectory_file):
        print(f"[Visu] Error: No trajectory file in {log_path}")
        return

    print(f"[Visu] Loading {trajectory_file}...")
    data = np.load(trajectory_file, allow_pickle=True)
    
    pos = data['pos'] 
    phi = data['phi'] 
    coverage = data['coverage'] if 'coverage' in data.files else None
    vz_data = data['vz'] if 'vz' in data.files else None
    
    params = data['params'].item() 
    title = f"Replay: y_att={params['y_att']:.2f}, Neigh={params.get('NEIGHBORS', NEIGHBORS)}"
    
    is_3d = config.ENABLE_3D
    full_milling = getattr(config, "FULL_MILLING_MODE", False)
    
    output_gif = os.path.join(log_path, f"animation_{suffix}.gif")
    
    # Create a temporary directory for parallel frame renders
    temp_dir = tempfile.mkdtemp()
    
    tasks = []
    for frame_idx in range(len(pos)):
        cov_f = coverage[frame_idx] if coverage is not None else None
        vz_f = vz_data[frame_idx] if vz_data is not None else None
        tasks.append((
            frame_idx, pos[frame_idx], phi[frame_idx], vz_f, cov_f,
            title, is_3d, full_milling, ARENA_RADIUS, temp_dir
        ))

    num_cores = os.cpu_count()
    print(f"[Visu] Generating frames on {num_cores} CPU cores...")
    
    frame_paths = []
    # Utilize multiprocessing to crunch the matplotlib queue
    with concurrent.futures.ProcessPoolExecutor(max_workers=num_cores) as executor:
        for path in executor.map(render_single_frame, tasks):
            frame_paths.append(path)

    print(f"[Visu] Compiling {len(frame_paths)} frames into GIF: {output_gif} (patience...)")
    
    # Use generator to prevent loading thousands of arrays into RAM at once
    frame_paths.sort()
    image_generator = (Image.open(p).convert('P', palette=Image.ADAPTIVE) for p in frame_paths)
    
    first_frame = next(image_generator)
    first_frame.save(
        output_gif,
        format='GIF',
        save_all=True,
        append_images=image_generator,
        duration=33, # ~30 fps
        loop=0,
        optimize=False
    )
    
    # Clean up the large pool of temporary files
    shutil.rmtree(temp_dir)
    
    if config.ENABLE_3D:
        vz_to_pass = vz_data if vz_data is not None else np.zeros_like(phi)
        generate_interactive_html(log_path, pos, phi, vz_to_pass, params)
        
    print("[Visu] Done.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        generate_gif_from_log(sys.argv[1])
    else:
        print("Usage: python visualization.py logs/DIR_NAME")