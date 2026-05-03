# Experiment Report - PyTorch_CUDA (2D)
**Date:** 2026-05-03_18-02-44

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
| NB_DRONES            | 20         |
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
| 00   | -1306.2596   | 3.24       | y_att=2.92, y_ali=3.38, y_f=1.69, d0_att=5.00, l_att=1.27, l_ali=4.59, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.77, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.35, y_acc=0.35, l_acc=1.81, d0_v=1.44, y_explo=4.67 |
| 01   | -1511.4633   | 3.18       | y_att=0.21, y_ali=1.98, y_f=0.55, d0_att=1.16, l_att=2.81, l_ali=3.65, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.96, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.25, y_acc=0.68, l_acc=1.37, d0_v=3.13, y_explo=3.75 |
| 02   | -1706.2114   | 3.34       | y_att=0.28, y_ali=3.25, y_f=1.86, d0_att=9.64, l_att=4.75, l_ali=4.64, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.74, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.23, y_acc=0.74, l_acc=3.52, d0_v=2.83, y_explo=3.87 |
| 03   | -1983.0426   | 3.21       | y_att=0.42, y_ali=1.08, y_f=1.54, d0_att=1.01, l_att=3.54, l_ali=2.20, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.52, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.17, y_acc=1.45, l_acc=1.32, d0_v=1.40, y_explo=2.62 |
| 04   | -2058.4761   | 3.15       | y_att=0.89, y_ali=1.47, y_f=0.66, d0_att=1.41, l_att=1.48, l_ali=4.69, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.68, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.36, y_acc=0.15, l_acc=2.22, d0_v=2.00, y_explo=1.30 |
| 05   | -3190.6941   | 3.01       | y_att=0.17, y_ali=2.20, y_f=0.45, d0_att=2.06, l_att=0.93, l_ali=3.46, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.99, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.27, y_acc=0.03, l_acc=2.84, d0_v=2.41, y_explo=4.86 |
| 06   | -3707.4136   | 2.98       | y_att=0.10, y_ali=2.04, y_f=1.65, d0_att=3.54, l_att=6.98, l_ali=5.04, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.31, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.56, y_acc=0.48, l_acc=0.66, d0_v=1.70, y_explo=4.01 |
| 07   | -3707.4136   | 2.98       | y_att=0.10, y_ali=2.04, y_f=1.65, d0_att=3.54, l_att=6.98, l_ali=5.04, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.31, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.56, y_acc=0.48, l_acc=0.66, d0_v=1.70, y_explo=4.01 |
| 08   | -3735.7441   | 3.05       | y_att=0.25, y_ali=2.78, y_f=1.74, d0_att=1.41, l_att=0.81, l_ali=2.21, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.42, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.82, y_acc=0.32, l_acc=1.46, d0_v=0.87, y_explo=1.76 |
| 09   | -5848.0962   | 3.01       | y_att=0.14, y_ali=1.85, y_f=1.53, d0_att=5.34, l_att=0.93, l_ali=4.83, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.16, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.34, y_acc=0.03, l_acc=1.80, d0_v=0.55, y_explo=1.12 |

**End of experiment.**
