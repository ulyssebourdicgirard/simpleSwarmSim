# Experiment Report - PyTorch_MULTI_2xGPU (3D)
**Date:** 2026-04-29_08-52-36

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
| 00   | -4492.2583   | 23.79      | y_att=3.93, y_ali=2.71, y_f=0.62, d0_att=1.12, l_att=1.50, l_ali=3.67, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.36, y_acc=0.22, l_acc=1.33, d0_v=1.93, y_explo=0.65 |
| 01   | -4621.1616   | 23.44      | y_att=0.88, y_ali=2.34, y_f=0.58, d0_att=2.13, l_att=4.08, l_ali=2.23, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.07, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.24, y_acc=0.47, l_acc=1.10, d0_v=2.82, y_explo=0.43 |
| 02   | -4621.1616   | 23.45      | y_att=0.88, y_ali=2.34, y_f=0.58, d0_att=2.13, l_att=4.08, l_ali=2.23, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.07, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.24, y_acc=0.47, l_acc=1.10, d0_v=2.82, y_explo=0.43 |
| 03   | -4831.9238   | 23.44      | y_att=2.34, y_ali=2.61, y_f=0.82, d0_att=1.42, l_att=1.48, l_ali=1.52, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.78, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.26, l_acc=1.55, d0_v=2.66, y_explo=0.10 |
| 04   | -4831.9238   | 23.45      | y_att=2.34, y_ali=2.61, y_f=0.82, d0_att=1.42, l_att=1.48, l_ali=1.52, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.78, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.26, l_acc=1.55, d0_v=2.66, y_explo=0.10 |
| 05   | -4831.9238   | 23.45      | y_att=2.34, y_ali=2.61, y_f=0.82, d0_att=1.42, l_att=1.48, l_ali=1.52, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.78, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.26, l_acc=1.55, d0_v=2.66, y_explo=0.10 |
| 06   | -4831.9238   | 23.45      | y_att=2.34, y_ali=2.61, y_f=0.82, d0_att=1.42, l_att=1.48, l_ali=1.52, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.78, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.26, l_acc=1.55, d0_v=2.66, y_explo=0.10 |
| 07   | -4831.9238   | 23.45      | y_att=2.34, y_ali=2.61, y_f=0.82, d0_att=1.42, l_att=1.48, l_ali=1.52, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.78, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.26, l_acc=1.55, d0_v=2.66, y_explo=0.10 |
| 08   | -4831.9238   | 23.45      | y_att=2.34, y_ali=2.61, y_f=0.82, d0_att=1.42, l_att=1.48, l_ali=1.52, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.78, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.26, l_acc=1.55, d0_v=2.66, y_explo=0.10 |
| 09   | -4846.9111   | 23.44      | y_att=3.78, y_ali=3.39, y_f=1.25, d0_att=1.13, l_att=1.30, l_ali=3.02, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.76, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.03, l_acc=1.21, d0_v=0.28, y_explo=0.14 |
| 10   | -4883.0508   | 23.44      | y_att=0.55, y_ali=7.66, y_f=1.07, d0_att=0.50, l_att=2.72, l_ali=1.74, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.62, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.64, y_acc=0.21, l_acc=0.91, d0_v=0.81, y_explo=0.13 |
| 11   | -4883.0508   | 23.44      | y_att=0.55, y_ali=7.66, y_f=1.07, d0_att=0.50, l_att=2.72, l_ali=1.74, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.62, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.64, y_acc=0.21, l_acc=0.91, d0_v=0.81, y_explo=0.13 |
| 12   | -4905.2959   | 23.44      | y_att=1.10, y_ali=2.29, y_f=0.71, d0_att=2.63, l_att=2.53, l_ali=0.03, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.87, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.36, y_acc=0.14, l_acc=0.64, d0_v=1.08, y_explo=0.10 |
| 13   | -4912.1729   | 23.44      | y_att=4.26, y_ali=4.99, y_f=1.22, d0_att=0.87, l_att=1.10, l_ali=2.30, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.85, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.44, l_acc=0.36, d0_v=0.80, y_explo=0.16 |
| 14   | -4939.6963   | 23.44      | y_att=1.20, y_ali=0.13, y_f=1.09, d0_att=1.39, l_att=2.45, l_ali=2.79, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.60, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.21, l_acc=1.22, d0_v=0.73, y_explo=0.10 |
| 15   | -4939.6963   | 23.44      | y_att=1.20, y_ali=0.13, y_f=1.09, d0_att=1.39, l_att=2.45, l_ali=2.79, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.60, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.21, l_acc=1.22, d0_v=0.73, y_explo=0.10 |
| 16   | -4939.6963   | 23.44      | y_att=1.20, y_ali=0.13, y_f=1.09, d0_att=1.39, l_att=2.45, l_ali=2.79, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.60, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.21, l_acc=1.22, d0_v=0.73, y_explo=0.10 |
| 17   | -4939.6963   | 23.44      | y_att=1.20, y_ali=0.13, y_f=1.09, d0_att=1.39, l_att=2.45, l_ali=2.79, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.60, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.21, l_acc=1.22, d0_v=0.73, y_explo=0.10 |
| 18   | -4989.4141   | 23.44      | y_att=2.20, y_ali=0.14, y_f=0.89, d0_att=0.96, l_att=1.30, l_ali=1.80, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.66, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.05, l_acc=1.39, d0_v=0.61, y_explo=0.10 |
| 19   | -4989.4141   | 23.44      | y_att=2.20, y_ali=0.14, y_f=0.89, d0_att=0.96, l_att=1.30, l_ali=1.80, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.66, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.05, l_acc=1.39, d0_v=0.61, y_explo=0.10 |

**End of experiment.**
