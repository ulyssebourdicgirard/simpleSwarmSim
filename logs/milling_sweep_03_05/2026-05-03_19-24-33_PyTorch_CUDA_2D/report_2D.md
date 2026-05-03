# Experiment Report - PyTorch_CUDA (2D)
**Date:** 2026-05-03_19-24-33

## 1. Initial Configuration
| Parameter | Value |
| :--- | :--- |
| ALPHA_LPF            | 0.2        |
| ARENA_RADIUS         | 50.0       |
| COLLISION_DIST       | 0.4        |
| DT                   | 0.1        |
| ENABLE_3D            | False      |
| EXPLO_STRATEGY       | global_best |
| FOV_FACTOR           | 0.9        |
| FULL_MILLING_MODE    | True       |
| GEN_CPU              | 20         |
| GEN_GPU              | 20         |
| GRID_RES             | 5.0        |
| MAP_STRATEGY         | local_shared |
| MAX_SPEED            | 30.0       |
| MAX_YAW_RATE         | 3.14       |
| MIN_SPAWN_DIST       | 2.0        |
| NB_DRONES            | 30         |
| NEIGHBORS            | 4          |
| N_INIT_CONDITIONS    | 4          |
| POP_SIZE_CPU         | 150        |
| POP_SIZE_GPU         | 5000       |
| REFRESH_MAP_TICKS    | 100        |
| SCENARIO             | default    |
| SIM_STEPS            | 800        |
| SPOIL_ADD            | 0.02       |
| SPOIL_MULT           | 1.002      |
| VISU_STEPS           | 2000       |
| W_COLL               | 10.0       |
| W_DISP               | 2.0        |
| W_EFFORT             | 0.5        |
| W_EXPLO              | 0.0        |
| W_MILL               | -300.0     |
| W_POL                | 0.0        |
| Z_MAX                | 10.0       |
| Z_MIN                | 1.0        |

