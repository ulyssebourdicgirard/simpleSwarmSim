# Experiment Report - PyTorch_MULTI_2xGPU (3D)
**Date:** 2026-04-28_14-59-29

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
| MAP_STRATEGY         | local_individual |
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
| 00   | -4173.4814   | 23.55      | y_att=2.52, y_ali=2.09, y_f=1.52, d0_att=4.73, l_att=4.76, l_ali=1.10, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.69, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.42, y_acc=0.27, l_acc=0.79, d0_v=2.02, y_explo=0.16 |
| 01   | -4436.4077   | 23.23      | y_att=2.02, y_ali=1.57, y_f=1.94, d0_att=1.73, l_att=1.94, l_ali=3.77, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.63, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.58, y_acc=0.17, l_acc=1.02, d0_v=1.75, y_explo=0.80 |
| 02   | -4436.4077   | 23.23      | y_att=2.02, y_ali=1.57, y_f=1.94, d0_att=1.73, l_att=1.94, l_ali=3.77, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.63, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.58, y_acc=0.17, l_acc=1.02, d0_v=1.75, y_explo=0.80 |
| 03   | -4544.1299   | 23.24      | y_att=1.72, y_ali=3.02, y_f=0.96, d0_att=1.82, l_att=2.38, l_ali=4.24, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.68, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.59, l_acc=0.21, d0_v=0.91, y_explo=0.50 |
| 04   | -4696.0171   | 23.23      | y_att=0.78, y_ali=2.68, y_f=1.51, d0_att=1.67, l_att=3.02, l_ali=3.17, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.33, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.39, y_acc=0.40, l_acc=1.04, d0_v=3.63, y_explo=0.15 |
| 05   | -4696.0171   | 23.23      | y_att=0.78, y_ali=2.68, y_f=1.51, d0_att=1.67, l_att=3.02, l_ali=3.17, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.33, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.39, y_acc=0.40, l_acc=1.04, d0_v=3.63, y_explo=0.15 |
| 06   | -4782.1074   | 23.23      | y_att=1.57, y_ali=1.98, y_f=1.68, d0_att=0.64, l_att=1.22, l_ali=3.16, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.77, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.36, l_acc=1.92, d0_v=3.59, y_explo=0.18 |
| 07   | -4795.0537   | 23.23      | y_att=0.68, y_ali=0.36, y_f=1.13, d0_att=2.87, l_att=4.46, l_ali=1.80, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.09, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.16, l_acc=1.01, d0_v=1.61, y_explo=0.34 |
| 08   | -4795.0537   | 23.23      | y_att=0.68, y_ali=0.36, y_f=1.13, d0_att=2.87, l_att=4.46, l_ali=1.80, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.09, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.16, l_acc=1.01, d0_v=1.61, y_explo=0.34 |
| 09   | -4795.0537   | 23.22      | y_att=0.68, y_ali=0.36, y_f=1.13, d0_att=2.87, l_att=4.46, l_ali=1.80, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.09, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.16, l_acc=1.01, d0_v=1.61, y_explo=0.34 |
| 10   | -4795.0537   | 23.22      | y_att=0.68, y_ali=0.36, y_f=1.13, d0_att=2.87, l_att=4.46, l_ali=1.80, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.09, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.16, l_acc=1.01, d0_v=1.61, y_explo=0.34 |
| 11   | -4795.0537   | 23.22      | y_att=0.68, y_ali=0.36, y_f=1.13, d0_att=2.87, l_att=4.46, l_ali=1.80, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.09, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.16, l_acc=1.01, d0_v=1.61, y_explo=0.34 |
| 12   | -4808.9424   | 23.22      | y_att=0.35, y_ali=1.52, y_f=1.21, d0_att=1.11, l_att=3.45, l_ali=0.43, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.80, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.50, y_acc=0.00, l_acc=0.93, d0_v=2.28, y_explo=0.10 |
| 13   | -4808.9424   | 23.22      | y_att=0.35, y_ali=1.52, y_f=1.21, d0_att=1.11, l_att=3.45, l_ali=0.43, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.80, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.50, y_acc=0.00, l_acc=0.93, d0_v=2.28, y_explo=0.10 |
| 14   | -4808.9424   | 23.22      | y_att=0.35, y_ali=1.52, y_f=1.21, d0_att=1.11, l_att=3.45, l_ali=0.43, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.80, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.50, y_acc=0.00, l_acc=0.93, d0_v=2.28, y_explo=0.10 |
| 15   | -4882.5444   | 23.22      | y_att=1.00, y_ali=4.21, y_f=1.58, d0_att=0.83, l_att=1.90, l_ali=0.23, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.55, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.09, l_acc=1.29, d0_v=0.90, y_explo=0.10 |
| 16   | -4882.5444   | 23.22      | y_att=1.00, y_ali=4.21, y_f=1.58, d0_att=0.83, l_att=1.90, l_ali=0.23, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.55, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.09, l_acc=1.29, d0_v=0.90, y_explo=0.10 |
| 17   | -4887.6147   | 23.22      | y_att=0.62, y_ali=10.57, y_f=1.09, d0_att=0.50, l_att=2.06, l_ali=2.12, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.58, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.24, l_acc=0.50, d0_v=0.73, y_explo=0.19 |
| 18   | -4887.6147   | 23.22      | y_att=0.62, y_ali=10.57, y_f=1.09, d0_att=0.50, l_att=2.06, l_ali=2.12, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.58, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.24, l_acc=0.50, d0_v=0.73, y_explo=0.19 |
| 19   | -4887.6147   | 23.22      | y_att=0.62, y_ali=10.57, y_f=1.09, d0_att=0.50, l_att=2.06, l_ali=2.12, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.58, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.24, l_acc=0.50, d0_v=0.73, y_explo=0.19 |

**End of experiment.**
