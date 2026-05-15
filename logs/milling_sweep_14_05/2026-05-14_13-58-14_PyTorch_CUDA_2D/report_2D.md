# Experiment Report - PyTorch_CUDA (2D)
**Date:** 2026-05-14_13-58-14

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
| NB_DRONES            | 25         |
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
| 00   | -131927.7500 | 8.07       | y_att=4.87, y_ali=2.59, y_f=0.79, d0_att=7.93, l_att=11.71, l_ali=3.03, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.40, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.54, y_acc=0.18, l_acc=2.01, d0_v=2.60, y_explo=2.72 |
| 01   | -145786.4531 | 7.43       | y_att=7.22, y_ali=2.05, y_f=1.12, d0_att=12.00, l_att=11.74, l_ali=3.18, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.25, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.00, y_acc=0.61, l_acc=1.33, d0_v=2.86, y_explo=0.93 |
| 02   | -190835.1250 | 7.19       | y_att=18.72, y_ali=5.21, y_f=1.66, d0_att=9.33, l_att=8.58, l_ali=4.46, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=3.18, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.88, y_acc=1.01, l_acc=2.15, d0_v=8.84, y_explo=2.16 |
| 03   | -190835.1250 | 7.26       | y_att=18.72, y_ali=5.21, y_f=1.66, d0_att=9.33, l_att=8.58, l_ali=4.46, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=3.18, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.88, y_acc=1.01, l_acc=2.15, d0_v=8.84, y_explo=2.16 |
| 04   | -195642.9062 | 7.18       | y_att=4.74, y_ali=1.15, y_f=5.05, d0_att=7.76, l_att=14.21, l_ali=2.07, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.74, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.71, y_acc=1.51, l_acc=1.51, d0_v=7.09, y_explo=5.89 |
| 05   | -195642.9062 | 7.22       | y_att=4.74, y_ali=1.15, y_f=5.05, d0_att=7.76, l_att=14.21, l_ali=2.07, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.74, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.71, y_acc=1.51, l_acc=1.51, d0_v=7.09, y_explo=5.89 |
| 06   | -195642.9062 | 7.37       | y_att=4.74, y_ali=1.15, y_f=5.05, d0_att=7.76, l_att=14.21, l_ali=2.07, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.74, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.71, y_acc=1.51, l_acc=1.51, d0_v=7.09, y_explo=5.89 |
| 07   | -195642.9062 | 7.18       | y_att=4.74, y_ali=1.15, y_f=5.05, d0_att=7.76, l_att=14.21, l_ali=2.07, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.74, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.71, y_acc=1.51, l_acc=1.51, d0_v=7.09, y_explo=5.89 |
| 08   | -197700.1250 | 7.44       | y_att=13.29, y_ali=1.69, y_f=9.88, d0_att=13.88, l_att=14.04, l_ali=2.43, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.32, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.86, y_acc=1.96, l_acc=1.29, d0_v=3.41, y_explo=3.06 |
| 09   | -197700.1250 | 7.39       | y_att=13.29, y_ali=1.69, y_f=9.88, d0_att=13.88, l_att=14.04, l_ali=2.43, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.32, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.86, y_acc=1.96, l_acc=1.29, d0_v=3.41, y_explo=3.06 |

**End of experiment.**
