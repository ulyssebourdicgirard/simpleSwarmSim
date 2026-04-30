# Experiment Report - PyTorch_CUDA (3D)
**Date:** 2026-04-30_18-48-09

## 1. Initial Configuration
| Parameter | Value |
| :--- | :--- |
| ALPHA_LPF            | 0.2        |
| ARENA_RADIUS         | 120.0      |
| COLLISION_DIST       | 0.4        |
| DT                   | 0.1        |
| ENABLE_3D            | True       |
| EXPLO_STRATEGY       | local_gradient |
| FOV_FACTOR           | 0.9        |
| FULL_MILLING_MODE    | False      |
| GEN_CPU              | 20         |
| GEN_GPU              | 10         |
| GRID_RES             | 5.0        |
| MAP_STRATEGY         | local_individual |
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
| 00   | -3168.4458   | 35.89      | y_att=1.77, y_ali=2.71, y_f=1.71, d0_att=6.75, l_att=4.66, l_ali=3.71, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.51, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.76, y_acc=0.05, l_acc=2.15, d0_v=0.57, y_explo=0.94 |
| 01   | -3232.5166   | 35.74      | y_att=2.04, y_ali=3.40, y_f=0.32, d0_att=4.69, l_att=10.92, l_ali=1.57, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.53, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.30, y_acc=0.20, l_acc=2.72, d0_v=2.12, y_explo=0.10 |
| 02   | -3351.6982   | 35.81      | y_att=1.32, y_ali=2.30, y_f=0.98, d0_att=6.45, l_att=5.89, l_ali=2.03, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.62, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.83, y_acc=0.45, l_acc=2.49, d0_v=1.98, y_explo=0.10 |
| 03   | -3389.5442   | 35.80      | y_att=0.61, y_ali=0.58, y_f=1.34, d0_att=1.56, l_att=2.10, l_ali=2.84, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.24, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.09, y_acc=0.06, l_acc=0.66, d0_v=2.79, y_explo=0.10 |
| 04   | -3393.2693   | 35.81      | y_att=0.61, y_ali=2.33, y_f=0.94, d0_att=1.56, l_att=3.02, l_ali=1.94, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.40, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.09, y_acc=0.21, l_acc=0.73, d0_v=2.74, y_explo=0.10 |
| 05   | -3442.8340   | 35.86      | y_att=1.36, y_ali=0.59, y_f=0.81, d0_att=1.30, l_att=3.07, l_ali=1.13, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.53, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.25, l_acc=1.31, d0_v=2.82, y_explo=0.27 |
| 06   | -3472.3525   | 35.82      | y_att=1.20, y_ali=0.08, y_f=1.35, d0_att=2.67, l_att=3.80, l_ali=4.12, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.08, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.29, l_acc=1.55, d0_v=1.65, y_explo=0.16 |
| 07   | -3472.3525   | 35.82      | y_att=1.20, y_ali=0.08, y_f=1.35, d0_att=2.67, l_att=3.80, l_ali=4.12, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.08, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.29, l_acc=1.55, d0_v=1.65, y_explo=0.16 |
| 08   | -3499.2756   | 35.81      | y_att=2.33, y_ali=3.65, y_f=0.91, d0_att=3.16, l_att=2.17, l_ali=2.22, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.89, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.95, y_acc=0.16, l_acc=1.87, d0_v=3.25, y_explo=0.11 |
| 09   | -3499.2756   | 35.84      | y_att=2.33, y_ali=3.65, y_f=0.91, d0_att=3.16, l_att=2.17, l_ali=2.22, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.89, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.95, y_acc=0.16, l_acc=1.87, d0_v=3.25, y_explo=0.11 |

**End of experiment.**
