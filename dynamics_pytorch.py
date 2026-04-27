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
    # Exploration
    y_explo: float = 0.0

@torch.no_grad()    # No graph to track gradients, better perf
def get_deterministic_initial_state(n_batch, n_drones, device=torch.device("cpu")):
    total_envs = n_batch * getattr(config, 'N_INIT_CONDITIONS', 4)
    
    radius = ARENA_RADIUS * 0.8
    theta = torch.empty((total_envs, n_drones), device=device, dtype=torch.float32).uniform_(0, 2.0 * math.pi)
    
    u = torch.rand((total_envs, n_drones), device=device, dtype=torch.float32)
    r = radius * torch.sqrt(u)
        
    x = r * torch.cos(theta)
    y = r * torch.sin(theta)
    
    if config.ENABLE_3D:
        z = torch.empty_like(theta).uniform_(config.Z_MIN + 1.0, config.Z_MAX - 1.0)
        pos = torch.stack([x, y, z], dim=-1)
    else:
        pos = torch.stack([x, y], dim=-1)
        
    min_dist = getattr(config, 'MIN_SPAWN_DIST', 2.0)
    for _ in range(20):
        pos_i = pos.unsqueeze(-2)
        pos_j = pos.unsqueeze(-3)
        dist = torch.linalg.norm(pos_i - pos_j, dim=-1)
        
        eye_mask = torch.eye(n_drones, dtype=torch.bool, device=device).expand(dist.shape)
        dist = dist.masked_fill(eye_mask, float('inf'))
        
        overlap = torch.clamp(min_dist - dist, min=0.0)
        direction = (pos_i - pos_j) / (dist.unsqueeze(-1) + 1e-6)
        push = torch.sum(direction * overlap.unsqueeze(-1), dim=-2) * 0.5
        pos += push

    # State vectors
    phi = torch.empty_like(theta).uniform_(-math.pi, math.pi) # Outward looking + offset
    v = torch.zeros_like(theta)
    
    if config.ENABLE_3D:
        # Added Z axis
        vz = torch.zeros_like(theta)
        return pos, phi, v, vz
    else:
        # 2D version
        return pos, phi, v, None
    
    
