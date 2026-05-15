# Experiment Report - PyTorch_CUDA (2D)
**Date:** 2026-05-14_13-57-01

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
| NB_DRONES            | 20         |
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
| 00   | -116491.7578 | 4.40       | y_att=4.44, y_ali=2.57, y_f=1.41, d0_att=7.01, l_att=5.43, l_ali=2.24, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.18, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.76, y_acc=0.30, l_acc=3.46, d0_v=2.71, y_explo=1.93 |
| 01   | -126913.5234 | 4.47       | y_att=11.50, y_ali=3.14, y_f=0.78, d0_att=7.21, l_att=20.98, l_ali=2.46, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.73, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.68, y_acc=0.15, l_acc=0.64, d0_v=2.67, y_explo=0.16 |
| 02   | -182117.7500 | 4.12       | y_att=10.01, y_ali=2.09, y_f=1.95, d0_att=6.46, l_att=10.31, l_ali=3.14, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.69, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.62, y_acc=0.61, l_acc=2.13, d0_v=2.53, y_explo=1.02 |
| 03   | -182181.2188 | 4.18       | y_att=12.62, y_ali=3.16, y_f=1.40, d0_att=10.96, l_att=4.41, l_ali=4.00, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.75, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.69, y_acc=0.23, l_acc=0.66, d0_v=12.77, y_explo=5.88 |
| 04   | -189181.5000 | 4.22       | y_att=6.82, y_ali=1.85, y_f=1.18, d0_att=7.83, l_att=14.05, l_ali=3.46, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=13.81, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.88, y_acc=1.95, l_acc=0.96, d0_v=3.39, y_explo=1.54 |
| 05   | -189181.5000 | 4.11       | y_att=6.82, y_ali=1.85, y_f=1.18, d0_att=7.83, l_att=14.05, l_ali=3.46, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=13.81, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.88, y_acc=1.95, l_acc=0.96, d0_v=3.39, y_explo=1.54 |
| 06   | -194858.1250 | 4.28       | y_att=13.73, y_ali=2.23, y_f=5.74, d0_att=7.00, l_att=9.18, l_ali=5.55, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.15, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.17, y_acc=0.04, l_acc=1.29, d0_v=1.86, y_explo=19.81 |
| 07   | -194858.1250 | 4.19       | y_att=13.73, y_ali=2.23, y_f=5.74, d0_att=7.00, l_att=9.18, l_ali=5.55, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.15, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.17, y_acc=0.04, l_acc=1.29, d0_v=1.86, y_explo=19.81 |
| 08   | -194858.1250 | 4.13       | y_att=13.73, y_ali=2.23, y_f=5.74, d0_att=7.00, l_att=9.18, l_ali=5.55, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.15, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.17, y_acc=0.04, l_acc=1.29, d0_v=1.86, y_explo=19.81 |
| 09   | -194858.1250 | 4.61       | y_att=13.73, y_ali=2.23, y_f=5.74, d0_att=7.00, l_att=9.18, l_ali=5.55, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.15, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.17, y_acc=0.04, l_acc=1.29, d0_v=1.86, y_explo=19.81 |

**End of experiment.**
