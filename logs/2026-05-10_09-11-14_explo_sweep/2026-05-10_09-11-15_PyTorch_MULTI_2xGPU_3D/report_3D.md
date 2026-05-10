# Experiment Report - PyTorch_MULTI_2xGPU (3D)
**Date:** 2026-05-10_09-11-15

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
| 00   | -133717.7344 | 24.22      | y_att=3.22, y_ali=0.43, y_f=0.03, d0_att=1.16, l_att=1.50, l_ali=2.13, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.75, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.87, y_acc=0.85, l_acc=2.85, d0_v=1.92, y_explo=0.14 |
| 01   | -133717.7344 | 23.88      | y_att=3.22, y_ali=0.43, y_f=0.03, d0_att=1.16, l_att=1.50, l_ali=2.13, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.75, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.87, y_acc=0.85, l_acc=2.85, d0_v=1.92, y_explo=0.14 |
| 02   | -133717.7344 | 23.89      | y_att=3.22, y_ali=0.43, y_f=0.03, d0_att=1.16, l_att=1.50, l_ali=2.13, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.75, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.87, y_acc=0.85, l_acc=2.85, d0_v=1.92, y_explo=0.14 |
| 03   | -136689.2812 | 23.92      | y_att=1.67, y_ali=0.43, y_f=0.10, d0_att=2.11, l_att=1.50, l_ali=1.79, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.81, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.76, y_acc=0.90, l_acc=2.85, d0_v=1.36, y_explo=0.14 |
| 04   | -136689.2812 | 23.95      | y_att=1.67, y_ali=0.43, y_f=0.10, d0_att=2.11, l_att=1.50, l_ali=1.79, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.81, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.76, y_acc=0.90, l_acc=2.85, d0_v=1.36, y_explo=0.14 |
| 05   | -138275.1719 | 23.98      | y_att=1.99, y_ali=0.98, y_f=0.15, d0_att=1.57, l_att=5.24, l_ali=2.67, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.77, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.81, y_acc=2.24, l_acc=0.39, d0_v=0.95, y_explo=0.85 |
| 06   | -138492.4531 | 24.00      | y_att=3.45, y_ali=0.91, y_f=0.10, d0_att=0.98, l_att=2.29, l_ali=1.79, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.49, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.76, l_acc=0.80, d0_v=0.99, y_explo=0.15 |
| 07   | -139880.0938 | 24.01      | y_att=0.48, y_ali=0.04, y_f=0.10, d0_att=3.34, l_att=4.52, l_ali=1.92, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.85, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.76, y_acc=1.89, l_acc=0.70, d0_v=0.62, y_explo=0.15 |
| 08   | -139880.0938 | 24.03      | y_att=0.48, y_ali=0.04, y_f=0.10, d0_att=3.34, l_att=4.52, l_ali=1.92, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.85, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.76, y_acc=1.89, l_acc=0.70, d0_v=0.62, y_explo=0.15 |
| 09   | -139880.0938 | 24.02      | y_att=0.48, y_ali=0.04, y_f=0.10, d0_att=3.34, l_att=4.52, l_ali=1.92, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.85, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.76, y_acc=1.89, l_acc=0.70, d0_v=0.62, y_explo=0.15 |
| 10   | -140496.2500 | 24.01      | y_att=0.58, y_ali=0.52, y_f=0.10, d0_att=2.71, l_att=2.44, l_ali=0.74, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.83, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=1.23, l_acc=1.47, d0_v=0.92, y_explo=0.14 |
| 11   | -140496.2500 | 24.02      | y_att=0.58, y_ali=0.52, y_f=0.10, d0_att=2.71, l_att=2.44, l_ali=0.74, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.83, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=1.23, l_acc=1.47, d0_v=0.92, y_explo=0.14 |
| 12   | -140496.2500 | 24.01      | y_att=0.58, y_ali=0.52, y_f=0.10, d0_att=2.71, l_att=2.44, l_ali=0.74, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.83, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=1.23, l_acc=1.47, d0_v=0.92, y_explo=0.14 |
| 13   | -140496.2500 | 24.01      | y_att=0.58, y_ali=0.52, y_f=0.10, d0_att=2.71, l_att=2.44, l_ali=0.74, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.83, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=1.23, l_acc=1.47, d0_v=0.92, y_explo=0.14 |
| 14   | -140496.2500 | 24.01      | y_att=0.58, y_ali=0.52, y_f=0.10, d0_att=2.71, l_att=2.44, l_ali=0.74, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.83, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=1.23, l_acc=1.47, d0_v=0.92, y_explo=0.14 |
| 15   | -140725.6562 | 24.01      | y_att=0.66, y_ali=2.96, y_f=0.10, d0_att=0.66, l_att=1.57, l_ali=1.24, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.45, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.62, l_acc=0.89, d0_v=0.28, y_explo=0.13 |
| 16   | -140725.6562 | 24.00      | y_att=0.66, y_ali=2.96, y_f=0.10, d0_att=0.66, l_att=1.57, l_ali=1.24, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.45, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.62, l_acc=0.89, d0_v=0.28, y_explo=0.13 |
| 17   | -140725.6562 | 24.01      | y_att=0.66, y_ali=2.96, y_f=0.10, d0_att=0.66, l_att=1.57, l_ali=1.24, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.45, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.62, l_acc=0.89, d0_v=0.28, y_explo=0.13 |
| 18   | -140800.8750 | 24.01      | y_att=0.25, y_ali=0.41, y_f=0.10, d0_att=0.97, l_att=2.68, l_ali=0.71, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.96, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=1.08, l_acc=1.41, d0_v=0.77, y_explo=0.11 |
| 19   | -140800.8750 | 24.00      | y_att=0.25, y_ali=0.41, y_f=0.10, d0_att=0.97, l_att=2.68, l_ali=0.71, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.96, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=1.08, l_acc=1.41, d0_v=0.77, y_explo=0.11 |

**End of experiment.**
