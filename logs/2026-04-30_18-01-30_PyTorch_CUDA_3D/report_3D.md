# Experiment Report - PyTorch_CUDA (3D)
**Date:** 2026-04-30_18-01-30

## 1. Initial Configuration
| Parameter | Value |
| :--- | :--- |
| ALPHA_LPF            | 0.2        |
| ARENA_RADIUS         | 100.0      |
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
| NB_DRONES            | 5          |
| NEIGHBORS            | 2          |
| N_INIT_CONDITIONS    | 4          |
| POP_SIZE_CPU         | 150        |
| POP_SIZE_GPU         | 250        |
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
| 00   | -2287.8230   | 6.22       | y_att=2.86, y_ali=0.89, y_f=1.28, d0_att=2.19, l_att=4.80, l_ali=2.07, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.41, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.06, y_acc=1.42, l_acc=0.51, d0_v=2.46, y_explo=0.02 |
| 01   | -2387.0317   | 5.94       | y_att=2.28, y_ali=3.78, y_f=1.87, d0_att=3.69, l_att=1.11, l_ali=5.10, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.04, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.10, y_acc=0.29, l_acc=2.89, d0_v=2.86, y_explo=0.21 |
| 02   | -2646.5962   | 5.97       | y_att=2.28, y_ali=3.78, y_f=1.56, d0_att=3.69, l_att=3.02, l_ali=5.10, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.29, l_acc=0.98, d0_v=1.20, y_explo=0.21 |
| 03   | -2646.5962   | 5.97       | y_att=2.28, y_ali=3.78, y_f=1.56, d0_att=3.69, l_att=3.02, l_ali=5.10, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.29, l_acc=0.98, d0_v=1.20, y_explo=0.21 |
| 04   | -2646.5962   | 6.00       | y_att=2.28, y_ali=3.78, y_f=1.56, d0_att=3.69, l_att=3.02, l_ali=5.10, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.29, l_acc=0.98, d0_v=1.20, y_explo=0.21 |
| 05   | -2646.5962   | 6.05       | y_att=2.28, y_ali=3.78, y_f=1.56, d0_att=3.69, l_att=3.02, l_ali=5.10, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.29, l_acc=0.98, d0_v=1.20, y_explo=0.21 |
| 06   | -2646.5962   | 6.05       | y_att=2.28, y_ali=3.78, y_f=1.56, d0_att=3.69, l_att=3.02, l_ali=5.10, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.29, l_acc=0.98, d0_v=1.20, y_explo=0.21 |
| 07   | -2772.1836   | 6.07       | y_att=0.74, y_ali=1.51, y_f=1.94, d0_att=2.88, l_att=5.38, l_ali=5.67, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.69, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.86, y_acc=0.30, l_acc=2.16, d0_v=0.84, y_explo=0.15 |
| 08   | -2772.1836   | 6.10       | y_att=0.74, y_ali=1.51, y_f=1.94, d0_att=2.88, l_att=5.38, l_ali=5.67, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.69, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.86, y_acc=0.30, l_acc=2.16, d0_v=0.84, y_explo=0.15 |
| 09   | -2772.1836   | 6.08       | y_att=0.74, y_ali=1.51, y_f=1.94, d0_att=2.88, l_att=5.38, l_ali=5.67, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.69, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.86, y_acc=0.30, l_acc=2.16, d0_v=0.84, y_explo=0.15 |

**End of experiment.**
