# Experiment Report - PyTorch_CUDA (3D)
**Date:** 2026-05-03_17-46-29

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
| NB_DRONES            | 5          |
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
| 00   | -3419.0918   | 4.34       | y_att=0.17, y_ali=3.91, y_f=1.48, d0_att=7.40, l_att=10.86, l_ali=1.10, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.26, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.78, y_acc=1.57, l_acc=0.59, d0_v=1.80, y_explo=4.46 |
| 01   | -5098.1533   | 4.29       | y_att=1.45, y_ali=2.31, y_f=0.95, d0_att=1.75, l_att=2.91, l_ali=0.76, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.75, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.30, y_acc=0.54, l_acc=2.46, d0_v=1.99, y_explo=1.77 |
| 02   | -5583.4326   | 4.33       | y_att=0.13, y_ali=0.38, y_f=1.19, d0_att=5.52, l_att=1.94, l_ali=3.83, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.15, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.67, y_acc=0.03, l_acc=1.16, d0_v=1.97, y_explo=1.66 |
| 03   | -7749.9868   | 4.20       | y_att=0.34, y_ali=2.12, y_f=1.69, d0_att=4.47, l_att=1.53, l_ali=7.55, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.49, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.89, y_acc=0.04, l_acc=3.42, d0_v=0.96, y_explo=2.68 |
| 04   | -7749.9868   | 4.08       | y_att=0.34, y_ali=2.12, y_f=1.69, d0_att=4.47, l_att=1.53, l_ali=7.55, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.49, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.89, y_acc=0.04, l_acc=3.42, d0_v=0.96, y_explo=2.68 |
| 05   | -7749.9868   | 3.95       | y_att=0.34, y_ali=2.12, y_f=1.69, d0_att=4.47, l_att=1.53, l_ali=7.55, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.49, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.89, y_acc=0.04, l_acc=3.42, d0_v=0.96, y_explo=2.68 |
| 06   | -7749.9868   | 4.19       | y_att=0.34, y_ali=2.12, y_f=1.69, d0_att=4.47, l_att=1.53, l_ali=7.55, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.49, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.89, y_acc=0.04, l_acc=3.42, d0_v=0.96, y_explo=2.68 |
| 07   | -7749.9868   | 4.24       | y_att=0.34, y_ali=2.12, y_f=1.69, d0_att=4.47, l_att=1.53, l_ali=7.55, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.49, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.89, y_acc=0.04, l_acc=3.42, d0_v=0.96, y_explo=2.68 |
| 08   | -7749.9868   | 4.05       | y_att=0.34, y_ali=2.12, y_f=1.69, d0_att=4.47, l_att=1.53, l_ali=7.55, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.49, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.89, y_acc=0.04, l_acc=3.42, d0_v=0.96, y_explo=2.68 |
| 09   | -7749.9868   | 4.08       | y_att=0.34, y_ali=2.12, y_f=1.69, d0_att=4.47, l_att=1.53, l_ali=7.55, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.49, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.89, y_acc=0.04, l_acc=3.42, d0_v=0.96, y_explo=2.68 |

**End of experiment.**
