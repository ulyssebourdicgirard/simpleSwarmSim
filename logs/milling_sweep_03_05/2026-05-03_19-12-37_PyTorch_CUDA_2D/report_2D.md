# Experiment Report - PyTorch_CUDA (2D)
**Date:** 2026-05-03_19-12-37

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
| NB_DRONES            | 15         |
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
| 00   | -38523.4023  | 4.63       | y_att=2.44, y_ali=0.72, y_f=1.18, d0_att=7.98, l_att=8.29, l_ali=2.08, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.89, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.09, y_acc=1.72, l_acc=1.32, d0_v=1.36, y_explo=4.08 |
| 01   | -38523.4023  | 4.34       | y_att=2.44, y_ali=0.72, y_f=1.18, d0_att=7.98, l_att=8.29, l_ali=2.08, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.89, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.09, y_acc=1.72, l_acc=1.32, d0_v=1.36, y_explo=4.08 |
| 02   | -38523.4023  | 4.38       | y_att=2.44, y_ali=0.72, y_f=1.18, d0_att=7.98, l_att=8.29, l_ali=2.08, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.89, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.09, y_acc=1.72, l_acc=1.32, d0_v=1.36, y_explo=4.08 |
| 03   | -38523.4023  | 4.28       | y_att=2.44, y_ali=0.72, y_f=1.18, d0_att=7.98, l_att=8.29, l_ali=2.08, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.89, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.09, y_acc=1.72, l_acc=1.32, d0_v=1.36, y_explo=4.08 |
| 04   | -68876.7500  | 4.30       | y_att=0.13, y_ali=1.33, y_f=2.57, d0_att=8.60, l_att=10.73, l_ali=4.54, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.30, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.72, y_acc=0.29, l_acc=0.66, d0_v=1.49, y_explo=3.04 |
| 05   | -68876.7500  | 4.20       | y_att=0.13, y_ali=1.33, y_f=2.57, d0_att=8.60, l_att=10.73, l_ali=4.54, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.30, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.72, y_acc=0.29, l_acc=0.66, d0_v=1.49, y_explo=3.04 |
| 06   | -68876.7500  | 4.38       | y_att=0.13, y_ali=1.33, y_f=2.57, d0_att=8.60, l_att=10.73, l_ali=4.54, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.30, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.72, y_acc=0.29, l_acc=0.66, d0_v=1.49, y_explo=3.04 |
| 07   | -68876.7500  | 4.37       | y_att=0.13, y_ali=1.33, y_f=2.57, d0_att=8.60, l_att=10.73, l_ali=4.54, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.30, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.72, y_acc=0.29, l_acc=0.66, d0_v=1.49, y_explo=3.04 |
| 08   | -68876.7500  | 4.41       | y_att=0.13, y_ali=1.33, y_f=2.57, d0_att=8.60, l_att=10.73, l_ali=4.54, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.30, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.72, y_acc=0.29, l_acc=0.66, d0_v=1.49, y_explo=3.04 |
| 09   | -77843.3516  | 4.45       | y_att=0.10, y_ali=0.52, y_f=1.43, d0_att=4.14, l_att=1.29, l_ali=15.58, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.44, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.18, y_acc=0.09, l_acc=0.92, d0_v=1.48, y_explo=7.48 |
| 10   | -77843.3516  | 4.45       | y_att=0.10, y_ali=0.52, y_f=1.43, d0_att=4.14, l_att=1.29, l_ali=15.58, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.44, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.18, y_acc=0.09, l_acc=0.92, d0_v=1.48, y_explo=7.48 |
| 11   | -82829.2891  | 4.21       | y_att=0.21, y_ali=0.52, y_f=0.90, d0_att=1.49, l_att=1.29, l_ali=16.94, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.95, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.18, y_acc=0.09, l_acc=0.80, d0_v=2.85, y_explo=2.23 |
| 12   | -105534.3672 | 4.38       | y_att=0.12, y_ali=0.42, y_f=1.85, d0_att=1.99, l_att=0.48, l_ali=26.64, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.55, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.11, y_acc=0.23, l_acc=1.62, d0_v=3.42, y_explo=0.56 |
| 13   | -105534.3672 | 4.40       | y_att=0.12, y_ali=0.42, y_f=1.85, d0_att=1.99, l_att=0.48, l_ali=26.64, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.55, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.11, y_acc=0.23, l_acc=1.62, d0_v=3.42, y_explo=0.56 |
| 14   | -120345.0781 | 4.18       | y_att=0.12, y_ali=0.67, y_f=3.32, d0_att=1.99, l_att=0.27, l_ali=26.64, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.05, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.50, y_acc=0.11, l_acc=1.45, d0_v=1.66, y_explo=0.78 |
| 15   | -120345.0781 | 4.27       | y_att=0.12, y_ali=0.67, y_f=3.32, d0_att=1.99, l_att=0.27, l_ali=26.64, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.05, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.50, y_acc=0.11, l_acc=1.45, d0_v=1.66, y_explo=0.78 |
| 16   | -120345.0781 | 4.20       | y_att=0.12, y_ali=0.67, y_f=3.32, d0_att=1.99, l_att=0.27, l_ali=26.64, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.05, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.50, y_acc=0.11, l_acc=1.45, d0_v=1.66, y_explo=0.78 |
| 17   | -120345.0781 | 4.28       | y_att=0.12, y_ali=0.67, y_f=3.32, d0_att=1.99, l_att=0.27, l_ali=26.64, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.05, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.50, y_acc=0.11, l_acc=1.45, d0_v=1.66, y_explo=0.78 |
| 18   | -120345.0781 | 4.34       | y_att=0.12, y_ali=0.67, y_f=3.32, d0_att=1.99, l_att=0.27, l_ali=26.64, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.05, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.50, y_acc=0.11, l_acc=1.45, d0_v=1.66, y_explo=0.78 |
| 19   | -120345.0781 | 4.19       | y_att=0.12, y_ali=0.67, y_f=3.32, d0_att=1.99, l_att=0.27, l_ali=26.64, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.05, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.50, y_acc=0.11, l_acc=1.45, d0_v=1.66, y_explo=0.78 |

**End of experiment.**
