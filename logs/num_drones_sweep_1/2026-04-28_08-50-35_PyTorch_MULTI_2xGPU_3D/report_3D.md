# Experiment Report - PyTorch_MULTI_2xGPU (3D)
**Date:** 2026-04-28_08-50-35

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
| NB_DRONES            | 15         |
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
| 00   | -1878.0657   | 23.81      | y_att=0.90, y_ali=3.29, y_f=1.94, d0_att=4.91, l_att=4.97, l_ali=3.41, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.80, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.70, y_acc=0.28, l_acc=0.65, d0_v=2.45, y_explo=0.10 |
| 01   | -1948.7961   | 23.44      | y_att=0.90, y_ali=3.29, y_f=1.94, d0_att=4.91, l_att=4.97, l_ali=3.41, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.22, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.70, y_acc=0.28, l_acc=0.65, d0_v=2.45, y_explo=0.10 |
| 02   | -1981.7856   | 23.44      | y_att=2.53, y_ali=2.84, y_f=1.51, d0_att=1.62, l_att=1.75, l_ali=2.45, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.93, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.74, y_acc=0.12, l_acc=0.36, d0_v=1.19, y_explo=0.24 |
| 03   | -2048.2566   | 23.45      | y_att=1.20, y_ali=1.29, y_f=2.06, d0_att=1.89, l_att=1.64, l_ali=1.48, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.92, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.15, l_acc=0.82, d0_v=1.35, y_explo=0.19 |
| 04   | -2169.7239   | 23.45      | y_att=0.57, y_ali=2.31, y_f=1.54, d0_att=1.70, l_att=2.11, l_ali=1.45, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.65, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.75, y_acc=0.11, l_acc=1.38, d0_v=1.69, y_explo=0.15 |
| 05   | -2177.7439   | 23.45      | y_att=0.13, y_ali=0.93, y_f=0.49, d0_att=3.68, l_att=12.31, l_ali=4.52, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.68, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.63, y_acc=0.16, l_acc=0.95, d0_v=2.65, y_explo=10.42 |
| 06   | -2217.8953   | 23.45      | y_att=0.13, y_ali=0.93, y_f=0.49, d0_att=3.68, l_att=1.41, l_ali=5.13, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.88, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.70, y_acc=0.16, l_acc=1.74, d0_v=1.91, y_explo=10.15 |
| 07   | -2241.7502   | 23.45      | y_att=0.30, y_ali=2.11, y_f=1.35, d0_att=0.81, l_att=3.22, l_ali=1.53, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.27, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.85, y_acc=1.18, l_acc=0.97, d0_v=1.84, y_explo=11.79 |
| 08   | -2241.7502   | 23.45      | y_att=0.30, y_ali=2.11, y_f=1.35, d0_att=0.81, l_att=3.22, l_ali=1.53, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.27, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.85, y_acc=1.18, l_acc=0.97, d0_v=1.84, y_explo=11.79 |
| 09   | -2250.4062   | 23.45      | y_att=0.98, y_ali=1.11, y_f=0.75, d0_att=0.63, l_att=2.39, l_ali=2.97, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.40, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.01, l_acc=0.72, d0_v=2.03, y_explo=10.74 |
| 10   | -2250.4062   | 23.45      | y_att=0.98, y_ali=1.11, y_f=0.75, d0_att=0.63, l_att=2.39, l_ali=2.97, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.40, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.01, l_acc=0.72, d0_v=2.03, y_explo=10.74 |
| 11   | -2260.0945   | 23.45      | y_att=1.73, y_ali=1.02, y_f=1.33, d0_att=3.18, l_att=1.28, l_ali=2.72, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.85, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.74, y_acc=0.04, l_acc=0.69, d0_v=2.82, y_explo=0.10 |
| 12   | -2268.8293   | 23.44      | y_att=0.15, y_ali=0.56, y_f=1.79, d0_att=0.81, l_att=3.71, l_ali=2.74, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.89, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.34, l_acc=0.78, d0_v=2.22, y_explo=11.08 |
| 13   | -2268.8293   | 23.44      | y_att=0.15, y_ali=0.56, y_f=1.79, d0_att=0.81, l_att=3.71, l_ali=2.74, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.89, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.34, l_acc=0.78, d0_v=2.22, y_explo=11.08 |
| 14   | -3589.7810   | 23.44      | y_att=1.02, y_ali=0.47, y_f=17.13, d0_att=1.23, l_att=0.77, l_ali=2.49, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.57, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.66, y_acc=0.01, l_acc=0.24, d0_v=2.12, y_explo=0.11 |
| 15   | -3925.0381   | 23.44      | y_att=1.56, y_ali=0.86, y_f=17.13, d0_att=1.23, l_att=0.77, l_ali=2.38, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.89, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.10, y_acc=0.16, l_acc=0.13, d0_v=1.58, y_explo=0.11 |
| 16   | -3960.4163   | 23.45      | y_att=0.57, y_ali=1.82, y_f=17.13, d0_att=1.29, l_att=3.06, l_ali=0.19, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.22, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.00, l_acc=1.45, d0_v=2.12, y_explo=0.10 |
| 17   | -4051.5479   | 23.45      | y_att=0.34, y_ali=6.79, y_f=17.13, d0_att=0.50, l_att=2.07, l_ali=1.44, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.70, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.76, y_acc=0.01, l_acc=1.56, d0_v=2.93, y_explo=0.10 |
| 18   | -4163.1016   | 23.45      | y_att=1.02, y_ali=0.24, y_f=19.26, d0_att=0.50, l_att=1.57, l_ali=0.11, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.20, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.86, y_acc=0.08, l_acc=0.84, d0_v=1.18, y_explo=0.10 |
| 19   | -4163.1016   | 23.45      | y_att=1.02, y_ali=0.24, y_f=19.26, d0_att=0.50, l_att=1.57, l_ali=0.11, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.20, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.86, y_acc=0.08, l_acc=0.84, d0_v=1.18, y_explo=0.10 |

**End of experiment.**
