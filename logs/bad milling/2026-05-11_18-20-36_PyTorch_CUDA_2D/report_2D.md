# Experiment Report - PyTorch_CUDA (2D)
**Date:** 2026-05-11_18-20-36

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
| MAX_SPEED            | 20.0       |
| MAX_YAW_RATE         | 3.14       |
| MIN_SPAWN_DIST       | 2.0        |
| NB_DRONES            | 10         |
| NEIGHBORS            | 2          |
| N_INIT_CONDITIONS    | 4          |
| POP_SIZE_CPU         | 150        |
| POP_SIZE_GPU         | 5000       |
| REFRESH_MAP_TICKS    | 100        |
| SCENARIO             | default    |
| SIM_STEPS            | 3000       |
| SPOIL_ADD            | 0.02       |
| SPOIL_MULT           | 1.002      |
| VISU_STEPS           | 6000       |
| W_COLL               | 500.0      |
| W_DISP               | 10.0       |
| W_EFFORT             | 0.3        |
| W_EXPLO              | 0.0        |
| W_MILL               | -600.0     |
| W_POL                | 250.0      |
| W_STATIONARY         | 400        |
| Z_MAX                | 10.0       |
| Z_MIN                | 1.0        |

## 2. Optimization Evolution
| Gen  |  Best Cost   |  Time (s)  |                                                                All Parameters                                                                |
| :--: | :----------: | :--------: | :------------------------------------------------------------------------------------------------------------------------------------------ |
| 00   | -214803.4844 | 13.86      | y_att=0.05, y_ali=2.79, y_f=0.60, d0_att=2.62, l_att=1.20, l_ali=2.99, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.96, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.10, y_acc=0.02, l_acc=1.60, d0_v=1.41, y_explo=1.04 |
| 01   | -214803.4844 | 13.21      | y_att=0.05, y_ali=2.79, y_f=0.60, d0_att=2.62, l_att=1.20, l_ali=2.99, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.96, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.10, y_acc=0.02, l_acc=1.60, d0_v=1.41, y_explo=1.04 |
| 02   | -270344.5938 | 14.15      | y_att=2.86, y_ali=0.97, y_f=1.33, d0_att=1.85, l_att=0.24, l_ali=4.47, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.16, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.08, y_acc=0.02, l_acc=0.44, d0_v=2.79, y_explo=7.16 |
| 03   | -279292.3438 | 13.57      | y_att=0.10, y_ali=2.71, y_f=1.42, d0_att=2.62, l_att=1.20, l_ali=2.99, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.18, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.00, y_acc=0.01, l_acc=2.62, d0_v=1.41, y_explo=2.73 |
| 04   | -317094.3750 | 13.65      | y_att=0.10, y_ali=2.43, y_f=0.56, d0_att=2.55, l_att=0.50, l_ali=2.73, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.26, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.43, y_acc=0.01, l_acc=0.64, d0_v=1.27, y_explo=4.56 |
| 05   | -407052.2500 | 13.33      | y_att=0.14, y_ali=1.99, y_f=1.78, d0_att=2.18, l_att=1.16, l_ali=3.20, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.01, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.40, y_acc=0.03, l_acc=2.17, d0_v=1.22, y_explo=2.79 |
| 06   | -407052.2500 | 13.15      | y_att=0.14, y_ali=1.99, y_f=1.78, d0_att=2.18, l_att=1.16, l_ali=3.20, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.01, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.40, y_acc=0.03, l_acc=2.17, d0_v=1.22, y_explo=2.79 |
| 07   | -452074.7812 | 13.39      | y_att=4.61, y_ali=3.78, y_f=1.28, d0_att=1.55, l_att=0.42, l_ali=16.58, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.01, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.55, y_acc=0.15, l_acc=0.68, d0_v=1.79, y_explo=9.27 |
| 08   | -659042.8125 | 14.11      | y_att=2.12, y_ali=1.61, y_f=0.99, d0_att=1.92, l_att=0.56, l_ali=13.81, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.21, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.70, y_acc=0.02, l_acc=0.95, d0_v=1.54, y_explo=4.85 |
| 09   | -800871.2500 | 14.27      | y_att=0.10, y_ali=0.95, y_f=3.69, d0_att=1.24, l_att=1.06, l_ali=16.66, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.48, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.05, y_acc=0.02, l_acc=1.51, d0_v=1.53, y_explo=3.09 |
| 10   | -992568.8125 | 13.41      | y_att=0.20, y_ali=1.21, y_f=1.58, d0_att=0.50, l_att=0.18, l_ali=23.00, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.39, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.71, y_acc=0.05, l_acc=2.04, d0_v=1.90, y_explo=4.26 |
| 11   | -992568.8125 | 13.56      | y_att=0.20, y_ali=1.21, y_f=1.58, d0_att=0.50, l_att=0.18, l_ali=23.00, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.39, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.71, y_acc=0.05, l_acc=2.04, d0_v=1.90, y_explo=4.26 |
| 12   | -1319947.3750 | 13.60      | y_att=0.18, y_ali=1.15, y_f=4.54, d0_att=2.01, l_att=1.11, l_ali=23.25, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.30, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.09, y_acc=0.09, l_acc=0.64, d0_v=0.60, y_explo=2.73 |
| 13   | -1319947.3750 | 13.51      | y_att=0.18, y_ali=1.15, y_f=4.54, d0_att=2.01, l_att=1.11, l_ali=23.25, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.30, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.09, y_acc=0.09, l_acc=0.64, d0_v=0.60, y_explo=2.73 |
| 14   | -1319947.3750 | 14.05      | y_att=0.18, y_ali=1.15, y_f=4.54, d0_att=2.01, l_att=1.11, l_ali=23.25, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.30, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.09, y_acc=0.09, l_acc=0.64, d0_v=0.60, y_explo=2.73 |
| 15   | -1319947.3750 | 14.09      | y_att=0.18, y_ali=1.15, y_f=4.54, d0_att=2.01, l_att=1.11, l_ali=23.25, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.30, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.09, y_acc=0.09, l_acc=0.64, d0_v=0.60, y_explo=2.73 |
| 16   | -1319947.3750 | 13.60      | y_att=0.18, y_ali=1.15, y_f=4.54, d0_att=2.01, l_att=1.11, l_ali=23.25, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.30, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.09, y_acc=0.09, l_acc=0.64, d0_v=0.60, y_explo=2.73 |
| 17   | -1319947.3750 | 13.13      | y_att=0.18, y_ali=1.15, y_f=4.54, d0_att=2.01, l_att=1.11, l_ali=23.25, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.30, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.09, y_acc=0.09, l_acc=0.64, d0_v=0.60, y_explo=2.73 |
| 18   | -1319947.3750 | 13.34      | y_att=0.18, y_ali=1.15, y_f=4.54, d0_att=2.01, l_att=1.11, l_ali=23.25, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.30, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.09, y_acc=0.09, l_acc=0.64, d0_v=0.60, y_explo=2.73 |
| 19   | -1319947.3750 | 13.20      | y_att=0.18, y_ali=1.15, y_f=4.54, d0_att=2.01, l_att=1.11, l_ali=23.25, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.30, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.09, y_acc=0.09, l_acc=0.64, d0_v=0.60, y_explo=2.73 |

**End of experiment.**
