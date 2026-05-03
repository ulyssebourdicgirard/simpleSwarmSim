# Experiment Report - PyTorch_CUDA (3D)
**Date:** 2026-05-03_17-55-58

## 1. Initial Configuration
| Parameter | Value |
| :--- | :--- |
| ALPHA_LPF            | 0.2        |
| ARENA_RADIUS         | 50.0       |
| COLLISION_DIST       | 0.4        |
| DT                   | 0.1        |
| ENABLE_3D            | True       |
| EXPLO_STRATEGY       | global_best |
| FOV_FACTOR           | 0.9        |
| FULL_MILLING_MODE    | True       |
| GEN_CPU              | 20         |
| GEN_GPU              | 10         |
| GRID_RES             | 5.0        |
| MAP_STRATEGY         | local_shared |
| MAX_SPEED            | 30.0       |
| MAX_YAW_RATE         | 3.14       |
| MIN_SPAWN_DIST       | 2.0        |
| NB_DRONES            | 30         |
| NEIGHBORS            | 2          |
| N_INIT_CONDITIONS    | 4          |
| POP_SIZE_CPU         | 150        |
| POP_SIZE_GPU         | 500        |
| REFRESH_MAP_TICKS    | 100        |
| SCENARIO             | default    |
| SIM_STEPS            | 800        |
| SPOIL_ADD            | 0.02       |
| SPOIL_MULT           | 1.002      |
| VISU_STEPS           | 2000       |
| W_COLL               | 10.0       |
| W_DISP               | 0.0        |
| W_EFFORT             | 1.0        |
| W_EXPLO              | 0.0        |
| W_MILL               | -30.0      |
| W_POL                | 0.0        |
| Z_MAX                | 10.0       |
| Z_MIN                | 1.0        |

## 2. Optimization Evolution
| Gen  |  Best Cost   |  Time (s)  |                                                                All Parameters                                                                |
| :--: | :----------: | :--------: | :------------------------------------------------------------------------------------------------------------------------------------------ |
| 00   | -197.4055    | 5.27       | y_att=1.40, y_ali=2.98, y_f=1.47, d0_att=7.41, l_att=5.68, l_ali=3.50, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.39, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.59, y_acc=0.56, l_acc=3.89, d0_v=2.49, y_explo=3.20 |
| 01   | -1227.9066   | 4.35       | y_att=0.10, y_ali=2.60, y_f=1.32, d0_att=3.13, l_att=11.00, l_ali=3.90, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.84, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.21, y_acc=0.25, l_acc=1.10, d0_v=1.51, y_explo=0.45 |
| 02   | -1227.9066   | 4.31       | y_att=0.10, y_ali=2.60, y_f=1.32, d0_att=3.13, l_att=11.00, l_ali=3.90, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.84, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.21, y_acc=0.25, l_acc=1.10, d0_v=1.51, y_explo=0.45 |
| 03   | -1227.9066   | 4.97       | y_att=0.10, y_ali=2.60, y_f=1.32, d0_att=3.13, l_att=11.00, l_ali=3.90, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.84, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.21, y_acc=0.25, l_acc=1.10, d0_v=1.51, y_explo=0.45 |
| 04   | -1227.9066   | 4.34       | y_att=0.10, y_ali=2.60, y_f=1.32, d0_att=3.13, l_att=11.00, l_ali=3.90, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.84, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.21, y_acc=0.25, l_acc=1.10, d0_v=1.51, y_explo=0.45 |
| 05   | -1227.9066   | 4.28       | y_att=0.10, y_ali=2.60, y_f=1.32, d0_att=3.13, l_att=11.00, l_ali=3.90, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.84, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.21, y_acc=0.25, l_acc=1.10, d0_v=1.51, y_explo=0.45 |
| 06   | -1227.9066   | 5.29       | y_att=0.10, y_ali=2.60, y_f=1.32, d0_att=3.13, l_att=11.00, l_ali=3.90, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.84, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.21, y_acc=0.25, l_acc=1.10, d0_v=1.51, y_explo=0.45 |
| 07   | -1653.3512   | 4.23       | y_att=0.10, y_ali=2.54, y_f=1.45, d0_att=1.91, l_att=7.86, l_ali=4.49, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.45, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.32, y_acc=0.12, l_acc=1.97, d0_v=0.72, y_explo=1.31 |
| 08   | -1653.3512   | 4.21       | y_att=0.10, y_ali=2.54, y_f=1.45, d0_att=1.91, l_att=7.86, l_ali=4.49, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.45, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.32, y_acc=0.12, l_acc=1.97, d0_v=0.72, y_explo=1.31 |
| 09   | -1653.3512   | 4.96       | y_att=0.10, y_ali=2.54, y_f=1.45, d0_att=1.91, l_att=7.86, l_ali=4.49, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.45, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.32, y_acc=0.12, l_acc=1.97, d0_v=0.72, y_explo=1.31 |

**End of experiment.**
