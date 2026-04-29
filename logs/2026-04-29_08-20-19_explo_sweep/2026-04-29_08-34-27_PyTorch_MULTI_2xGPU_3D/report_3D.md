# Experiment Report - PyTorch_MULTI_2xGPU (3D)
**Date:** 2026-04-29_08-34-27

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
| 00   | -4524.7583   | 23.55      | y_att=1.58, y_ali=0.63, y_f=1.86, d0_att=1.30, l_att=2.73, l_ali=4.01, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.51, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.82, y_acc=0.07, l_acc=2.16, d0_v=2.59, y_explo=0.35 |
| 01   | -4524.7583   | 23.22      | y_att=1.58, y_ali=0.63, y_f=1.86, d0_att=1.30, l_att=2.73, l_ali=4.01, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.51, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.82, y_acc=0.07, l_acc=2.16, d0_v=2.59, y_explo=0.35 |
| 02   | -4524.7583   | 23.23      | y_att=1.58, y_ali=0.63, y_f=1.86, d0_att=1.30, l_att=2.73, l_ali=4.01, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.51, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.82, y_acc=0.07, l_acc=2.16, d0_v=2.59, y_explo=0.35 |
| 03   | -4524.7583   | 23.23      | y_att=1.58, y_ali=0.63, y_f=1.86, d0_att=1.30, l_att=2.73, l_ali=4.01, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.51, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.82, y_acc=0.07, l_acc=2.16, d0_v=2.59, y_explo=0.35 |
| 04   | -4604.0723   | 23.23      | y_att=1.98, y_ali=1.20, y_f=1.51, d0_att=1.02, l_att=0.98, l_ali=1.54, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.55, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.23, l_acc=0.61, d0_v=2.13, y_explo=0.42 |
| 05   | -4633.3247   | 23.23      | y_att=0.35, y_ali=1.10, y_f=1.27, d0_att=1.71, l_att=5.78, l_ali=1.74, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.71, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.21, l_acc=0.61, d0_v=0.64, y_explo=0.18 |
| 06   | -4671.7275   | 23.23      | y_att=1.22, y_ali=0.06, y_f=0.85, d0_att=0.99, l_att=1.67, l_ali=3.43, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.61, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.52, y_acc=0.11, l_acc=2.05, d0_v=3.90, y_explo=0.19 |
| 07   | -4671.7275   | 23.23      | y_att=1.22, y_ali=0.06, y_f=0.85, d0_att=0.99, l_att=1.67, l_ali=3.43, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.61, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.52, y_acc=0.11, l_acc=2.05, d0_v=3.90, y_explo=0.19 |
| 08   | -4728.3428   | 23.23      | y_att=2.76, y_ali=1.34, y_f=1.60, d0_att=0.50, l_att=1.08, l_ali=0.79, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.10, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.53, y_acc=0.05, l_acc=2.45, d0_v=1.13, y_explo=0.10 |
| 09   | -4761.8921   | 23.23      | y_att=1.11, y_ali=0.82, y_f=0.90, d0_att=1.21, l_att=1.84, l_ali=2.95, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.92, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.17, l_acc=0.61, d0_v=1.05, y_explo=0.31 |
| 10   | -4781.6938   | 23.23      | y_att=0.40, y_ali=1.17, y_f=1.26, d0_att=0.54, l_att=3.91, l_ali=1.40, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.46, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.52, y_acc=0.39, l_acc=1.27, d0_v=2.68, y_explo=0.24 |
| 11   | -4789.1230   | 23.23      | y_att=1.03, y_ali=3.29, y_f=1.95, d0_att=1.44, l_att=3.34, l_ali=0.63, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.60, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.19, l_acc=1.89, d0_v=1.70, y_explo=0.19 |
| 12   | -4829.8335   | 23.23      | y_att=3.76, y_ali=0.06, y_f=0.74, d0_att=0.90, l_att=1.33, l_ali=1.16, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.87, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.90, y_acc=0.17, l_acc=0.69, d0_v=0.97, y_explo=0.12 |
| 13   | -4902.3237   | 23.23      | y_att=0.93, y_ali=3.35, y_f=2.39, d0_att=1.05, l_att=2.42, l_ali=0.77, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.73, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.18, l_acc=0.54, d0_v=0.86, y_explo=0.10 |
| 14   | -4902.3237   | 23.23      | y_att=0.93, y_ali=3.35, y_f=2.39, d0_att=1.05, l_att=2.42, l_ali=0.77, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.73, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.18, l_acc=0.54, d0_v=0.86, y_explo=0.10 |
| 15   | -4902.3237   | 23.22      | y_att=0.93, y_ali=3.35, y_f=2.39, d0_att=1.05, l_att=2.42, l_ali=0.77, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.73, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.18, l_acc=0.54, d0_v=0.86, y_explo=0.10 |
| 16   | -4902.3237   | 23.23      | y_att=0.93, y_ali=3.35, y_f=2.39, d0_att=1.05, l_att=2.42, l_ali=0.77, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.73, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.18, l_acc=0.54, d0_v=0.86, y_explo=0.10 |
| 17   | -4902.3237   | 23.22      | y_att=0.93, y_ali=3.35, y_f=2.39, d0_att=1.05, l_att=2.42, l_ali=0.77, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.73, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.18, l_acc=0.54, d0_v=0.86, y_explo=0.10 |
| 18   | -4902.3237   | 23.22      | y_att=0.93, y_ali=3.35, y_f=2.39, d0_att=1.05, l_att=2.42, l_ali=0.77, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.73, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.18, l_acc=0.54, d0_v=0.86, y_explo=0.10 |
| 19   | -4902.3237   | 23.23      | y_att=0.93, y_ali=3.35, y_f=2.39, d0_att=1.05, l_att=2.42, l_ali=0.77, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.73, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.18, l_acc=0.54, d0_v=0.86, y_explo=0.10 |

**End of experiment.**
