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
    a_att: float = 0.0
    b1_att: float = 0.0
    b2_att: float = 0.0
    d0_ali: float = 1.0
    a_ali: float = 0.0
    b1_ali: float = 0.0
    b2_ali: float = 0.0
    # 3D Parameters
    y_z: float = 1.0
    l_z: float = 3.0
    a_z: float = 1.0
    d0_z: float = 0.5
    sigma_z: float = 1.0 
    y_z_w: float = 2.0
    dz_w: float = 1.0
    # Nav
    y_z_nav: float = 1.0
    y_vz_nav: float = 1.0
    target_altitude: float = 5.0
    # Speed (Social)
    y_acc: float = 1.0
    l_acc: float = 2.0
    d0_v: float = 1.0

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
    a_att, b1_att, b2_att = p.a_att, p.b1_att, p.b2_att
    d0_ali, a_ali, b1_ali, b2_ali = p.d0_ali, p.a_ali, p.b1_ali, p.b2_ali
    y_acc, l_acc, d0_v = p.y_acc, p.l_acc, p.d0_v
    target_alt = p.target_altitude

    if hasattr(y_att, 'ndim') and y_att.ndim == 2:
        y_att, y_ali = y_att[..., None], y_ali[..., None]
        d0_att, l_att, l_ali = d0_att[..., None], l_att[..., None], l_ali[..., None]
        a_att, b1_att, b2_att = a_att[..., None], b1_att[..., None], b2_att[..., None]
        d0_ali, a_ali, b1_ali, b2_ali = d0_ali[..., None], a_ali[..., None], b1_ali[..., None], b2_ali[..., None]
        y_acc, l_acc, d0_v = y_acc[..., None], l_acc[..., None], d0_v[..., None]
        
            
    # Wall interaction (Cylindrical Arena)
    dist_xy = xp.linalg.norm(pos[..., 0:2], axis=-1) if config.ENABLE_3D else xp.linalg.norm(pos, axis=-1)
    
    # Heading error rel. to center
    angle_to_center = xp.arctan2(-pos[..., 1], -pos[..., 0])
    psi_center = (angle_to_center - phi + xp.pi) % (2 * xp.pi) - xp.pi
    
    # Exponential repulsion
    if getattr(config, "FULL_MILLING_MODE", False):
        w_force = 0.0 # disabled -> no arena
    else:
        w_force = 100.0 * xp.exp(2.0 * (dist_xy - ARENA_RADIUS)) * xp.sin(psi_center)

    # Social interaction
    pos_i = xp.expand_dims(pos, -2) 
    pos_j = xp.expand_dims(pos, -3)
    r_ij = pos_i - pos_j
    
    if config.ENABLE_3D:
        # 3D version
        dxy_sq = xp.sum((pos_i[..., 0:2] - pos_j[..., 0:2])**2, axis=-1)
        dz_sq = ((pos_i[..., 2] - pos_j[..., 2]) / p.sigma_z)**2
        d_ij = xp.sqrt(dxy_sq + dz_sq)
    else:
        # 2D version
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
    f_att_base = y_att * ((d_ij / d0_att) - 1.0) / (1.0 + (d_ij / l_att)**2)
    o_att = xp.sin(psi) * (1.0 + a_att * xp.cos(psi))
    e_att = 1.0 - b1_att * xp.cos(d_phi) - b2_att * xp.cos(2.0 * d_phi)
    f_att = f_att_base * o_att * e_att

    f_ali_base = y_ali * ((d_ij / d0_ali) + 1.0) * xp.exp(-(d_ij / l_ali)**2)
    o_ali = xp.sin(d_phi) * (1.0 + a_ali * xp.cos(2.0 * d_phi))
    e_ali = 1.0 + b1_ali * xp.cos(psi) - b2_ali * xp.cos(2.0 * psi)
    f_ali = f_ali_base * o_ali * e_ali

    # Social speed
    dv_ij = y_acc * xp.cos(psi) * ((d_ij / d0_v) - 1.0) / (1.0 + d_ij / l_acc)

    # Collision avoidance (Z-axis)
    f_vz = 0.0
    if config.ENABLE_3D and vz is not None:
        dz_ij = pos_j[..., 2] - pos_i[..., 2]
        term_tanh = xp.tanh((dz_ij - xp.sign(dz_ij) * p.d0_z) / p.a_z)
        term_exp = xp.exp(-(d_ij / p.l_z)**2)
        f_vz = p.y_z * term_tanh * term_exp

    f_rep = 0.0

    # Init scope
    vz_dot_social = 0.0

    # Filtering
    if NEIGHBORS == 0:  
        social_sum = xp.zeros_like(phi)
        rep_sum = xp.zeros_like(phi)
        acc_social = xp.zeros_like(v)
        if config.ENABLE_3D and vz is not None:
            vz_dot_social = xp.zeros_like(phi)
        
    elif NEIGHBORS is None or NEIGHBORS >= (d_ij.shape[-1] - 1):    
        social_sum = xp.sum((f_att + f_ali) * (~eye_mask), axis=-1)
        rep_sum = xp.sum(f_rep * (~eye_mask), axis=-1)
        acc_social = xp.sum(dv_ij * (~eye_mask), axis=-1)
        if config.ENABLE_3D and vz is not None:
            vz_dot_social = xp.sum(f_vz * (~eye_mask), axis=-1)
            
    else:   
        # Partition max influence
        f_course = f_att + f_ali
        if config.ENABLE_3D and vz is not None:
            influence_ij = xp.sqrt(dv_ij**2 + (f_course * v[..., None])**2 + f_vz**2)
        else:
            influence_ij = xp.sqrt(dv_ij**2 + (f_course * v[..., None])**2)
            
        influence_ij[eye_mask] = -xp.inf 
        
        k_idx = NEIGHBORS - 1
        # Reverse sign for descending order
        threshold = xp.partition(-influence_ij, k_idx, axis=-1)[..., k_idx:k_idx+1] 
        top_k_mask = -influence_ij <= threshold
        
        social_sum = xp.sum(f_course * top_k_mask, axis=-1)
        rep_sum = xp.sum(f_rep * top_k_mask, axis=-1)
        acc_social = xp.sum(dv_ij * top_k_mask, axis=-1)
        if config.ENABLE_3D and vz is not None:
            vz_dot_social = xp.sum(f_vz * top_k_mask, axis=-1)

    # Noise addition
    noise = xp.random.uniform(-0.1, 0.1, size=phi.shape[-1])
    
    phi_dot_social = xp.clip(social_sum + noise, -3.0, 3.0)
    phi_dot_vital = xp.clip(rep_sum + w_force, -10.0, 10.0)
    
    phi_dot = phi_dot_social + phi_dot_vital
    acc = acc_social + y_f * (1.0 - v)

    vz_dot = 0.0
    if config.ENABLE_3D and vz is not None:
        dz_floor = pos[..., 2] - config.Z_MIN
        f_floor = 2.0 * p.y_z_w / (1.0 + xp.exp((dz_floor - p.dz_w) / p.dz_w))
        
        dz_ceil = config.Z_MAX - pos[..., 2]
        f_ceil = -2.0 * p.y_z_w / (1.0 + xp.exp((dz_ceil - p.dz_w) / p.dz_w))
        
        f_nav = -p.y_z_nav * xp.tanh((pos[..., 2] - target_alt) / p.a_z)
        
        vz_cmd = vz_dot_social + f_floor + f_ceil + f_nav
        speed_3d = xp.sqrt(v**2 + vz**2)
        vz_cmd -= p.y_f * vz / xp.maximum(speed_3d, 0.1)
        vz_dot = p.y_f * (vz_cmd - vz)
    
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



