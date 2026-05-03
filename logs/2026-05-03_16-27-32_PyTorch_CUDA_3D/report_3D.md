# Experiment Report - PyTorch_CUDA (3D)
**Date:** 2026-05-03_16-27-32

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
| GEN_GPU              | 15         |
| GRID_RES             | 10.0       |
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
| SCENARIO             | exploration |
| SIM_STEPS            | 5000       |
| SPOIL_ADD            | 0.02       |
| SPOIL_MULT           | 1.002      |
| VISU_STEPS           | 5000       |
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
| 00   | -140156.7812 | 60.92      | y_att=2.78, y_ali=0.42, y_f=1.03, d0_att=3.01, l_att=9.39, l_ali=2.96, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.59, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.18, y_acc=0.42, l_acc=0.87, d0_v=1.99, y_explo=2.74 |
| 01   | -162317.0938 | 59.92      | y_att=2.98, y_ali=2.71, y_f=1.26, d0_att=1.31, l_att=8.07, l_ali=1.97, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.25, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.48, y_acc=0.22, l_acc=2.51, d0_v=2.33, y_explo=8.52 |
| 02   | -165362.4219 | 61.42      | y_att=2.98, y_ali=2.71, y_f=1.26, d0_att=1.31, l_att=8.07, l_ali=1.97, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.48, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.48, y_acc=0.22, l_acc=2.51, d0_v=2.33, y_explo=8.52 |
| 03   | -167130.9219 | 62.18      | y_att=3.10, y_ali=1.71, y_f=1.32, d0_att=1.31, l_att=8.57, l_ali=2.21, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.99, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.48, y_acc=0.17, l_acc=2.51, d0_v=2.02, y_explo=8.52 |
| 04   | -167130.9219 | 61.55      | y_att=3.10, y_ali=1.71, y_f=1.32, d0_att=1.31, l_att=8.57, l_ali=2.21, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.99, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.48, y_acc=0.17, l_acc=2.51, d0_v=2.02, y_explo=8.52 |
| 05   | -169424.0469 | 61.84      | y_att=3.53, y_ali=0.26, y_f=2.41, d0_att=4.00, l_att=12.99, l_ali=1.17, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.57, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.48, y_acc=0.51, l_acc=0.58, d0_v=2.63, y_explo=8.79 |
| 06   | -169424.0469 | 61.89      | y_att=3.53, y_ali=0.26, y_f=2.41, d0_att=4.00, l_att=12.99, l_ali=1.17, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.57, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.48, y_acc=0.51, l_acc=0.58, d0_v=2.63, y_explo=8.79 |
| 07   | -170686.1562 | 60.22      | y_att=3.03, y_ali=0.54, y_f=0.73, d0_att=1.20, l_att=4.12, l_ali=2.12, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.13, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.94, y_acc=0.43, l_acc=0.63, d0_v=1.42, y_explo=9.25 |
| 08   | -175405.9062 | 60.27      | y_att=7.95, y_ali=0.49, y_f=2.41, d0_att=1.81, l_att=4.29, l_ali=1.53, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.67, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.00, y_acc=0.25, l_acc=3.70, d0_v=1.73, y_explo=7.81 |
| 09   | -175405.9062 | 60.29      | y_att=7.95, y_ali=0.49, y_f=2.41, d0_att=1.81, l_att=4.29, l_ali=1.53, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.67, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.00, y_acc=0.25, l_acc=3.70, d0_v=1.73, y_explo=7.81 |
| 10   | -175405.9062 | 62.13      | y_att=7.95, y_ali=0.49, y_f=2.41, d0_att=1.81, l_att=4.29, l_ali=1.53, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.67, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.00, y_acc=0.25, l_acc=3.70, d0_v=1.73, y_explo=7.81 |
| 11   | -176153.2031 | 60.39      | y_att=8.53, y_ali=0.92, y_f=0.66, d0_att=2.25, l_att=4.74, l_ali=2.04, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.36, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.80, y_acc=0.78, l_acc=0.55, d0_v=1.73, y_explo=9.25 |
| 12   | -176153.2031 | 60.85      | y_att=8.53, y_ali=0.92, y_f=0.66, d0_att=2.25, l_att=4.74, l_ali=2.04, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.36, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.80, y_acc=0.78, l_acc=0.55, d0_v=1.73, y_explo=9.25 |
| 13   | -176153.2031 | 62.66      | y_att=8.53, y_ali=0.92, y_f=0.66, d0_att=2.25, l_att=4.74, l_ali=2.04, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.36, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.80, y_acc=0.78, l_acc=0.55, d0_v=1.73, y_explo=9.25 |
| 14   | -176153.2031 | 60.93      | y_att=8.53, y_ali=0.92, y_f=0.66, d0_att=2.25, l_att=4.74, l_ali=2.04, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.36, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.80, y_acc=0.78, l_acc=0.55, d0_v=1.73, y_explo=9.25 |

**End of experiment.**
