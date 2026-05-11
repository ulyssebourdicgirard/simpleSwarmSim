# Experiment Report - PyTorch_CUDA (2D)
**Date:** 2026-05-11_19-17-47

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
| NB_DRONES            | 25         |
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
| 00   | 257815.7188  | 53.86      | y_att=0.02, y_ali=2.10, y_f=1.15, d0_att=2.22, l_att=5.88, l_ali=4.67, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.50, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.21, y_acc=0.14, l_acc=0.71, d0_v=1.63, y_explo=2.87 |
| 01   | 104070.5078  | 53.62      | y_att=1.80, y_ali=3.28, y_f=1.82, d0_att=6.81, l_att=11.31, l_ali=7.12, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.08, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.88, y_acc=0.04, l_acc=0.63, d0_v=2.60, y_explo=1.72 |
| 02   | 104070.5078  | 53.60      | y_att=1.80, y_ali=3.28, y_f=1.82, d0_att=6.81, l_att=11.31, l_ali=7.12, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.08, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.88, y_acc=0.04, l_acc=0.63, d0_v=2.60, y_explo=1.72 |
| 03   | 104070.5078  | 53.57      | y_att=1.80, y_ali=3.28, y_f=1.82, d0_att=6.81, l_att=11.31, l_ali=7.12, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.08, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.88, y_acc=0.04, l_acc=0.63, d0_v=2.60, y_explo=1.72 |
| 04   | -95853.4297  | 53.52      | y_att=0.10, y_ali=2.07, y_f=0.46, d0_att=1.87, l_att=7.90, l_ali=11.52, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.54, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.02, l_acc=0.92, d0_v=1.80, y_explo=3.17 |
| 05   | -144007.8125 | 53.45      | y_att=0.10, y_ali=1.28, y_f=2.56, d0_att=6.36, l_att=12.72, l_ali=10.00, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.51, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.24, y_acc=0.05, l_acc=0.33, d0_v=1.08, y_explo=1.99 |
| 06   | -389318.1250 | 53.34      | y_att=0.16, y_ali=2.00, y_f=1.89, d0_att=2.76, l_att=11.49, l_ali=19.62, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.78, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.18, y_acc=0.09, l_acc=0.89, d0_v=1.70, y_explo=2.61 |
| 07   | -389318.1250 | 53.25      | y_att=0.16, y_ali=2.00, y_f=1.89, d0_att=2.76, l_att=11.49, l_ali=19.62, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.78, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.18, y_acc=0.09, l_acc=0.89, d0_v=1.70, y_explo=2.61 |
| 08   | -389318.1250 | 53.16      | y_att=0.16, y_ali=2.00, y_f=1.89, d0_att=2.76, l_att=11.49, l_ali=19.62, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.78, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.18, y_acc=0.09, l_acc=0.89, d0_v=1.70, y_explo=2.61 |
| 09   | -616268.6250 | 53.17      | y_att=0.12, y_ali=0.78, y_f=0.50, d0_att=3.51, l_att=0.42, l_ali=18.14, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.59, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.84, y_acc=0.02, l_acc=0.53, d0_v=1.62, y_explo=2.00 |
| 10   | -616268.6250 | 53.17      | y_att=0.12, y_ali=0.78, y_f=0.50, d0_att=3.51, l_att=0.42, l_ali=18.14, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.59, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.84, y_acc=0.02, l_acc=0.53, d0_v=1.62, y_explo=2.00 |
| 11   | -616268.6250 | 53.18      | y_att=0.12, y_ali=0.78, y_f=0.50, d0_att=3.51, l_att=0.42, l_ali=18.14, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.59, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.84, y_acc=0.02, l_acc=0.53, d0_v=1.62, y_explo=2.00 |
| 12   | -1053161.6250 | 53.22      | y_att=0.13, y_ali=0.74, y_f=0.55, d0_att=10.23, l_att=2.95, l_ali=26.33, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.59, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.81, y_acc=0.02, l_acc=0.76, d0_v=1.35, y_explo=0.68 |
| 13   | -1053161.6250 | 53.21      | y_att=0.13, y_ali=0.74, y_f=0.55, d0_att=10.23, l_att=2.95, l_ali=26.33, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.59, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.81, y_acc=0.02, l_acc=0.76, d0_v=1.35, y_explo=0.68 |
| 14   | -1053161.6250 | 56.31      | y_att=0.13, y_ali=0.74, y_f=0.55, d0_att=10.23, l_att=2.95, l_ali=26.33, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.59, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.81, y_acc=0.02, l_acc=0.76, d0_v=1.35, y_explo=0.68 |
| 15   | -1063297.6250 | 54.77      | y_att=0.10, y_ali=0.73, y_f=1.56, d0_att=1.85, l_att=0.62, l_ali=23.81, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.64, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.04, y_acc=0.05, l_acc=1.23, d0_v=2.28, y_explo=6.70 |
| 16   | -1154548.3750 | 54.70      | y_att=0.10, y_ali=0.76, y_f=2.86, d0_att=1.85, l_att=1.21, l_ali=39.65, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.05, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.79, y_acc=0.08, l_acc=0.82, d0_v=0.63, y_explo=2.60 |
| 17   | -1154548.3750 | 54.72      | y_att=0.10, y_ali=0.76, y_f=2.86, d0_att=1.85, l_att=1.21, l_ali=39.65, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.05, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.79, y_acc=0.08, l_acc=0.82, d0_v=0.63, y_explo=2.60 |
| 18   | -1154548.3750 | 54.71      | y_att=0.10, y_ali=0.76, y_f=2.86, d0_att=1.85, l_att=1.21, l_ali=39.65, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.05, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.79, y_acc=0.08, l_acc=0.82, d0_v=0.63, y_explo=2.60 |
| 19   | -1165033.2500 | 53.94      | y_att=0.16, y_ali=0.83, y_f=1.74, d0_att=0.72, l_att=0.43, l_ali=35.62, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.33, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.21, y_acc=0.05, l_acc=1.73, d0_v=2.23, y_explo=1.52 |

**End of experiment.**
