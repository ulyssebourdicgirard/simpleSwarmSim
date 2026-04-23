# Experiment Report - PyTorch_CUDA (2D)
**Date:** 2026-04-23_14-12-47

## 1. Initial Configuration
| Parameter | Value |
| :--- | :--- |
| ALPHA_LPF            | 0.2        |
| ARENA_RADIUS         | 100.0      |
| COLLISION_DIST       | 0.4        |
| DT                   | 0.1        |
| ENABLE_3D            | False      |
| FULL_MILLING_MODE    | True       |
| GEN_CPU              | 20         |
| GEN_GPU              | 20         |
| GRID_RES             | 5.0        |
| MAX_SPEED            | 20.0       |
| MAX_YAW_RATE         | 3.14       |
| NB_DRONES            | 15         |
| NEIGHBORS            | 4          |
| POP_SIZE_CPU         | 150        |
| POP_SIZE_GPU         | 50000      |
| SCENARIO             | default    |
| SIM_STEPS            | 500        |
| SPOIL_ADD            | 0.05       |
| SPOIL_MULT           | 1.01       |
| VISU_STEPS           | 1000       |
| W_COLL               | 0          |
| W_DISP               | 0.0        |
| W_EFFORT             | 1.0        |
| W_EXPLO              | 0.0        |
| W_MILL               | -100.0     |
| W_POL                | 0.0        |
| Z_MAX                | 10.0       |
| Z_MIN                | 1.0        |

## 2. Optimization Evolution
| Gen  |  Best Cost   |  Time (s)  |                                                                All Parameters                                                                |
| :--: | :----------: | :--------: | :------------------------------------------------------------------------------------------------------------------------------------------ |
| 00   | -19616.6914  | 9.32       | y_att=3.21, y_ali=0.70, y_f=1.90, d0_att=1.49, l_att=2.91, l_ali=1.23, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.53, y_acc=1.98, l_acc=0.62, d0_v=0.77 |
| 01   | -37882.5898  | 9.30       | y_att=2.40, y_ali=0.48, y_f=1.80, d0_att=1.00, l_att=2.00, l_ali=3.96, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=1.66, l_acc=0.13, d0_v=0.20 |
| 02   | -38933.6953  | 9.14       | y_att=3.43, y_ali=1.51, y_f=1.94, d0_att=2.27, l_att=2.38, l_ali=4.08, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.03, y_acc=1.40, l_acc=0.33, d0_v=0.57 |
| 03   | -38933.6953  | 9.28       | y_att=3.43, y_ali=1.51, y_f=1.94, d0_att=2.27, l_att=2.38, l_ali=4.08, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.03, y_acc=1.40, l_acc=0.33, d0_v=0.57 |
| 04   | -38933.6953  | 9.00       | y_att=3.43, y_ali=1.51, y_f=1.94, d0_att=2.27, l_att=2.38, l_ali=4.08, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.03, y_acc=1.40, l_acc=0.33, d0_v=0.57 |
| 05   | -38933.6953  | 8.91       | y_att=3.43, y_ali=1.51, y_f=1.94, d0_att=2.27, l_att=2.38, l_ali=4.08, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.03, y_acc=1.40, l_acc=0.33, d0_v=0.57 |
| 06   | -38933.6953  | 9.07       | y_att=3.43, y_ali=1.51, y_f=1.94, d0_att=2.27, l_att=2.38, l_ali=4.08, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.03, y_acc=1.40, l_acc=0.33, d0_v=0.57 |
| 07   | -38933.6953  | 9.12       | y_att=3.43, y_ali=1.51, y_f=1.94, d0_att=2.27, l_att=2.38, l_ali=4.08, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.03, y_acc=1.40, l_acc=0.33, d0_v=0.57 |
| 08   | -38933.6953  | 8.90       | y_att=3.43, y_ali=1.51, y_f=1.94, d0_att=2.27, l_att=2.38, l_ali=4.08, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.03, y_acc=1.40, l_acc=0.33, d0_v=0.57 |
| 09   | -38933.6953  | 8.94       | y_att=3.43, y_ali=1.51, y_f=1.94, d0_att=2.27, l_att=2.38, l_ali=4.08, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.03, y_acc=1.40, l_acc=0.33, d0_v=0.57 |
| 10   | -38933.6953  | 8.74       | y_att=3.43, y_ali=1.51, y_f=1.94, d0_att=2.27, l_att=2.38, l_ali=4.08, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.03, y_acc=1.40, l_acc=0.33, d0_v=0.57 |
| 11   | -38933.6953  | 8.80       | y_att=3.43, y_ali=1.51, y_f=1.94, d0_att=2.27, l_att=2.38, l_ali=4.08, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.03, y_acc=1.40, l_acc=0.33, d0_v=0.57 |
| 12   | -38933.6953  | 8.66       | y_att=3.43, y_ali=1.51, y_f=1.94, d0_att=2.27, l_att=2.38, l_ali=4.08, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.03, y_acc=1.40, l_acc=0.33, d0_v=0.57 |
| 13   | -38933.6953  | 8.64       | y_att=3.43, y_ali=1.51, y_f=1.94, d0_att=2.27, l_att=2.38, l_ali=4.08, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.03, y_acc=1.40, l_acc=0.33, d0_v=0.57 |
| 14   | -38933.6953  | 8.78       | y_att=3.43, y_ali=1.51, y_f=1.94, d0_att=2.27, l_att=2.38, l_ali=4.08, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.03, y_acc=1.40, l_acc=0.33, d0_v=0.57 |
| 15   | -38933.6953  | 8.81       | y_att=3.43, y_ali=1.51, y_f=1.94, d0_att=2.27, l_att=2.38, l_ali=4.08, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.03, y_acc=1.40, l_acc=0.33, d0_v=0.57 |
| 16   | -38933.6953  | 8.88       | y_att=3.43, y_ali=1.51, y_f=1.94, d0_att=2.27, l_att=2.38, l_ali=4.08, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.03, y_acc=1.40, l_acc=0.33, d0_v=0.57 |
| 17   | -38933.6953  | 8.33       | y_att=3.43, y_ali=1.51, y_f=1.94, d0_att=2.27, l_att=2.38, l_ali=4.08, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.03, y_acc=1.40, l_acc=0.33, d0_v=0.57 |
| 18   | -38933.6953  | 8.33       | y_att=3.43, y_ali=1.51, y_f=1.94, d0_att=2.27, l_att=2.38, l_ali=4.08, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.03, y_acc=1.40, l_acc=0.33, d0_v=0.57 |
| 19   | -38933.6953  | 8.15       | y_att=3.43, y_ali=1.51, y_f=1.94, d0_att=2.27, l_att=2.38, l_ali=4.08, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.03, y_acc=1.40, l_acc=0.33, d0_v=0.57 |

**End of experiment.**
