from dataclasses import dataclass
import torch
import math
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
    # Directional parameters
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

@torch.no_grad()    # No graph to track gradients, better perf
def get_deterministic_initial_state(n_batch, n_drones, device=torch.device("cpu")):
    # Circle layout (Deterministic)
    radius = ARENA_RADIUS // 2
    theta = torch.arange(n_drones, device=device, dtype=torch.float32) * (2.0 * math.pi / n_drones)
    
    # Broadcast (Batch, N)
    if n_batch > 1:
        theta = theta.tile((n_batch, 1))
        
    x = radius * torch.cos(theta)
    y = radius * torch.sin(theta)
    
    # State vectors
    phi = theta + 0.1 # Outward looking + offset
    v = torch.zeros_like(theta)
    
    if config.ENABLE_3D:
        # Added Z axis
        z = torch.empty_like(theta).uniform_(config.Z_MIN + 1.0, config.Z_MAX - 1.0)
        pos = torch.stack([x, y, z], dim=-1)
        vz = torch.zeros_like(theta)
        return pos, phi, v, vz
    else:
        # 2D version
        pos = torch.stack([x, y], dim=-1)
        return pos, phi, v, None
    
    
@torch.no_grad()
def compute_derivatives(pos, phi, v, p, vz=None, phi_dot_mem=None):
    device = pos.device
    
    # Unpack
    y_att, y_ali, y_f = p.y_att, p.y_ali, p.y_f
    d0_att, l_att, l_ali = p.d0_att, p.l_att, p.l_ali
    a_att, b1_att, b2_att = p.a_att, p.b1_att, p.b2_att
    d0_ali, a_ali, b1_ali, b2_ali = p.d0_ali, p.a_ali, p.b1_ali, p.b2_ali
    y_acc, l_acc, d0_v = p.y_acc, p.l_acc, p.d0_v
    target_alt = p.target_altitude

    # Broadcast (Batch, N, 1)
    if hasattr(y_att, 'ndim') and y_att.dim() == 2:
        y_att, y_ali = y_att.unsqueeze(-1), y_ali.unsqueeze(-1)
        d0_att, l_att, l_ali = d0_att.unsqueeze(-1), l_att.unsqueeze(-1), l_ali.unsqueeze(-1)
        a_att, b1_att, b2_att = a_att.unsqueeze(-1), b1_att.unsqueeze(-1), b2_att.unsqueeze(-1)
        d0_ali, a_ali, b1_ali, b2_ali = d0_ali.unsqueeze(-1), a_ali.unsqueeze(-1), b1_ali.unsqueeze(-1), b2_ali.unsqueeze(-1)
        y_acc, l_acc, d0_v = y_acc.unsqueeze(-1), l_acc.unsqueeze(-1), d0_v.unsqueeze(-1)
        
        
        
    # Wall interaction (Cylindrical Arena)
    dist_xy = torch.linalg.norm(pos[..., 0:2], dim=-1) if config.ENABLE_3D else torch.linalg.norm(pos, dim=-1)
    
    # Heading error rel. to center
    angle_to_center = torch.atan2(-pos[..., 1], -pos[..., 0])
    psi_center = (angle_to_center - phi + math.pi) % (2 * math.pi) - math.pi
    
    # Exponential repulsion
    if getattr(config, "FULL_MILLING_MODE", False):
        w_force = 0.0
    else:
        w_force = 100.0 * torch.exp(2.0 * (dist_xy - ARENA_RADIUS)) * torch.sin(psi_center)

    # Social interaction
    pos_i = pos.unsqueeze(-2) 
    pos_j = pos.unsqueeze(-3)
    r_ij = pos_i - pos_j 
    
    if config.ENABLE_3D:
        # 3D version
        dxy_sq = torch.sum((pos_i[..., 0:2] - pos_j[..., 0:2])**2, dim=-1)
        dz_sq = ((pos_i[..., 2] - pos_j[..., 2]) / p.sigma_z)**2
        d_ij = torch.sqrt(dxy_sq + dz_sq)
    else:
        # 2D version
        d_ij = torch.linalg.norm(r_ij, dim=-1)
    
    # Mask self
    eye_mask = torch.eye(d_ij.shape[-1], dtype=torch.bool, device=device)
    if len(d_ij.shape) > 2: 
        eye_mask = eye_mask.expand(d_ij.shape)
    d_ij = torch.clamp(d_ij, min=0.01)

    # Angles
    a_ij = torch.atan2(r_ij[..., 1], r_ij[..., 0])
    psi = (a_ij - phi[..., :, None] + math.pi) % (2 * math.pi) - math.pi
    d_phi = (phi[..., None, :] - phi[..., :, None] + math.pi) % (2 * math.pi) - math.pi

    # Forces 
    # Attraction
    f_att_base = y_att * ((d_ij / d0_att) - 1.0) / (1.0 + (d_ij / l_att)**2)
    o_att = torch.sin(psi) * (1.0 + a_att * torch.cos(psi))
    e_att = 1.0 - b1_att * torch.cos(d_phi) - b2_att * torch.cos(2.0 * d_phi)
    f_att = f_att_base * o_att * e_att

    # Alignement
    f_ali_base = y_ali * ((d_ij / d0_ali) + 1.0) * torch.exp(-(d_ij / l_ali)**2)
    o_ali = torch.sin(d_phi) * (1.0 + a_ali * torch.cos(2.0 * d_phi))
    e_ali = 1.0 + b1_ali * torch.cos(psi) - b2_ali * torch.cos(2.0 * psi)
    f_ali = f_ali_base * o_ali * e_ali

    # Social speed
    dv_ij = y_acc * torch.cos(psi) * ((d_ij / d0_v) - 1.0) / (1.0 + d_ij / l_acc)

    # Collision avoidance (Z-axis)
    f_vz = 0.0
    if config.ENABLE_3D and vz is not None:
        dz_ij = pos_j[..., 2] - pos_i[..., 2]
        term_tanh = torch.tanh((dz_ij - torch.sign(dz_ij) * p.d0_z) / p.a_z)
        term_exp = torch.exp(-(d_ij / p.l_z)**2)
        f_vz = p.y_z * term_tanh * term_exp

    f_rep = 0.0
    vz_dot_social = 0.0

    # Filtering
    if NEIGHBORS == 0:  
        social_sum = torch.zeros_like(phi)
        rep_sum = torch.zeros_like(phi)
        acc_social = torch.zeros_like(v)
        if config.ENABLE_3D and vz is not None:
            vz_dot_social = torch.zeros_like(phi)
        
    elif NEIGHBORS is None or NEIGHBORS >= (d_ij.shape[-1] - 1):    
        social_sum = torch.sum((f_att + f_ali) * (~eye_mask), dim=-1)
        rep_sum = torch.sum(f_rep * (~eye_mask), dim=-1)
        acc_social = torch.sum(dv_ij * (~eye_mask), dim=-1)
        if config.ENABLE_3D and vz is not None:
            vz_dot_social = torch.sum(f_vz * (~eye_mask), dim=-1)
            
    else:   
        # Partition max influence
        f_course = f_att + f_ali
        if config.ENABLE_3D and vz is not None:
            influence_ij = torch.sqrt(dv_ij**2 + (f_course * v.unsqueeze(-1))**2 + f_vz**2)
        else:
            influence_ij = torch.sqrt(dv_ij**2 + (f_course * v.unsqueeze(-1))**2)
            
        influence_ij = influence_ij.masked_fill(eye_mask, -float('inf'))
        
        top_k_vals, _ = torch.topk(influence_ij, NEIGHBORS, dim=-1)
        threshold = top_k_vals[..., -1:]
        top_k_mask = influence_ij >= threshold
        
        social_sum = torch.sum(f_course * top_k_mask, dim=-1)
        rep_sum = torch.sum(f_rep * top_k_mask, dim=-1)
        acc_social = torch.sum(dv_ij * top_k_mask, dim=-1)
        if config.ENABLE_3D and vz is not None:
            vz_dot_social = torch.sum(f_vz * top_k_mask, dim=-1)

    # Noise addition
    noise = torch.empty_like(phi).uniform_(-0.1, 0.1)
    
    phi_dot_social = torch.clamp(social_sum + noise, -3.0, 3.0)
    phi_dot_vital = torch.clamp(rep_sum + w_force, -10.0, 10.0)
    
    # Raw command & clamp
    phi_dot_cmd = phi_dot_social + phi_dot_vital
    phi_dot_cmd = torch.clamp(phi_dot_cmd, -config.MAX_YAW_RATE, config.MAX_YAW_RATE)

    # LPF 
    if phi_dot_mem is not None:
        phi_dot = config.ALPHA_LPF * phi_dot_cmd + (1.0 - config.ALPHA_LPF) * phi_dot_mem
    else:
        phi_dot = phi_dot_cmd

    acc = acc_social + y_f * (1.0 - v)

    vz_dot = 0.0
    if config.ENABLE_3D and vz is not None:
        dz_floor = pos[..., 2] - config.Z_MIN
        f_floor = 2.0 * p.y_z_w / (1.0 + torch.exp((dz_floor - p.dz_w) / p.dz_w))
        
        dz_ceil = config.Z_MAX - pos[..., 2]
        f_ceil = -2.0 * p.y_z_w / (1.0 + torch.exp((dz_ceil - p.dz_w) / p.dz_w))
        
        # Target altitude tracking
        f_nav = -p.y_z_nav * torch.tanh((pos[..., 2] - target_alt) / p.a_z)
        
        vz_cmd = vz_dot_social + f_floor + f_ceil + f_nav
        
        # Damp
        speed_3d = torch.sqrt(v**2 + vz**2)
        vz_cmd -= p.y_f * vz / torch.clamp(speed_3d, min=0.1)
        
        # Simulates controller
        vz_dot = p.y_f * (vz_cmd - vz)
        
    if config.ENABLE_3D:
        return acc, phi_dot, vz_dot
    return acc, phi_dot, None


