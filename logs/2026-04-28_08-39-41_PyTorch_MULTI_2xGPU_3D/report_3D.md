# Experiment Report - PyTorch_MULTI_2xGPU (3D)
**Date:** 2026-04-28_08-39-41

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
| 00   | -718.9162    | 8.20       | y_att=1.20, y_ali=3.76, y_f=1.94, d0_att=2.69, l_att=4.42, l_ali=2.58, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.12, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.29, y_acc=0.31, l_acc=1.64, d0_v=1.96, y_explo=0.94 |
| 01   | -763.3964    | 7.83       | y_att=2.37, y_ali=2.87, y_f=1.07, d0_att=2.85, l_att=1.37, l_ali=3.88, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.15, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.83, y_acc=0.33, l_acc=1.09, d0_v=2.28, y_explo=0.15 |
| 02   | -865.8256    | 7.84       | y_att=0.13, y_ali=0.93, y_f=1.28, d0_att=7.66, l_att=9.86, l_ali=4.15, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.15, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.17, y_acc=0.07, l_acc=1.95, d0_v=2.33, y_explo=8.42 |
