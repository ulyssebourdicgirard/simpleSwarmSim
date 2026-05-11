# Experiment Report - PyTorch_CUDA (2D)
**Date:** 2026-05-11_19-04-53

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
| NB_DRONES            | 20         |
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
| 00   | 342621.6875  | 32.08      | y_att=2.34, y_ali=3.59, y_f=1.67, d0_att=7.71, l_att=5.78, l_ali=2.61, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.37, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.85, y_acc=0.43, l_acc=3.45, d0_v=0.50, y_explo=0.41 |
| 01   | 87950.6094   | 31.69      | y_att=0.10, y_ali=2.26, y_f=1.91, d0_att=5.94, l_att=5.91, l_ali=5.94, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.64, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.18, y_acc=0.01, l_acc=1.93, d0_v=2.95, y_explo=0.34 |
| 02   | -3364.5278   | 31.73      | y_att=0.10, y_ali=2.26, y_f=1.91, d0_att=5.94, l_att=5.91, l_ali=5.94, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.66, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.18, y_acc=0.01, l_acc=1.93, d0_v=2.95, y_explo=0.34 |
| 03   | -45562.7695  | 31.68      | y_att=0.10, y_ali=2.15, y_f=1.85, d0_att=1.25, l_att=1.03, l_ali=3.82, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.10, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.75, y_acc=0.03, l_acc=0.65, d0_v=1.80, y_explo=3.34 |
| 04   | -157077.0625 | 31.64      | y_att=0.78, y_ali=2.17, y_f=1.64, d0_att=1.54, l_att=3.28, l_ali=10.60, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.18, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.15, y_acc=0.08, l_acc=0.85, d0_v=1.27, y_explo=0.20 |
| 05   | -179165.6719 | 31.58      | y_att=0.36, y_ali=1.61, y_f=2.91, d0_att=2.08, l_att=3.17, l_ali=13.02, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.93, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.27, l_acc=1.11, d0_v=1.76, y_explo=4.03 |
| 06   | -249397.2812 | 31.50      | y_att=0.26, y_ali=2.87, y_f=0.45, d0_att=2.11, l_att=5.76, l_ali=13.17, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.80, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.58, y_acc=0.02, l_acc=0.64, d0_v=1.24, y_explo=4.15 |
| 07   | -488404.2188 | 31.46      | y_att=0.70, y_ali=1.39, y_f=2.03, d0_att=6.39, l_att=7.18, l_ali=21.55, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.53, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.60, y_acc=0.07, l_acc=1.93, d0_v=1.20, y_explo=4.70 |
| 08   | -488404.2188 | 31.41      | y_att=0.70, y_ali=1.39, y_f=2.03, d0_att=6.39, l_att=7.18, l_ali=21.55, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.53, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.60, y_acc=0.07, l_acc=1.93, d0_v=1.20, y_explo=4.70 |
| 09   | -772765.5625 | 31.43      | y_att=0.14, y_ali=0.86, y_f=3.38, d0_att=3.56, l_att=0.12, l_ali=12.43, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.19, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.79, y_acc=0.04, l_acc=0.49, d0_v=1.42, y_explo=0.46 |
| 10   | -774431.3750 | 31.46      | y_att=0.16, y_ali=1.65, y_f=1.56, d0_att=3.62, l_att=1.03, l_ali=13.27, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.70, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.60, y_acc=0.02, l_acc=0.44, d0_v=2.54, y_explo=3.00 |
| 11   | -890210.2500 | 31.36      | y_att=0.16, y_ali=1.27, y_f=1.23, d0_att=3.82, l_att=4.16, l_ali=19.14, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.83, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.83, y_acc=0.04, l_acc=0.66, d0_v=1.82, y_explo=0.39 |
| 12   | -1046195.5000 | 31.41      | y_att=0.42, y_ali=0.99, y_f=1.60, d0_att=1.39, l_att=0.15, l_ali=22.83, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.22, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.31, y_acc=0.02, l_acc=0.96, d0_v=0.74, y_explo=0.59 |
| 13   | -1104665.1250 | 31.43      | y_att=0.13, y_ali=1.26, y_f=0.85, d0_att=3.50, l_att=1.60, l_ali=23.74, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.95, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.61, y_acc=0.05, l_acc=0.29, d0_v=1.05, y_explo=4.93 |
| 14   | -1144613.6250 | 31.39      | y_att=0.18, y_ali=0.91, y_f=2.29, d0_att=2.09, l_att=0.30, l_ali=26.41, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.13, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.51, y_acc=0.10, l_acc=0.31, d0_v=0.66, y_explo=1.76 |
| 15   | -1144613.6250 | 31.45      | y_att=0.18, y_ali=0.91, y_f=2.29, d0_att=2.09, l_att=0.30, l_ali=26.41, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.13, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.51, y_acc=0.10, l_acc=0.31, d0_v=0.66, y_explo=1.76 |
| 16   | -1209088.0000 | 31.46      | y_att=0.10, y_ali=0.47, y_f=2.42, d0_att=4.53, l_att=0.25, l_ali=30.36, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.12, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.63, y_acc=0.21, l_acc=0.44, d0_v=1.89, y_explo=2.91 |
| 17   | -1219009.5000 | 31.31      | y_att=0.11, y_ali=0.91, y_f=0.70, d0_att=3.75, l_att=0.52, l_ali=29.62, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.38, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.24, y_acc=0.02, l_acc=0.72, d0_v=0.88, y_explo=11.11 |
| 18   | -1219009.5000 | 31.40      | y_att=0.11, y_ali=0.91, y_f=0.70, d0_att=3.75, l_att=0.52, l_ali=29.62, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.38, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.24, y_acc=0.02, l_acc=0.72, d0_v=0.88, y_explo=11.11 |
| 19   | -1219009.5000 | 31.48      | y_att=0.11, y_ali=0.91, y_f=0.70, d0_att=3.75, l_att=0.52, l_ali=29.62, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.38, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.24, y_acc=0.02, l_acc=0.72, d0_v=0.88, y_explo=11.11 |

**End of experiment.**
