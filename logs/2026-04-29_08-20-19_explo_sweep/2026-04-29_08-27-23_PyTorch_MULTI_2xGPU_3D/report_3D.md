# Experiment Report - PyTorch_MULTI_2xGPU (3D)
**Date:** 2026-04-29_08-27-23

## 1. Initial Configuration
| Parameter | Value |
| :--- | :--- |
| ALPHA_LPF            | 0.2        |
| ARENA_RADIUS         | 100.0      |
| COLLISION_DIST       | 0.4        |
| DT                   | 0.1        |
| ENABLE_3D            | True       |
| EXPLO_STRATEGY       | global_closest |
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
| 00   | -4778.7173   | 17.53      | y_att=0.55, y_ali=2.85, y_f=0.55, d0_att=3.40, l_att=9.21, l_ali=2.15, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.49, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.94, y_acc=0.13, l_acc=1.92, d0_v=1.34, y_explo=0.15 |
| 01   | -4908.3442   | 17.21      | y_att=2.47, y_ali=1.66, y_f=1.56, d0_att=1.53, l_att=1.82, l_ali=4.97, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.20, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.83, y_acc=0.31, l_acc=2.07, d0_v=2.65, y_explo=0.52 |
| 02   | -5059.5708   | 17.21      | y_att=0.11, y_ali=0.89, y_f=2.05, d0_att=3.89, l_att=6.87, l_ali=5.59, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.72, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.86, y_acc=1.06, l_acc=1.10, d0_v=1.82, y_explo=0.48 |
| 03   | -5077.2769   | 17.21      | y_att=0.50, y_ali=1.57, y_f=0.61, d0_att=6.68, l_att=5.62, l_ali=1.24, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.02, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.76, y_acc=0.03, l_acc=2.83, d0_v=0.83, y_explo=0.32 |
| 04   | -5077.2769   | 17.22      | y_att=0.50, y_ali=1.57, y_f=0.61, d0_att=6.68, l_att=5.62, l_ali=1.24, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.02, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.76, y_acc=0.03, l_acc=2.83, d0_v=0.83, y_explo=0.32 |
| 05   | -5180.6665   | 17.22      | y_att=0.74, y_ali=0.59, y_f=1.87, d0_att=3.13, l_att=4.15, l_ali=3.77, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.78, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.84, y_acc=0.46, l_acc=1.01, d0_v=0.98, y_explo=0.25 |
| 06   | -5180.6665   | 17.22      | y_att=0.74, y_ali=0.59, y_f=1.87, d0_att=3.13, l_att=4.15, l_ali=3.77, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.78, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.84, y_acc=0.46, l_acc=1.01, d0_v=0.98, y_explo=0.25 |
| 07   | -5180.6665   | 17.23      | y_att=0.74, y_ali=0.59, y_f=1.87, d0_att=3.13, l_att=4.15, l_ali=3.77, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.78, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.84, y_acc=0.46, l_acc=1.01, d0_v=0.98, y_explo=0.25 |
| 08   | -5180.6665   | 17.23      | y_att=0.74, y_ali=0.59, y_f=1.87, d0_att=3.13, l_att=4.15, l_ali=3.77, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.78, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.84, y_acc=0.46, l_acc=1.01, d0_v=0.98, y_explo=0.25 |
| 09   | -5253.4673   | 17.23      | y_att=0.98, y_ali=0.06, y_f=5.73, d0_att=7.13, l_att=0.53, l_ali=1.14, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.84, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.47, l_acc=1.73, d0_v=1.63, y_explo=0.13 |
| 10   | -5253.4673   | 17.23      | y_att=0.98, y_ali=0.06, y_f=5.73, d0_att=7.13, l_att=0.53, l_ali=1.14, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.84, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.47, l_acc=1.73, d0_v=1.63, y_explo=0.13 |
| 11   | -5253.4673   | 17.23      | y_att=0.98, y_ali=0.06, y_f=5.73, d0_att=7.13, l_att=0.53, l_ali=1.14, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.84, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.47, l_acc=1.73, d0_v=1.63, y_explo=0.13 |
| 12   | -5253.4673   | 17.23      | y_att=0.98, y_ali=0.06, y_f=5.73, d0_att=7.13, l_att=0.53, l_ali=1.14, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.84, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.47, l_acc=1.73, d0_v=1.63, y_explo=0.13 |
| 13   | -5253.4673   | 17.23      | y_att=0.98, y_ali=0.06, y_f=5.73, d0_att=7.13, l_att=0.53, l_ali=1.14, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.84, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.47, l_acc=1.73, d0_v=1.63, y_explo=0.13 |
| 14   | -5253.4673   | 17.23      | y_att=0.98, y_ali=0.06, y_f=5.73, d0_att=7.13, l_att=0.53, l_ali=1.14, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.84, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.47, l_acc=1.73, d0_v=1.63, y_explo=0.13 |
| 15   | -5253.4673   | 17.23      | y_att=0.98, y_ali=0.06, y_f=5.73, d0_att=7.13, l_att=0.53, l_ali=1.14, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.84, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.47, l_acc=1.73, d0_v=1.63, y_explo=0.13 |
| 16   | -5264.9341   | 17.23      | y_att=0.41, y_ali=1.20, y_f=1.00, d0_att=1.09, l_att=3.55, l_ali=4.87, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.01, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.54, l_acc=0.65, d0_v=1.14, y_explo=0.10 |
| 17   | -5264.9341   | 17.23      | y_att=0.41, y_ali=1.20, y_f=1.00, d0_att=1.09, l_att=3.55, l_ali=4.87, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.01, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.54, l_acc=0.65, d0_v=1.14, y_explo=0.10 |
| 18   | -5266.8013   | 17.23      | y_att=0.13, y_ali=5.71, y_f=0.69, d0_att=1.06, l_att=4.07, l_ali=0.17, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.79, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.42, y_acc=0.20, l_acc=0.99, d0_v=2.18, y_explo=0.15 |
| 19   | -5344.5532   | 17.23      | y_att=0.35, y_ali=0.10, y_f=0.77, d0_att=1.26, l_att=1.18, l_ali=1.03, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.78, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.08, l_acc=1.18, d0_v=0.61, y_explo=0.10 |

**End of experiment.**
