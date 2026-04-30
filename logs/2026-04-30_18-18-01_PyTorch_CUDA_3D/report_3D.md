# Experiment Report - PyTorch_CUDA (3D)
**Date:** 2026-04-30_18-18-01

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
| MAP_STRATEGY         | local_shared |
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
| 00   | -3165.7546   | 59.05      | y_att=0.97, y_ali=2.79, y_f=1.90, d0_att=4.05, l_att=5.40, l_ali=2.71, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.78, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.73, y_acc=0.86, l_acc=1.62, d0_v=2.67, y_explo=0.14 |
| 01   | -3190.7559   | 58.95      | y_att=1.03, y_ali=0.11, y_f=1.58, d0_att=4.66, l_att=6.02, l_ali=2.97, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.19, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.97, y_acc=0.97, l_acc=1.05, d0_v=3.39, y_explo=0.47 |
| 02   | -3431.5017   | 59.05      | y_att=1.33, y_ali=0.97, y_f=2.21, d0_att=2.22, l_att=2.94, l_ali=2.40, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.32, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.65, l_acc=0.76, d0_v=2.82, y_explo=0.19 |
| 03   | -3431.5017   | 59.14      | y_att=1.33, y_ali=0.97, y_f=2.21, d0_att=2.22, l_att=2.94, l_ali=2.40, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.32, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.65, l_acc=0.76, d0_v=2.82, y_explo=0.19 |
| 04   | -3431.5017   | 59.12      | y_att=1.33, y_ali=0.97, y_f=2.21, d0_att=2.22, l_att=2.94, l_ali=2.40, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.32, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.65, l_acc=0.76, d0_v=2.82, y_explo=0.19 |
| 05   | -3431.5017   | 59.16      | y_att=1.33, y_ali=0.97, y_f=2.21, d0_att=2.22, l_att=2.94, l_ali=2.40, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.32, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.65, l_acc=0.76, d0_v=2.82, y_explo=0.19 |
| 06   | -3431.5017   | 59.18      | y_att=1.33, y_ali=0.97, y_f=2.21, d0_att=2.22, l_att=2.94, l_ali=2.40, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.32, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.65, l_acc=0.76, d0_v=2.82, y_explo=0.19 |
| 07   | -3435.8699   | 59.26      | y_att=0.53, y_ali=0.96, y_f=1.16, d0_att=2.14, l_att=5.76, l_ali=1.28, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.49, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.16, l_acc=1.10, d0_v=0.97, y_explo=0.14 |
| 08   | -3515.3333   | 59.19      | y_att=0.47, y_ali=0.49, y_f=1.00, d0_att=3.52, l_att=5.38, l_ali=3.76, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.52, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.44, l_acc=0.67, d0_v=0.86, y_explo=0.18 |
| 09   | -3515.3333   | 59.19      | y_att=0.47, y_ali=0.49, y_f=1.00, d0_att=3.52, l_att=5.38, l_ali=3.76, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.52, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.44, l_acc=0.67, d0_v=0.86, y_explo=0.18 |

**End of experiment.**
