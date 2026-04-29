# Experiment Report - PyTorch_MULTI_2xGPU (3D)
**Date:** 2026-04-29_08-43-32

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
| 00   | -4423.7700   | 23.53      | y_att=3.59, y_ali=0.07, y_f=1.83, d0_att=3.25, l_att=3.38, l_ali=4.39, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.53, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.14, y_acc=0.17, l_acc=1.31, d0_v=2.45, y_explo=0.04 |
| 01   | -4423.7700   | 23.23      | y_att=3.59, y_ali=0.07, y_f=1.83, d0_att=3.25, l_att=3.38, l_ali=4.39, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.53, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.14, y_acc=0.17, l_acc=1.31, d0_v=2.45, y_explo=0.04 |
| 02   | -4616.2236   | 23.23      | y_att=3.37, y_ali=3.90, y_f=1.49, d0_att=4.89, l_att=3.26, l_ali=5.05, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.74, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.20, l_acc=1.22, d0_v=1.26, y_explo=0.32 |
| 03   | -4616.2236   | 23.23      | y_att=3.37, y_ali=3.90, y_f=1.49, d0_att=4.89, l_att=3.26, l_ali=5.05, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.74, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.20, l_acc=1.22, d0_v=1.26, y_explo=0.32 |
| 04   | -4632.4399   | 23.23      | y_att=4.93, y_ali=3.77, y_f=2.05, d0_att=1.17, l_att=1.49, l_ali=2.05, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.71, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.54, l_acc=1.01, d0_v=2.29, y_explo=0.10 |
| 05   | -4699.2617   | 23.23      | y_att=4.93, y_ali=3.77, y_f=2.05, d0_att=1.17, l_att=1.49, l_ali=2.05, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.46, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.54, l_acc=1.01, d0_v=2.29, y_explo=0.10 |
| 06   | -4746.6641   | 23.23      | y_att=3.37, y_ali=1.98, y_f=1.78, d0_att=1.17, l_att=1.49, l_ali=3.77, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.34, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.54, l_acc=0.89, d0_v=2.29, y_explo=0.10 |
| 07   | -4746.6641   | 23.23      | y_att=3.37, y_ali=1.98, y_f=1.78, d0_att=1.17, l_att=1.49, l_ali=3.77, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.34, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.54, l_acc=0.89, d0_v=2.29, y_explo=0.10 |
| 08   | -4746.6641   | 23.23      | y_att=3.37, y_ali=1.98, y_f=1.78, d0_att=1.17, l_att=1.49, l_ali=3.77, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.34, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.54, l_acc=0.89, d0_v=2.29, y_explo=0.10 |
| 09   | -4761.8794   | 23.23      | y_att=1.78, y_ali=2.47, y_f=0.61, d0_att=1.09, l_att=1.71, l_ali=1.05, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.87, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.55, y_acc=0.36, l_acc=0.47, d0_v=1.99, y_explo=0.10 |
| 10   | -4781.8574   | 23.23      | y_att=3.91, y_ali=0.38, y_f=1.33, d0_att=1.75, l_att=1.98, l_ali=0.70, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.78, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.82, l_acc=0.38, d0_v=1.73, y_explo=0.16 |
| 11   | -4840.3916   | 23.22      | y_att=0.34, y_ali=2.51, y_f=1.57, d0_att=0.88, l_att=2.89, l_ali=3.38, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.65, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.17, l_acc=0.43, d0_v=0.94, y_explo=0.10 |
| 12   | -4840.3916   | 23.22      | y_att=0.34, y_ali=2.51, y_f=1.57, d0_att=0.88, l_att=2.89, l_ali=3.38, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.65, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.17, l_acc=0.43, d0_v=0.94, y_explo=0.10 |
| 13   | -4840.3916   | 23.22      | y_att=0.34, y_ali=2.51, y_f=1.57, d0_att=0.88, l_att=2.89, l_ali=3.38, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.65, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.17, l_acc=0.43, d0_v=0.94, y_explo=0.10 |
| 14   | -4840.3916   | 23.22      | y_att=0.34, y_ali=2.51, y_f=1.57, d0_att=0.88, l_att=2.89, l_ali=3.38, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.65, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.17, l_acc=0.43, d0_v=0.94, y_explo=0.10 |
| 15   | -4840.3916   | 23.22      | y_att=0.34, y_ali=2.51, y_f=1.57, d0_att=0.88, l_att=2.89, l_ali=3.38, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.65, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.17, l_acc=0.43, d0_v=0.94, y_explo=0.10 |
| 16   | -4840.3916   | 23.23      | y_att=0.34, y_ali=2.51, y_f=1.57, d0_att=0.88, l_att=2.89, l_ali=3.38, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.65, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.17, l_acc=0.43, d0_v=0.94, y_explo=0.10 |
| 17   | -4840.3916   | 23.23      | y_att=0.34, y_ali=2.51, y_f=1.57, d0_att=0.88, l_att=2.89, l_ali=3.38, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.65, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.17, l_acc=0.43, d0_v=0.94, y_explo=0.10 |
| 18   | -4869.8306   | 23.22      | y_att=0.43, y_ali=0.06, y_f=1.52, d0_att=0.54, l_att=2.99, l_ali=4.38, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.95, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.32, l_acc=0.43, d0_v=0.94, y_explo=0.29 |
| 19   | -4869.8306   | 23.23      | y_att=0.43, y_ali=0.06, y_f=1.52, d0_att=0.54, l_att=2.99, l_ali=4.38, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.95, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.32, l_acc=0.43, d0_v=0.94, y_explo=0.29 |

**End of experiment.**
