# Experiment Report - PyTorch_CUDA (2D)
**Date:** 2026-05-11_18-56-33

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
| NB_DRONES            | 15         |
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
| 00   | -26589.8984  | 18.30      | y_att=0.02, y_ali=1.64, y_f=1.99, d0_att=3.54, l_att=5.74, l_ali=3.90, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.92, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.17, y_acc=0.31, l_acc=0.55, d0_v=2.04, y_explo=1.79 |
| 01   | -26589.8984  | 18.08      | y_att=0.02, y_ali=1.64, y_f=1.99, d0_att=3.54, l_att=5.74, l_ali=3.90, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.92, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.17, y_acc=0.31, l_acc=0.55, d0_v=2.04, y_explo=1.79 |
| 02   | -316889.0000 | 18.20      | y_att=0.10, y_ali=2.30, y_f=1.51, d0_att=2.37, l_att=1.31, l_ali=3.40, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.29, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.58, y_acc=0.02, l_acc=2.19, d0_v=1.21, y_explo=1.27 |
| 03   | -316889.0000 | 17.77      | y_att=0.10, y_ali=2.30, y_f=1.51, d0_att=2.37, l_att=1.31, l_ali=3.40, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.29, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.58, y_acc=0.02, l_acc=2.19, d0_v=1.21, y_explo=1.27 |
| 04   | -321671.6875 | 16.92      | y_att=0.11, y_ali=1.89, y_f=1.65, d0_att=1.95, l_att=1.10, l_ali=4.85, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.68, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.71, y_acc=0.07, l_acc=1.62, d0_v=2.08, y_explo=3.74 |
| 05   | -384951.4375 | 17.91      | y_att=0.88, y_ali=2.34, y_f=1.92, d0_att=3.62, l_att=2.66, l_ali=16.27, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.26, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.33, y_acc=0.12, l_acc=1.10, d0_v=1.96, y_explo=1.65 |
| 06   | -520844.5000 | 17.03      | y_att=0.34, y_ali=2.05, y_f=2.75, d0_att=5.38, l_att=1.18, l_ali=8.68, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.87, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.40, y_acc=0.11, l_acc=0.38, d0_v=0.88, y_explo=6.24 |
| 07   | -520844.5000 | 16.70      | y_att=0.34, y_ali=2.05, y_f=2.75, d0_att=5.38, l_att=1.18, l_ali=8.68, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.87, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.40, y_acc=0.11, l_acc=0.38, d0_v=0.88, y_explo=6.24 |
| 08   | -520844.5000 | 16.91      | y_att=0.34, y_ali=2.05, y_f=2.75, d0_att=5.38, l_att=1.18, l_ali=8.68, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.87, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.40, y_acc=0.11, l_acc=0.38, d0_v=0.88, y_explo=6.24 |
| 09   | -660377.0625 | 17.19      | y_att=0.10, y_ali=2.52, y_f=2.93, d0_att=2.03, l_att=0.45, l_ali=25.51, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.18, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.12, y_acc=0.26, l_acc=0.84, d0_v=1.42, y_explo=3.26 |
| 10   | -660377.0625 | 16.91      | y_att=0.10, y_ali=2.52, y_f=2.93, d0_att=2.03, l_att=0.45, l_ali=25.51, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.18, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.12, y_acc=0.26, l_acc=0.84, d0_v=1.42, y_explo=3.26 |
| 11   | -660377.0625 | 16.70      | y_att=0.10, y_ali=2.52, y_f=2.93, d0_att=2.03, l_att=0.45, l_ali=25.51, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.18, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.12, y_acc=0.26, l_acc=0.84, d0_v=1.42, y_explo=3.26 |
| 12   | -660377.0625 | 16.62      | y_att=0.10, y_ali=2.52, y_f=2.93, d0_att=2.03, l_att=0.45, l_ali=25.51, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.18, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.12, y_acc=0.26, l_acc=0.84, d0_v=1.42, y_explo=3.26 |
| 13   | -896975.2500 | 16.91      | y_att=0.10, y_ali=0.66, y_f=0.86, d0_att=2.53, l_att=0.85, l_ali=33.97, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.57, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.17, y_acc=0.04, l_acc=0.64, d0_v=1.75, y_explo=3.80 |
| 14   | -896975.2500 | 17.53      | y_att=0.10, y_ali=0.66, y_f=0.86, d0_att=2.53, l_att=0.85, l_ali=33.97, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.57, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.17, y_acc=0.04, l_acc=0.64, d0_v=1.75, y_explo=3.80 |
| 15   | -896975.2500 | 16.39      | y_att=0.10, y_ali=0.66, y_f=0.86, d0_att=2.53, l_att=0.85, l_ali=33.97, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.57, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.17, y_acc=0.04, l_acc=0.64, d0_v=1.75, y_explo=3.80 |
| 16   | -896975.2500 | 16.90      | y_att=0.10, y_ali=0.66, y_f=0.86, d0_att=2.53, l_att=0.85, l_ali=33.97, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.57, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.17, y_acc=0.04, l_acc=0.64, d0_v=1.75, y_explo=3.80 |
| 17   | -1133912.0000 | 17.31      | y_att=0.10, y_ali=0.54, y_f=1.65, d0_att=1.17, l_att=0.11, l_ali=34.82, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.28, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.43, y_acc=0.02, l_acc=2.25, d0_v=1.20, y_explo=1.29 |
| 18   | -1133912.0000 | 16.73      | y_att=0.10, y_ali=0.54, y_f=1.65, d0_att=1.17, l_att=0.11, l_ali=34.82, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.28, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.43, y_acc=0.02, l_acc=2.25, d0_v=1.20, y_explo=1.29 |
| 19   | -1133912.0000 | 16.55      | y_att=0.10, y_ali=0.54, y_f=1.65, d0_att=1.17, l_att=0.11, l_ali=34.82, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.28, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.43, y_acc=0.02, l_acc=2.25, d0_v=1.20, y_explo=1.29 |

**End of experiment.**
