# Experiment Report - PyTorch_CUDA (2D)
**Date:** 2026-05-03_19-14-57

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
| 00   | -24499.1016  | 9.12       | y_att=4.67, y_ali=2.38, y_f=0.13, d0_att=7.90, l_att=5.50, l_ali=2.16, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.92, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.87, y_acc=1.17, l_acc=3.21, d0_v=1.13, y_explo=3.72 |
| 01   | -24864.3066  | 8.97       | y_att=0.10, y_ali=4.82, y_f=1.51, d0_att=6.17, l_att=7.13, l_ali=2.18, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.31, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.12, y_acc=0.53, l_acc=0.56, d0_v=2.01, y_explo=3.78 |
| 02   | -31453.2930  | 8.76       | y_att=0.14, y_ali=5.47, y_f=1.73, d0_att=4.27, l_att=13.55, l_ali=10.95, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.44, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.84, y_acc=0.37, l_acc=0.89, d0_v=3.09, y_explo=4.22 |
| 03   | -31453.2930  | 8.85       | y_att=0.14, y_ali=5.47, y_f=1.73, d0_att=4.27, l_att=13.55, l_ali=10.95, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.44, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.84, y_acc=0.37, l_acc=0.89, d0_v=3.09, y_explo=4.22 |
| 04   | -31453.2930  | 8.73       | y_att=0.14, y_ali=5.47, y_f=1.73, d0_att=4.27, l_att=13.55, l_ali=10.95, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.44, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.84, y_acc=0.37, l_acc=0.89, d0_v=3.09, y_explo=4.22 |
| 05   | -59515.8242  | 8.65       | y_att=0.18, y_ali=3.69, y_f=1.43, d0_att=1.61, l_att=11.12, l_ali=9.19, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.96, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.00, y_acc=0.08, l_acc=0.59, d0_v=1.25, y_explo=2.68 |
| 06   | -59515.8242  | 8.79       | y_att=0.18, y_ali=3.69, y_f=1.43, d0_att=1.61, l_att=11.12, l_ali=9.19, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.96, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.00, y_acc=0.08, l_acc=0.59, d0_v=1.25, y_explo=2.68 |
| 07   | -59515.8242  | 8.72       | y_att=0.18, y_ali=3.69, y_f=1.43, d0_att=1.61, l_att=11.12, l_ali=9.19, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.96, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.00, y_acc=0.08, l_acc=0.59, d0_v=1.25, y_explo=2.68 |
| 08   | -59515.8242  | 8.75       | y_att=0.18, y_ali=3.69, y_f=1.43, d0_att=1.61, l_att=11.12, l_ali=9.19, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.96, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.00, y_acc=0.08, l_acc=0.59, d0_v=1.25, y_explo=2.68 |
| 09   | -59515.8242  | 8.74       | y_att=0.18, y_ali=3.69, y_f=1.43, d0_att=1.61, l_att=11.12, l_ali=9.19, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.96, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.00, y_acc=0.08, l_acc=0.59, d0_v=1.25, y_explo=2.68 |
| 10   | -61294.3008  | 8.72       | y_att=0.27, y_ali=0.68, y_f=1.02, d0_att=3.40, l_att=0.65, l_ali=17.21, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.51, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.22, y_acc=0.03, l_acc=0.96, d0_v=1.28, y_explo=0.82 |
| 11   | -63833.2891  | 8.74       | y_att=0.27, y_ali=5.99, y_f=1.78, d0_att=2.27, l_att=1.22, l_ali=10.85, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.30, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.46, y_acc=0.02, l_acc=1.83, d0_v=0.63, y_explo=2.84 |
| 12   | -74204.2891  | 8.76       | y_att=0.16, y_ali=0.54, y_f=1.46, d0_att=5.73, l_att=1.37, l_ali=22.30, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.99, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.77, y_acc=0.45, l_acc=0.47, d0_v=2.51, y_explo=5.03 |
| 13   | -99588.5234  | 8.72       | y_att=0.14, y_ali=0.70, y_f=2.78, d0_att=3.65, l_att=1.13, l_ali=17.50, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.35, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.29, y_acc=0.11, l_acc=2.78, d0_v=2.49, y_explo=1.85 |
| 14   | -104712.3984 | 8.84       | y_att=0.10, y_ali=0.89, y_f=6.13, d0_att=1.22, l_att=0.34, l_ali=13.35, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.93, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.50, y_acc=0.17, l_acc=0.45, d0_v=3.96, y_explo=3.08 |
| 15   | -109148.6484 | 8.77       | y_att=0.10, y_ali=0.62, y_f=1.58, d0_att=1.53, l_att=0.48, l_ali=24.82, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.86, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.72, y_acc=0.07, l_acc=0.45, d0_v=0.88, y_explo=8.50 |
| 16   | -111776.8203 | 8.68       | y_att=0.12, y_ali=0.70, y_f=0.82, d0_att=2.29, l_att=1.35, l_ali=19.53, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.55, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.32, y_acc=0.04, l_acc=0.50, d0_v=0.76, y_explo=4.80 |
| 17   | -126832.5000 | 8.84       | y_att=0.14, y_ali=0.60, y_f=1.57, d0_att=1.97, l_att=0.64, l_ali=12.38, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.65, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.02, y_acc=0.02, l_acc=0.49, d0_v=3.12, y_explo=0.50 |
| 18   | -128960.3359 | 8.71       | y_att=0.10, y_ali=0.47, y_f=5.03, d0_att=1.13, l_att=1.20, l_ali=20.48, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.71, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.49, y_acc=0.06, l_acc=1.85, d0_v=1.35, y_explo=1.59 |
| 19   | -128960.3359 | 8.69       | y_att=0.10, y_ali=0.47, y_f=5.03, d0_att=1.13, l_att=1.20, l_ali=20.48, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.71, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.49, y_acc=0.06, l_acc=1.85, d0_v=1.35, y_explo=1.59 |

**End of experiment.**
