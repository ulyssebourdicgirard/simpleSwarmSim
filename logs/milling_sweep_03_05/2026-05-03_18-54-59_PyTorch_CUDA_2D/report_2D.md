# Experiment Report - PyTorch_CUDA (2D)
**Date:** 2026-05-03_18-54-59

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
| MAX_SPEED            | 30.0       |
| MAX_YAW_RATE         | 3.14       |
| MIN_SPAWN_DIST       | 2.0        |
| NB_DRONES            | 20         |
| NEIGHBORS            | 4          |
| N_INIT_CONDITIONS    | 4          |
| POP_SIZE_CPU         | 150        |
| POP_SIZE_GPU         | 5000       |
| REFRESH_MAP_TICKS    | 100        |
| SCENARIO             | default    |
| SIM_STEPS            | 800        |
| SPOIL_ADD            | 0.02       |
| SPOIL_MULT           | 1.002      |
| VISU_STEPS           | 2000       |
| W_COLL               | 1.0        |
| W_DISP               | 2.0        |
| W_EFFORT             | 0.0        |
| W_EXPLO              | 0.0        |
| W_MILL               | -300.0     |
| W_POL                | 0.0        |
| Z_MAX                | 10.0       |
| Z_MIN                | 1.0        |

## 2. Optimization Evolution
| Gen  |  Best Cost   |  Time (s)  |                                                                All Parameters                                                                |
| :--: | :----------: | :--------: | :------------------------------------------------------------------------------------------------------------------------------------------ |
| 00   | -33258.2500  | 8.99       | y_att=2.28, y_ali=1.70, y_f=1.48, d0_att=7.69, l_att=7.22, l_ali=2.73, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.49, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.64, y_acc=1.39, l_acc=1.52, d0_v=1.32, y_explo=3.72 |
| 01   | -37235.5312  | 8.47       | y_att=4.63, y_ali=0.18, y_f=1.84, d0_att=12.54, l_att=9.84, l_ali=4.60, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.47, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.13, y_acc=1.21, l_acc=0.92, d0_v=2.48, y_explo=4.16 |
| 02   | -78469.3516  | 8.37       | y_att=8.37, y_ali=1.79, y_f=0.91, d0_att=7.07, l_att=3.41, l_ali=4.77, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.03, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.06, y_acc=0.23, l_acc=1.02, d0_v=1.70, y_explo=1.68 |
| 03   | -94125.6250  | 8.47       | y_att=6.17, y_ali=0.33, y_f=1.07, d0_att=10.62, l_att=8.48, l_ali=3.41, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.55, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.16, y_acc=0.95, l_acc=3.40, d0_v=4.37, y_explo=0.57 |
| 04   | -116730.3750 | 8.38       | y_att=2.78, y_ali=0.28, y_f=1.62, d0_att=13.95, l_att=11.54, l_ali=1.60, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.79, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.81, y_acc=1.44, l_acc=0.32, d0_v=2.78, y_explo=0.13 |
| 05   | -116730.3750 | 8.33       | y_att=2.78, y_ali=0.28, y_f=1.62, d0_att=13.95, l_att=11.54, l_ali=1.60, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.79, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.81, y_acc=1.44, l_acc=0.32, d0_v=2.78, y_explo=0.13 |
| 06   | -124349.0547 | 8.45       | y_att=3.44, y_ali=0.39, y_f=1.13, d0_att=16.24, l_att=8.20, l_ali=2.76, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.07, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.16, y_acc=0.07, l_acc=0.38, d0_v=1.49, y_explo=2.76 |
| 07   | -124349.0547 | 8.39       | y_att=3.44, y_ali=0.39, y_f=1.13, d0_att=16.24, l_att=8.20, l_ali=2.76, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.07, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.16, y_acc=0.07, l_acc=0.38, d0_v=1.49, y_explo=2.76 |
| 08   | -125289.2188 | 8.35       | y_att=6.06, y_ali=0.57, y_f=0.86, d0_att=9.35, l_att=12.49, l_ali=2.87, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.78, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.81, y_acc=0.22, l_acc=1.35, d0_v=1.39, y_explo=0.67 |
| 09   | -125289.2188 | 8.55       | y_att=6.06, y_ali=0.57, y_f=0.86, d0_att=9.35, l_att=12.49, l_ali=2.87, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.78, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.81, y_acc=0.22, l_acc=1.35, d0_v=1.39, y_explo=0.67 |
| 10   | -125289.2188 | 8.48       | y_att=6.06, y_ali=0.57, y_f=0.86, d0_att=9.35, l_att=12.49, l_ali=2.87, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.78, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.81, y_acc=0.22, l_acc=1.35, d0_v=1.39, y_explo=0.67 |
| 11   | -126936.7891 | 8.35       | y_att=1.84, y_ali=0.15, y_f=2.43, d0_att=26.25, l_att=7.23, l_ali=4.58, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.87, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.46, y_acc=0.02, l_acc=0.47, d0_v=4.77, y_explo=5.73 |
| 12   | -128135.8359 | 8.28       | y_att=2.07, y_ali=0.15, y_f=4.02, d0_att=18.89, l_att=7.23, l_ali=3.60, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.89, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.46, y_acc=0.17, l_acc=0.47, d0_v=4.77, y_explo=5.73 |
| 13   | -129284.7109 | 8.45       | y_att=3.12, y_ali=0.17, y_f=1.29, d0_att=19.13, l_att=9.79, l_ali=3.29, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.59, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.53, y_acc=0.27, l_acc=2.83, d0_v=3.13, y_explo=2.47 |
| 14   | -138283.4844 | 8.58       | y_att=2.81, y_ali=0.14, y_f=0.10, d0_att=37.27, l_att=11.85, l_ali=3.82, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.70, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.65, l_acc=0.44, d0_v=5.91, y_explo=3.93 |
| 15   | -138283.4844 | 8.45       | y_att=2.81, y_ali=0.14, y_f=0.10, d0_att=37.27, l_att=11.85, l_ali=3.82, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.70, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.65, l_acc=0.44, d0_v=5.91, y_explo=3.93 |
| 16   | -138283.4844 | 8.25       | y_att=2.81, y_ali=0.14, y_f=0.10, d0_att=37.27, l_att=11.85, l_ali=3.82, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.70, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.65, l_acc=0.44, d0_v=5.91, y_explo=3.93 |
| 17   | -138820.3594 | 8.24       | y_att=2.67, y_ali=0.32, y_f=4.59, d0_att=21.16, l_att=9.40, l_ali=2.96, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.87, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.19, y_acc=0.08, l_acc=0.37, d0_v=1.93, y_explo=1.29 |
| 18   | -138820.3594 | 8.31       | y_att=2.67, y_ali=0.32, y_f=4.59, d0_att=21.16, l_att=9.40, l_ali=2.96, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.87, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.19, y_acc=0.08, l_acc=0.37, d0_v=1.93, y_explo=1.29 |
| 19   | -138820.3594 | 8.26       | y_att=2.67, y_ali=0.32, y_f=4.59, d0_att=21.16, l_att=9.40, l_ali=2.96, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.87, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.19, y_acc=0.08, l_acc=0.37, d0_v=1.93, y_explo=1.29 |

**End of experiment.**
