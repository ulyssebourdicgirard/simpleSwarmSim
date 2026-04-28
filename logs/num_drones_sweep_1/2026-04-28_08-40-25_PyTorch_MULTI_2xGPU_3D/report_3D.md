# Experiment Report - PyTorch_MULTI_2xGPU (3D)
**Date:** 2026-04-28_08-40-25

## 1. Initial Configuration
| Parameter | Value |
| :--- | :--- |
| ALPHA_LPF            | 0.2        |
| ARENA_RADIUS         | 100.0      |
| COLLISION_DIST       | 0.4        |
| DT                   | 0.1        |
| ENABLE_3D            | True       |
| EXPLO_STRATEGY       | local_gradient |
| FOV_FACTOR           | 0.577      |
| FULL_MILLING_MODE    | False      |
| GEN_CPU              | 20         |
| GEN_GPU              | 20         |
| GRID_RES             | 5.0        |
| MAP_STRATEGY         | local_shared |
| MAX_SPEED            | 20.0       |
| MAX_YAW_RATE         | 3.14       |
| MIN_SPAWN_DIST       | 2.0        |
| NB_DRONES            | 5          |
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
| 00   | -759.7386    | 8.18       | y_att=1.66, y_ali=3.16, y_f=1.73, d0_att=6.92, l_att=1.06, l_ali=2.01, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.79, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.77, y_acc=0.19, l_acc=0.67, d0_v=1.60, y_explo=0.39 |
| 01   | -789.2297    | 7.84       | y_att=1.79, y_ali=1.32, y_f=0.64, d0_att=1.09, l_att=1.66, l_ali=1.32, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.39, y_acc=0.15, l_acc=1.84, d0_v=1.09, y_explo=3.21 |
| 02   | -811.3313    | 7.84       | y_att=0.15, y_ali=0.94, y_f=1.58, d0_att=5.23, l_att=7.70, l_ali=3.95, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.74, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.75, y_acc=0.11, l_acc=0.51, d0_v=2.94, y_explo=9.27 |
| 03   | -948.9655    | 7.84       | y_att=2.52, y_ali=0.56, y_f=0.55, d0_att=5.03, l_att=4.45, l_ali=7.06, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.37, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.20, l_acc=1.64, d0_v=1.44, y_explo=8.75 |
| 04   | -948.9655    | 7.85       | y_att=2.52, y_ali=0.56, y_f=0.55, d0_att=5.03, l_att=4.45, l_ali=7.06, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.37, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.20, l_acc=1.64, d0_v=1.44, y_explo=8.75 |
| 05   | -978.9703    | 7.84       | y_att=0.59, y_ali=2.42, y_f=1.45, d0_att=5.45, l_att=7.36, l_ali=2.65, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.96, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.44, y_acc=0.56, l_acc=1.47, d0_v=1.76, y_explo=8.60 |
| 06   | -1057.8157   | 7.85       | y_att=0.35, y_ali=0.37, y_f=0.77, d0_att=3.40, l_att=4.29, l_ali=1.59, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.71, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.05, y_acc=0.23, l_acc=2.54, d0_v=2.41, y_explo=10.17 |
| 07   | -1057.8157   | 7.85       | y_att=0.35, y_ali=0.37, y_f=0.77, d0_att=3.40, l_att=4.29, l_ali=1.59, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.71, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.05, y_acc=0.23, l_acc=2.54, d0_v=2.41, y_explo=10.17 |
| 08   | -1057.8157   | 7.85       | y_att=0.35, y_ali=0.37, y_f=0.77, d0_att=3.40, l_att=4.29, l_ali=1.59, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.71, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.05, y_acc=0.23, l_acc=2.54, d0_v=2.41, y_explo=10.17 |
| 09   | -1057.8157   | 7.85       | y_att=0.35, y_ali=0.37, y_f=0.77, d0_att=3.40, l_att=4.29, l_ali=1.59, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.71, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.05, y_acc=0.23, l_acc=2.54, d0_v=2.41, y_explo=10.17 |
| 10   | -1057.8157   | 7.85       | y_att=0.35, y_ali=0.37, y_f=0.77, d0_att=3.40, l_att=4.29, l_ali=1.59, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.71, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.05, y_acc=0.23, l_acc=2.54, d0_v=2.41, y_explo=10.17 |
| 11   | -1057.8157   | 7.85       | y_att=0.35, y_ali=0.37, y_f=0.77, d0_att=3.40, l_att=4.29, l_ali=1.59, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.71, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.05, y_acc=0.23, l_acc=2.54, d0_v=2.41, y_explo=10.17 |
| 12   | -1057.8157   | 7.85       | y_att=0.35, y_ali=0.37, y_f=0.77, d0_att=3.40, l_att=4.29, l_ali=1.59, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.71, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.05, y_acc=0.23, l_acc=2.54, d0_v=2.41, y_explo=10.17 |
| 13   | -1057.8157   | 7.85       | y_att=0.35, y_ali=0.37, y_f=0.77, d0_att=3.40, l_att=4.29, l_ali=1.59, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.71, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.05, y_acc=0.23, l_acc=2.54, d0_v=2.41, y_explo=10.17 |
| 14   | -1057.8157   | 7.85       | y_att=0.35, y_ali=0.37, y_f=0.77, d0_att=3.40, l_att=4.29, l_ali=1.59, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.71, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.05, y_acc=0.23, l_acc=2.54, d0_v=2.41, y_explo=10.17 |
| 15   | -1069.1000   | 7.85       | y_att=1.31, y_ali=1.97, y_f=0.77, d0_att=2.24, l_att=1.07, l_ali=1.19, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.07, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.38, y_acc=0.36, l_acc=0.81, d0_v=0.65, y_explo=10.03 |
| 16   | -1069.1000   | 7.85       | y_att=1.31, y_ali=1.97, y_f=0.77, d0_att=2.24, l_att=1.07, l_ali=1.19, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.07, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.38, y_acc=0.36, l_acc=0.81, d0_v=0.65, y_explo=10.03 |
| 17   | -1069.1000   | 7.85       | y_att=1.31, y_ali=1.97, y_f=0.77, d0_att=2.24, l_att=1.07, l_ali=1.19, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.07, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.38, y_acc=0.36, l_acc=0.81, d0_v=0.65, y_explo=10.03 |
| 18   | -1069.1000   | 7.85       | y_att=1.31, y_ali=1.97, y_f=0.77, d0_att=2.24, l_att=1.07, l_ali=1.19, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.07, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.38, y_acc=0.36, l_acc=0.81, d0_v=0.65, y_explo=10.03 |
| 19   | -1119.2766   | 7.86       | y_att=0.34, y_ali=0.35, y_f=0.63, d0_att=3.95, l_att=1.75, l_ali=0.07, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.07, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.32, l_acc=0.83, d0_v=0.92, y_explo=11.45 |

**End of experiment.**
