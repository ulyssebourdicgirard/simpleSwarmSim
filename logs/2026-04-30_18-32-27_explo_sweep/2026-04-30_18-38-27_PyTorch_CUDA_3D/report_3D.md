# Experiment Report - PyTorch_CUDA (3D)
**Date:** 2026-04-30_18-38-27

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
| MAP_STRATEGY         | global     |
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
| 00   | -3056.0920   | 49.10      | y_att=1.72, y_ali=3.80, y_f=0.71, d0_att=3.19, l_att=3.80, l_ali=3.75, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.16, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.62, y_acc=0.00, l_acc=0.78, d0_v=1.11, y_explo=0.35 |
| 01   | -3176.2468   | 48.98      | y_att=3.19, y_ali=0.09, y_f=1.94, d0_att=2.55, l_att=7.31, l_ali=2.99, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.51, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.71, y_acc=0.88, l_acc=1.52, d0_v=2.82, y_explo=0.10 |
| 02   | -3422.7993   | 49.02      | y_att=5.10, y_ali=1.68, y_f=1.67, d0_att=3.42, l_att=2.56, l_ali=3.61, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.99, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.96, y_acc=0.54, l_acc=0.65, d0_v=2.59, y_explo=0.10 |
| 03   | -3664.5081   | 49.08      | y_att=0.41, y_ali=3.55, y_f=0.32, d0_att=2.53, l_att=2.33, l_ali=4.44, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.11, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.92, y_acc=0.20, l_acc=1.66, d0_v=2.78, y_explo=0.10 |
| 04   | -3664.5081   | 49.08      | y_att=0.41, y_ali=3.55, y_f=0.32, d0_att=2.53, l_att=2.33, l_ali=4.44, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.11, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.92, y_acc=0.20, l_acc=1.66, d0_v=2.78, y_explo=0.10 |
| 05   | -3679.5256   | 49.09      | y_att=2.00, y_ali=1.97, y_f=0.75, d0_att=7.17, l_att=1.54, l_ali=1.13, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.12, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.31, l_acc=1.33, d0_v=0.94, y_explo=0.12 |
| 06   | -3679.5256   | 49.12      | y_att=2.00, y_ali=1.97, y_f=0.75, d0_att=7.17, l_att=1.54, l_ali=1.13, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.12, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.31, l_acc=1.33, d0_v=0.94, y_explo=0.12 |
| 07   | -3679.5256   | 49.13      | y_att=2.00, y_ali=1.97, y_f=0.75, d0_att=7.17, l_att=1.54, l_ali=1.13, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.12, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.31, l_acc=1.33, d0_v=0.94, y_explo=0.12 |
| 08   | -3679.5256   | 49.15      | y_att=2.00, y_ali=1.97, y_f=0.75, d0_att=7.17, l_att=1.54, l_ali=1.13, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.12, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.31, l_acc=1.33, d0_v=0.94, y_explo=0.12 |
| 09   | -3679.5256   | 49.12      | y_att=2.00, y_ali=1.97, y_f=0.75, d0_att=7.17, l_att=1.54, l_ali=1.13, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.12, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.31, l_acc=1.33, d0_v=0.94, y_explo=0.12 |

**End of experiment.**
