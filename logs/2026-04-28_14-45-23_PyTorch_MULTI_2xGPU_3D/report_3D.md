# Experiment Report - PyTorch_MULTI_2xGPU (3D)
**Date:** 2026-04-28_14-45-23

## 1. Initial Configuration
| Parameter | Value |
| :--- | :--- |
| ALPHA_LPF            | 0.2        |
| ARENA_RADIUS         | 100.0      |
| COLLISION_DIST       | 0.4        |
| DT                   | 0.1        |
| ENABLE_3D            | True       |
| EXPLO_STRATEGY       | local_gradient |
| FOV_FACTOR           | 0.9        |
| FULL_MILLING_MODE    | False      |
| GEN_CPU              | 20         |
| GEN_GPU              | 20         |
| GRID_RES             | 5.0        |
| MAP_STRATEGY         | global     |
| MAX_SPEED            | 20.0       |
| MAX_YAW_RATE         | 3.14       |
| MIN_SPAWN_DIST       | 2.0        |
| NB_DRONES            | 15         |
| NEIGHBORS            | 2          |
| N_INIT_CONDITIONS    | 4          |
| POP_SIZE_CPU         | 150        |
| POP_SIZE_GPU         | 5000       |
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
| 00   | -4609.1147   | 17.49      | y_att=1.19, y_ali=0.99, y_f=1.96, d0_att=3.02, l_att=2.61, l_ali=4.99, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.50, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.85, y_acc=0.68, l_acc=1.11, d0_v=2.86, y_explo=0.42 |
| 01   | -4936.6230   | 17.19      | y_att=3.28, y_ali=1.55, y_f=1.28, d0_att=3.07, l_att=2.62, l_ali=1.23, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.38, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.89, y_acc=0.41, l_acc=1.15, d0_v=1.40, y_explo=0.10 |
| 02   | -4948.6650   | 17.19      | y_att=1.19, y_ali=0.99, y_f=1.64, d0_att=2.86, l_att=2.61, l_ali=4.99, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.04, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.85, y_acc=1.68, l_acc=1.11, d0_v=2.86, y_explo=0.42 |
| 03   | -5086.2607   | 17.19      | y_att=0.18, y_ali=3.15, y_f=0.96, d0_att=2.82, l_att=0.87, l_ali=2.02, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.02, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.23, y_acc=0.58, l_acc=0.96, d0_v=1.55, y_explo=0.55 |
| 04   | -5134.8086   | 17.20      | y_att=0.85, y_ali=0.06, y_f=1.16, d0_att=1.41, l_att=3.09, l_ali=2.54, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.85, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.75, y_acc=0.36, l_acc=1.52, d0_v=1.95, y_explo=0.11 |
| 05   | -5134.8086   | 17.20      | y_att=0.85, y_ali=0.06, y_f=1.16, d0_att=1.41, l_att=3.09, l_ali=2.54, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.85, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.75, y_acc=0.36, l_acc=1.52, d0_v=1.95, y_explo=0.11 |
| 06   | -5134.8086   | 17.21      | y_att=0.85, y_ali=0.06, y_f=1.16, d0_att=1.41, l_att=3.09, l_ali=2.54, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.85, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.75, y_acc=0.36, l_acc=1.52, d0_v=1.95, y_explo=0.11 |
| 07   | -5169.2666   | 17.22      | y_att=0.45, y_ali=1.97, y_f=1.04, d0_att=0.57, l_att=2.13, l_ali=1.17, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.10, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.66, y_acc=0.27, l_acc=1.47, d0_v=1.04, y_explo=0.26 |
| 08   | -5169.2666   | 17.22      | y_att=0.45, y_ali=1.97, y_f=1.04, d0_att=0.57, l_att=2.13, l_ali=1.17, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.10, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.66, y_acc=0.27, l_acc=1.47, d0_v=1.04, y_explo=0.26 |
| 09   | -5169.2666   | 17.22      | y_att=0.45, y_ali=1.97, y_f=1.04, d0_att=0.57, l_att=2.13, l_ali=1.17, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.10, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.66, y_acc=0.27, l_acc=1.47, d0_v=1.04, y_explo=0.26 |
| 10   | -5169.2666   | 17.22      | y_att=0.45, y_ali=1.97, y_f=1.04, d0_att=0.57, l_att=2.13, l_ali=1.17, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.10, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.66, y_acc=0.27, l_acc=1.47, d0_v=1.04, y_explo=0.26 |
| 11   | -5188.9512   | 17.22      | y_att=0.18, y_ali=0.26, y_f=0.60, d0_att=2.78, l_att=0.80, l_ali=2.75, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.87, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.35, l_acc=0.67, d0_v=1.28, y_explo=0.20 |
| 12   | -5236.1675   | 17.23      | y_att=0.13, y_ali=0.71, y_f=0.70, d0_att=1.93, l_att=5.08, l_ali=2.31, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.99, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.31, l_acc=0.48, d0_v=1.06, y_explo=0.17 |
| 13   | -5270.9678   | 17.23      | y_att=0.14, y_ali=1.04, y_f=0.72, d0_att=1.17, l_att=2.44, l_ali=1.69, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.93, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.14, l_acc=1.30, d0_v=0.89, y_explo=0.31 |
| 14   | -5270.9678   | 17.22      | y_att=0.14, y_ali=1.04, y_f=0.72, d0_att=1.17, l_att=2.44, l_ali=1.69, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.93, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.14, l_acc=1.30, d0_v=0.89, y_explo=0.31 |
| 15   | -5270.9678   | 17.22      | y_att=0.14, y_ali=1.04, y_f=0.72, d0_att=1.17, l_att=2.44, l_ali=1.69, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.93, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.14, l_acc=1.30, d0_v=0.89, y_explo=0.31 |
| 16   | -5270.9678   | 17.23      | y_att=0.14, y_ali=1.04, y_f=0.72, d0_att=1.17, l_att=2.44, l_ali=1.69, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.93, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.14, l_acc=1.30, d0_v=0.89, y_explo=0.31 |
| 17   | -5270.9678   | 17.23      | y_att=0.14, y_ali=1.04, y_f=0.72, d0_att=1.17, l_att=2.44, l_ali=1.69, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.93, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.14, l_acc=1.30, d0_v=0.89, y_explo=0.31 |
| 18   | -5270.9678   | 17.23      | y_att=0.14, y_ali=1.04, y_f=0.72, d0_att=1.17, l_att=2.44, l_ali=1.69, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.93, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.14, l_acc=1.30, d0_v=0.89, y_explo=0.31 |
| 19   | -5277.0029   | 17.23      | y_att=0.70, y_ali=0.10, y_f=0.46, d0_att=0.51, l_att=1.53, l_ali=1.42, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.84, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.14, l_acc=1.18, d0_v=1.24, y_explo=0.23 |

**End of experiment.**
