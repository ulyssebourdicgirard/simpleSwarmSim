# Experiment Report - PyTorch_MULTI_2xGPU (3D)
**Date:** 2026-05-10_10-03-41

## 1. Initial Configuration
| Parameter | Value |
| :--- | :--- |
| ALPHA_LPF            | 0.2        |
| ARENA_RADIUS         | 50.0       |
| COLLISION_DIST       | 0.4        |
| DT                   | 0.1        |
| ENABLE_3D            | True       |
| EXPLO_STRATEGY       | local_gradient |
| FOV_FACTOR           | 0.9        |
| FULL_MILLING_MODE    | False      |
| GEN_CPU              | 20         |
| GEN_GPU              | 20         |
| GRID_RES             | 5.0        |
| MAP_STRATEGY         | local_shared |
| MAX_SPEED            | 20.0       |
| MAX_YAW_RATE         | 3.14       |
| MIN_SPAWN_DIST       | 2.0        |
| NB_DRONES            | 10         |
| NEIGHBORS            | 2          |
| N_INIT_CONDITIONS    | 4          |
| POP_SIZE_CPU         | 150        |
| POP_SIZE_GPU         | 5000       |
| REFRESH_MAP_TICKS    | 100        |
| SCENARIO             | exploration |
| SIM_STEPS            | 3000       |
| SPOIL_ADD            | 0.02       |
| SPOIL_MULT           | 1.002      |
| VISU_STEPS           | 6000       |
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
| 00   | -127638.3828 | 30.71      | y_att=1.50, y_ali=2.49, y_f=0.14, d0_att=1.91, l_att=6.80, l_ali=1.92, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.52, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.96, y_acc=0.68, l_acc=2.29, d0_v=1.54, y_explo=0.01 |
| 01   | -127638.3828 | 30.37      | y_att=1.50, y_ali=2.49, y_f=0.14, d0_att=1.91, l_att=6.80, l_ali=1.92, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.52, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.96, y_acc=0.68, l_acc=2.29, d0_v=1.54, y_explo=0.01 |
| 02   | -132546.8750 | 30.42      | y_att=2.82, y_ali=1.17, y_f=1.12, d0_att=1.04, l_att=2.15, l_ali=1.86, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.86, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.85, y_acc=0.65, l_acc=0.61, d0_v=0.95, y_explo=0.44 |
| 03   | -134513.5625 | 30.42      | y_att=3.71, y_ali=3.55, y_f=0.11, d0_att=1.11, l_att=2.63, l_ali=3.68, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.82, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.32, y_acc=0.53, l_acc=0.80, d0_v=1.01, y_explo=0.14 |
| 04   | -134513.5625 | 30.39      | y_att=3.71, y_ali=3.55, y_f=0.11, d0_att=1.11, l_att=2.63, l_ali=3.68, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.82, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.32, y_acc=0.53, l_acc=0.80, d0_v=1.01, y_explo=0.14 |
| 05   | -135036.9688 | 30.38      | y_att=0.82, y_ali=0.19, y_f=0.12, d0_att=1.18, l_att=6.08, l_ali=2.80, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.65, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=1.95, l_acc=1.65, d0_v=2.54, y_explo=0.11 |
| 06   | -135733.9375 | 30.39      | y_att=1.83, y_ali=0.18, y_f=0.13, d0_att=1.56, l_att=4.78, l_ali=7.24, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.01, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.03, y_acc=1.08, l_acc=0.56, d0_v=1.55, y_explo=0.95 |
| 07   | -136027.3906 | 30.39      | y_att=1.06, y_ali=0.28, y_f=0.10, d0_att=0.50, l_att=3.80, l_ali=3.19, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.06, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.83, l_acc=2.08, d0_v=1.32, y_explo=0.95 |
| 08   | -136949.5938 | 30.39      | y_att=2.88, y_ali=1.46, y_f=0.10, d0_att=1.34, l_att=3.20, l_ali=0.38, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.92, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.49, y_acc=1.11, l_acc=0.69, d0_v=0.99, y_explo=0.10 |
| 09   | -136949.5938 | 30.38      | y_att=2.88, y_ali=1.46, y_f=0.10, d0_att=1.34, l_att=3.20, l_ali=0.38, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.92, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.49, y_acc=1.11, l_acc=0.69, d0_v=0.99, y_explo=0.10 |
| 10   | -138301.0625 | 30.39      | y_att=2.42, y_ali=0.00, y_f=0.12, d0_att=1.33, l_att=4.54, l_ali=1.41, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.61, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=1.60, l_acc=1.24, d0_v=1.01, y_explo=0.15 |
| 11   | -138397.1406 | 30.39      | y_att=1.53, y_ali=1.39, y_f=0.10, d0_att=0.58, l_att=2.49, l_ali=0.89, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.62, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=1.15, l_acc=0.44, d0_v=0.65, y_explo=0.11 |
| 12   | -138397.1406 | 30.39      | y_att=1.53, y_ali=1.39, y_f=0.10, d0_att=0.58, l_att=2.49, l_ali=0.89, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.62, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=1.15, l_acc=0.44, d0_v=0.65, y_explo=0.11 |
| 13   | -138397.1406 | 30.38      | y_att=1.53, y_ali=1.39, y_f=0.10, d0_att=0.58, l_att=2.49, l_ali=0.89, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.62, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=1.15, l_acc=0.44, d0_v=0.65, y_explo=0.11 |
| 14   | -138557.5312 | 30.39      | y_att=0.69, y_ali=1.38, y_f=0.13, d0_att=0.58, l_att=4.61, l_ali=3.12, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.47, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=1.96, l_acc=0.72, d0_v=1.15, y_explo=0.10 |
| 15   | -138557.5312 | 30.38      | y_att=0.69, y_ali=1.38, y_f=0.13, d0_att=0.58, l_att=4.61, l_ali=3.12, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.47, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=1.96, l_acc=0.72, d0_v=1.15, y_explo=0.10 |
| 16   | -138567.2188 | 30.38      | y_att=1.10, y_ali=0.45, y_f=0.10, d0_att=0.50, l_att=2.56, l_ali=0.13, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.63, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.86, l_acc=0.83, d0_v=1.18, y_explo=0.13 |
| 17   | -138567.2188 | 30.37      | y_att=1.10, y_ali=0.45, y_f=0.10, d0_att=0.50, l_att=2.56, l_ali=0.13, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.63, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.86, l_acc=0.83, d0_v=1.18, y_explo=0.13 |
| 18   | -138716.6562 | 30.38      | y_att=1.20, y_ali=0.68, y_f=0.10, d0_att=0.51, l_att=2.94, l_ali=0.21, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.35, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.85, l_acc=1.26, d0_v=0.80, y_explo=0.10 |
| 19   | -138716.6562 | 30.38      | y_att=1.20, y_ali=0.68, y_f=0.10, d0_att=0.51, l_att=2.94, l_ali=0.21, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.35, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.85, l_acc=1.26, d0_v=0.80, y_explo=0.10 |

**End of experiment.**