@torch.no_grad()
def compute_metrics(pos, phi, phi_dot, v):
    """
    Centralized Cost Function Logic.
    Handles both CPU (N, 2) and GPU (Batch, N, 2) arrays.
    """
    device = pos.device
    
    # Detect batch mode based on dimensions
    is_batch = (pos.dim() == 3)
    dim_agent = 1 if is_batch else 0
    
    # Effort: Minimize turn rate
    c_effort = torch.sum(torch.abs(phi_dot), dim=dim_agent) * W_EFFORT
    
    # Dispersion: Target 5.0m from center
    center = torch.mean(pos, dim=dim_agent, keepdim=True)
    d_center = torch.linalg.norm(pos - center, dim=-1)
    # Mean distance of agents to swarm center
    c_disp = torch.abs(torch.mean(d_center, dim=dim_agent) - 5.0) * W_DISP
    
    # Polarization: Maximize alignment (minimize 1 - Pol)
    u_vec = torch.cos(phi)
    v_vec = torch.sin(phi)
    pol = torch.sqrt(torch.mean(u_vec, dim=dim_agent)**2 + torch.mean(v_vec, dim=dim_agent)**2)
    c_pol = (1.0 - pol) * W_POL
    
    # Collisions: Distance < 0.6m
    if is_batch:
        r_ij = pos[:, :, None, :] - pos[:, None, :, :] # (B, N, N, 2)
    else:
        r_ij = pos[:, None, :] - pos[None, :, :]       # (N, N, 2)
        
    d_ij = torch.linalg.norm(r_ij, dim=-1)
    
    # Mask diagonal (self-distance)
    eye = torch.eye(pos.shape[dim_agent], dtype=torch.bool, device=device)
    if is_batch:
        eye = eye.expand(d_ij.shape)
    
    # Set self-distance to infinity to avoid counting it
    d_ij = torch.where(eye, torch.tensor(float('inf'), device=device), d_ij)
    
    # Count collisions (symmetric matrix, so divide count by 2)
    sum_dims = (1, 2) if is_batch else (0, 1)
    n_coll = torch.sum(d_ij < COLLISION_DIST, dim=sum_dims) / 2.0
    c_coll = n_coll * W_COLL
    
    vel_x = v * torch.cos(phi)
    vel_y = v * torch.sin(phi)
    vel = torch.stack([vel_x, vel_y], dim=-1)
    
    vel_bary = torch.mean(vel, dim=dim_agent, keepdim=True)
    dvel = vel - vel_bary
    dpos = pos - center
    
    theta = torch.atan2(dpos[..., 1], dpos[..., 0])
    phi_vel = torch.atan2(dvel[..., 1], dvel[..., 0])
    
    mill = torch.abs(torch.mean(torch.sin(theta - phi_vel), dim=dim_agent))
    c_mill = mill * W_MILL
    
    return c_disp, c_effort, c_coll, c_pol, c_mill


