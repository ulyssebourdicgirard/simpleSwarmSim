# Experiment Report - PyTorch_CUDA (2D)
**Date:** 2026-05-03_18-04-10

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
| GEN_GPU              | 10         |
| GRID_RES             | 5.0        |
| MAP_STRATEGY         | local_shared |
| MAX_SPEED            | 30.0       |
| MAX_YAW_RATE         | 3.14       |
| MIN_SPAWN_DIST       | 2.0        |
| NB_DRONES            | 25         |
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
| 00   | -643.6212    | 3.27       | y_att=0.09, y_ali=2.05, y_f=0.85, d0_att=7.38, l_att=3.92, l_ali=4.01, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.97, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.61, y_acc=0.61, l_acc=3.02, d0_v=2.40, y_explo=4.49 |
| 01   | -1375.2740   | 4.25       | y_att=0.10, y_ali=3.62, y_f=1.40, d0_att=4.44, l_att=3.47, l_ali=4.37, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.42, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.91, y_acc=1.65, l_acc=3.39, d0_v=2.67, y_explo=1.96 |
| 02   | -1375.2740   | 3.29       | y_att=0.10, y_ali=3.62, y_f=1.40, d0_att=4.44, l_att=3.47, l_ali=4.37, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.42, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.91, y_acc=1.65, l_acc=3.39, d0_v=2.67, y_explo=1.96 |
| 03   | -2138.4915   | 3.33       | y_att=0.10, y_ali=0.54, y_f=0.89, d0_att=2.86, l_att=2.60, l_ali=6.36, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.68, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.30, y_acc=0.40, l_acc=2.10, d0_v=2.09, y_explo=0.15 |
| 04   | -2352.0671   | 3.95       | y_att=0.10, y_ali=0.86, y_f=1.59, d0_att=2.46, l_att=2.02, l_ali=6.13, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.53, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.25, y_acc=0.39, l_acc=2.32, d0_v=1.59, y_explo=5.55 |
| 05   | -2909.1201   | 3.30       | y_att=0.10, y_ali=2.31, y_f=2.12, d0_att=2.70, l_att=14.84, l_ali=4.74, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.81, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.79, y_acc=0.74, l_acc=1.68, d0_v=1.94, y_explo=5.71 |
| 06   | -2909.1201   | 3.11       | y_att=0.10, y_ali=2.31, y_f=2.12, d0_att=2.70, l_att=14.84, l_ali=4.74, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.81, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.79, y_acc=0.74, l_acc=1.68, d0_v=1.94, y_explo=5.71 |
| 07   | -2909.1201   | 3.01       | y_att=0.10, y_ali=2.31, y_f=2.12, d0_att=2.70, l_att=14.84, l_ali=4.74, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.81, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.79, y_acc=0.74, l_acc=1.68, d0_v=1.94, y_explo=5.71 |
| 08   | -2909.1201   | 3.23       | y_att=0.10, y_ali=2.31, y_f=2.12, d0_att=2.70, l_att=14.84, l_ali=4.74, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.81, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.79, y_acc=0.74, l_acc=1.68, d0_v=1.94, y_explo=5.71 |
| 09   | -2909.1201   | 3.30       | y_att=0.10, y_ali=2.31, y_f=2.12, d0_att=2.70, l_att=14.84, l_ali=4.74, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.81, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.79, y_acc=0.74, l_acc=1.68, d0_v=1.94, y_explo=5.71 |

**End of experiment.**
