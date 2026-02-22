from dataclasses import dataclass
import numpy as np
import config
from config import DT, ARENA_RADIUS, W_EFFORT, W_DISP, W_POL, W_COLL, W_MILL, NEIGHBORS, COLLISION_DIST, Z_MIN, Z_MAX

@dataclass
class SwarmParams:
    y_att: float 
    y_ali: float
    y_f: float    
    d0_att: float
    l_att: float
    l_ali: float
    alpha_att: float = 1.0 
    alpha_ali: float = 0.0 
    # 3D Parameters
    y_z: float = 1.0
    l_z: float = 3.0
    a_z: float = 1.0
    d0_z: float = 0.5
    sigma_z: float = 1.0 
    y_z_w: float = 2.0
    dz_w: float = 1.0

def get_deterministic_initial_state(n_batch, n_drones, xp=np):
    # Circle layout (Deterministic)
    radius = ARENA_RADIUS//2
    theta = xp.linspace(0, 2*xp.pi, n_drones, endpoint=False)
    
    # Broadcast (Batch, N)
    if n_batch > 1:
        theta = xp.tile(theta, (n_batch, 1))
        
    x = radius * xp.cos(theta)
    y = radius * xp.sin(theta)
    
    # State vectors
    phi = theta + 0.1 # Outward looking + offset
    v = xp.zeros_like(theta)
    
    if config.ENABLE_3D:
        # Added Z axis
        z = xp.random.uniform(config.Z_MIN + 1.0, config.Z_MAX - 1.0, size=theta.shape)
        pos = xp.stack([x, y, z], axis=-1)
        vz = xp.zeros_like(theta)
        return pos, phi, v, vz
    else:
        # 2D version
        pos = xp.stack([x, y], axis=-1)
        return pos, phi, v, None

def compute_derivatives(pos, phi, v, p, vz=None, xp=np):
    # Unpack
    y_att, y_ali, y_f = p.y_att, p.y_ali, p.y_f
    d0_att, l_att, l_ali = p.d0_att, p.l_att, p.l_ali

    # Broadcast (Batch, N, 1) => All in one calculus
    if hasattr(y_att, 'ndim') and y_att.ndim == 2:
        y_att, y_ali = y_att[..., None], y_ali[..., None]
        d0_att, l_att, l_ali = d0_att[..., None], l_att[..., None], l_ali[..., None]

    # --- Wall Interaction (Cylindrical Arena) ---
    dist_xy = xp.linalg.norm(pos[..., 0:2], axis=-1) if config.ENABLE_3D else xp.linalg.norm(pos, axis=-1)
    
    # Heading error rel. to center
    angle_to_center = xp.arctan2(-pos[..., 1], -pos[..., 0])
    psi_center = (angle_to_center - phi + xp.pi) % (2 * xp.pi) - xp.pi
    
    # Exponential repulsion
    w_force = 100.0 * xp.exp(2.0 * (dist_xy - ARENA_RADIUS)) * xp.sin(psi_center)

    # --- Social Interaction ---
    pos_i = xp.expand_dims(pos, -2) 
    pos_j = xp.expand_dims(pos, -3)
    
    r_ij = pos_i - pos_j
    
    if config.ENABLE_3D:
        # 3D Version
        dxy_sq = xp.sum((pos_i[..., 0:2] - pos_j[..., 0:2])**2, axis=-1)
        dz_sq = ((pos_i[..., 2] - pos_j[..., 2]) / p.sigma_z)**2
        d_ij = xp.sqrt(dxy_sq + dz_sq)
    else:
        # 2D Version
        d_ij = xp.linalg.norm(r_ij, axis=-1)
    
    # Mask self
    eye_mask = xp.eye(d_ij.shape[-1], dtype=bool)
    if len(d_ij.shape) > 2: 
        eye_mask = xp.broadcast_to(eye_mask, d_ij.shape)
    d_ij = xp.maximum(d_ij, 0.01)

    # Angles
    a_ij = xp.arctan2(r_ij[..., 1], r_ij[..., 0])
    psi = (a_ij - phi[..., :, None] + xp.pi) % (2 * xp.pi) - xp.pi
    d_phi = (phi[..., None, :] - phi[..., :, None] + xp.pi) % (2 * xp.pi) - xp.pi

    # Forces 
    w_att = 1.0 / (1.0 + (d_ij / l_att)**2)
    f_att = y_att * ((d_ij / d0_att) - 1.0) * w_att * xp.sin(psi)

    w_ali = 1.0 / (1.0 + (d_ij / l_ali)**2)
    f_ali = y_ali * ((d_ij / d0_att) + 1.0) * w_ali * xp.sin(d_phi)

    # Collision avoidance
    f_rep = 0 # Disabled because of bad effects

    # NEIGHBORS logic
    if NEIGHBORS == 0:  
        social_sum = xp.zeros_like(phi)
        rep_sum = xp.zeros_like(phi)
        
    elif NEIGHBORS is None or NEIGHBORS >= (d_ij.shape[-1] - 1):    
        social_sum = xp.sum((f_att + f_ali) * (~eye_mask), axis=-1)
        rep_sum = xp.sum(f_rep * (~eye_mask), axis=-1)
        
    else:   
        d_topo = d_ij.copy()
        d_topo[eye_mask] = xp.inf 
        k_idx = NEIGHBORS - 1
        threshold = xp.partition(d_topo, k_idx, axis=-1)[..., k_idx:k_idx+1] 
        top_k_mask = d_topo <= threshold
        
        social_sum = xp.sum((f_att + f_ali) * top_k_mask, axis=-1)
        rep_sum = xp.sum(f_rep * top_k_mask, axis=-1)
    
    # Noise & Dynamics
    noise = xp.random.uniform(-0.1, 0.1, size=phi.shape[-1])
    
    phi_dot_social = xp.clip(social_sum + noise, -3.0, 3.0)
    phi_dot_vital = xp.clip(rep_sum + w_force, -10.0, 10.0)
    
    phi_dot = phi_dot_social + phi_dot_vital
    acc = y_f * (1.0 - v)

    vz_dot = 0.0
    if config.ENABLE_3D and vz is not None:
        
        # Social vertical alignment
        dz_ij = pos_j[..., 2] - pos_i[..., 2]
        term_tanh = xp.tanh((dz_ij - xp.sign(dz_ij) * p.d0_z) / p.a_z)
        term_exp = xp.exp(-(d_ij / p.l_z)**2)
        f_vz = p.y_z * term_tanh * term_exp
        
        if NEIGHBORS == 0:
            vz_dot_social = xp.zeros_like(vz)
        else:
            vz_dot_social = xp.sum(f_vz * (~eye_mask), axis=-1)
            
        # Floor & Ceiling interactions
        dz_floor = pos[..., 2] - config.Z_MIN
        f_floor = 2.0 * p.y_z_w / (1.0 + xp.exp((dz_floor - p.dz_w) / p.dz_w))
        
        dz_ceil = config.Z_MAX - pos[..., 2]
        f_ceil = -2.0 * p.y_z_w / (1.0 + xp.exp((dz_ceil - p.dz_w) / p.dz_w))
        
        vz_dot = vz_dot_social + f_floor + f_ceil
    
    if config.ENABLE_3D:
        return acc, phi_dot, vz_dot
    return acc, phi_dot, None