## 2. Optimization Evolution
| Gen  |  Best Cost   |  Time (s)  |                                                                All Parameters                                                                |
| :--: | :----------: | :--------: | :------------------------------------------------------------------------------------------------------------------------------------------ |
| 00   | -5250.6753   | 20.20      | y_att=4.73, y_ali=1.17, y_f=0.31, d0_att=7.99, l_att=10.57, l_ali=3.09, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.22, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.30, y_acc=1.59, l_acc=2.65, d0_v=1.42, y_explo=3.05 |
| 01   | -24397.1406  | 19.95      | y_att=0.10, y_ali=1.95, y_f=1.00, d0_att=4.78, l_att=3.63, l_ali=2.46, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.91, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.16, y_acc=0.05, l_acc=2.52, d0_v=2.31, y_explo=0.87 |
| 02   | -39968.1953  | 20.15      | y_att=0.10, y_ali=2.13, y_f=2.12, d0_att=4.33, l_att=6.33, l_ali=2.18, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.19, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.41, y_acc=0.07, l_acc=2.69, d0_v=2.21, y_explo=1.12 |
| 03   | -39968.1953  | 20.10      | y_att=0.10, y_ali=2.13, y_f=2.12, d0_att=4.33, l_att=6.33, l_ali=2.18, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.19, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.41, y_acc=0.07, l_acc=2.69, d0_v=2.21, y_explo=1.12 |
| 04   | -58693.8359  | 19.90      | y_att=0.10, y_ali=1.15, y_f=1.51, d0_att=7.55, l_att=14.82, l_ali=2.63, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.59, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.24, y_acc=0.19, l_acc=0.38, d0_v=0.67, y_explo=0.86 |
| 05   | -58693.8359  | 19.89      | y_att=0.10, y_ali=1.15, y_f=1.51, d0_att=7.55, l_att=14.82, l_ali=2.63, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.59, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.24, y_acc=0.19, l_acc=0.38, d0_v=0.67, y_explo=0.86 |
| 06   | -58693.8359  | 19.85      | y_att=0.10, y_ali=1.15, y_f=1.51, d0_att=7.55, l_att=14.82, l_ali=2.63, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.59, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.24, y_acc=0.19, l_acc=0.38, d0_v=0.67, y_explo=0.86 |
| 07   | -58693.8359  | 19.86      | y_att=0.10, y_ali=1.15, y_f=1.51, d0_att=7.55, l_att=14.82, l_ali=2.63, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.59, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.24, y_acc=0.19, l_acc=0.38, d0_v=0.67, y_explo=0.86 |
| 08   | -58693.8359  | 19.83      | y_att=0.10, y_ali=1.15, y_f=1.51, d0_att=7.55, l_att=14.82, l_ali=2.63, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.59, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.24, y_acc=0.19, l_acc=0.38, d0_v=0.67, y_explo=0.86 |
| 09   | -58693.8359  | 19.84      | y_att=0.10, y_ali=1.15, y_f=1.51, d0_att=7.55, l_att=14.82, l_ali=2.63, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.59, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.24, y_acc=0.19, l_acc=0.38, d0_v=0.67, y_explo=0.86 |
| 10   | -58693.8359  | 19.86      | y_att=0.10, y_ali=1.15, y_f=1.51, d0_att=7.55, l_att=14.82, l_ali=2.63, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.59, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.24, y_acc=0.19, l_acc=0.38, d0_v=0.67, y_explo=0.86 |
| 11   | -58693.8359  | 19.87      | y_att=0.10, y_ali=1.15, y_f=1.51, d0_att=7.55, l_att=14.82, l_ali=2.63, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.59, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.24, y_acc=0.19, l_acc=0.38, d0_v=0.67, y_explo=0.86 |
| 12   | -58693.8359  | 19.87      | y_att=0.10, y_ali=1.15, y_f=1.51, d0_att=7.55, l_att=14.82, l_ali=2.63, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.59, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.24, y_acc=0.19, l_acc=0.38, d0_v=0.67, y_explo=0.86 |
| 13   | -58693.8359  | 19.85      | y_att=0.10, y_ali=1.15, y_f=1.51, d0_att=7.55, l_att=14.82, l_ali=2.63, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.59, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.24, y_acc=0.19, l_acc=0.38, d0_v=0.67, y_explo=0.86 |
| 14   | -58693.8359  | 19.86      | y_att=0.10, y_ali=1.15, y_f=1.51, d0_att=7.55, l_att=14.82, l_ali=2.63, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.59, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.24, y_acc=0.19, l_acc=0.38, d0_v=0.67, y_explo=0.86 |
| 15   | -58693.8359  | 19.83      | y_att=0.10, y_ali=1.15, y_f=1.51, d0_att=7.55, l_att=14.82, l_ali=2.63, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.59, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.24, y_acc=0.19, l_acc=0.38, d0_v=0.67, y_explo=0.86 |
| 16   | -58693.8359  | 19.82      | y_att=0.10, y_ali=1.15, y_f=1.51, d0_att=7.55, l_att=14.82, l_ali=2.63, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.59, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.24, y_acc=0.19, l_acc=0.38, d0_v=0.67, y_explo=0.86 |
| 17   | -58693.8359  | 19.82      | y_att=0.10, y_ali=1.15, y_f=1.51, d0_att=7.55, l_att=14.82, l_ali=2.63, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.59, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.24, y_acc=0.19, l_acc=0.38, d0_v=0.67, y_explo=0.86 |
| 18   | -58693.8359  | 19.80      | y_att=0.10, y_ali=1.15, y_f=1.51, d0_att=7.55, l_att=14.82, l_ali=2.63, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.59, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.24, y_acc=0.19, l_acc=0.38, d0_v=0.67, y_explo=0.86 |
| 19   | -58693.8359  | 19.78      | y_att=0.10, y_ali=1.15, y_f=1.51, d0_att=7.55, l_att=14.82, l_ali=2.63, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.59, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.24, y_acc=0.19, l_acc=0.38, d0_v=0.67, y_explo=0.86 |

**End of experiment.**
