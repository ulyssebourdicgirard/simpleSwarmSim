# Experiment Report - PyTorch_MULTI_2xGPU (3D)
**Date:** 2026-05-10_10-15-36

## 1. Initial Configuration
| Parameter | Value |
| :--- | :--- |
| ALPHA_LPF            | 0.2        |
| ARENA_RADIUS         | 50.0       |
| COLLISION_DIST       | 0.4        |
| DT                   | 0.1        |
| ENABLE_3D            | True       |
| EXPLO_STRATEGY       | global_best |
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
| 00   | -130900.9219 | 44.48      | y_att=1.56, y_ali=0.27, y_f=0.00, d0_att=5.50, l_att=5.81, l_ali=3.96, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.16, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.68, y_acc=1.37, l_acc=3.67, d0_v=1.83, y_explo=0.09 |
| 01   | -130900.9219 | 44.22      | y_att=1.56, y_ali=0.27, y_f=0.00, d0_att=5.50, l_att=5.81, l_ali=3.96, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.16, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.68, y_acc=1.37, l_acc=3.67, d0_v=1.83, y_explo=0.09 |
| 02   | -132954.7500 | 44.18      | y_att=4.33, y_ali=1.82, y_f=0.10, d0_att=2.12, l_att=3.40, l_ali=2.01, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.67, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.64, y_acc=1.02, l_acc=1.34, d0_v=1.14, y_explo=0.55 |
| 03   | -136068.6562 | 44.16      | y_att=1.71, y_ali=1.80, y_f=0.10, d0_att=0.89, l_att=4.55, l_ali=2.74, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.06, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.71, l_acc=3.20, d0_v=1.13, y_explo=1.82 |
| 04   | -136068.6562 | 44.13      | y_att=1.71, y_ali=1.80, y_f=0.10, d0_att=0.89, l_att=4.55, l_ali=2.74, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.06, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.71, l_acc=3.20, d0_v=1.13, y_explo=1.82 |
| 05   | -138908.8125 | 44.10      | y_att=1.48, y_ali=1.31, y_f=0.11, d0_att=1.04, l_att=4.24, l_ali=5.64, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.83, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.26, y_acc=0.24, l_acc=2.81, d0_v=0.44, y_explo=1.01 |
| 06   | -138908.8125 | 44.06      | y_att=1.48, y_ali=1.31, y_f=0.11, d0_att=1.04, l_att=4.24, l_ali=5.64, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.83, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.26, y_acc=0.24, l_acc=2.81, d0_v=0.44, y_explo=1.01 |
| 07   | -138931.6250 | 44.03      | y_att=1.80, y_ali=2.82, y_f=0.10, d0_att=0.50, l_att=2.13, l_ali=1.49, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.25, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=1.03, l_acc=0.56, d0_v=0.87, y_explo=0.69 |
| 08   | -138931.6250 | 44.01      | y_att=1.80, y_ali=2.82, y_f=0.10, d0_att=0.50, l_att=2.13, l_ali=1.49, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.25, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=1.03, l_acc=0.56, d0_v=0.87, y_explo=0.69 |
| 09   | -138985.7344 | 43.98      | y_att=1.92, y_ali=1.27, y_f=0.10, d0_att=0.79, l_att=3.14, l_ali=2.47, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.64, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.93, y_acc=1.23, l_acc=0.56, d0_v=0.64, y_explo=0.80 |
| 10   | -138985.7344 | 43.96      | y_att=1.92, y_ali=1.27, y_f=0.10, d0_att=0.79, l_att=3.14, l_ali=2.47, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.64, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.93, y_acc=1.23, l_acc=0.56, d0_v=0.64, y_explo=0.80 |
| 11   | -139413.0625 | 43.93      | y_att=2.16, y_ali=1.26, y_f=0.10, d0_att=0.65, l_att=2.46, l_ali=2.13, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.96, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.55, l_acc=3.93, d0_v=1.70, y_explo=0.46 |
| 12   | -139812.9688 | 43.92      | y_att=2.20, y_ali=1.31, y_f=0.10, d0_att=0.60, l_att=2.39, l_ali=1.61, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.56, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.97, y_acc=1.15, l_acc=1.55, d0_v=1.04, y_explo=0.11 |
| 13   | -141264.7656 | 43.90      | y_att=1.89, y_ali=0.07, y_f=0.13, d0_att=0.78, l_att=2.43, l_ali=1.70, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.54, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.72, l_acc=1.11, d0_v=0.62, y_explo=0.10 |
| 14   | -141264.7656 | 43.90      | y_att=1.89, y_ali=0.07, y_f=0.13, d0_att=0.78, l_att=2.43, l_ali=1.70, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.54, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.72, l_acc=1.11, d0_v=0.62, y_explo=0.10 |
| 15   | -141264.7656 | 43.88      | y_att=1.89, y_ali=0.07, y_f=0.13, d0_att=0.78, l_att=2.43, l_ali=1.70, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.54, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.72, l_acc=1.11, d0_v=0.62, y_explo=0.10 |
| 16   | -141264.7656 | 43.87      | y_att=1.89, y_ali=0.07, y_f=0.13, d0_att=0.78, l_att=2.43, l_ali=1.70, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.54, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.72, l_acc=1.11, d0_v=0.62, y_explo=0.10 |
| 17   | -141264.7656 | 43.85      | y_att=1.89, y_ali=0.07, y_f=0.13, d0_att=0.78, l_att=2.43, l_ali=1.70, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.54, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.72, l_acc=1.11, d0_v=0.62, y_explo=0.10 |
| 18   | -141264.7656 | 43.85      | y_att=1.89, y_ali=0.07, y_f=0.13, d0_att=0.78, l_att=2.43, l_ali=1.70, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.54, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.72, l_acc=1.11, d0_v=0.62, y_explo=0.10 |
| 19   | -141264.7656 | 43.84      | y_att=1.89, y_ali=0.07, y_f=0.13, d0_att=0.78, l_att=2.43, l_ali=1.70, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.54, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.72, l_acc=1.11, d0_v=0.62, y_explo=0.10 |

**End of experiment.**
