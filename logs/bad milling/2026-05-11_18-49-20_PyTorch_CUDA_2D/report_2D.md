# Experiment Report - PyTorch_CUDA (2D)
**Date:** 2026-05-11_18-49-20

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
| W_COLL               | 50.0       |
| W_DISP               | 10.0       |
| W_EFFORT             | 0          |
| W_EXPLO              | 0.0        |
| W_MILL               | -600.0     |
| W_POL                | 250.0      |
| W_STATIONARY         | 1000       |
| Z_MAX                | 10.0       |
| Z_MIN                | 1.0        |

## 2. Optimization Evolution
| Gen  |  Best Cost   |  Time (s)  |                                                                All Parameters                                                                |
| :--: | :----------: | :--------: | :------------------------------------------------------------------------------------------------------------------------------------------ |
| 00   | 18002.7422   | 13.74      | y_att=0.03, y_ali=2.65, y_f=1.54, d0_att=4.73, l_att=7.79, l_ali=3.41, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.93, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.91, y_acc=0.15, l_acc=0.77, d0_v=2.10, y_explo=4.10 |
| 01   | -177273.6094 | 13.21      | y_att=0.14, y_ali=1.99, y_f=1.38, d0_att=2.97, l_att=1.38, l_ali=4.76, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.97, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.81, y_acc=0.02, l_acc=3.16, d0_v=1.66, y_explo=0.68 |
| 02   | -241676.9375 | 13.32      | y_att=0.14, y_ali=1.99, y_f=1.82, d0_att=3.32, l_att=1.38, l_ali=4.16, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.67, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.78, y_acc=0.02, l_acc=3.07, d0_v=1.66, y_explo=0.67 |
| 03   | -322821.7188 | 13.24      | y_att=0.10, y_ali=1.65, y_f=1.43, d0_att=2.37, l_att=1.07, l_ali=3.11, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.23, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.07, y_acc=0.04, l_acc=2.67, d0_v=1.85, y_explo=0.95 |
| 04   | -343831.5000 | 13.46      | y_att=0.87, y_ali=3.31, y_f=1.98, d0_att=5.11, l_att=0.10, l_ali=2.53, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.95, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.70, y_acc=0.06, l_acc=0.31, d0_v=2.99, y_explo=4.63 |
| 05   | -545707.5625 | 13.17      | y_att=1.58, y_ali=1.51, y_f=1.04, d0_att=5.97, l_att=1.11, l_ali=11.74, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.49, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.96, y_acc=0.03, l_acc=0.90, d0_v=2.92, y_explo=4.82 |
| 06   | -545707.5625 | 13.37      | y_att=1.58, y_ali=1.51, y_f=1.04, d0_att=5.97, l_att=1.11, l_ali=11.74, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.49, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.96, y_acc=0.03, l_acc=0.90, d0_v=2.92, y_explo=4.82 |
| 07   | -1052611.8750 | 13.45      | y_att=0.16, y_ali=1.33, y_f=1.39, d0_att=6.12, l_att=1.52, l_ali=17.52, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.28, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.74, y_acc=0.16, l_acc=0.61, d0_v=4.14, y_explo=2.68 |
| 08   | -1052611.8750 | 13.41      | y_att=0.16, y_ali=1.33, y_f=1.39, d0_att=6.12, l_att=1.52, l_ali=17.52, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.28, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.74, y_acc=0.16, l_acc=0.61, d0_v=4.14, y_explo=2.68 |
| 09   | -1052611.8750 | 13.51      | y_att=0.16, y_ali=1.33, y_f=1.39, d0_att=6.12, l_att=1.52, l_ali=17.52, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.28, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.74, y_acc=0.16, l_acc=0.61, d0_v=4.14, y_explo=2.68 |
| 10   | -1175225.2500 | 13.33      | y_att=0.24, y_ali=1.21, y_f=2.29, d0_att=1.88, l_att=0.82, l_ali=23.91, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.01, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.71, y_acc=0.08, l_acc=1.11, d0_v=1.85, y_explo=5.73 |
| 11   | -1175225.2500 | 13.60      | y_att=0.24, y_ali=1.21, y_f=2.29, d0_att=1.88, l_att=0.82, l_ali=23.91, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.01, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.71, y_acc=0.08, l_acc=1.11, d0_v=1.85, y_explo=5.73 |
| 12   | -1265628.0000 | 13.13      | y_att=0.12, y_ali=0.85, y_f=0.67, d0_att=4.31, l_att=0.10, l_ali=32.04, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.64, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.69, y_acc=0.04, l_acc=0.51, d0_v=1.35, y_explo=0.43 |
| 13   | -1265628.0000 | 13.44      | y_att=0.12, y_ali=0.85, y_f=0.67, d0_att=4.31, l_att=0.10, l_ali=32.04, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.64, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.69, y_acc=0.04, l_acc=0.51, d0_v=1.35, y_explo=0.43 |
| 14   | -1265628.0000 | 13.31      | y_att=0.12, y_ali=0.85, y_f=0.67, d0_att=4.31, l_att=0.10, l_ali=32.04, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.64, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.69, y_acc=0.04, l_acc=0.51, d0_v=1.35, y_explo=0.43 |
| 15   | -1265628.0000 | 13.80      | y_att=0.12, y_ali=0.85, y_f=0.67, d0_att=4.31, l_att=0.10, l_ali=32.04, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.64, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.69, y_acc=0.04, l_acc=0.51, d0_v=1.35, y_explo=0.43 |
| 16   | -1265628.0000 | 13.57      | y_att=0.12, y_ali=0.85, y_f=0.67, d0_att=4.31, l_att=0.10, l_ali=32.04, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.64, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.69, y_acc=0.04, l_acc=0.51, d0_v=1.35, y_explo=0.43 |
| 17   | -1265628.0000 | 13.92      | y_att=0.12, y_ali=0.85, y_f=0.67, d0_att=4.31, l_att=0.10, l_ali=32.04, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.64, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.69, y_acc=0.04, l_acc=0.51, d0_v=1.35, y_explo=0.43 |
| 18   | -1265628.0000 | 13.15      | y_att=0.12, y_ali=0.85, y_f=0.67, d0_att=4.31, l_att=0.10, l_ali=32.04, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.64, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.69, y_acc=0.04, l_acc=0.51, d0_v=1.35, y_explo=0.43 |
| 19   | -1265628.0000 | 13.41      | y_att=0.12, y_ali=0.85, y_f=0.67, d0_att=4.31, l_att=0.10, l_ali=32.04, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.64, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.69, y_acc=0.04, l_acc=0.51, d0_v=1.35, y_explo=0.43 |

**End of experiment.**