class TensorExplorationGrid:
    def __init__(self, batch_size, arena_radius=50.0, res=5.0, xp=np):
        self.xp = xp
        self.res = res
        self.radius = arena_radius
        self.size = int((arena_radius * 2) / res)
        
        # Spoilage parameters
        self.MAX_SPOIL = 100.0
        self.FRESH_RATE = self.MAX_SPOIL / 4.0
        self.SENSOR_H = 10.0
        
        # Continuous grid [Batch, X, Y]
        self.spoilage = self.xp.full((batch_size, self.size, self.size), self.MAX_SPOIL, dtype=self.xp.float32)
        self.b_idx = self.xp.arange(batch_size)[:, None]

    def update(self, pos):
        # Format (Batch, N, Dim)
        p = pos if pos.ndim == 3 else pos[None, ...]
        
        # Exponential spoilage
        self.spoilage *= self.xp.float32(1.01)
        self.spoilage += self.xp.float32(0.05)
        self.xp.clip(self.spoilage, 0.0, self.MAX_SPOIL, out=self.spoilage)
        
        # Spatial hashing
        idx_x = self.xp.clip(((p[..., 0] + self.radius) / self.res).astype(self.xp.int32), 0, self.size - 1)
        idx_y = self.xp.clip(((p[..., 1] + self.radius) / self.res).astype(self.xp.int32), 0, self.size - 1)
        
        # Freshening
        if p.shape[-1] == 3:
            z = self.xp.maximum(p[..., 2], 0.1)
        else:
            z = self.xp.full(p[..., 0].shape, self.SENSOR_H, dtype=self.xp.float32)
            
        freshen_val = self.FRESH_RATE * self.xp.exp(-z / (2.0 * self.SENSOR_H))
        
        current = self.spoilage[self.b_idx, idx_x, idx_y]
        self.spoilage[self.b_idx, idx_x, idx_y] = self.xp.maximum(self.xp.float32(0.0), current - freshen_val)

    def get_score(self):
        # Freshness ratio (1.0 = fully fresh)
        freshness = 1.0 - (self.spoilage / self.MAX_SPOIL)
        return self.xp.mean(freshness, axis=(1, 2))