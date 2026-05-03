# Experiment Report - PyTorch_CUDA (3D)
**Date:** 2026-05-03_15-52-30

## 1. Initial Configuration
| Parameter | Value |
| :--- | :--- |
| ALPHA_LPF            | 0.2        |
| ARENA_RADIUS         | 120.0      |
| COLLISION_DIST       | 0.4        |
| DT                   | 0.1        |
| ENABLE_3D            | True       |
| EXPLO_STRATEGY       | global_best |
| FOV_FACTOR           | 0.9        |
| FULL_MILLING_MODE    | False      |
| GEN_CPU              | 20         |
| GEN_GPU              | 10         |
| GRID_RES             | 5.0        |
| MAP_STRATEGY         | global     |
| MAX_SPEED            | 20.0       |
| MAX_YAW_RATE         | 3.14       |
| MIN_SPAWN_DIST       | 2.0        |
| NB_DRONES            | 10         |
| NEIGHBORS            | 2          |
| N_INIT_CONDITIONS    | 4          |
| POP_SIZE_CPU         | 150        |
| POP_SIZE_GPU         | 1000       |
| REFRESH_MAP_TICKS    | 50         |
| SCENARIO             | exploration |
| SIM_STEPS            | 500        |
| SPOIL_ADD            | 0.05       |
| SPOIL_MULT           | 1.01       |
| VISU_STEPS           | 1000       |
| W_COLL               | 500.0      |
| W_DISP               | 0.0        |
| W_EFFORT             | 1.0        |
| W_EXPLO              | -50.0      |
| W_MILL               | 0          |
| W_POL                | -0.0       |
| Z_MAX                | 10.0       |
| Z_MIN                | 1.0        |

## 2. Optimization Evolution
| Gen  |  Best Cost   |  Time (s)  |                                                                All Parameters                                                                |
| :--: | :----------: | :--------: | :------------------------------------------------------------------------------------------------------------------------------------------ |
| 00   | -3402.6375   | 14.05      | y_att=0.24, y_ali=2.46, y_f=1.84, d0_att=6.24, l_att=7.77, l_ali=1.26, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.71, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.10, y_acc=0.30, l_acc=1.65, d0_v=1.52, y_explo=0.17 |
| 01   | -3402.6375   | 13.14      | y_att=0.24, y_ali=2.46, y_f=1.84, d0_att=6.24, l_att=7.77, l_ali=1.26, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.71, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.10, y_acc=0.30, l_acc=1.65, d0_v=1.52, y_explo=0.17 |
| 02   | -3681.9314   | 13.13      | y_att=0.19, y_ali=1.40, y_f=1.84, d0_att=3.17, l_att=7.77, l_ali=1.27, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.33, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.10, y_acc=0.30, l_acc=2.57, d0_v=1.66, y_explo=0.16 |
| 03   | -3681.9314   | 13.48      | y_att=0.19, y_ali=1.40, y_f=1.84, d0_att=3.17, l_att=7.77, l_ali=1.27, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.33, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.10, y_acc=0.30, l_acc=2.57, d0_v=1.66, y_explo=0.16 |
| 04   | -3681.9314   | 13.07      | y_att=0.19, y_ali=1.40, y_f=1.84, d0_att=3.17, l_att=7.77, l_ali=1.27, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.33, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.10, y_acc=0.30, l_acc=2.57, d0_v=1.66, y_explo=0.16 |
| 05   | -3681.9314   | 13.27      | y_att=0.19, y_ali=1.40, y_f=1.84, d0_att=3.17, l_att=7.77, l_ali=1.27, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.33, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.10, y_acc=0.30, l_acc=2.57, d0_v=1.66, y_explo=0.16 |
| 06   | -3692.8433   | 13.45      | y_att=2.18, y_ali=0.05, y_f=1.47, d0_att=5.30, l_att=3.58, l_ali=1.05, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.52, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.47, y_acc=0.36, l_acc=1.58, d0_v=1.52, y_explo=0.15 |
| 07   | -3752.6274   | 14.06      | y_att=4.10, y_ali=0.90, y_f=1.19, d0_att=9.03, l_att=2.00, l_ali=2.03, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.33, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.22, l_acc=1.72, d0_v=2.59, y_explo=0.24 |
| 08   | -3752.6274   | 14.02      | y_att=4.10, y_ali=0.90, y_f=1.19, d0_att=9.03, l_att=2.00, l_ali=2.03, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.33, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.22, l_acc=1.72, d0_v=2.59, y_explo=0.24 |
| 09   | -3752.6274   | 13.77      | y_att=4.10, y_ali=0.90, y_f=1.19, d0_att=9.03, l_att=2.00, l_ali=2.03, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.33, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.22, l_acc=1.72, d0_v=2.59, y_explo=0.24 |

**End of experiment.**
