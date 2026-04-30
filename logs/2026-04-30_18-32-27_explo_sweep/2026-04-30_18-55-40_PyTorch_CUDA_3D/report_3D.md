# Experiment Report - PyTorch_CUDA (3D)
**Date:** 2026-04-30_18-55-40

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
| MAP_STRATEGY         | local_individual |
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
| 00   | -3102.3806   | 58.87      | y_att=1.47, y_ali=1.70, y_f=1.62, d0_att=6.58, l_att=8.44, l_ali=2.34, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.17, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.81, y_acc=0.53, l_acc=0.98, d0_v=1.60, y_explo=0.37 |
| 01   | -3155.1396   | 58.74      | y_att=0.95, y_ali=3.47, y_f=1.37, d0_att=1.97, l_att=2.94, l_ali=1.52, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.68, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.26, y_acc=0.61, l_acc=1.31, d0_v=3.17, y_explo=0.29 |
| 02   | -3405.7375   | 58.77      | y_att=4.44, y_ali=2.89, y_f=1.97, d0_att=5.93, l_att=4.89, l_ali=0.48, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.80, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.38, y_acc=1.27, l_acc=1.34, d0_v=1.92, y_explo=0.10 |
| 03   | -3405.7375   | 58.80      | y_att=4.44, y_ali=2.89, y_f=1.97, d0_att=5.93, l_att=4.89, l_ali=0.48, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.80, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.38, y_acc=1.27, l_acc=1.34, d0_v=1.92, y_explo=0.10 |
| 04   | -3440.8022   | 58.83      | y_att=1.31, y_ali=4.81, y_f=0.89, d0_att=1.75, l_att=3.09, l_ali=1.43, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.61, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.44, y_acc=0.33, l_acc=2.70, d0_v=3.47, y_explo=0.31 |
| 05   | -3440.8022   | 58.83      | y_att=1.31, y_ali=4.81, y_f=0.89, d0_att=1.75, l_att=3.09, l_ali=1.43, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.61, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.44, y_acc=0.33, l_acc=2.70, d0_v=3.47, y_explo=0.31 |
| 06   | -3440.8022   | 58.83      | y_att=1.31, y_ali=4.81, y_f=0.89, d0_att=1.75, l_att=3.09, l_ali=1.43, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.61, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.44, y_acc=0.33, l_acc=2.70, d0_v=3.47, y_explo=0.31 |
| 07   | -3467.5640   | 58.81      | y_att=0.99, y_ali=1.40, y_f=1.99, d0_att=1.34, l_att=3.43, l_ali=5.46, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.47, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.45, l_acc=3.93, d0_v=2.61, y_explo=0.12 |
| 08   | -3475.2576   | 58.84      | y_att=0.45, y_ali=1.40, y_f=1.23, d0_att=1.25, l_att=3.08, l_ali=2.25, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.47, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.74, y_acc=0.10, l_acc=1.19, d0_v=1.92, y_explo=0.12 |
| 09   | -3514.3611   | 58.86      | y_att=0.51, y_ali=0.55, y_f=0.43, d0_att=0.50, l_att=2.02, l_ali=2.23, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.39, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.30, l_acc=0.92, d0_v=4.67, y_explo=0.12 |

**End of experiment.**
