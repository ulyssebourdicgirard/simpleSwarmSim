# Experiment Report - PyTorch_MULTI_2xGPU (2D)
**Date:** 2026-05-03_23-59-55

## 1. Initial Configuration
| Parameter | Value |
| :--- | :--- |
| ALPHA_LPF            | 0.2        |
| ARENA_RADIUS         | 50.0       |
| COLLISION_DIST       | 0.4        |
| DT                   | 0.1        |
| ENABLE_3D            | False      |
| EXPLO_STRATEGY       | local_gradient |
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
| 00   | -95188.7344  | 7.14       | y_att=0.21, y_ali=1.73, y_f=1.40, d0_att=6.23, l_att=1.39, l_ali=3.68, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.07, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.65, y_acc=0.09, l_acc=2.78, d0_v=2.99, y_explo=1.03 |
| 01   | -97978.7266  | 6.88       | y_att=0.23, y_ali=1.73, y_f=1.95, d0_att=4.32, l_att=1.39, l_ali=3.29, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.76, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.78, y_acc=0.11, l_acc=0.57, d0_v=1.40, y_explo=0.72 |
| 02   | -173250.1406 | 6.86       | y_att=0.20, y_ali=1.90, y_f=1.38, d0_att=2.67, l_att=0.94, l_ali=3.38, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.70, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.01, y_acc=0.03, l_acc=0.69, d0_v=0.65, y_explo=4.92 |
| 03   | -251079.2656 | 6.82       | y_att=0.27, y_ali=0.96, y_f=1.88, d0_att=6.49, l_att=1.68, l_ali=4.01, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.42, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.44, y_acc=0.08, l_acc=0.99, d0_v=1.21, y_explo=3.55 |
| 04   | -251079.2656 | 6.78       | y_att=0.27, y_ali=0.96, y_f=1.88, d0_att=6.49, l_att=1.68, l_ali=4.01, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.42, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.44, y_acc=0.08, l_acc=0.99, d0_v=1.21, y_explo=3.55 |
| 05   | -270718.1562 | 6.83       | y_att=0.10, y_ali=1.21, y_f=2.70, d0_att=2.00, l_att=0.49, l_ali=4.10, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.26, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.11, y_acc=0.09, l_acc=2.53, d0_v=3.23, y_explo=6.55 |
| 06   | -316956.0000 | 6.92       | y_att=1.12, y_ali=2.27, y_f=3.36, d0_att=2.89, l_att=0.47, l_ali=14.61, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.96, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.02, y_acc=0.06, l_acc=0.84, d0_v=2.73, y_explo=3.23 |
| 07   | -409109.8125 | 6.80       | y_att=0.43, y_ali=1.58, y_f=1.83, d0_att=8.77, l_att=0.10, l_ali=11.80, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.26, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.56, y_acc=0.05, l_acc=0.93, d0_v=4.25, y_explo=1.36 |
| 08   | -409109.8125 | 6.83       | y_att=0.43, y_ali=1.58, y_f=1.83, d0_att=8.77, l_att=0.10, l_ali=11.80, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.26, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.56, y_acc=0.05, l_acc=0.93, d0_v=4.25, y_explo=1.36 |
| 09   | -410551.8750 | 6.83       | y_att=0.10, y_ali=0.57, y_f=1.73, d0_att=6.39, l_att=0.65, l_ali=15.61, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.86, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.82, y_acc=0.01, l_acc=3.01, d0_v=1.47, y_explo=2.83 |
| 10   | -424976.6562 | 6.81       | y_att=0.10, y_ali=1.29, y_f=3.31, d0_att=3.36, l_att=0.54, l_ali=14.67, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.09, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.79, y_acc=0.10, l_acc=1.05, d0_v=4.02, y_explo=0.44 |
| 11   | -424976.6562 | 6.82       | y_att=0.10, y_ali=1.29, y_f=3.31, d0_att=3.36, l_att=0.54, l_ali=14.67, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.09, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.79, y_acc=0.10, l_acc=1.05, d0_v=4.02, y_explo=0.44 |
| 12   | -424976.6562 | 6.85       | y_att=0.10, y_ali=1.29, y_f=3.31, d0_att=3.36, l_att=0.54, l_ali=14.67, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.09, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.79, y_acc=0.10, l_acc=1.05, d0_v=4.02, y_explo=0.44 |
| 13   | -424976.6562 | 6.84       | y_att=0.10, y_ali=1.29, y_f=3.31, d0_att=3.36, l_att=0.54, l_ali=14.67, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.09, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.79, y_acc=0.10, l_acc=1.05, d0_v=4.02, y_explo=0.44 |
| 14   | -424976.6562 | 6.82       | y_att=0.10, y_ali=1.29, y_f=3.31, d0_att=3.36, l_att=0.54, l_ali=14.67, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.09, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.79, y_acc=0.10, l_acc=1.05, d0_v=4.02, y_explo=0.44 |
| 15   | -424976.6562 | 6.84       | y_att=0.10, y_ali=1.29, y_f=3.31, d0_att=3.36, l_att=0.54, l_ali=14.67, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.09, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.79, y_acc=0.10, l_acc=1.05, d0_v=4.02, y_explo=0.44 |
| 16   | -424976.6562 | 6.87       | y_att=0.10, y_ali=1.29, y_f=3.31, d0_att=3.36, l_att=0.54, l_ali=14.67, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.09, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.79, y_acc=0.10, l_acc=1.05, d0_v=4.02, y_explo=0.44 |
| 17   | -424976.6562 | 6.82       | y_att=0.10, y_ali=1.29, y_f=3.31, d0_att=3.36, l_att=0.54, l_ali=14.67, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.09, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.79, y_acc=0.10, l_acc=1.05, d0_v=4.02, y_explo=0.44 |
| 18   | -424976.6562 | 6.84       | y_att=0.10, y_ali=1.29, y_f=3.31, d0_att=3.36, l_att=0.54, l_ali=14.67, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.09, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.79, y_acc=0.10, l_acc=1.05, d0_v=4.02, y_explo=0.44 |
| 19   | -424976.6562 | 6.83       | y_att=0.10, y_ali=1.29, y_f=3.31, d0_att=3.36, l_att=0.54, l_ali=14.67, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.09, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.79, y_acc=0.10, l_acc=1.05, d0_v=4.02, y_explo=0.44 |

**End of experiment.**