@torch.no_grad()
def compute_derivatives(pos, phi, v, p, vz=None, phi_dot_mem=None, grid=None):
    device = pos.device
    
    # Unpack
    y_att, y_ali, y_f = p.y_att, p.y_ali, p.y_f
    d0_att, l_att, l_ali = p.d0_att, p.l_att, p.l_ali
    a_att, b1_att, b2_att = p.a_att, p.b1_att, p.b2_att
    d0_ali, a_ali, b1_ali, b2_ali = p.d0_ali, p.a_ali, p.b1_ali, p.b2_ali
    y_acc, l_acc, d0_v = p.y_acc, p.l_acc, p.d0_v
    target_alt = p.target_altitude
    y_explo = getattr(p, 'y_explo', 0.0)

    # Broadcast (Batch, N, 1)
    if isinstance(y_att, torch.Tensor) and y_att.dim() == 2:
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

    
    # Exploration force
    phi_dot_explo = 0.0
    vz_dot_explo = 0.0
    
    if grid is not None and getattr(config, 'SCENARIO', 'default') == 'exploration':
        grad_x, grad_y = grid.get_gradient(pos)
        
        # Angle vers la direction la plus inexplorée
        target_angle = torch.atan2(grad_y, grad_x)
        angle_diff = (target_angle - phi + math.pi) % (2 * math.pi) - math.pi
        
        # Force activée proportionnellement à l'urgence d'explorer (magnitude du gradient)
        grad_mag = torch.sqrt(grad_x**2 + grad_y**2)
        explo_activation = torch.clamp(grad_mag / (grid.MAX_SPOIL * 0.1), 0.0, 1.0)
        
        phi_dot_explo = y_explo * angle_diff * explo_activation
        
        # Optionnel : si Z est activé, plonger légèrement vers le sol (-Z) pour utiliser la puissance max du FOV
        if config.ENABLE_3D and vz is not None:
            vz_dot_explo = - y_explo * explo_activation * 0.5

    # Noise addition
    noise = torch.empty_like(phi).uniform_(-0.1, 0.1)
    
    phi_dot_social = torch.clamp(social_sum + phi_dot_explo + noise, -3.0, 3.0)
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
        
        vz_cmd = vz_dot_social + f_floor + f_ceil + f_nav + vz_dot_explo
        
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
    def __init__(self, batch_size, n_drones, arena_radius=50.0, res=5.0, device=torch.device("cpu")):
        self.device = device
        self.res = res
        self.radius = arena_radius
        self.size = int((arena_radius * 2) / res)
        self.strategy = getattr(config, 'MAP_STRATEGY', 'global')
        self.n_drones = n_drones
        
        # Spoilage parameters
        self.spoil_mult = config.SPOIL_MULT
        self.spoil_add = config.SPOIL_ADD
        self.MAX_SPOIL = 100.0
        self.FRESH_RATE = self.MAX_SPOIL / 4.0
        self.SENSOR_H = 10.0
        
        # Grid [Batch, X, Y]
        if self.strategy == "global":
            self.spoilage = torch.full((batch_size, self.size, self.size), self.MAX_SPOIL, dtype=torch.float32, device=self.device)
        else:
            # Each drone in each swarm gets its own map
            self.spoilage = torch.full((batch_size, n_drones, self.size, self.size), self.MAX_SPOIL, dtype=torch.float32, device=self.device)

        # Coordinate grids for FOV vectorization
        xs = torch.linspace(-self.radius + res/2, self.radius - res/2, self.size, device=self.device)
        ys = torch.linspace(-self.radius + res/2, self.radius - res/2, self.size, device=self.device)
        grid_x, grid_y = torch.meshgrid(xs, ys, indexing='ij')
        # Format [1, 1, X, Y] for partial broadcasting (VRAM Optimization)
        self.grid_x = grid_x.view(1, 1, self.size, self.size)
        self.grid_y = grid_y.view(1, 1, self.size, self.size)

    @torch.no_grad()
    def update(self, pos):
        # Format (Batch, N, Dim)
        p = pos if pos.dim() == 3 else pos.unsqueeze(0)
        
        # Exponential spoilage (sort of)
        self.spoilage *= self.spoil_mult
        self.spoilage += self.spoil_add
        self.spoilage.clamp_(min=0.0, max=self.MAX_SPOIL)
        
        fov_factor = getattr(config, 'FOV_FACTOR', 1.0)
        
        for i in range(self.n_drones):
            # Distance calculation for FOV instead of simple spatial hashing
            px = p[:, i:i+1, 0:1, None]
            py = p[:, i:i+1, 1:2, None]
            
            # Optimized VRAM usage
            dist_sq = torch.sub(self.grid_x, px).pow_(2)
            dist_sq.add_(torch.sub(self.grid_y, py).pow_(2))
            
            if p.shape[-1] == 3:
                z = torch.clamp(p[:, i:i+1, 2:3, None], min=0.5)
            else:
                z = torch.full_like(px, self.SENSOR_H)
                
            # FOV geometry and Inverse Square Law intensity
            sigma = torch.clamp(z * fov_factor, min=self.res / 2.0)
            intensity = (self.FRESH_RATE * self.SENSOR_H) / (z**2)
            
            # Freshening matrix (Gaussian splat)
            freshen_matrix = intensity * torch.exp(-dist_sq / (2.0 * sigma**2))
            
            if self.strategy == "global":
                # Sequential writing to avoid conflicts -> Summing contributions for the global map
                self.spoilage -= freshen_matrix.squeeze(1)
            else:
                # each drone updates his own map
                self.spoilage[:, i:i+1] -= freshen_matrix
                
        self.spoilage.clamp_(min=0.0)

    @torch.no_grad()
    def share_maps(self, pos, neighbors_k):
        if self.strategy != "local_shared" or neighbors_k is None or neighbors_k == 0:
            return
            
        pos_i = pos.unsqueeze(-2)
        pos_j = pos.unsqueeze(-3)
        dist = torch.linalg.norm(pos_i - pos_j, dim=-1)
        
        eye_mask = torch.eye(self.n_drones, dtype=torch.bool, device=self.device).expand(dist.shape) # mask own distance
        dist = dist.masked_fill(eye_mask, float('inf'))
        
        _, top_indices = torch.topk(dist, neighbors_k, dim=-1, largest=False) # k closest neighbors
        
        new_spoilage = self.spoilage.clone()
        batch_idx_1d = torch.arange(pos.shape[0], device=self.device)
        
        for d in range(self.n_drones):
            for k in range(neighbors_k):
                n_idx = top_indices[:, d, k]
                neighbor_map = self.spoilage[batch_idx_1d, n_idx]           # getting the neighbors's maps
                torch.minimum(new_spoilage[:, d], neighbor_map, out=new_spoilage[:, d]) # keeping the best information (unilateral)
                
        self.spoilage.copy_(new_spoilage)

    @torch.no_grad()
    def get_score(self):
        if self.strategy == "global":
            freshness = 1.0 - (self.spoilage / self.MAX_SPOIL) # freshness 1.0 = fully fresh
            return torch.mean(freshness, dim=(1, 2))
        else:
            global_spoilage, _ = torch.min(self.spoilage, dim=1)
            freshness = 1.0 - (global_spoilage / self.MAX_SPOIL)
            return torch.mean(freshness, dim=(1, 2))
        
        
    @torch.no_grad()
    def get_gradient(self, pos):
        """Returns spatial gradient of freshness"""
        offset = 3 # Anticipation by 3 blocks
        
        idx_x = ((pos[..., 0] + self.radius) / self.res).to(torch.int64)
        idx_y = ((pos[..., 1] + self.radius) / self.res).to(torch.int64)
        
        # To stay on the grid
        idx_x_p = torch.clamp(idx_x + offset, 0, self.size - 1)
        idx_x_m = torch.clamp(idx_x - offset, 0, self.size - 1)
        idx_y_p = torch.clamp(idx_y + offset, 0, self.size - 1)
        idx_y_m = torch.clamp(idx_y - offset, 0, self.size - 1)
        idx_x_c = torch.clamp(idx_x, 0, self.size - 1)
        idx_y_c = torch.clamp(idx_y, 0, self.size - 1)
        
        batch_size = pos.shape[0]
        b_idx = torch.arange(batch_size, device=self.device).unsqueeze(1)
        
        if self.strategy == "global":
            spoil_x_p = self.spoilage[b_idx, idx_x_p, idx_y_c]
            spoil_x_m = self.spoilage[b_idx, idx_x_m, idx_y_c]
            spoil_y_p = self.spoilage[b_idx, idx_x_c, idx_y_p]
            spoil_y_m = self.spoilage[b_idx, idx_x_c, idx_y_m]
        else:
            n_idx = torch.arange(self.n_drones, device=self.device).unsqueeze(0)
            spoil_x_p = self.spoilage[b_idx, n_idx, idx_x_p, idx_y_c]
            spoil_x_m = self.spoilage[b_idx, n_idx, idx_x_m, idx_y_c]
            spoil_y_p = self.spoilage[b_idx, n_idx, idx_x_c, idx_y_p]
            spoil_y_m = self.spoilage[b_idx, n_idx, idx_x_c, idx_y_m]
            
        # The gradient is counted as positive if the "+ offset" block is less fresh, more spoiled
        grad_x = spoil_x_p - spoil_x_m
        grad_y = spoil_y_p - spoil_y_m
        
        return grad_x, grad_y