# Experiment Report - PyTorch_MULTI_2xGPU (3D)
**Date:** 2026-04-28_15-08-33

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
| 00   | -4285.7876   | 23.54      | y_att=4.25, y_ali=1.42, y_f=1.95, d0_att=1.78, l_att=1.95, l_ali=1.64, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.93, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.91, y_acc=0.00, l_acc=3.29, d0_v=2.09, y_explo=1.50 |
| 01   | -4359.1250   | 23.23      | y_att=1.16, y_ali=0.91, y_f=1.47, d0_att=1.94, l_att=3.99, l_ali=3.56, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.55, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.77, y_acc=0.06, l_acc=0.84, d0_v=3.25, y_explo=0.10 |
| 02   | -4513.5986   | 23.23      | y_att=1.66, y_ali=2.24, y_f=1.70, d0_att=1.94, l_att=2.89, l_ali=1.05, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.88, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.74, y_acc=0.04, l_acc=2.72, d0_v=0.81, y_explo=0.16 |
| 03   | -4622.3232   | 23.23      | y_att=1.66, y_ali=2.24, y_f=1.70, d0_att=1.94, l_att=2.89, l_ali=1.05, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.98, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.74, y_acc=0.04, l_acc=2.72, d0_v=0.81, y_explo=0.16 |
| 04   | -4622.3232   | 23.23      | y_att=1.66, y_ali=2.24, y_f=1.70, d0_att=1.94, l_att=2.89, l_ali=1.05, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.98, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.74, y_acc=0.04, l_acc=2.72, d0_v=0.81, y_explo=0.16 |
| 05   | -4622.3232   | 23.23      | y_att=1.66, y_ali=2.24, y_f=1.70, d0_att=1.94, l_att=2.89, l_ali=1.05, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.98, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.74, y_acc=0.04, l_acc=2.72, d0_v=0.81, y_explo=0.16 |
| 06   | -4719.5464   | 23.23      | y_att=0.29, y_ali=4.58, y_f=2.40, d0_att=0.60, l_att=3.99, l_ali=1.13, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.08, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.28, l_acc=0.99, d0_v=1.43, y_explo=0.13 |
| 07   | -4719.5464   | 23.22      | y_att=0.29, y_ali=4.58, y_f=2.40, d0_att=0.60, l_att=3.99, l_ali=1.13, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.08, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.28, l_acc=0.99, d0_v=1.43, y_explo=0.13 |
| 08   | -4719.5464   | 23.22      | y_att=0.29, y_ali=4.58, y_f=2.40, d0_att=0.60, l_att=3.99, l_ali=1.13, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.08, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.28, l_acc=0.99, d0_v=1.43, y_explo=0.13 |
| 09   | -4804.3540   | 23.22      | y_att=0.82, y_ali=0.36, y_f=2.04, d0_att=0.82, l_att=2.01, l_ali=0.58, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.89, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.14, l_acc=1.79, d0_v=2.92, y_explo=0.10 |
| 10   | -4804.3540   | 23.22      | y_att=0.82, y_ali=0.36, y_f=2.04, d0_att=0.82, l_att=2.01, l_ali=0.58, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.89, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.14, l_acc=1.79, d0_v=2.92, y_explo=0.10 |
| 11   | -4804.3540   | 23.22      | y_att=0.82, y_ali=0.36, y_f=2.04, d0_att=0.82, l_att=2.01, l_ali=0.58, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.89, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.14, l_acc=1.79, d0_v=2.92, y_explo=0.10 |
| 12   | -4804.3540   | 23.22      | y_att=0.82, y_ali=0.36, y_f=2.04, d0_att=0.82, l_att=2.01, l_ali=0.58, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.89, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.14, l_acc=1.79, d0_v=2.92, y_explo=0.10 |
| 13   | -4804.3540   | 23.22      | y_att=0.82, y_ali=0.36, y_f=2.04, d0_att=0.82, l_att=2.01, l_ali=0.58, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.89, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.14, l_acc=1.79, d0_v=2.92, y_explo=0.10 |
| 14   | -4804.3540   | 23.22      | y_att=0.82, y_ali=0.36, y_f=2.04, d0_att=0.82, l_att=2.01, l_ali=0.58, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.89, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.14, l_acc=1.79, d0_v=2.92, y_explo=0.10 |
| 15   | -4896.5254   | 23.22      | y_att=1.26, y_ali=0.05, y_f=7.24, d0_att=1.20, l_att=2.66, l_ali=4.56, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.16, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.61, y_acc=0.25, l_acc=0.33, d0_v=0.43, y_explo=0.36 |
| 16   | -4896.5254   | 23.22      | y_att=1.26, y_ali=0.05, y_f=7.24, d0_att=1.20, l_att=2.66, l_ali=4.56, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.16, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.61, y_acc=0.25, l_acc=0.33, d0_v=0.43, y_explo=0.36 |
| 17   | -4896.5254   | 23.22      | y_att=1.26, y_ali=0.05, y_f=7.24, d0_att=1.20, l_att=2.66, l_ali=4.56, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.16, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.61, y_acc=0.25, l_acc=0.33, d0_v=0.43, y_explo=0.36 |
| 18   | -4896.5254   | 23.22      | y_att=1.26, y_ali=0.05, y_f=7.24, d0_att=1.20, l_att=2.66, l_ali=4.56, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.16, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.61, y_acc=0.25, l_acc=0.33, d0_v=0.43, y_explo=0.36 |
| 19   | -4900.4595   | 23.22      | y_att=0.63, y_ali=0.14, y_f=1.19, d0_att=0.61, l_att=2.34, l_ali=0.88, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.55, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.17, l_acc=0.69, d0_v=0.83, y_explo=0.26 |

**End of experiment.**
