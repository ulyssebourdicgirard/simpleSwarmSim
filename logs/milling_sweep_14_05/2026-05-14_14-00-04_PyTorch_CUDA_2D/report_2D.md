# Experiment Report - PyTorch_CUDA (2D)
**Date:** 2026-05-14_14-00-04

## 1. Initial Configuration
| Parameter | Value |
| :--- | :--- |
| ALPHA_LPF            | 0.2        |
| ARENA_RADIUS         | 50.0       |
| COLLISION_DIST       | 0.4        |
| DT                   | 0.1        |
| ENABLE_3D            | False      |
| EVAL_STRATEGY        | average    |
| EXPLO_STRATEGY       | global_best |
| FOV_FACTOR           | 0.9        |
| FULL_MILLING_MODE    | True       |
| GEN_CPU              | 20         |
| GEN_GPU              | 10         |
| GRID_RES             | 5.0        |
| MAP_STRATEGY         | local_shared |
| MAX_SPEED            | 20.0       |
| MAX_YAW_RATE         | 3.14       |
| MIN_SPAWN_DIST       | 2.0        |
| NB_DRONES            | 30         |
| NEIGHBORS            | 2          |
| N_INIT_CONDITIONS    | 4          |
| POP_SIZE_CPU         | 150        |
| POP_SIZE_GPU         | 5000       |
| REFRESH_MAP_TICKS    | 100        |
| SCENARIO             | default    |
| SIM_STEPS            | 400        |
| SPOIL_ADD            | 0.02       |
| SPOIL_MULT           | 1.002      |
| VISU_STEPS           | 800        |
| W_COLL               | 0          |
| W_DISP               | 0          |
| W_EFFORT             | 0          |
| W_EXPLO              | 0.0        |
| W_MILL               | -600.0     |
| W_POL                | 0          |
| W_STATIONARY         | 0          |
| Z_MAX                | 10.0       |
| Z_MIN                | 1.0        |

## 2. Optimization Evolution
| Gen  |  Best Cost   |  Time (s)  |                                                                All Parameters                                                                |
| :--: | :----------: | :--------: | :------------------------------------------------------------------------------------------------------------------------------------------ |
| 00   | -154385.8906 | 11.07      | y_att=4.91, y_ali=2.92, y_f=0.49, d0_att=6.16, l_att=9.67, l_ali=1.89, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.97, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.02, y_acc=0.09, l_acc=1.93, d0_v=1.55, y_explo=3.40 |
| 01   | -158773.2500 | 10.03      | y_att=4.29, y_ali=2.06, y_f=0.83, d0_att=6.21, l_att=7.44, l_ali=3.09, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.89, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.67, y_acc=0.82, l_acc=2.27, d0_v=14.52, y_explo=1.16 |
| 02   | -196973.3750 | 10.14      | y_att=10.51, y_ali=1.32, y_f=0.95, d0_att=13.41, l_att=12.20, l_ali=3.64, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.92, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.25, y_acc=1.64, l_acc=1.79, d0_v=6.31, y_explo=1.87 |
| 03   | -196973.3750 | 10.02      | y_att=10.51, y_ali=1.32, y_f=0.95, d0_att=13.41, l_att=12.20, l_ali=3.64, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.92, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.25, y_acc=1.64, l_acc=1.79, d0_v=6.31, y_explo=1.87 |
| 04   | -196973.3750 | 10.07      | y_att=10.51, y_ali=1.32, y_f=0.95, d0_att=13.41, l_att=12.20, l_ali=3.64, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.92, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.25, y_acc=1.64, l_acc=1.79, d0_v=6.31, y_explo=1.87 |
| 05   | -196973.3750 | 10.08      | y_att=10.51, y_ali=1.32, y_f=0.95, d0_att=13.41, l_att=12.20, l_ali=3.64, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.92, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.25, y_acc=1.64, l_acc=1.79, d0_v=6.31, y_explo=1.87 |
| 06   | -196973.3750 | 10.08      | y_att=10.51, y_ali=1.32, y_f=0.95, d0_att=13.41, l_att=12.20, l_ali=3.64, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.92, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.25, y_acc=1.64, l_acc=1.79, d0_v=6.31, y_explo=1.87 |
| 07   | -196973.3750 | 10.13      | y_att=10.51, y_ali=1.32, y_f=0.95, d0_att=13.41, l_att=12.20, l_ali=3.64, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.92, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.25, y_acc=1.64, l_acc=1.79, d0_v=6.31, y_explo=1.87 |
| 08   | -197543.1875 | 10.30      | y_att=12.12, y_ali=0.65, y_f=0.92, d0_att=10.21, l_att=9.88, l_ali=3.96, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.28, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.93, y_acc=2.14, l_acc=5.02, d0_v=5.33, y_explo=1.79 |
| 09   | -197657.2969 | 10.02      | y_att=11.46, y_ali=3.17, y_f=9.18, d0_att=10.16, l_att=9.10, l_ali=5.57, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.94, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.30, y_acc=3.21, l_acc=0.48, d0_v=6.35, y_explo=1.54 |

**End of experiment.**
