# Experiment Report - PyTorch_CUDA (3D)
**Date:** 2026-04-30_19-07-03

## 1. Initial Configuration
| Parameter | Value |
| :--- | :--- |
| ALPHA_LPF            | 0.2        |
| ARENA_RADIUS         | 120.0      |
| COLLISION_DIST       | 0.4        |
| DT                   | 0.1        |
| ENABLE_3D            | True       |
| EXPLO_STRATEGY       | local_gradient |
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
| 00   | -3431.9138   | 36.24      | y_att=2.81, y_ali=1.59, y_f=1.04, d0_att=6.86, l_att=4.53, l_ali=4.05, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.40, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.77, y_acc=0.53, l_acc=1.71, d0_v=2.93, y_explo=0.21 |
| 01   | -3431.9138   | 36.13      | y_att=2.81, y_ali=1.59, y_f=1.04, d0_att=6.86, l_att=4.53, l_ali=4.05, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.40, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.77, y_acc=0.53, l_acc=1.71, d0_v=2.93, y_explo=0.21 |
| 02   | -3431.9138   | 36.15      | y_att=2.81, y_ali=1.59, y_f=1.04, d0_att=6.86, l_att=4.53, l_ali=4.05, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.40, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.77, y_acc=0.53, l_acc=1.71, d0_v=2.93, y_explo=0.21 |
| 03   | -3457.7979   | 36.17      | y_att=0.10, y_ali=1.08, y_f=0.93, d0_att=3.46, l_att=8.66, l_ali=0.92, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.47, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.71, y_acc=0.09, l_acc=0.71, d0_v=0.94, y_explo=0.10 |
| 04   | -3457.7979   | 36.17      | y_att=0.10, y_ali=1.08, y_f=0.93, d0_att=3.46, l_att=8.66, l_ali=0.92, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.47, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.71, y_acc=0.09, l_acc=0.71, d0_v=0.94, y_explo=0.10 |
| 05   | -3457.7979   | 36.18      | y_att=0.10, y_ali=1.08, y_f=0.93, d0_att=3.46, l_att=8.66, l_ali=0.92, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.47, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.71, y_acc=0.09, l_acc=0.71, d0_v=0.94, y_explo=0.10 |
| 06   | -3457.7979   | 36.09      | y_att=0.10, y_ali=1.08, y_f=0.93, d0_att=3.46, l_att=8.66, l_ali=0.92, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.47, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.71, y_acc=0.09, l_acc=0.71, d0_v=0.94, y_explo=0.10 |
| 07   | -3458.1602   | 36.08      | y_att=0.15, y_ali=0.68, y_f=1.35, d0_att=2.47, l_att=3.71, l_ali=1.86, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.35, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.81, y_acc=0.03, l_acc=0.26, d0_v=1.38, y_explo=0.21 |
| 08   | -3462.9570   | 36.06      | y_att=2.75, y_ali=1.52, y_f=1.13, d0_att=1.03, l_att=1.21, l_ali=2.10, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.13, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.93, y_acc=0.15, l_acc=0.42, d0_v=2.14, y_explo=0.14 |
| 09   | -3480.4072   | 36.03      | y_att=0.80, y_ali=1.94, y_f=2.09, d0_att=1.42, l_att=1.89, l_ali=0.82, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.67, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.09, l_acc=0.78, d0_v=1.59, y_explo=0.10 |

**End of experiment.**
