# Experiment Report - PyTorch_CUDA (2D)
**Date:** 2026-05-03_18-52-40

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
| W_COLL               | 1.0        |
| W_DISP               | 2.0        |
| W_EFFORT             | 0.0        |
| W_EXPLO              | 0.0        |
| W_MILL               | -300.0     |
| W_POL                | 0.0        |
| Z_MAX                | 10.0       |
| Z_MIN                | 1.0        |

## 2. Optimization Evolution
| Gen  |  Best Cost   |  Time (s)  |                                                                All Parameters                                                                |
| :--: | :----------: | :--------: | :------------------------------------------------------------------------------------------------------------------------------------------ |
| 00   | -31193.0000  | 4.46       | y_att=1.96, y_ali=2.91, y_f=0.59, d0_att=7.50, l_att=11.33, l_ali=1.09, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.08, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.09, y_acc=0.90, l_acc=1.02, d0_v=1.21, y_explo=4.80 |
| 01   | -47228.0781  | 4.31       | y_att=6.36, y_ali=0.28, y_f=1.93, d0_att=8.00, l_att=8.10, l_ali=1.27, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.72, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.36, y_acc=1.87, l_acc=0.53, d0_v=2.18, y_explo=0.30 |
| 02   | -77921.4844  | 4.16       | y_att=2.85, y_ali=0.22, y_f=1.21, d0_att=13.81, l_att=5.57, l_ali=1.14, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.96, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.04, y_acc=0.01, l_acc=2.26, d0_v=3.43, y_explo=3.78 |
| 03   | -125645.7969 | 4.12       | y_att=3.43, y_ali=0.44, y_f=1.42, d0_att=7.84, l_att=11.01, l_ali=5.84, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.02, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.12, y_acc=0.02, l_acc=1.57, d0_v=1.61, y_explo=2.77 |
| 04   | -130044.6250 | 4.11       | y_att=3.93, y_ali=0.59, y_f=3.73, d0_att=13.81, l_att=7.89, l_ali=2.69, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.63, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.75, y_acc=0.12, l_acc=2.25, d0_v=2.46, y_explo=4.03 |
| 05   | -130044.6250 | 4.06       | y_att=3.93, y_ali=0.59, y_f=3.73, d0_att=13.81, l_att=7.89, l_ali=2.69, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.63, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.75, y_acc=0.12, l_acc=2.25, d0_v=2.46, y_explo=4.03 |
| 06   | -132176.5312 | 4.16       | y_att=3.64, y_ali=0.34, y_f=2.43, d0_att=10.52, l_att=5.72, l_ali=3.20, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.51, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.19, y_acc=0.08, l_acc=2.05, d0_v=2.43, y_explo=3.28 |
| 07   | -138879.3281 | 4.25       | y_att=3.54, y_ali=0.32, y_f=2.28, d0_att=10.20, l_att=12.95, l_ali=4.25, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.59, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.56, y_acc=0.05, l_acc=0.15, d0_v=1.47, y_explo=4.95 |
| 08   | -141683.3438 | 4.17       | y_att=16.37, y_ali=1.85, y_f=2.57, d0_att=25.41, l_att=10.18, l_ali=2.47, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.39, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.24, y_acc=0.07, l_acc=1.25, d0_v=1.11, y_explo=4.85 |
| 09   | -143267.5156 | 4.27       | y_att=16.37, y_ali=1.85, y_f=2.57, d0_att=25.41, l_att=10.18, l_ali=2.47, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.13, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.24, y_acc=0.07, l_acc=1.25, d0_v=1.11, y_explo=4.85 |
| 10   | -143267.5156 | 4.23       | y_att=16.37, y_ali=1.85, y_f=2.57, d0_att=25.41, l_att=10.18, l_ali=2.47, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.13, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.24, y_acc=0.07, l_acc=1.25, d0_v=1.11, y_explo=4.85 |
| 11   | -156764.2812 | 4.07       | y_att=2.75, y_ali=0.32, y_f=3.74, d0_att=20.54, l_att=10.48, l_ali=4.24, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.82, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.91, y_acc=0.01, l_acc=1.05, d0_v=1.28, y_explo=6.39 |
| 12   | -156764.2812 | 4.23       | y_att=2.75, y_ali=0.32, y_f=3.74, d0_att=20.54, l_att=10.48, l_ali=4.24, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.82, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.91, y_acc=0.01, l_acc=1.05, d0_v=1.28, y_explo=6.39 |
| 13   | -156764.2812 | 4.29       | y_att=2.75, y_ali=0.32, y_f=3.74, d0_att=20.54, l_att=10.48, l_ali=4.24, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.82, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.91, y_acc=0.01, l_acc=1.05, d0_v=1.28, y_explo=6.39 |
| 14   | -156764.2812 | 4.24       | y_att=2.75, y_ali=0.32, y_f=3.74, d0_att=20.54, l_att=10.48, l_ali=4.24, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.82, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.91, y_acc=0.01, l_acc=1.05, d0_v=1.28, y_explo=6.39 |
| 15   | -156764.2812 | 4.43       | y_att=2.75, y_ali=0.32, y_f=3.74, d0_att=20.54, l_att=10.48, l_ali=4.24, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.82, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.91, y_acc=0.01, l_acc=1.05, d0_v=1.28, y_explo=6.39 |
| 16   | -156764.2812 | 4.34       | y_att=2.75, y_ali=0.32, y_f=3.74, d0_att=20.54, l_att=10.48, l_ali=4.24, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.82, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.91, y_acc=0.01, l_acc=1.05, d0_v=1.28, y_explo=6.39 |
| 17   | -156764.2812 | 4.22       | y_att=2.75, y_ali=0.32, y_f=3.74, d0_att=20.54, l_att=10.48, l_ali=4.24, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.82, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.91, y_acc=0.01, l_acc=1.05, d0_v=1.28, y_explo=6.39 |
| 18   | -156764.2812 | 4.36       | y_att=2.75, y_ali=0.32, y_f=3.74, d0_att=20.54, l_att=10.48, l_ali=4.24, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.82, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.91, y_acc=0.01, l_acc=1.05, d0_v=1.28, y_explo=6.39 |
| 19   | -158696.4844 | 4.23       | y_att=2.49, y_ali=0.34, y_f=2.65, d0_att=25.57, l_att=10.38, l_ali=6.50, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.72, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.01, l_acc=1.88, d0_v=1.76, y_explo=4.73 |

**End of experiment.**