class TensorExplorationGrid:
    def __init__(self, batch_size, arena_radius=50.0, res=5.0, device=torch.device("cpu")):
        self.device = device
        self.res = res
        self.radius = arena_radius
        self.size = int((arena_radius * 2) / res)
        
        # Spoilage parameters
        self.spoil_mult = config.SPOIL_MULT
        self.spoil_add = config.SPOIL_ADD
        
        self.MAX_SPOIL = 100.0
        self.FRESH_RATE = self.MAX_SPOIL / 4.0
        self.SENSOR_H = 10.0
        
        # Grid [Batch, X, Y]
        self.spoilage = torch.full((batch_size, self.size, self.size), self.MAX_SPOIL, dtype=torch.float32, device=self.device)
        self.b_idx = torch.arange(batch_size, device=self.device)[:, None]

    @torch.no_grad()
    def update(self, pos):
        # Format (Batch, N, Dim)
        p = pos if pos.dim() == 3 else pos.unsqueeze(0)
        
        # Exponential spoilage (sort of)
        self.spoilage *= self.spoil_mult
        self.spoilage += self.spoil_add
        self.spoilage.clamp_(min=0.0, max=self.MAX_SPOIL)
        
        # Spatial hashing
        idx_x = torch.clamp(((p[..., 0] + self.radius) / self.res).to(torch.int32), 0, self.size - 1)
        idx_y = torch.clamp(((p[..., 1] + self.radius) / self.res).to(torch.int32), 0, self.size - 1)
        
        # Freshening
        if p.shape[-1] == 3:
            z = torch.clamp(p[..., 2], min=0.1)
        else:
            z = torch.full(p[..., 0].shape, self.SENSOR_H, dtype=torch.float32, device=self.device)
            
        freshen_val = self.FRESH_RATE * torch.exp(-z / (2.0 * self.SENSOR_H))
        
        current = self.spoilage[self.b_idx, idx_x, idx_y]
        self.spoilage[self.b_idx, idx_x, idx_y] = torch.clamp(current - freshen_val, min=0.0)

    @torch.no_grad()
    def get_score(self):
        # Freshness ratio (1.0 = fully fresh)
        freshness = 1.0 - (self.spoilage / self.MAX_SPOIL)
        return torch.mean(freshness, dim=(1, 2))