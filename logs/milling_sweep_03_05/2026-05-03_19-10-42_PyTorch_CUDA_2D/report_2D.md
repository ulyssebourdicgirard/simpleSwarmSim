# Experiment Report - PyTorch_CUDA (2D)
**Date:** 2026-05-03_19-10-42

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
| NB_DRONES            | 10         |
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
| 00   | -29253.3652  | 3.12       | y_att=1.21, y_ali=3.54, y_f=0.24, d0_att=4.27, l_att=10.88, l_ali=4.69, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.48, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.52, y_acc=0.00, l_acc=3.41, d0_v=1.24, y_explo=2.79 |
| 01   | -37166.4414  | 3.23       | y_att=0.10, y_ali=0.58, y_f=1.65, d0_att=6.87, l_att=7.43, l_ali=4.26, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.02, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.00, y_acc=0.07, l_acc=3.01, d0_v=2.50, y_explo=3.68 |
| 02   | -52780.4219  | 3.30       | y_att=0.10, y_ali=1.56, y_f=2.45, d0_att=3.69, l_att=5.14, l_ali=4.51, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.58, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.41, y_acc=0.50, l_acc=0.64, d0_v=1.91, y_explo=3.69 |
| 03   | -52780.4219  | 3.12       | y_att=0.10, y_ali=1.56, y_f=2.45, d0_att=3.69, l_att=5.14, l_ali=4.51, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.58, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.41, y_acc=0.50, l_acc=0.64, d0_v=1.91, y_explo=3.69 |
| 04   | -52780.4219  | 3.00       | y_att=0.10, y_ali=1.56, y_f=2.45, d0_att=3.69, l_att=5.14, l_ali=4.51, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.58, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.41, y_acc=0.50, l_acc=0.64, d0_v=1.91, y_explo=3.69 |
| 05   | -56491.5664  | 2.98       | y_att=0.30, y_ali=2.43, y_f=1.59, d0_att=4.94, l_att=3.45, l_ali=7.44, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.01, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.04, l_acc=0.59, d0_v=1.68, y_explo=0.17 |
| 06   | -56491.5664  | 2.96       | y_att=0.30, y_ali=2.43, y_f=1.59, d0_att=4.94, l_att=3.45, l_ali=7.44, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.01, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.04, l_acc=0.59, d0_v=1.68, y_explo=0.17 |
| 07   | -74051.6562  | 2.91       | y_att=1.68, y_ali=0.80, y_f=1.77, d0_att=2.74, l_att=0.62, l_ali=13.80, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.53, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.54, y_acc=0.04, l_acc=2.19, d0_v=1.81, y_explo=5.09 |
| 08   | -114703.0469 | 2.88       | y_att=0.13, y_ali=1.00, y_f=3.17, d0_att=2.70, l_att=1.18, l_ali=13.62, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.86, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.14, y_acc=0.05, l_acc=1.20, d0_v=1.78, y_explo=7.01 |
| 09   | -114703.0469 | 3.20       | y_att=0.13, y_ali=1.00, y_f=3.17, d0_att=2.70, l_att=1.18, l_ali=13.62, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.86, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.14, y_acc=0.05, l_acc=1.20, d0_v=1.78, y_explo=7.01 |
| 10   | -114703.0469 | 3.08       | y_att=0.13, y_ali=1.00, y_f=3.17, d0_att=2.70, l_att=1.18, l_ali=13.62, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.86, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.14, y_acc=0.05, l_acc=1.20, d0_v=1.78, y_explo=7.01 |
| 11   | -135791.7656 | 2.99       | y_att=0.12, y_ali=0.83, y_f=2.76, d0_att=4.68, l_att=0.62, l_ali=20.94, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.14, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.32, y_acc=0.05, l_acc=0.86, d0_v=1.57, y_explo=1.57 |
| 12   | -135791.7656 | 2.93       | y_att=0.12, y_ali=0.83, y_f=2.76, d0_att=4.68, l_att=0.62, l_ali=20.94, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.14, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.32, y_acc=0.05, l_acc=0.86, d0_v=1.57, y_explo=1.57 |
| 13   | -150533.7812 | 2.95       | y_att=0.12, y_ali=0.45, y_f=2.17, d0_att=3.16, l_att=0.70, l_ali=26.77, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.02, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.08, y_acc=0.02, l_acc=0.90, d0_v=0.61, y_explo=3.50 |
| 14   | -150533.7812 | 3.03       | y_att=0.12, y_ali=0.45, y_f=2.17, d0_att=3.16, l_att=0.70, l_ali=26.77, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.02, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.08, y_acc=0.02, l_acc=0.90, d0_v=0.61, y_explo=3.50 |
| 15   | -150533.7812 | 2.98       | y_att=0.12, y_ali=0.45, y_f=2.17, d0_att=3.16, l_att=0.70, l_ali=26.77, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.02, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.08, y_acc=0.02, l_acc=0.90, d0_v=0.61, y_explo=3.50 |
| 16   | -150533.7812 | 3.05       | y_att=0.12, y_ali=0.45, y_f=2.17, d0_att=3.16, l_att=0.70, l_ali=26.77, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.02, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.08, y_acc=0.02, l_acc=0.90, d0_v=0.61, y_explo=3.50 |
| 17   | -150533.7812 | 3.33       | y_att=0.12, y_ali=0.45, y_f=2.17, d0_att=3.16, l_att=0.70, l_ali=26.77, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.02, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.08, y_acc=0.02, l_acc=0.90, d0_v=0.61, y_explo=3.50 |
| 18   | -150533.7812 | 3.29       | y_att=0.12, y_ali=0.45, y_f=2.17, d0_att=3.16, l_att=0.70, l_ali=26.77, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.02, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.08, y_acc=0.02, l_acc=0.90, d0_v=0.61, y_explo=3.50 |
| 19   | -150533.7812 | 3.08       | y_att=0.12, y_ali=0.45, y_f=2.17, d0_att=3.16, l_att=0.70, l_ali=26.77, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.02, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.08, y_acc=0.02, l_acc=0.90, d0_v=0.61, y_explo=3.50 |

**End of experiment.**
