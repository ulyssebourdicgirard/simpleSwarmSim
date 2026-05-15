# Experiment Report - PyTorch_CUDA (2D)
**Date:** 2026-05-14_13-55-26

## 1. Initial Configuration
| Parameter | Value |
| :--- | :--- |
| ALPHA_LPF            | 0.2        |
| ARENA_RADIUS         | 50.0       |
| COLLISION_DIST       | 0.4        |
| DT                   | 0.1        |
| ENABLE_3D            | False      |
| EVAL_STRATEGY        | average    |
| EXPLO_STRATEGY       | global_best |
| FOV_FACTOR           | 0.9        |
| FULL_MILLING_MODE    | True       |
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
| POP_SIZE_GPU         | 5000       |
| REFRESH_MAP_TICKS    | 100        |
| SCENARIO             | default    |
| SIM_STEPS            | 400        |
| SPOIL_ADD            | 0.02       |
| SPOIL_MULT           | 1.002      |
| VISU_STEPS           | 800        |
| W_COLL               | 0          |
| W_DISP               | 0          |
| W_EFFORT             | 0          |
| W_EXPLO              | 0.0        |
| W_MILL               | -600.0     |
| W_POL                | 0          |
| W_STATIONARY         | 0          |
| Z_MAX                | 10.0       |
| Z_MIN                | 1.0        |

## 2. Optimization Evolution
| Gen  |  Best Cost   |  Time (s)  |                                                                All Parameters                                                                |
| :--: | :----------: | :--------: | :------------------------------------------------------------------------------------------------------------------------------------------ |
| 00   | -85041.2969  | 1.79       | y_att=1.63, y_ali=2.61, y_f=1.46, d0_att=5.85, l_att=4.06, l_ali=1.89, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.79, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.02, y_acc=0.08, l_acc=1.11, d0_v=2.26, y_explo=4.37 |
| 01   | -117004.4922 | 1.60       | y_att=0.51, y_ali=0.47, y_f=0.94, d0_att=6.56, l_att=5.33, l_ali=4.03, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.96, y_acc=0.00, l_acc=2.36, d0_v=0.87, y_explo=1.43 |
| 02   | -117004.4922 | 2.44       | y_att=0.51, y_ali=0.47, y_f=0.94, d0_att=6.56, l_att=5.33, l_ali=4.03, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.96, y_acc=0.00, l_acc=2.36, d0_v=0.87, y_explo=1.43 |
| 03   | -117004.4922 | 1.51       | y_att=0.51, y_ali=0.47, y_f=0.94, d0_att=6.56, l_att=5.33, l_ali=4.03, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.96, y_acc=0.00, l_acc=2.36, d0_v=0.87, y_explo=1.43 |
| 04   | -117004.4922 | 1.60       | y_att=0.51, y_ali=0.47, y_f=0.94, d0_att=6.56, l_att=5.33, l_ali=4.03, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.96, y_acc=0.00, l_acc=2.36, d0_v=0.87, y_explo=1.43 |
| 05   | -141046.6406 | 1.58       | y_att=0.39, y_ali=1.10, y_f=7.19, d0_att=13.49, l_att=11.74, l_ali=2.39, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.53, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.29, y_acc=0.12, l_acc=4.01, d0_v=1.92, y_explo=0.19 |
| 06   | -141046.6406 | 1.52       | y_att=0.39, y_ali=1.10, y_f=7.19, d0_att=13.49, l_att=11.74, l_ali=2.39, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.53, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.29, y_acc=0.12, l_acc=4.01, d0_v=1.92, y_explo=0.19 |
| 07   | -147876.9219 | 1.55       | y_att=14.50, y_ali=4.76, y_f=10.88, d0_att=16.27, l_att=15.94, l_ali=1.72, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.10, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.96, y_acc=1.18, l_acc=0.92, d0_v=3.58, y_explo=1.54 |
| 08   | -153805.9688 | 1.56       | y_att=13.61, y_ali=1.26, y_f=7.96, d0_att=21.29, l_att=6.47, l_ali=3.00, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.42, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.94, y_acc=0.34, l_acc=2.26, d0_v=2.60, y_explo=0.81 |
| 09   | -153805.9688 | 1.76       | y_att=13.61, y_ali=1.26, y_f=7.96, d0_att=21.29, l_att=6.47, l_ali=3.00, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.42, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.94, y_acc=0.34, l_acc=2.26, d0_v=2.60, y_explo=0.81 |

**End of experiment.**
