from dataclasses import dataclass
import numpy as np
from config import DT, ARENA_RADIUS, W_EFFORT, W_DISP, W_POL, W_COLL, NEIGHBORS

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

def get_deterministic_initial_state(n_batch, n_drones, xp=np):
    # Circle layout (Deterministic)
    radius = 6.0
    theta = xp.linspace(0, 2*xp.pi, n_drones, endpoint=False)
    
    # Broadcast (Batch, N)
    if n_batch > 1:
        theta = xp.tile(theta, (n_batch, 1))
        
    x = radius * xp.cos(theta)
    y = radius * xp.sin(theta)
    
    # State vectors
    pos = xp.stack([x, y], axis=-1)
    phi = theta + 0.1 # Outward looking + offset
    v = xp.zeros_like(theta)
    
    return pos, phi, v

def compute_derivatives(pos, phi, v, p, xp=np):
    # Unpack
    y_att, y_ali, y_f = p.y_att, p.y_ali, p.y_f
    d0_att, l_att, l_ali = p.d0_att, p.l_att, p.l_ali

    # Broadcast (Batch, N, 1) => All in one calculus
    if hasattr(y_att, 'ndim') and y_att.ndim == 2:
        y_att, y_ali = y_att[..., None], y_ali[..., None]
        d0_att, l_att, l_ali = d0_att[..., None], l_att[..., None], l_ali[..., None]

    # --- Wall Interaction (Exp) ---
    dist_center = xp.linalg.norm(pos, axis=-1)
    
    # Heading error rel. to center
    angle_to_center = xp.arctan2(-pos[..., 1], -pos[..., 0])
    psi_center = (angle_to_center - phi + xp.pi) % (2 * xp.pi) - xp.pi
    
    # Exponential repulsion: F ~ 0 at 4m, F >> 1 at 0m
    # 100 * exp(-8) ~= 0.033 (Negligible at 4m)
    # 100 * exp(0)   = 100.0 (Saturates at contact)
    w_force = 100.0 * xp.exp(2.0 * (dist_center - ARENA_RADIUS)) * xp.sin(psi_center)

    # --- Social Interaction ---
    pos_i = xp.expand_dims(pos, -2) 
    pos_j = xp.expand_dims(pos, -3)
    r_ij = pos_i - pos_j
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

    # NEIGHBORS logic
    
    if NEIGHBORS == 0:  # No interactions
        social_sum = xp.zeros_like(phi)
        
    elif NEIGHBORS is None or NEIGHBORS >= (d_ij.shape[-1] - 1):    # All interactions
        social_sum = xp.sum((f_att + f_ali) * (~eye_mask), axis=-1)
        
    else:   # Nominal case
        d_topo = d_ij.copy()
        
        d_topo[eye_mask] = xp.inf # "self-distance" rejected
        
        k_idx = NEIGHBORS - 1
        
        threshold = xp.partition(d_topo, k_idx, axis=-1)[..., k_idx:k_idx+1] # partition is better than sort, we just want the k smallest, order doesn't matter
        
        top_k_mask = d_topo <= threshold
        
        social_sum = xp.sum((f_att + f_ali) * top_k_mask, axis=-1) # Filtered sum (by mask)
    
    # Noise & Dynamics
    noise = xp.random.uniform(-0.1, 0.1, size=phi.shape)
    phi_dot = xp.clip(social_sum + w_force + noise, -3.0, 3.0)
    acc = y_f * (1.0 - v)

    return acc, phi_dot

def compute_metrics(pos, phi, phi_dot, xp=np):
    """
    Centralized Cost Function Logic.
    Handles both CPU (N, 2) and GPU (Batch, N, 2) arrays.
    """
    # Detect batch mode based on dimensions
    is_batch = (pos.ndim == 3)
    axis_agent = 1 if is_batch else 0
    
    # 1. Effort: Minimize turn rate
    c_effort = xp.sum(xp.abs(phi_dot), axis=axis_agent) * W_EFFORT
    
    # 2. Dispersion: Target 5.0m from center
    center = xp.mean(pos, axis=axis_agent, keepdims=True)
    d_center = xp.linalg.norm(pos - center, axis=-1)
    # Mean distance of agents to swarm center
    c_disp = xp.abs(xp.mean(d_center, axis=axis_agent) - 5.0) * W_DISP
    
    # 3. Polarization: Maximize alignment (minimize 1 - Pol)
    u = xp.cos(phi)
    v = xp.sin(phi)
    pol = xp.sqrt(xp.mean(u, axis=axis_agent)**2 + xp.mean(v, axis=axis_agent)**2)
    c_pol = (1.0 - pol) * W_POL
    
    # 4. Collisions: Distance < 0.6m
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
    n_coll = xp.sum(d_ij < 0.6, axis=sum_axes) / 2.0
    c_coll = n_coll * W_COLL
    
    return c_disp, c_effort, c_coll, c_pol