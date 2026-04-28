# Experiment Report - PyTorch_MULTI_2xGPU (3D)
**Date:** 2026-04-28_15-17-37

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
| 00   | -4479.5630   | 23.82      | y_att=3.40, y_ali=3.46, y_f=1.06, d0_att=4.43, l_att=3.40, l_ali=2.73, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.77, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.70, y_acc=0.42, l_acc=2.63, d0_v=2.97, y_explo=0.73 |
| 01   | -4479.5630   | 23.44      | y_att=3.40, y_ali=3.46, y_f=1.06, d0_att=4.43, l_att=3.40, l_ali=2.73, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.77, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.70, y_acc=0.42, l_acc=2.63, d0_v=2.97, y_explo=0.73 |
| 02   | -4718.7759   | 23.45      | y_att=1.02, y_ali=0.67, y_f=1.99, d0_att=5.90, l_att=3.57, l_ali=4.64, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.53, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.17, l_acc=0.70, d0_v=2.19, y_explo=0.17 |
| 03   | -4807.7759   | 23.45      | y_att=3.95, y_ali=0.48, y_f=1.21, d0_att=1.34, l_att=1.42, l_ali=3.00, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.58, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.87, y_acc=1.30, l_acc=0.26, d0_v=2.89, y_explo=0.12 |
| 04   | -4807.7759   | 23.45      | y_att=3.95, y_ali=0.48, y_f=1.21, d0_att=1.34, l_att=1.42, l_ali=3.00, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.58, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.87, y_acc=1.30, l_acc=0.26, d0_v=2.89, y_explo=0.12 |
| 05   | -4807.7759   | 23.45      | y_att=3.95, y_ali=0.48, y_f=1.21, d0_att=1.34, l_att=1.42, l_ali=3.00, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.58, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.87, y_acc=1.30, l_acc=0.26, d0_v=2.89, y_explo=0.12 |
| 06   | -4807.7759   | 23.44      | y_att=3.95, y_ali=0.48, y_f=1.21, d0_att=1.34, l_att=1.42, l_ali=3.00, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.58, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.87, y_acc=1.30, l_acc=0.26, d0_v=2.89, y_explo=0.12 |
| 07   | -4857.0674   | 23.45      | y_att=0.58, y_ali=0.57, y_f=1.10, d0_att=1.11, l_att=3.27, l_ali=0.81, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.93, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.17, l_acc=0.59, d0_v=0.84, y_explo=0.10 |
| 08   | -4857.0674   | 23.44      | y_att=0.58, y_ali=0.57, y_f=1.10, d0_att=1.11, l_att=3.27, l_ali=0.81, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.93, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.17, l_acc=0.59, d0_v=0.84, y_explo=0.10 |
| 09   | -4903.5049   | 23.44      | y_att=0.86, y_ali=0.16, y_f=1.10, d0_att=2.58, l_att=2.89, l_ali=3.38, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.36, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.24, l_acc=0.87, d0_v=2.83, y_explo=0.10 |
| 10   | -4909.6167   | 23.44      | y_att=0.46, y_ali=2.28, y_f=1.40, d0_att=0.50, l_att=2.37, l_ali=0.65, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.94, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.96, y_acc=0.17, l_acc=0.54, d0_v=0.65, y_explo=0.13 |
| 11   | -4909.6167   | 23.44      | y_att=0.46, y_ali=2.28, y_f=1.40, d0_att=0.50, l_att=2.37, l_ali=0.65, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.94, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.96, y_acc=0.17, l_acc=0.54, d0_v=0.65, y_explo=0.13 |
| 12   | -4909.6167   | 23.44      | y_att=0.46, y_ali=2.28, y_f=1.40, d0_att=0.50, l_att=2.37, l_ali=0.65, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.94, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.96, y_acc=0.17, l_acc=0.54, d0_v=0.65, y_explo=0.13 |
| 13   | -4912.0820   | 23.44      | y_att=0.26, y_ali=2.16, y_f=0.67, d0_att=1.20, l_att=3.76, l_ali=0.87, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.49, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.28, l_acc=0.42, d0_v=0.98, y_explo=0.10 |
| 14   | -4912.0820   | 23.44      | y_att=0.26, y_ali=2.16, y_f=0.67, d0_att=1.20, l_att=3.76, l_ali=0.87, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.49, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.28, l_acc=0.42, d0_v=0.98, y_explo=0.10 |
| 15   | -4912.0820   | 23.44      | y_att=0.26, y_ali=2.16, y_f=0.67, d0_att=1.20, l_att=3.76, l_ali=0.87, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.49, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.28, l_acc=0.42, d0_v=0.98, y_explo=0.10 |
| 16   | -4940.1191   | 23.44      | y_att=0.25, y_ali=0.02, y_f=1.16, d0_att=0.93, l_att=3.17, l_ali=2.25, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.61, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.70, y_acc=0.06, l_acc=0.54, d0_v=0.62, y_explo=0.12 |
| 17   | -4940.1191   | 23.44      | y_att=0.25, y_ali=0.02, y_f=1.16, d0_att=0.93, l_att=3.17, l_ali=2.25, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.61, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.70, y_acc=0.06, l_acc=0.54, d0_v=0.62, y_explo=0.12 |
| 18   | -4983.0054   | 23.44      | y_att=0.94, y_ali=0.02, y_f=6.80, d0_att=1.19, l_att=1.68, l_ali=0.43, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.59, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.11, l_acc=0.26, d0_v=0.37, y_explo=0.11 |
| 19   | -4990.2891   | 23.44      | y_att=0.34, y_ali=0.00, y_f=0.66, d0_att=0.53, l_att=2.52, l_ali=0.56, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.49, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.24, l_acc=0.79, d0_v=0.86, y_explo=0.13 |

**End of experiment.**
