# Experiment Report - PyTorch_MULTI_2xGPU (3D)
**Date:** 2026-04-28_08-37-30

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
| NB_DRONES            | 5          |
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
| 00   | -756.1028    | 8.19       | y_att=0.00, y_ali=1.27, y_f=1.23, d0_att=2.43, l_att=10.53, l_ali=4.03, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.04, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.50, y_acc=0.37, l_acc=2.83, d0_v=2.35, y_explo=0.05 |
| 01   | -798.0615    | 7.84       | y_att=0.74, y_ali=1.07, y_f=0.87, d0_att=4.85, l_att=1.98, l_ali=3.37, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.34, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.14, l_acc=1.11, d0_v=3.55, y_explo=0.10 |
| 02   | -1114.0161   | 7.84       | y_att=0.27, y_ali=2.32, y_f=1.23, d0_att=5.11, l_att=10.24, l_ali=1.72, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.04, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.00, y_acc=0.38, l_acc=1.29, d0_v=1.13, y_explo=7.45 |
| 03   | -1114.0161   | 7.84       | y_att=0.27, y_ali=2.32, y_f=1.23, d0_att=5.11, l_att=10.24, l_ali=1.72, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.04, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.00, y_acc=0.38, l_acc=1.29, d0_v=1.13, y_explo=7.45 |
| 04   | -1114.0161   | 7.84       | y_att=0.27, y_ali=2.32, y_f=1.23, d0_att=5.11, l_att=10.24, l_ali=1.72, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.04, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.00, y_acc=0.38, l_acc=1.29, d0_v=1.13, y_explo=7.45 |
| 05   | -1114.0161   | 7.84       | y_att=0.27, y_ali=2.32, y_f=1.23, d0_att=5.11, l_att=10.24, l_ali=1.72, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.04, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.00, y_acc=0.38, l_acc=1.29, d0_v=1.13, y_explo=7.45 |
| 06   | -1114.0161   | 7.84       | y_att=0.27, y_ali=2.32, y_f=1.23, d0_att=5.11, l_att=10.24, l_ali=1.72, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.04, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.00, y_acc=0.38, l_acc=1.29, d0_v=1.13, y_explo=7.45 |
| 07   | -1114.0161   | 7.85       | y_att=0.27, y_ali=2.32, y_f=1.23, d0_att=5.11, l_att=10.24, l_ali=1.72, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.04, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.00, y_acc=0.38, l_acc=1.29, d0_v=1.13, y_explo=7.45 |
| 08   | -1114.0161   | 7.84       | y_att=0.27, y_ali=2.32, y_f=1.23, d0_att=5.11, l_att=10.24, l_ali=1.72, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.04, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.00, y_acc=0.38, l_acc=1.29, d0_v=1.13, y_explo=7.45 |
| 09   | -1114.0161   | 7.85       | y_att=0.27, y_ali=2.32, y_f=1.23, d0_att=5.11, l_att=10.24, l_ali=1.72, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.04, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.00, y_acc=0.38, l_acc=1.29, d0_v=1.13, y_explo=7.45 |
