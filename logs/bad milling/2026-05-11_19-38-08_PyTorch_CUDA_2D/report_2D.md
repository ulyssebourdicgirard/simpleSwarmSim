# Experiment Report - PyTorch_CUDA (2D)
**Date:** 2026-05-11_19-38-08

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
| NB_DRONES            | 30         |
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
| W_COLL               | 50.0       |
| W_DISP               | 10.0       |
| W_EFFORT             | 0          |
| W_EXPLO              | 0.0        |
| W_MILL               | -600.0     |
| W_POL                | 250.0      |
| W_STATIONARY         | 1000       |
| Z_MAX                | 10.0       |
| Z_MIN                | 1.0        |

## 2. Optimization Evolution
| Gen  |  Best Cost   |  Time (s)  |                                                                All Parameters                                                                |
| :--: | :----------: | :--------: | :------------------------------------------------------------------------------------------------------------------------------------------ |
| 00   | 294784.5000  | 75.40      | y_att=0.00, y_ali=1.14, y_f=0.89, d0_att=6.23, l_att=3.08, l_ali=3.90, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.33, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.30, y_acc=0.05, l_acc=1.74, d0_v=2.05, y_explo=1.98 |
| 01   | 207777.3906  | 75.03      | y_att=0.75, y_ali=3.33, y_f=1.24, d0_att=4.32, l_att=1.25, l_ali=6.07, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.98, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.77, y_acc=0.02, l_acc=0.83, d0_v=2.03, y_explo=0.64 |
| 02   | 67148.1406   | 75.00      | y_att=0.10, y_ali=3.48, y_f=0.50, d0_att=2.12, l_att=6.70, l_ali=8.02, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.67, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.78, y_acc=0.17, l_acc=0.40, d0_v=2.32, y_explo=4.47 |
| 03   | -56952.6211  | 74.93      | y_att=0.10, y_ali=2.61, y_f=3.18, d0_att=2.64, l_att=2.20, l_ali=4.80, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.74, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.64, y_acc=0.06, l_acc=1.08, d0_v=2.45, y_explo=4.16 |
| 04   | -56952.6211  | 75.00      | y_att=0.10, y_ali=2.61, y_f=3.18, d0_att=2.64, l_att=2.20, l_ali=4.80, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.74, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.64, y_acc=0.06, l_acc=1.08, d0_v=2.45, y_explo=4.16 |
| 05   | -147075.8438 | 74.76      | y_att=0.27, y_ali=2.32, y_f=0.99, d0_att=0.60, l_att=1.82, l_ali=11.39, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.82, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.38, y_acc=0.01, l_acc=2.09, d0_v=1.29, y_explo=1.23 |
| 06   | -193155.2344 | 74.91      | y_att=0.12, y_ali=3.23, y_f=1.05, d0_att=2.32, l_att=0.24, l_ali=2.86, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.72, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.72, y_acc=0.00, l_acc=3.00, d0_v=1.18, y_explo=2.24 |
| 07   | -227171.7031 | 77.99      | y_att=0.37, y_ali=1.72, y_f=0.20, d0_att=1.57, l_att=2.26, l_ali=11.92, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.81, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.86, y_acc=0.05, l_acc=0.99, d0_v=4.22, y_explo=0.81 |
| 08   | -329449.0312 | 76.54      | y_att=0.10, y_ali=1.76, y_f=0.89, d0_att=3.28, l_att=0.90, l_ali=20.16, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.21, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.25, y_acc=0.05, l_acc=1.49, d0_v=1.61, y_explo=1.40 |
| 09   | -329449.0312 | 77.24      | y_att=0.10, y_ali=1.76, y_f=0.89, d0_att=3.28, l_att=0.90, l_ali=20.16, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.21, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.25, y_acc=0.05, l_acc=1.49, d0_v=1.61, y_explo=1.40 |
| 10   | -516861.9062 | 76.98      | y_att=0.33, y_ali=0.97, y_f=1.30, d0_att=1.60, l_att=1.94, l_ali=23.82, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.21, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.11, y_acc=0.01, l_acc=2.09, d0_v=2.39, y_explo=0.27 |
| 11   | -710054.1250 | 75.26      | y_att=0.13, y_ali=0.96, y_f=2.74, d0_att=1.82, l_att=0.34, l_ali=20.88, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.03, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.78, y_acc=0.01, l_acc=1.13, d0_v=4.80, y_explo=1.42 |
| 12   | -710054.1250 | 74.94      | y_att=0.13, y_ali=0.96, y_f=2.74, d0_att=1.82, l_att=0.34, l_ali=20.88, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.03, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.78, y_acc=0.01, l_acc=1.13, d0_v=4.80, y_explo=1.42 |
| 13   | -950579.0625 | 74.75      | y_att=0.17, y_ali=1.08, y_f=1.60, d0_att=2.19, l_att=0.65, l_ali=25.64, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.81, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.03, l_acc=2.24, d0_v=2.77, y_explo=1.60 |
| 14   | -950579.0625 | 76.58      | y_att=0.17, y_ali=1.08, y_f=1.60, d0_att=2.19, l_att=0.65, l_ali=25.64, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.81, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.03, l_acc=2.24, d0_v=2.77, y_explo=1.60 |
| 15   | -1147815.2500 | 73.78      | y_att=0.10, y_ali=0.92, y_f=0.96, d0_att=3.87, l_att=1.10, l_ali=26.17, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.30, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.89, y_acc=0.06, l_acc=1.23, d0_v=3.09, y_explo=0.91 |
| 16   | -1147815.2500 | 73.99      | y_att=0.10, y_ali=0.92, y_f=0.96, d0_att=3.87, l_att=1.10, l_ali=26.17, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.30, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.89, y_acc=0.06, l_acc=1.23, d0_v=3.09, y_explo=0.91 |
| 17   | -1147815.2500 | 75.14      | y_att=0.10, y_ali=0.92, y_f=0.96, d0_att=3.87, l_att=1.10, l_ali=26.17, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.30, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.89, y_acc=0.06, l_acc=1.23, d0_v=3.09, y_explo=0.91 |
| 18   | -1167389.8750 | 76.16      | y_att=0.16, y_ali=0.87, y_f=1.06, d0_att=1.45, l_att=0.17, l_ali=58.79, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.80, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.09, y_acc=0.05, l_acc=1.30, d0_v=2.87, y_explo=2.46 |
| 19   | -1189881.6250 | 76.11      | y_att=0.10, y_ali=0.93, y_f=0.64, d0_att=6.06, l_att=0.10, l_ali=31.25, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.69, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.73, y_acc=0.02, l_acc=0.63, d0_v=1.30, y_explo=4.69 |

**End of experiment.**
