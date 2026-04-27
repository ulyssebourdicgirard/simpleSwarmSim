# Experiment Report - PyTorch_CUDA (3D)
**Date:** 2026-04-27_13-12-06

## 1. Initial Configuration
| Parameter | Value |
| :--- | :--- |
| ALPHA_LPF            | 0.2        |
| ARENA_RADIUS         | 100.0      |
| COLLISION_DIST       | 0.4        |
| DT                   | 0.1        |
| ENABLE_3D            | True       |
| EXPLO_STRATEGY       | local_gradient |
| FOV_FACTOR           | 1.0        |
| FULL_MILLING_MODE    | False      |
| GEN_CPU              | 20         |
| GEN_GPU              | 20         |
| GRID_RES             | 5.0        |
| MAP_STRATEGY         | local_shared |
| MAX_SPEED            | 20.0       |
| MAX_YAW_RATE         | 3.14       |
| MIN_SPAWN_DIST       | 2.0        |
| NB_DRONES            | 30         |
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
| 00   | -8546.4736   | 112.66     | y_att=1.84, y_ali=1.18, y_f=1.10, d0_att=3.13, l_att=2.78, l_ali=1.11, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.60, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.92, y_acc=0.08, l_acc=0.80, d0_v=1.78, y_explo=0.53 |
| 01   | -8546.4736   | 114.99     | y_att=1.84, y_ali=1.18, y_f=1.10, d0_att=3.13, l_att=2.78, l_ali=1.11, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.60, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.92, y_acc=0.08, l_acc=0.80, d0_v=1.78, y_explo=0.53 |
| 02   | -8889.3008   | 112.32     | y_att=1.49, y_ali=1.88, y_f=1.28, d0_att=0.92, l_att=1.52, l_ali=2.21, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.67, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.67, y_acc=0.03, l_acc=3.24, d0_v=1.71, y_explo=0.45 |
| 03   | -8889.3008   | 112.29     | y_att=1.49, y_ali=1.88, y_f=1.28, d0_att=0.92, l_att=1.52, l_ali=2.21, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.67, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.67, y_acc=0.03, l_acc=3.24, d0_v=1.71, y_explo=0.45 |
| 04   | -8889.3008   | 112.96     | y_att=1.49, y_ali=1.88, y_f=1.28, d0_att=0.92, l_att=1.52, l_ali=2.21, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.67, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.67, y_acc=0.03, l_acc=3.24, d0_v=1.71, y_explo=0.45 |
| 05   | -8903.0137   | 112.31     | y_att=1.09, y_ali=0.88, y_f=0.74, d0_att=1.14, l_att=2.22, l_ali=4.65, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.78, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.86, y_acc=0.57, l_acc=0.35, d0_v=1.03, y_explo=1.12 |
| 06   | -9074.7705   | 112.95     | y_att=1.29, y_ali=0.03, y_f=1.78, d0_att=1.06, l_att=2.09, l_ali=4.73, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.20, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.16, l_acc=1.92, d0_v=2.49, y_explo=0.17 |
| 07   | -9074.7705   | 112.89     | y_att=1.29, y_ali=0.03, y_f=1.78, d0_att=1.06, l_att=2.09, l_ali=4.73, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.20, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.16, l_acc=1.92, d0_v=2.49, y_explo=0.17 |
| 08   | -9199.6475   | 113.18     | y_att=0.73, y_ali=0.99, y_f=2.09, d0_att=1.11, l_att=2.16, l_ali=1.50, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.68, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.25, l_acc=0.77, d0_v=1.82, y_explo=0.70 |
| 09   | -9199.6475   | 112.16     | y_att=0.73, y_ali=0.99, y_f=2.09, d0_att=1.11, l_att=2.16, l_ali=1.50, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.68, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.25, l_acc=0.77, d0_v=1.82, y_explo=0.70 |
| 10   | -9199.6475   | 112.71     | y_att=0.73, y_ali=0.99, y_f=2.09, d0_att=1.11, l_att=2.16, l_ali=1.50, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.68, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.25, l_acc=0.77, d0_v=1.82, y_explo=0.70 |
| 11   | -9199.6475   | 112.13     | y_att=0.73, y_ali=0.99, y_f=2.09, d0_att=1.11, l_att=2.16, l_ali=1.50, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.68, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.25, l_acc=0.77, d0_v=1.82, y_explo=0.70 |
| 12   | -9240.5400   | 112.11     | y_att=0.13, y_ali=0.06, y_f=1.58, d0_att=0.59, l_att=3.80, l_ali=4.65, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.72, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.18, l_acc=0.36, d0_v=2.94, y_explo=0.19 |
| 13   | -9243.6621   | 112.12     | y_att=2.37, y_ali=0.01, y_f=0.85, d0_att=0.81, l_att=1.38, l_ali=2.71, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.52, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.93, y_acc=0.12, l_acc=0.66, d0_v=0.90, y_explo=0.31 |
| 14   | -9325.4463   | 112.11     | y_att=0.37, y_ali=1.01, y_f=0.83, d0_att=0.59, l_att=1.77, l_ali=1.14, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.42, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.41, y_acc=0.04, l_acc=1.07, d0_v=1.40, y_explo=0.10 |
| 15   | -9325.4463   | 112.11     | y_att=0.37, y_ali=1.01, y_f=0.83, d0_att=0.59, l_att=1.77, l_ali=1.14, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.42, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.41, y_acc=0.04, l_acc=1.07, d0_v=1.40, y_explo=0.10 |
| 16   | -9333.4941   | 112.11     | y_att=0.89, y_ali=1.36, y_f=6.39, d0_att=1.20, l_att=2.97, l_ali=1.81, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.90, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.21, l_acc=0.40, d0_v=2.24, y_explo=0.11 |
| 17   | -9333.4941   | 112.11     | y_att=0.89, y_ali=1.36, y_f=6.39, d0_att=1.20, l_att=2.97, l_ali=1.81, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.90, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.21, l_acc=0.40, d0_v=2.24, y_explo=0.11 |
| 18   | -9343.5508   | 112.11     | y_att=0.53, y_ali=0.05, y_f=0.86, d0_att=1.06, l_att=2.36, l_ali=1.82, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.30, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.19, l_acc=0.58, d0_v=1.34, y_explo=0.10 |
| 19   | -9343.5508   | 112.11     | y_att=0.53, y_ali=0.05, y_f=0.86, d0_att=1.06, l_att=2.36, l_ali=1.82, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.30, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.19, l_acc=0.58, d0_v=1.34, y_explo=0.10 |

**End of experiment.**
