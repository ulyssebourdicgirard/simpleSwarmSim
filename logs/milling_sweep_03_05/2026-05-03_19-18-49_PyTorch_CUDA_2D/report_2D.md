# Experiment Report - PyTorch_CUDA (2D)
**Date:** 2026-05-03_19-18-49

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
| NB_DRONES            | 25         |
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
| 00   | -57506.2734  | 15.42      | y_att=0.13, y_ali=1.00, y_f=1.63, d0_att=6.77, l_att=10.65, l_ali=4.33, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.93, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.00, y_acc=0.08, l_acc=1.04, d0_v=0.76, y_explo=4.70 |
| 01   | -57506.2734  | 14.73      | y_att=0.13, y_ali=1.00, y_f=1.63, d0_att=6.77, l_att=10.65, l_ali=4.33, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.93, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.00, y_acc=0.08, l_acc=1.04, d0_v=0.76, y_explo=4.70 |
| 02   | -57506.2734  | 16.70      | y_att=0.13, y_ali=1.00, y_f=1.63, d0_att=6.77, l_att=10.65, l_ali=4.33, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.93, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.00, y_acc=0.08, l_acc=1.04, d0_v=0.76, y_explo=4.70 |
| 03   | -57506.2734  | 16.31      | y_att=0.13, y_ali=1.00, y_f=1.63, d0_att=6.77, l_att=10.65, l_ali=4.33, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.93, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.00, y_acc=0.08, l_acc=1.04, d0_v=0.76, y_explo=4.70 |
| 04   | -57506.2734  | 14.84      | y_att=0.13, y_ali=1.00, y_f=1.63, d0_att=6.77, l_att=10.65, l_ali=4.33, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.93, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.00, y_acc=0.08, l_acc=1.04, d0_v=0.76, y_explo=4.70 |
| 05   | -57506.2734  | 14.16      | y_att=0.13, y_ali=1.00, y_f=1.63, d0_att=6.77, l_att=10.65, l_ali=4.33, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.93, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.00, y_acc=0.08, l_acc=1.04, d0_v=0.76, y_explo=4.70 |
| 06   | -57506.2734  | 14.14      | y_att=0.13, y_ali=1.00, y_f=1.63, d0_att=6.77, l_att=10.65, l_ali=4.33, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.93, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.00, y_acc=0.08, l_acc=1.04, d0_v=0.76, y_explo=4.70 |
| 07   | -57506.2734  | 14.11      | y_att=0.13, y_ali=1.00, y_f=1.63, d0_att=6.77, l_att=10.65, l_ali=4.33, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.93, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.00, y_acc=0.08, l_acc=1.04, d0_v=0.76, y_explo=4.70 |
| 08   | -57506.2734  | 14.15      | y_att=0.13, y_ali=1.00, y_f=1.63, d0_att=6.77, l_att=10.65, l_ali=4.33, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.93, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.00, y_acc=0.08, l_acc=1.04, d0_v=0.76, y_explo=4.70 |
| 09   | -75060.4609  | 14.12      | y_att=0.13, y_ali=0.70, y_f=1.84, d0_att=1.78, l_att=1.93, l_ali=11.90, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.02, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.29, y_acc=0.00, l_acc=0.49, d0_v=1.16, y_explo=1.42 |
| 10   | -75060.4609  | 14.17      | y_att=0.13, y_ali=0.70, y_f=1.84, d0_att=1.78, l_att=1.93, l_ali=11.90, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.02, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.29, y_acc=0.00, l_acc=0.49, d0_v=1.16, y_explo=1.42 |
| 11   | -75060.4609  | 14.16      | y_att=0.13, y_ali=0.70, y_f=1.84, d0_att=1.78, l_att=1.93, l_ali=11.90, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.02, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.29, y_acc=0.00, l_acc=0.49, d0_v=1.16, y_explo=1.42 |
| 12   | -75060.4609  | 14.14      | y_att=0.13, y_ali=0.70, y_f=1.84, d0_att=1.78, l_att=1.93, l_ali=11.90, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.02, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.29, y_acc=0.00, l_acc=0.49, d0_v=1.16, y_explo=1.42 |
| 13   | -91331.0234  | 14.17      | y_att=0.10, y_ali=0.54, y_f=4.76, d0_att=15.24, l_att=1.45, l_ali=18.84, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.06, l_acc=1.30, d0_v=0.73, y_explo=2.07 |
| 14   | -91331.0234  | 14.12      | y_att=0.10, y_ali=0.54, y_f=4.76, d0_att=15.24, l_att=1.45, l_ali=18.84, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.06, l_acc=1.30, d0_v=0.73, y_explo=2.07 |
| 15   | -91331.0234  | 14.13      | y_att=0.10, y_ali=0.54, y_f=4.76, d0_att=15.24, l_att=1.45, l_ali=18.84, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.06, l_acc=1.30, d0_v=0.73, y_explo=2.07 |
| 16   | -91331.0234  | 14.09      | y_att=0.10, y_ali=0.54, y_f=4.76, d0_att=15.24, l_att=1.45, l_ali=18.84, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.06, l_acc=1.30, d0_v=0.73, y_explo=2.07 |
| 17   | -91331.0234  | 14.13      | y_att=0.10, y_ali=0.54, y_f=4.76, d0_att=15.24, l_att=1.45, l_ali=18.84, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.06, l_acc=1.30, d0_v=0.73, y_explo=2.07 |
| 18   | -109669.4375 | 14.10      | y_att=0.10, y_ali=0.67, y_f=2.04, d0_att=1.49, l_att=0.94, l_ali=15.77, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.42, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.11, y_acc=0.03, l_acc=0.40, d0_v=1.46, y_explo=18.18 |
| 19   | -109669.4375 | 14.09      | y_att=0.10, y_ali=0.67, y_f=2.04, d0_att=1.49, l_att=0.94, l_ali=15.77, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.42, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.11, y_acc=0.03, l_acc=0.40, d0_v=1.46, y_explo=18.18 |

**End of experiment.**
