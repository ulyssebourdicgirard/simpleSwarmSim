# Experiment Report - PyTorch_CUDA (3D)
**Date:** 2026-05-03_17-48-12

## 1. Initial Configuration
| Parameter | Value |
| :--- | :--- |
| ALPHA_LPF            | 0.2        |
| ARENA_RADIUS         | 50.0       |
| COLLISION_DIST       | 0.4        |
| DT                   | 0.1        |
| ENABLE_3D            | True       |
| EXPLO_STRATEGY       | global_best |
| FOV_FACTOR           | 0.9        |
| FULL_MILLING_MODE    | True       |
| GEN_CPU              | 20         |
| GEN_GPU              | 10         |
| GRID_RES             | 5.0        |
| MAP_STRATEGY         | local_shared |
| MAX_SPEED            | 30.0       |
| MAX_YAW_RATE         | 3.14       |
| MIN_SPAWN_DIST       | 2.0        |
| NB_DRONES            | 10         |
| NEIGHBORS            | 2          |
| N_INIT_CONDITIONS    | 4          |
| POP_SIZE_CPU         | 150        |
| POP_SIZE_GPU         | 500        |
| REFRESH_MAP_TICKS    | 100        |
| SCENARIO             | default    |
| SIM_STEPS            | 800        |
| SPOIL_ADD            | 0.02       |
| SPOIL_MULT           | 1.002      |
| VISU_STEPS           | 2000       |
| W_COLL               | 10.0       |
| W_DISP               | 0.0        |
| W_EFFORT             | 1.0        |
| W_EXPLO              | 0.0        |
| W_MILL               | -30.0      |
| W_POL                | 0.0        |
| Z_MAX                | 10.0       |
| Z_MIN                | 1.0        |

## 2. Optimization Evolution
| Gen  |  Best Cost   |  Time (s)  |                                                                All Parameters                                                                |
| :--: | :----------: | :--------: | :------------------------------------------------------------------------------------------------------------------------------------------ |
| 00   | -2578.2319   | 4.32       | y_att=2.23, y_ali=1.93, y_f=1.39, d0_att=1.03, l_att=3.02, l_ali=1.06, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.60, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.40, y_acc=0.57, l_acc=1.85, d0_v=1.11, y_explo=0.57 |
| 01   | -3403.9868   | 4.39       | y_att=0.10, y_ali=0.95, y_f=0.32, d0_att=3.32, l_att=1.05, l_ali=3.76, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.50, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.65, y_acc=0.04, l_acc=4.47, d0_v=1.76, y_explo=0.11 |
| 02   | -3403.9868   | 4.19       | y_att=0.10, y_ali=0.95, y_f=0.32, d0_att=3.32, l_att=1.05, l_ali=3.76, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.50, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.65, y_acc=0.04, l_acc=4.47, d0_v=1.76, y_explo=0.11 |
| 03   | -3403.9868   | 4.12       | y_att=0.10, y_ali=0.95, y_f=0.32, d0_att=3.32, l_att=1.05, l_ali=3.76, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.50, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.65, y_acc=0.04, l_acc=4.47, d0_v=1.76, y_explo=0.11 |
| 04   | -3403.9868   | 4.07       | y_att=0.10, y_ali=0.95, y_f=0.32, d0_att=3.32, l_att=1.05, l_ali=3.76, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.50, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.65, y_acc=0.04, l_acc=4.47, d0_v=1.76, y_explo=0.11 |
| 05   | -3403.9868   | 4.03       | y_att=0.10, y_ali=0.95, y_f=0.32, d0_att=3.32, l_att=1.05, l_ali=3.76, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.50, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.65, y_acc=0.04, l_acc=4.47, d0_v=1.76, y_explo=0.11 |
| 06   | -4214.2539   | 4.06       | y_att=2.27, y_ali=2.42, y_f=0.92, d0_att=4.99, l_att=0.62, l_ali=5.40, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.66, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.20, y_acc=0.03, l_acc=1.53, d0_v=2.53, y_explo=1.22 |
| 07   | -5116.0854   | 4.14       | y_att=0.53, y_ali=1.93, y_f=0.71, d0_att=1.04, l_att=1.34, l_ali=5.95, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.81, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.94, y_acc=0.19, l_acc=1.20, d0_v=2.10, y_explo=0.99 |
| 08   | -5116.0854   | 4.13       | y_att=0.53, y_ali=1.93, y_f=0.71, d0_att=1.04, l_att=1.34, l_ali=5.95, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.81, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.94, y_acc=0.19, l_acc=1.20, d0_v=2.10, y_explo=0.99 |
| 09   | -5116.0854   | 4.14       | y_att=0.53, y_ali=1.93, y_f=0.71, d0_att=1.04, l_att=1.34, l_ali=5.95, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.81, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.94, y_acc=0.19, l_acc=1.20, d0_v=2.10, y_explo=0.99 |

**End of experiment.**
