# Experiment Report - PyTorch_MULTI_2xGPU (2D)
**Date:** 2026-05-04_00-07-50

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
| MAP_STRATEGY         | local_individual |
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
| 00   | -103746.3438 | 7.14       | y_att=0.10, y_ali=0.99, y_f=0.94, d0_att=5.03, l_att=1.26, l_ali=4.04, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.93, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.49, y_acc=0.10, l_acc=1.04, d0_v=2.26, y_explo=0.93 |
| 01   | -175989.0000 | 6.84       | y_att=0.10, y_ali=0.99, y_f=0.94, d0_att=5.03, l_att=1.26, l_ali=4.04, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.38, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.49, y_acc=0.10, l_acc=1.04, d0_v=2.26, y_explo=0.93 |
| 02   | -188400.9219 | 6.85       | y_att=0.36, y_ali=0.96, y_f=0.90, d0_att=6.60, l_att=11.46, l_ali=4.94, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.24, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.90, y_acc=0.00, l_acc=2.89, d0_v=1.78, y_explo=1.33 |
| 03   | -219204.6562 | 6.80       | y_att=0.71, y_ali=2.85, y_f=1.77, d0_att=2.94, l_att=1.14, l_ali=5.24, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.45, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.76, y_acc=0.18, l_acc=0.64, d0_v=1.32, y_explo=3.70 |
| 04   | -238937.6719 | 6.79       | y_att=0.10, y_ali=1.57, y_f=1.76, d0_att=3.62, l_att=0.75, l_ali=3.27, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.82, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.86, y_acc=0.03, l_acc=1.52, d0_v=1.07, y_explo=2.68 |
| 05   | -342841.3750 | 6.83       | y_att=0.32, y_ali=1.23, y_f=0.74, d0_att=2.80, l_att=1.78, l_ali=15.75, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.90, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.50, y_acc=0.02, l_acc=1.02, d0_v=1.24, y_explo=5.42 |
| 06   | -342841.3750 | 6.83       | y_att=0.32, y_ali=1.23, y_f=0.74, d0_att=2.80, l_att=1.78, l_ali=15.75, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.90, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.50, y_acc=0.02, l_acc=1.02, d0_v=1.24, y_explo=5.42 |
| 07   | -342841.3750 | 6.85       | y_att=0.32, y_ali=1.23, y_f=0.74, d0_att=2.80, l_att=1.78, l_ali=15.75, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.90, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.50, y_acc=0.02, l_acc=1.02, d0_v=1.24, y_explo=5.42 |
| 08   | -354716.3750 | 6.83       | y_att=1.06, y_ali=1.21, y_f=0.28, d0_att=2.66, l_att=0.51, l_ali=12.77, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.72, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.40, y_acc=0.02, l_acc=0.73, d0_v=3.81, y_explo=2.13 |
| 09   | -462338.3750 | 6.85       | y_att=0.31, y_ali=1.42, y_f=4.11, d0_att=6.47, l_att=1.42, l_ali=15.71, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.23, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.99, y_acc=0.05, l_acc=0.93, d0_v=3.80, y_explo=0.23 |
| 10   | -482114.5000 | 6.84       | y_att=0.34, y_ali=1.42, y_f=4.11, d0_att=5.76, l_att=2.20, l_ali=15.71, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.01, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.99, y_acc=0.05, l_acc=2.95, d0_v=3.80, y_explo=0.23 |
| 11   | -483795.5312 | 6.84       | y_att=0.20, y_ali=1.03, y_f=5.85, d0_att=6.16, l_att=1.24, l_ali=18.90, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.98, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.00, y_acc=0.11, l_acc=2.40, d0_v=2.27, y_explo=5.78 |
| 12   | -483795.5312 | 6.83       | y_att=0.20, y_ali=1.03, y_f=5.85, d0_att=6.16, l_att=1.24, l_ali=18.90, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.98, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.00, y_acc=0.11, l_acc=2.40, d0_v=2.27, y_explo=5.78 |
| 13   | -483795.5312 | 6.83       | y_att=0.20, y_ali=1.03, y_f=5.85, d0_att=6.16, l_att=1.24, l_ali=18.90, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.98, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.00, y_acc=0.11, l_acc=2.40, d0_v=2.27, y_explo=5.78 |
| 14   | -483795.5312 | 6.84       | y_att=0.20, y_ali=1.03, y_f=5.85, d0_att=6.16, l_att=1.24, l_ali=18.90, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.98, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.00, y_acc=0.11, l_acc=2.40, d0_v=2.27, y_explo=5.78 |
| 15   | -483795.5312 | 6.86       | y_att=0.20, y_ali=1.03, y_f=5.85, d0_att=6.16, l_att=1.24, l_ali=18.90, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.98, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.00, y_acc=0.11, l_acc=2.40, d0_v=2.27, y_explo=5.78 |
| 16   | -483795.5312 | 6.87       | y_att=0.20, y_ali=1.03, y_f=5.85, d0_att=6.16, l_att=1.24, l_ali=18.90, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.98, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.00, y_acc=0.11, l_acc=2.40, d0_v=2.27, y_explo=5.78 |
| 17   | -483795.5312 | 6.86       | y_att=0.20, y_ali=1.03, y_f=5.85, d0_att=6.16, l_att=1.24, l_ali=18.90, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.98, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.00, y_acc=0.11, l_acc=2.40, d0_v=2.27, y_explo=5.78 |
| 18   | -483795.5312 | 6.88       | y_att=0.20, y_ali=1.03, y_f=5.85, d0_att=6.16, l_att=1.24, l_ali=18.90, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.98, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.00, y_acc=0.11, l_acc=2.40, d0_v=2.27, y_explo=5.78 |
| 19   | -483795.5312 | 6.85       | y_att=0.20, y_ali=1.03, y_f=5.85, d0_att=6.16, l_att=1.24, l_ali=18.90, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.98, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.00, y_acc=0.11, l_acc=2.40, d0_v=2.27, y_explo=5.78 |

**End of experiment.**
