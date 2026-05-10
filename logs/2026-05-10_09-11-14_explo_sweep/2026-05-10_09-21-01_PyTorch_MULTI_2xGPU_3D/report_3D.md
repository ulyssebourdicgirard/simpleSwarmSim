# Experiment Report - PyTorch_MULTI_2xGPU (3D)
**Date:** 2026-05-10_09-21-01

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
| MAP_STRATEGY         | global     |
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
| 00   | -134453.8750 | 37.74      | y_att=1.12, y_ali=1.10, y_f=0.02, d0_att=5.44, l_att=7.39, l_ali=4.73, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.64, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.12, y_acc=1.21, l_acc=1.79, d0_v=0.93, y_explo=1.59 |
| 01   | -134453.8750 | 37.49      | y_att=1.12, y_ali=1.10, y_f=0.02, d0_att=5.44, l_att=7.39, l_ali=4.73, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.64, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.12, y_acc=1.21, l_acc=1.79, d0_v=0.93, y_explo=1.59 |
| 02   | -137293.8750 | 37.54      | y_att=1.83, y_ali=0.98, y_f=0.10, d0_att=1.14, l_att=4.04, l_ali=3.00, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.54, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.94, y_acc=0.28, l_acc=2.36, d0_v=0.55, y_explo=0.52 |
| 03   | -138172.2656 | 37.51      | y_att=1.93, y_ali=1.94, y_f=0.10, d0_att=1.16, l_att=3.33, l_ali=8.67, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.44, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.66, y_acc=2.08, l_acc=1.26, d0_v=1.69, y_explo=1.92 |
| 04   | -138172.2656 | 37.47      | y_att=1.93, y_ali=1.94, y_f=0.10, d0_att=1.16, l_att=3.33, l_ali=8.67, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.44, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.66, y_acc=2.08, l_acc=1.26, d0_v=1.69, y_explo=1.92 |
| 05   | -139051.9375 | 37.41      | y_att=4.23, y_ali=2.75, y_f=0.10, d0_att=1.54, l_att=2.41, l_ali=4.08, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.87, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.81, y_acc=0.47, l_acc=3.09, d0_v=0.83, y_explo=0.84 |
| 06   | -139051.9375 | 37.37      | y_att=4.23, y_ali=2.75, y_f=0.10, d0_att=1.54, l_att=2.41, l_ali=4.08, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.87, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.81, y_acc=0.47, l_acc=3.09, d0_v=0.83, y_explo=0.84 |
| 07   | -139695.1875 | 37.33      | y_att=1.92, y_ali=3.15, y_f=0.11, d0_att=0.78, l_att=2.85, l_ali=2.15, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.68, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.39, l_acc=1.74, d0_v=0.34, y_explo=0.20 |
| 08   | -139707.2656 | 37.30      | y_att=4.66, y_ali=0.27, y_f=0.12, d0_att=1.16, l_att=1.77, l_ali=4.04, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.64, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.89, l_acc=0.85, d0_v=1.47, y_explo=0.45 |
| 09   | -139888.8125 | 37.28      | y_att=1.26, y_ali=0.76, y_f=0.12, d0_att=1.49, l_att=4.94, l_ali=1.28, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.48, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=1.90, l_acc=0.81, d0_v=0.52, y_explo=0.10 |
| 10   | -140571.4375 | 37.27      | y_att=1.31, y_ali=3.44, y_f=0.10, d0_att=0.94, l_att=4.06, l_ali=0.84, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.42, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.74, y_acc=1.37, l_acc=0.56, d0_v=0.50, y_explo=0.40 |
| 11   | -140844.4688 | 37.26      | y_att=0.55, y_ali=1.09, y_f=0.11, d0_att=1.64, l_att=6.65, l_ali=1.43, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.64, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=1.36, l_acc=0.71, d0_v=1.18, y_explo=0.18 |
| 12   | -140844.4688 | 37.25      | y_att=0.55, y_ali=1.09, y_f=0.11, d0_att=1.64, l_att=6.65, l_ali=1.43, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.64, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=1.36, l_acc=0.71, d0_v=1.18, y_explo=0.18 |
| 13   | -140869.9531 | 37.24      | y_att=2.11, y_ali=2.56, y_f=0.12, d0_att=0.73, l_att=2.63, l_ali=1.20, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.66, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=1.31, l_acc=0.71, d0_v=0.59, y_explo=1.01 |
| 14   | -140942.1562 | 37.24      | y_att=0.32, y_ali=0.32, y_f=0.10, d0_att=0.50, l_att=5.68, l_ali=6.26, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.72, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=1.74, l_acc=0.83, d0_v=0.50, y_explo=0.74 |
| 15   | -140942.1562 | 37.22      | y_att=0.32, y_ali=0.32, y_f=0.10, d0_att=0.50, l_att=5.68, l_ali=6.26, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.72, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=1.74, l_acc=0.83, d0_v=0.50, y_explo=0.74 |
| 16   | -141658.2188 | 37.26      | y_att=3.62, y_ali=1.83, y_f=0.11, d0_att=0.92, l_att=1.76, l_ali=1.36, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.15, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.72, y_acc=0.87, l_acc=1.06, d0_v=0.86, y_explo=0.79 |
| 17   | -141658.2188 | 37.22      | y_att=3.62, y_ali=1.83, y_f=0.11, d0_att=0.92, l_att=1.76, l_ali=1.36, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.15, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.72, y_acc=0.87, l_acc=1.06, d0_v=0.86, y_explo=0.79 |
| 18   | -141658.2188 | 37.23      | y_att=3.62, y_ali=1.83, y_f=0.11, d0_att=0.92, l_att=1.76, l_ali=1.36, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.15, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.72, y_acc=0.87, l_acc=1.06, d0_v=0.86, y_explo=0.79 |
| 19   | -141658.2188 | 37.22      | y_att=3.62, y_ali=1.83, y_f=0.11, d0_att=0.92, l_att=1.76, l_ali=1.36, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.15, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.72, y_acc=0.87, l_acc=1.06, d0_v=0.86, y_explo=0.79 |

**End of experiment.**
