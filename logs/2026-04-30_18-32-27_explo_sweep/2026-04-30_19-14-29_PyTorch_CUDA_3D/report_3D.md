# Experiment Report - PyTorch_CUDA (3D)
**Date:** 2026-04-30_19-14-29

## 1. Initial Configuration
| Parameter | Value |
| :--- | :--- |
| ALPHA_LPF            | 0.2        |
| ARENA_RADIUS         | 120.0      |
| COLLISION_DIST       | 0.4        |
| DT                   | 0.1        |
| ENABLE_3D            | True       |
| EXPLO_STRATEGY       | global_best |
| FOV_FACTOR           | 0.9        |
| FULL_MILLING_MODE    | False      |
| GEN_CPU              | 20         |
| GEN_GPU              | 10         |
| GRID_RES             | 5.0        |
| MAP_STRATEGY         | local_shared |
| MAX_SPEED            | 20.0       |
| MAX_YAW_RATE         | 3.14       |
| MIN_SPAWN_DIST       | 2.0        |
| NB_DRONES            | 10         |
| NEIGHBORS            | 2          |
| N_INIT_CONDITIONS    | 4          |
| POP_SIZE_CPU         | 150        |
| POP_SIZE_GPU         | 1000       |
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
| 00   | -3205.2405   | 59.04      | y_att=3.68, y_ali=2.60, y_f=1.97, d0_att=3.01, l_att=2.08, l_ali=1.26, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.87, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.34, y_acc=0.01, l_acc=3.72, d0_v=2.55, y_explo=0.14 |
| 01   | -3205.2405   | 58.77      | y_att=3.68, y_ali=2.60, y_f=1.97, d0_att=3.01, l_att=2.08, l_ali=1.26, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.87, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.34, y_acc=0.01, l_acc=3.72, d0_v=2.55, y_explo=0.14 |
| 02   | -3470.2229   | 58.80      | y_att=3.11, y_ali=1.81, y_f=1.01, d0_att=3.66, l_att=3.05, l_ali=2.74, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.87, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.22, y_acc=0.63, l_acc=1.27, d0_v=1.75, y_explo=0.30 |
| 03   | -3470.2229   | 58.85      | y_att=3.11, y_ali=1.81, y_f=1.01, d0_att=3.66, l_att=3.05, l_ali=2.74, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.87, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.22, y_acc=0.63, l_acc=1.27, d0_v=1.75, y_explo=0.30 |
| 04   | -3470.2229   | 58.82      | y_att=3.11, y_ali=1.81, y_f=1.01, d0_att=3.66, l_att=3.05, l_ali=2.74, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.87, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.22, y_acc=0.63, l_acc=1.27, d0_v=1.75, y_explo=0.30 |
| 05   | -3470.2229   | 58.89      | y_att=3.11, y_ali=1.81, y_f=1.01, d0_att=3.66, l_att=3.05, l_ali=2.74, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.87, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.22, y_acc=0.63, l_acc=1.27, d0_v=1.75, y_explo=0.30 |
| 06   | -3594.1973   | 58.90      | y_att=2.90, y_ali=8.02, y_f=1.63, d0_att=1.32, l_att=2.89, l_ali=3.42, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.25, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.30, y_acc=0.36, l_acc=1.03, d0_v=0.68, y_explo=0.14 |
| 07   | -3594.1973   | 58.86      | y_att=2.90, y_ali=8.02, y_f=1.63, d0_att=1.32, l_att=2.89, l_ali=3.42, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.25, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.30, y_acc=0.36, l_acc=1.03, d0_v=0.68, y_explo=0.14 |
| 08   | -3735.4819   | 58.82      | y_att=0.74, y_ali=2.05, y_f=0.58, d0_att=2.37, l_att=4.28, l_ali=1.91, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.49, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.19, l_acc=1.21, d0_v=0.94, y_explo=0.13 |
| 09   | -3735.4819   | 58.84      | y_att=0.74, y_ali=2.05, y_f=0.58, d0_att=2.37, l_att=4.28, l_ali=1.91, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.49, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.19, l_acc=1.21, d0_v=0.94, y_explo=0.13 |

**End of experiment.**
