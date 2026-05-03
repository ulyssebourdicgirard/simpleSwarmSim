# Experiment Report - PyTorch_CUDA (2D)
**Date:** 2026-05-03_18-50-44

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
| W_COLL               | 1.0        |
| W_DISP               | 20.0       |
| W_EFFORT             | 0.0        |
| W_EXPLO              | 0.0        |
| W_MILL               | -300.0     |
| W_POL                | 0.0        |
| Z_MAX                | 10.0       |
| Z_MIN                | 1.0        |

## 2. Optimization Evolution
| Gen  |  Best Cost   |  Time (s)  |                                                                All Parameters                                                                |
| :--: | :----------: | :--------: | :------------------------------------------------------------------------------------------------------------------------------------------ |
| 00   | -1830.4623   | 3.36       | y_att=4.67, y_ali=1.10, y_f=1.88, d0_att=7.79, l_att=6.35, l_ali=2.88, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.04, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.95, y_acc=1.49, l_acc=3.77, d0_v=1.19, y_explo=0.15 |
| 01   | -1830.4623   | 3.19       | y_att=4.67, y_ali=1.10, y_f=1.88, d0_att=7.79, l_att=6.35, l_ali=2.88, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.04, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.95, y_acc=1.49, l_acc=3.77, d0_v=1.19, y_explo=0.15 |
| 02   | -22946.3887  | 3.25       | y_att=4.90, y_ali=0.56, y_f=0.31, d0_att=10.95, l_att=9.05, l_ali=3.66, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.79, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.56, y_acc=0.27, l_acc=0.75, d0_v=2.03, y_explo=2.24 |
| 03   | -51940.7109  | 3.13       | y_att=4.26, y_ali=0.45, y_f=0.51, d0_att=7.40, l_att=8.16, l_ali=4.04, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.09, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.48, y_acc=0.12, l_acc=1.27, d0_v=1.65, y_explo=5.88 |
| 04   | -61264.3320  | 3.15       | y_att=6.22, y_ali=0.97, y_f=0.26, d0_att=11.54, l_att=10.65, l_ali=2.00, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.57, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.92, y_acc=0.01, l_acc=2.38, d0_v=1.67, y_explo=2.01 |
| 05   | -63016.1562  | 3.06       | y_att=7.97, y_ali=0.82, y_f=1.04, d0_att=11.94, l_att=6.86, l_ali=4.26, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.54, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.03, y_acc=0.08, l_acc=4.66, d0_v=3.28, y_explo=6.63 |
| 06   | -81949.6953  | 3.06       | y_att=10.59, y_ali=2.31, y_f=1.56, d0_att=8.90, l_att=4.50, l_ali=1.75, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.28, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.96, y_acc=0.06, l_acc=0.69, d0_v=1.31, y_explo=0.78 |
| 07   | -81949.6953  | 3.08       | y_att=10.59, y_ali=2.31, y_f=1.56, d0_att=8.90, l_att=4.50, l_ali=1.75, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.28, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.96, y_acc=0.06, l_acc=0.69, d0_v=1.31, y_explo=0.78 |
| 08   | -81949.6953  | 3.10       | y_att=10.59, y_ali=2.31, y_f=1.56, d0_att=8.90, l_att=4.50, l_ali=1.75, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.28, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.96, y_acc=0.06, l_acc=0.69, d0_v=1.31, y_explo=0.78 |
| 09   | -81949.6953  | 3.51       | y_att=10.59, y_ali=2.31, y_f=1.56, d0_att=8.90, l_att=4.50, l_ali=1.75, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.28, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.96, y_acc=0.06, l_acc=0.69, d0_v=1.31, y_explo=0.78 |
| 10   | -81949.6953  | 3.23       | y_att=10.59, y_ali=2.31, y_f=1.56, d0_att=8.90, l_att=4.50, l_ali=1.75, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.28, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.96, y_acc=0.06, l_acc=0.69, d0_v=1.31, y_explo=0.78 |
| 11   | -81949.6953  | 3.17       | y_att=10.59, y_ali=2.31, y_f=1.56, d0_att=8.90, l_att=4.50, l_ali=1.75, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.28, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.96, y_acc=0.06, l_acc=0.69, d0_v=1.31, y_explo=0.78 |
| 12   | -81949.6953  | 3.01       | y_att=10.59, y_ali=2.31, y_f=1.56, d0_att=8.90, l_att=4.50, l_ali=1.75, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.28, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.96, y_acc=0.06, l_acc=0.69, d0_v=1.31, y_explo=0.78 |
| 13   | -81949.6953  | 3.18       | y_att=10.59, y_ali=2.31, y_f=1.56, d0_att=8.90, l_att=4.50, l_ali=1.75, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.28, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.96, y_acc=0.06, l_acc=0.69, d0_v=1.31, y_explo=0.78 |
| 14   | -81949.6953  | 3.03       | y_att=10.59, y_ali=2.31, y_f=1.56, d0_att=8.90, l_att=4.50, l_ali=1.75, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.28, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.96, y_acc=0.06, l_acc=0.69, d0_v=1.31, y_explo=0.78 |
| 15   | -90415.1562  | 3.14       | y_att=8.54, y_ali=0.75, y_f=0.58, d0_att=19.97, l_att=11.82, l_ali=2.64, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.25, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.20, y_acc=0.03, l_acc=0.57, d0_v=2.66, y_explo=6.17 |
| 16   | -90415.1562  | 3.49       | y_att=8.54, y_ali=0.75, y_f=0.58, d0_att=19.97, l_att=11.82, l_ali=2.64, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.25, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.20, y_acc=0.03, l_acc=0.57, d0_v=2.66, y_explo=6.17 |
| 17   | -92832.6719  | 3.30       | y_att=9.16, y_ali=0.92, y_f=2.16, d0_att=10.46, l_att=9.63, l_ali=2.22, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.71, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.59, y_acc=0.15, l_acc=3.66, d0_v=2.06, y_explo=1.52 |
| 18   | -92832.6719  | 3.07       | y_att=9.16, y_ali=0.92, y_f=2.16, d0_att=10.46, l_att=9.63, l_ali=2.22, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.71, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.59, y_acc=0.15, l_acc=3.66, d0_v=2.06, y_explo=1.52 |
| 19   | -92832.6719  | 3.27       | y_att=9.16, y_ali=0.92, y_f=2.16, d0_att=10.46, l_att=9.63, l_ali=2.22, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.71, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.59, y_acc=0.15, l_acc=3.66, d0_v=2.06, y_explo=1.52 |

**End of experiment.**
