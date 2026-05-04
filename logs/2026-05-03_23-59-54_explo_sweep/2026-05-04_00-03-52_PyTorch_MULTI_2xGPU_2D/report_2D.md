# Experiment Report - PyTorch_MULTI_2xGPU (2D)
**Date:** 2026-05-04_00-03-52

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
| MAP_STRATEGY         | global     |
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
| W_COLL               | 10.0       |
| W_DISP               | 2.0        |
| W_EFFORT             | 0.5        |
| W_EXPLO              | 0.0        |
| W_MILL               | -300.0     |
| W_POL                | 0.0        |
| Z_MAX                | 10.0       |
| Z_MIN                | 1.0        |

## 2. Optimization Evolution
| Gen  |  Best Cost   |  Time (s)  |                                                                All Parameters                                                                |
| :--: | :----------: | :--------: | :------------------------------------------------------------------------------------------------------------------------------------------ |
| 00   | -63436.7227  | 7.18       | y_att=0.08, y_ali=3.72, y_f=1.42, d0_att=5.47, l_att=1.21, l_ali=2.50, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.70, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.57, y_acc=0.06, l_acc=1.22, d0_v=1.04, y_explo=4.37 |
| 01   | -127978.3438 | 6.82       | y_att=0.10, y_ali=2.19, y_f=0.91, d0_att=6.42, l_att=3.78, l_ali=3.28, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.80, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.14, y_acc=0.15, l_acc=0.57, d0_v=1.29, y_explo=3.05 |
| 02   | -132672.8281 | 6.79       | y_att=0.16, y_ali=1.65, y_f=1.84, d0_att=6.65, l_att=3.52, l_ali=4.15, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.29, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.30, y_acc=0.09, l_acc=0.52, d0_v=0.98, y_explo=2.05 |
| 03   | -266650.6875 | 6.86       | y_att=0.10, y_ali=1.68, y_f=1.90, d0_att=6.43, l_att=0.71, l_ali=3.11, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.83, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.11, y_acc=0.14, l_acc=1.06, d0_v=2.35, y_explo=1.76 |
| 04   | -267776.2188 | 6.86       | y_att=0.91, y_ali=1.93, y_f=1.53, d0_att=12.53, l_att=5.52, l_ali=3.13, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.85, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.14, y_acc=0.00, l_acc=0.62, d0_v=1.43, y_explo=6.36 |
| 05   | -269806.9688 | 6.84       | y_att=0.17, y_ali=2.20, y_f=1.89, d0_att=1.53, l_att=0.24, l_ali=12.74, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.35, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.79, y_acc=0.07, l_acc=1.88, d0_v=2.35, y_explo=3.23 |
| 06   | -269806.9688 | 6.82       | y_att=0.17, y_ali=2.20, y_f=1.89, d0_att=1.53, l_att=0.24, l_ali=12.74, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.35, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.79, y_acc=0.07, l_acc=1.88, d0_v=2.35, y_explo=3.23 |
| 07   | -269806.9688 | 6.83       | y_att=0.17, y_ali=2.20, y_f=1.89, d0_att=1.53, l_att=0.24, l_ali=12.74, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.35, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.79, y_acc=0.07, l_acc=1.88, d0_v=2.35, y_explo=3.23 |
| 08   | -292669.1875 | 6.82       | y_att=0.14, y_ali=2.58, y_f=1.08, d0_att=7.14, l_att=1.19, l_ali=10.07, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.22, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.59, y_acc=0.02, l_acc=1.56, d0_v=1.86, y_explo=1.29 |
| 09   | -466288.3438 | 6.83       | y_att=0.66, y_ali=1.31, y_f=1.46, d0_att=4.13, l_att=0.58, l_ali=14.26, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.33, y_acc=0.03, l_acc=1.25, d0_v=2.98, y_explo=0.72 |
| 10   | -466288.3438 | 6.83       | y_att=0.66, y_ali=1.31, y_f=1.46, d0_att=4.13, l_att=0.58, l_ali=14.26, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.33, y_acc=0.03, l_acc=1.25, d0_v=2.98, y_explo=0.72 |
| 11   | -466288.3438 | 6.83       | y_att=0.66, y_ali=1.31, y_f=1.46, d0_att=4.13, l_att=0.58, l_ali=14.26, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.33, y_acc=0.03, l_acc=1.25, d0_v=2.98, y_explo=0.72 |
| 12   | -466288.3438 | 6.84       | y_att=0.66, y_ali=1.31, y_f=1.46, d0_att=4.13, l_att=0.58, l_ali=14.26, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.33, y_acc=0.03, l_acc=1.25, d0_v=2.98, y_explo=0.72 |
| 13   | -466288.3438 | 6.83       | y_att=0.66, y_ali=1.31, y_f=1.46, d0_att=4.13, l_att=0.58, l_ali=14.26, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.33, y_acc=0.03, l_acc=1.25, d0_v=2.98, y_explo=0.72 |
| 14   | -502080.4062 | 6.84       | y_att=0.10, y_ali=1.62, y_f=1.46, d0_att=2.61, l_att=1.17, l_ali=14.26, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.64, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.32, y_acc=0.03, l_acc=0.71, d0_v=2.93, y_explo=0.72 |
| 15   | -502080.4062 | 6.79       | y_att=0.10, y_ali=1.62, y_f=1.46, d0_att=2.61, l_att=1.17, l_ali=14.26, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.64, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.32, y_acc=0.03, l_acc=0.71, d0_v=2.93, y_explo=0.72 |
| 16   | -502080.4062 | 6.86       | y_att=0.10, y_ali=1.62, y_f=1.46, d0_att=2.61, l_att=1.17, l_ali=14.26, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.64, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.32, y_acc=0.03, l_acc=0.71, d0_v=2.93, y_explo=0.72 |
| 17   | -502080.4062 | 6.80       | y_att=0.10, y_ali=1.62, y_f=1.46, d0_att=2.61, l_att=1.17, l_ali=14.26, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.64, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.32, y_acc=0.03, l_acc=0.71, d0_v=2.93, y_explo=0.72 |
| 18   | -502080.4062 | 6.84       | y_att=0.10, y_ali=1.62, y_f=1.46, d0_att=2.61, l_att=1.17, l_ali=14.26, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.64, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.32, y_acc=0.03, l_acc=0.71, d0_v=2.93, y_explo=0.72 |
| 19   | -502080.4062 | 6.83       | y_att=0.10, y_ali=1.62, y_f=1.46, d0_att=2.61, l_att=1.17, l_ali=14.26, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.64, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.32, y_acc=0.03, l_acc=0.71, d0_v=2.93, y_explo=0.72 |

**End of experiment.**