def compute_metrics(pos, phi, phi_dot, v, xp=np):
    """
    Centralized Cost Function Logic.
    Handles both CPU (N, 2) and GPU (Batch, N, 2) arrays.
    """
    # Detect batch mode based on dimensions
    is_batch = (pos.ndim == 3)
    axis_agent = 1 if is_batch else 0
    
    # Effort: Minimize turn rate
    c_effort = xp.sum(xp.abs(phi_dot), axis=axis_agent) * W_EFFORT
    
    # Dispersion: Target 5.0m from center
    center = xp.mean(pos, axis=axis_agent, keepdims=True)
    d_center = xp.linalg.norm(pos - center, axis=-1)
    # Mean distance of agents to swarm center
    c_disp = xp.abs(xp.mean(d_center, axis=axis_agent) - 5.0) * W_DISP
    
    # Polarization: Maximize alignment (minimize 1 - Pol)
    u_vec = xp.cos(phi)
    v_vec = xp.sin(phi)
    pol = xp.sqrt(xp.mean(u_vec, axis=axis_agent)**2 + xp.mean(v_vec, axis=axis_agent)**2)
    c_pol = (1.0 - pol) * W_POL
    
    # Collisions: Distance < 0.6m
    if is_batch:
        r_ij = pos[:, :, None, :] - pos[:, None, :, :] # (B, N, N, 2)
    else:
        r_ij = pos[:, None, :] - pos[None, :, :]       # (N, N, 2)
        
    d_ij = xp.linalg.norm(r_ij, axis=-1)
    
    # Mask diagonal (self-distance)
    eye = xp.eye(pos.shape[axis_agent], dtype=bool)
    if is_batch:
        eye = xp.broadcast_to(eye, d_ij.shape)
    
    # Set self-distance to infinity to avoid counting it
    d_ij = xp.where(eye, xp.inf, d_ij)
    
    # Count collisions (symmetric matrix, so divide count by 2)
    sum_axes = (1, 2) if is_batch else (0, 1)
    n_coll = xp.sum(d_ij < COLLISION_DIST, axis=sum_axes) / 2.0
    c_coll = n_coll * W_COLL
    vel_x = v * xp.cos(phi)
    vel_y = v * xp.sin(phi)
    vel = xp.stack([vel_x, vel_y], axis=-1)
    
    vel_bary = xp.mean(vel, axis=axis_agent, keepdims=True)
    dvel = vel - vel_bary
    dpos = pos - center
    
    theta = xp.arctan2(dpos[..., 1], dpos[..., 0])
    phi_vel = xp.arctan2(dvel[..., 1], dvel[..., 0])
    
    mill = xp.abs(xp.mean(xp.sin(theta - phi_vel), axis=axis_agent))
    c_mill = mill * W_MILL
    
    return c_disp, c_effort, c_coll, c_pol, c_mill