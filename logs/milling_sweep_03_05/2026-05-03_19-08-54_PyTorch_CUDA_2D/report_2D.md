# Experiment Report - PyTorch_CUDA (2D)
**Date:** 2026-05-03_19-08-54

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
| NB_DRONES            | 5          |
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
| 00   | -37710.3867  | 3.03       | y_att=2.72, y_ali=1.81, y_f=1.88, d0_att=7.67, l_att=2.22, l_ali=4.94, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.19, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.52, y_acc=0.04, l_acc=3.40, d0_v=1.56, y_explo=1.90 |
| 01   | -50606.7109  | 3.14       | y_att=0.16, y_ali=1.58, y_f=1.41, d0_att=7.81, l_att=1.21, l_ali=4.26, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.88, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.05, l_acc=2.79, d0_v=2.64, y_explo=0.35 |
| 02   | -89301.6094  | 2.94       | y_att=0.68, y_ali=0.90, y_f=0.15, d0_att=9.84, l_att=8.93, l_ali=4.75, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.16, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.00, y_acc=0.00, l_acc=2.65, d0_v=2.09, y_explo=3.96 |
| 03   | -89301.6094  | 2.86       | y_att=0.68, y_ali=0.90, y_f=0.15, d0_att=9.84, l_att=8.93, l_ali=4.75, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.16, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.00, y_acc=0.00, l_acc=2.65, d0_v=2.09, y_explo=3.96 |
| 04   | -102129.0312 | 2.84       | y_att=0.67, y_ali=2.76, y_f=0.71, d0_att=14.30, l_att=9.91, l_ali=2.50, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.29, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.23, y_acc=0.23, l_acc=0.48, d0_v=0.78, y_explo=2.83 |
| 05   | -102129.0312 | 2.82       | y_att=0.67, y_ali=2.76, y_f=0.71, d0_att=14.30, l_att=9.91, l_ali=2.50, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.29, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.23, y_acc=0.23, l_acc=0.48, d0_v=0.78, y_explo=2.83 |
| 06   | -102129.0312 | 2.78       | y_att=0.67, y_ali=2.76, y_f=0.71, d0_att=14.30, l_att=9.91, l_ali=2.50, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.29, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.23, y_acc=0.23, l_acc=0.48, d0_v=0.78, y_explo=2.83 |
| 07   | -102129.0312 | 2.73       | y_att=0.67, y_ali=2.76, y_f=0.71, d0_att=14.30, l_att=9.91, l_ali=2.50, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.29, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.23, y_acc=0.23, l_acc=0.48, d0_v=0.78, y_explo=2.83 |
| 08   | -125449.6797 | 2.76       | y_att=0.89, y_ali=1.85, y_f=1.23, d0_att=19.54, l_att=3.84, l_ali=4.17, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.44, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.86, y_acc=0.03, l_acc=2.52, d0_v=1.34, y_explo=4.12 |
| 09   | -132932.9688 | 2.79       | y_att=0.24, y_ali=0.43, y_f=0.63, d0_att=14.35, l_att=12.92, l_ali=3.85, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.38, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.01, l_acc=0.50, d0_v=1.97, y_explo=5.15 |
| 10   | -146217.9062 | 3.02       | y_att=0.24, y_ali=0.43, y_f=0.63, d0_att=14.35, l_att=12.92, l_ali=3.85, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.52, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.01, l_acc=0.50, d0_v=1.97, y_explo=5.15 |
| 11   | -146217.9062 | 3.07       | y_att=0.24, y_ali=0.43, y_f=0.63, d0_att=14.35, l_att=12.92, l_ali=3.85, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.52, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.01, l_acc=0.50, d0_v=1.97, y_explo=5.15 |
| 12   | -170702.5312 | 2.89       | y_att=0.19, y_ali=0.89, y_f=3.95, d0_att=44.28, l_att=15.62, l_ali=3.82, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.51, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.61, y_acc=0.02, l_acc=1.17, d0_v=0.22, y_explo=1.62 |
| 13   | -170702.5312 | 2.86       | y_att=0.19, y_ali=0.89, y_f=3.95, d0_att=44.28, l_att=15.62, l_ali=3.82, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.51, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.61, y_acc=0.02, l_acc=1.17, d0_v=0.22, y_explo=1.62 |
| 14   | -170702.5312 | 2.85       | y_att=0.19, y_ali=0.89, y_f=3.95, d0_att=44.28, l_att=15.62, l_ali=3.82, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.51, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.61, y_acc=0.02, l_acc=1.17, d0_v=0.22, y_explo=1.62 |
| 15   | -170702.5312 | 2.78       | y_att=0.19, y_ali=0.89, y_f=3.95, d0_att=44.28, l_att=15.62, l_ali=3.82, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.51, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.61, y_acc=0.02, l_acc=1.17, d0_v=0.22, y_explo=1.62 |
| 16   | -170702.5312 | 2.76       | y_att=0.19, y_ali=0.89, y_f=3.95, d0_att=44.28, l_att=15.62, l_ali=3.82, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.51, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.61, y_acc=0.02, l_acc=1.17, d0_v=0.22, y_explo=1.62 |
| 17   | -170702.5312 | 2.85       | y_att=0.19, y_ali=0.89, y_f=3.95, d0_att=44.28, l_att=15.62, l_ali=3.82, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.51, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.61, y_acc=0.02, l_acc=1.17, d0_v=0.22, y_explo=1.62 |
| 18   | -170702.5312 | 2.92       | y_att=0.19, y_ali=0.89, y_f=3.95, d0_att=44.28, l_att=15.62, l_ali=3.82, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.51, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.61, y_acc=0.02, l_acc=1.17, d0_v=0.22, y_explo=1.62 |
| 19   | -170702.5312 | 2.93       | y_att=0.19, y_ali=0.89, y_f=3.95, d0_att=44.28, l_att=15.62, l_ali=3.82, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.51, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.61, y_acc=0.02, l_acc=1.17, d0_v=0.22, y_explo=1.62 |

**End of experiment.**
