# Experiment Report - PyTorch_MULTI_2xGPU (3D)
**Date:** 2026-04-28_14-52-25

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
| 00   | -4947.5005   | 17.50      | y_att=4.86, y_ali=1.54, y_f=1.28, d0_att=4.83, l_att=1.64, l_ali=3.13, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.14, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.93, y_acc=0.25, l_acc=2.90, d0_v=1.12, y_explo=0.58 |
| 01   | -4947.5005   | 17.21      | y_att=4.86, y_ali=1.54, y_f=1.28, d0_att=4.83, l_att=1.64, l_ali=3.13, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.14, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.93, y_acc=0.25, l_acc=2.90, d0_v=1.12, y_explo=0.58 |
| 02   | -5027.3833   | 17.21      | y_att=3.55, y_ali=0.98, y_f=1.52, d0_att=2.83, l_att=1.19, l_ali=3.55, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.98, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.13, l_acc=2.24, d0_v=3.36, y_explo=0.10 |
| 03   | -5027.3833   | 17.21      | y_att=3.55, y_ali=0.98, y_f=1.52, d0_att=2.83, l_att=1.19, l_ali=3.55, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.98, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.13, l_acc=2.24, d0_v=3.36, y_explo=0.10 |
| 04   | -5035.3784   | 17.22      | y_att=2.49, y_ali=1.46, y_f=1.58, d0_att=1.21, l_att=0.41, l_ali=2.37, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.12, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.68, y_acc=0.46, l_acc=2.23, d0_v=2.10, y_explo=0.33 |
| 05   | -5035.3784   | 17.22      | y_att=2.49, y_ali=1.46, y_f=1.58, d0_att=1.21, l_att=0.41, l_ali=2.37, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.12, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.68, y_acc=0.46, l_acc=2.23, d0_v=2.10, y_explo=0.33 |
| 06   | -5086.3262   | 17.23      | y_att=0.74, y_ali=0.19, y_f=0.89, d0_att=11.59, l_att=5.23, l_ali=3.68, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.34, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.90, y_acc=0.35, l_acc=0.60, d0_v=2.18, y_explo=0.21 |
| 07   | -5111.4697   | 17.23      | y_att=0.15, y_ali=0.88, y_f=1.32, d0_att=5.95, l_att=2.53, l_ali=1.38, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.81, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.43, y_acc=0.22, l_acc=0.80, d0_v=1.36, y_explo=0.22 |
| 08   | -5170.8652   | 17.23      | y_att=0.39, y_ali=5.62, y_f=1.14, d0_att=1.84, l_att=3.46, l_ali=0.44, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.31, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.15, l_acc=1.44, d0_v=2.51, y_explo=0.21 |
| 09   | -5170.8652   | 17.23      | y_att=0.39, y_ali=5.62, y_f=1.14, d0_att=1.84, l_att=3.46, l_ali=0.44, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.31, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.15, l_acc=1.44, d0_v=2.51, y_explo=0.21 |
| 10   | -5170.8652   | 17.23      | y_att=0.39, y_ali=5.62, y_f=1.14, d0_att=1.84, l_att=3.46, l_ali=0.44, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.31, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.15, l_acc=1.44, d0_v=2.51, y_explo=0.21 |
| 11   | -5219.5137   | 17.23      | y_att=0.22, y_ali=0.99, y_f=1.18, d0_att=2.57, l_att=7.61, l_ali=2.20, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.23, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.38, l_acc=0.55, d0_v=0.43, y_explo=0.20 |
| 12   | -5219.5137   | 17.23      | y_att=0.22, y_ali=0.99, y_f=1.18, d0_att=2.57, l_att=7.61, l_ali=2.20, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.23, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.38, l_acc=0.55, d0_v=0.43, y_explo=0.20 |
| 13   | -5228.5400   | 17.23      | y_att=2.43, y_ali=3.64, y_f=0.77, d0_att=0.50, l_att=0.80, l_ali=2.16, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.74, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.27, l_acc=2.88, d0_v=3.94, y_explo=0.15 |
| 14   | -5291.7300   | 17.22      | y_att=0.29, y_ali=0.21, y_f=0.74, d0_att=1.10, l_att=0.98, l_ali=1.79, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.81, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.16, l_acc=1.83, d0_v=2.65, y_explo=0.19 |
| 15   | -5291.7300   | 17.23      | y_att=0.29, y_ali=0.21, y_f=0.74, d0_att=1.10, l_att=0.98, l_ali=1.79, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.81, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.16, l_acc=1.83, d0_v=2.65, y_explo=0.19 |
| 16   | -5291.7300   | 17.22      | y_att=0.29, y_ali=0.21, y_f=0.74, d0_att=1.10, l_att=0.98, l_ali=1.79, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.81, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.16, l_acc=1.83, d0_v=2.65, y_explo=0.19 |
| 17   | -5291.7300   | 17.23      | y_att=0.29, y_ali=0.21, y_f=0.74, d0_att=1.10, l_att=0.98, l_ali=1.79, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.81, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.16, l_acc=1.83, d0_v=2.65, y_explo=0.19 |
| 18   | -5291.7300   | 17.22      | y_att=0.29, y_ali=0.21, y_f=0.74, d0_att=1.10, l_att=0.98, l_ali=1.79, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.81, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.16, l_acc=1.83, d0_v=2.65, y_explo=0.19 |
| 19   | -5291.7300   | 17.23      | y_att=0.29, y_ali=0.21, y_f=0.74, d0_att=1.10, l_att=0.98, l_ali=1.79, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.81, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.16, l_acc=1.83, d0_v=2.65, y_explo=0.19 |

**End of experiment.**
