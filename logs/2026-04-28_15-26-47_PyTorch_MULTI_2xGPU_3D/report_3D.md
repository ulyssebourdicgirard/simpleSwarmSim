# Experiment Report - PyTorch_MULTI_2xGPU (3D)
**Date:** 2026-04-28_15-26-47

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
| MAP_STRATEGY         | local_shared |
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
| 00   | -4381.7109   | 23.81      | y_att=2.40, y_ali=1.30, y_f=0.61, d0_att=5.01, l_att=1.78, l_ali=3.71, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.82, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.64, y_acc=0.17, l_acc=0.78, d0_v=2.33, y_explo=0.03 |
| 01   | -4545.0859   | 23.44      | y_att=2.11, y_ali=3.13, y_f=1.63, d0_att=1.70, l_att=1.36, l_ali=1.95, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.11, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.35, y_acc=0.27, l_acc=2.57, d0_v=2.94, y_explo=0.33 |
| 02   | -4603.1255   | 23.45      | y_att=0.23, y_ali=0.08, y_f=1.64, d0_att=4.71, l_att=8.13, l_ali=2.39, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.37, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.11, l_acc=0.76, d0_v=2.78, y_explo=0.10 |
| 03   | -4604.1836   | 23.45      | y_att=2.87, y_ali=1.98, y_f=1.40, d0_att=3.67, l_att=4.04, l_ali=1.47, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.93, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.82, l_acc=0.89, d0_v=2.46, y_explo=0.19 |
| 04   | -4749.1973   | 23.45      | y_att=0.19, y_ali=3.97, y_f=0.76, d0_att=1.10, l_att=4.73, l_ali=3.44, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.93, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.72, y_acc=0.39, l_acc=0.56, d0_v=2.09, y_explo=0.33 |
| 05   | -4749.1973   | 23.45      | y_att=0.19, y_ali=3.97, y_f=0.76, d0_att=1.10, l_att=4.73, l_ali=3.44, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.93, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.72, y_acc=0.39, l_acc=0.56, d0_v=2.09, y_explo=0.33 |
| 06   | -4807.8042   | 23.45      | y_att=5.86, y_ali=3.01, y_f=1.41, d0_att=1.85, l_att=1.32, l_ali=2.48, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.67, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.84, l_acc=0.35, d0_v=1.90, y_explo=0.10 |
| 07   | -4876.8418   | 23.45      | y_att=5.86, y_ali=3.01, y_f=1.41, d0_att=1.85, l_att=1.32, l_ali=2.48, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.36, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.84, l_acc=0.35, d0_v=1.90, y_explo=0.10 |
| 08   | -4876.8418   | 23.45      | y_att=5.86, y_ali=3.01, y_f=1.41, d0_att=1.85, l_att=1.32, l_ali=2.48, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.36, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.84, l_acc=0.35, d0_v=1.90, y_explo=0.10 |
| 09   | -4876.8418   | 23.45      | y_att=5.86, y_ali=3.01, y_f=1.41, d0_att=1.85, l_att=1.32, l_ali=2.48, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.36, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.84, l_acc=0.35, d0_v=1.90, y_explo=0.10 |
| 10   | -4898.5249   | 23.45      | y_att=0.15, y_ali=0.66, y_f=1.22, d0_att=0.57, l_att=4.35, l_ali=3.05, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.54, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.15, l_acc=1.43, d0_v=1.43, y_explo=0.13 |
| 11   | -4898.5249   | 23.45      | y_att=0.15, y_ali=0.66, y_f=1.22, d0_att=0.57, l_att=4.35, l_ali=3.05, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.54, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.15, l_acc=1.43, d0_v=1.43, y_explo=0.13 |
| 12   | -4922.2051   | 23.45      | y_att=0.22, y_ali=0.06, y_f=1.09, d0_att=1.36, l_att=4.47, l_ali=0.23, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.62, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.14, l_acc=1.11, d0_v=2.51, y_explo=0.10 |
| 13   | -4922.2051   | 23.44      | y_att=0.22, y_ali=0.06, y_f=1.09, d0_att=1.36, l_att=4.47, l_ali=0.23, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.62, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.14, l_acc=1.11, d0_v=2.51, y_explo=0.10 |
| 14   | -4922.2051   | 23.44      | y_att=0.22, y_ali=0.06, y_f=1.09, d0_att=1.36, l_att=4.47, l_ali=0.23, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.62, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.14, l_acc=1.11, d0_v=2.51, y_explo=0.10 |
| 15   | -4922.2051   | 23.44      | y_att=0.22, y_ali=0.06, y_f=1.09, d0_att=1.36, l_att=4.47, l_ali=0.23, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.62, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.14, l_acc=1.11, d0_v=2.51, y_explo=0.10 |
| 16   | -4922.2051   | 23.44      | y_att=0.22, y_ali=0.06, y_f=1.09, d0_att=1.36, l_att=4.47, l_ali=0.23, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.62, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.14, l_acc=1.11, d0_v=2.51, y_explo=0.10 |
| 17   | -4964.5312   | 23.44      | y_att=1.45, y_ali=0.49, y_f=1.07, d0_att=1.22, l_att=1.67, l_ali=1.31, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.60, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.30, y_acc=0.28, l_acc=0.65, d0_v=0.62, y_explo=0.10 |
| 18   | -4964.5312   | 23.44      | y_att=1.45, y_ali=0.49, y_f=1.07, d0_att=1.22, l_att=1.67, l_ali=1.31, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.60, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.30, y_acc=0.28, l_acc=0.65, d0_v=0.62, y_explo=0.10 |
| 19   | -5079.8691   | 23.44      | y_att=0.81, y_ali=0.10, y_f=1.39, d0_att=1.01, l_att=2.40, l_ali=1.95, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=3.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.42, l_acc=0.57, d0_v=0.54, y_explo=0.14 |

**End of experiment.**
