# Experiment Report - PyTorch_MULTI_2xGPU (3D)
**Date:** 2026-04-28_08-59-45

## 1. Initial Configuration
| Parameter | Value |
| :--- | :--- |
| ALPHA_LPF            | 0.2        |
| ARENA_RADIUS         | 100.0      |
| COLLISION_DIST       | 0.4        |
| DT                   | 0.1        |
| ENABLE_3D            | True       |
| EXPLO_STRATEGY       | local_gradient |
| FOV_FACTOR           | 0.577      |
| FULL_MILLING_MODE    | False      |
| GEN_CPU              | 20         |
| GEN_GPU              | 20         |
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
| 00   | -2242.1621   | 32.14      | y_att=1.29, y_ali=3.46, y_f=0.60, d0_att=2.54, l_att=4.26, l_ali=2.21, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.74, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.81, y_acc=0.07, l_acc=2.83, d0_v=2.82, y_explo=0.45 |
| 01   | -2345.6108   | 31.79      | y_att=0.77, y_ali=4.06, y_f=0.83, d0_att=4.23, l_att=3.02, l_ali=2.33, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.40, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.05, y_acc=0.02, l_acc=0.70, d0_v=0.73, y_explo=0.29 |
| 02   | -2391.8086   | 31.80      | y_att=2.16, y_ali=0.02, y_f=1.52, d0_att=1.61, l_att=2.65, l_ali=2.96, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.91, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.52, y_acc=0.29, l_acc=1.52, d0_v=3.19, y_explo=0.15 |
| 03   | -2557.2366   | 31.79      | y_att=3.59, y_ali=1.13, y_f=1.66, d0_att=3.55, l_att=2.48, l_ali=3.03, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.91, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.24, y_acc=0.00, l_acc=0.94, d0_v=0.57, y_explo=0.10 |
| 04   | -2623.6072   | 31.78      | y_att=0.63, y_ali=0.05, y_f=0.99, d0_att=1.42, l_att=1.06, l_ali=3.15, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.78, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.80, y_acc=0.09, l_acc=1.09, d0_v=1.47, y_explo=0.12 |
| 05   | -2738.0515   | 31.78      | y_att=0.66, y_ali=0.33, y_f=1.66, d0_att=1.31, l_att=1.64, l_ali=3.03, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.64, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.24, y_acc=0.00, l_acc=0.65, d0_v=0.62, y_explo=0.10 |
| 06   | -2781.3972   | 31.78      | y_att=0.43, y_ali=3.15, y_f=0.95, d0_att=1.71, l_att=3.35, l_ali=0.55, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.90, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.56, y_acc=0.16, l_acc=0.54, d0_v=1.83, y_explo=0.14 |
| 07   | -2781.3972   | 31.77      | y_att=0.43, y_ali=3.15, y_f=0.95, d0_att=1.71, l_att=3.35, l_ali=0.55, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.90, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.56, y_acc=0.16, l_acc=0.54, d0_v=1.83, y_explo=0.14 |
| 08   | -2781.3972   | 31.77      | y_att=0.43, y_ali=3.15, y_f=0.95, d0_att=1.71, l_att=3.35, l_ali=0.55, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.90, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.56, y_acc=0.16, l_acc=0.54, d0_v=1.83, y_explo=0.14 |
| 09   | -2818.7021   | 31.77      | y_att=0.46, y_ali=0.41, y_f=0.49, d0_att=1.05, l_att=0.18, l_ali=0.77, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.29, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.01, l_acc=0.17, d0_v=1.60, y_explo=0.10 |
| 10   | -2818.7021   | 31.77      | y_att=0.46, y_ali=0.41, y_f=0.49, d0_att=1.05, l_att=0.18, l_ali=0.77, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.29, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.01, l_acc=0.17, d0_v=1.60, y_explo=0.10 |
| 11   | -2818.7021   | 31.77      | y_att=0.46, y_ali=0.41, y_f=0.49, d0_att=1.05, l_att=0.18, l_ali=0.77, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.29, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.01, l_acc=0.17, d0_v=1.60, y_explo=0.10 |
| 12   | -2851.2385   | 31.77      | y_att=0.22, y_ali=1.50, y_f=1.36, d0_att=1.59, l_att=2.38, l_ali=0.19, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.95, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.06, l_acc=0.80, d0_v=0.73, y_explo=0.10 |
| 13   | -2865.5325   | 31.77      | y_att=0.76, y_ali=1.29, y_f=0.57, d0_att=1.19, l_att=1.17, l_ali=2.31, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.66, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.03, l_acc=1.87, d0_v=2.66, y_explo=0.13 |
| 14   | -2865.5325   | 31.77      | y_att=0.76, y_ali=1.29, y_f=0.57, d0_att=1.19, l_att=1.17, l_ali=2.31, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.66, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.03, l_acc=1.87, d0_v=2.66, y_explo=0.13 |
| 15   | -2900.2512   | 31.77      | y_att=0.95, y_ali=0.88, y_f=1.83, d0_att=0.65, l_att=0.98, l_ali=2.93, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.29, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.08, l_acc=1.43, d0_v=1.68, y_explo=0.10 |
| 16   | -2908.3171   | 31.76      | y_att=0.87, y_ali=2.17, y_f=1.07, d0_att=1.43, l_att=1.19, l_ali=2.40, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.82, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.03, l_acc=0.59, d0_v=0.75, y_explo=0.10 |
| 17   | -2908.3171   | 31.76      | y_att=0.87, y_ali=2.17, y_f=1.07, d0_att=1.43, l_att=1.19, l_ali=2.40, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.82, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.03, l_acc=0.59, d0_v=0.75, y_explo=0.10 |
| 18   | -2908.3171   | 31.76      | y_att=0.87, y_ali=2.17, y_f=1.07, d0_att=1.43, l_att=1.19, l_ali=2.40, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.82, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.03, l_acc=0.59, d0_v=0.75, y_explo=0.10 |
| 19   | -2908.3171   | 31.76      | y_att=0.87, y_ali=2.17, y_f=1.07, d0_att=1.43, l_att=1.19, l_ali=2.40, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.82, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.03, l_acc=0.59, d0_v=0.75, y_explo=0.10 |

**End of experiment.**
