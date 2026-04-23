# Experiment Report - PyTorch_CUDA (2D)
**Date:** 2026-04-23_14-10-10

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
| NB_DRONES            | 10         |
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
| 00   | -34471.1484  | 3.63       | y_att=1.83, y_ali=1.16, y_f=1.97, d0_att=1.84, l_att=3.42, l_ali=1.09, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.27, y_acc=1.62, l_acc=1.39, d0_v=2.37 |
| 01   | -34942.6836  | 4.19       | y_att=1.19, y_ali=3.23, y_f=2.92, d0_att=1.38, l_att=4.60, l_ali=1.63, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.61, y_acc=0.54, l_acc=3.90, d0_v=1.15 |
| 02   | -35057.3086  | 3.41       | y_att=3.24, y_ali=2.12, y_f=3.48, d0_att=2.38, l_att=3.80, l_ali=2.61, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.80, y_acc=1.38, l_acc=1.87, d0_v=1.50 |
| 03   | -35143.4414  | 3.31       | y_att=1.73, y_ali=1.44, y_f=3.77, d0_att=0.71, l_att=2.46, l_ali=3.02, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.11, y_acc=1.33, l_acc=1.76, d0_v=2.43 |
| 04   | -35319.6953  | 4.03       | y_att=2.91, y_ali=1.59, y_f=4.86, d0_att=1.21, l_att=3.54, l_ali=3.31, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.57, y_acc=2.36, l_acc=2.75, d0_v=2.19 |
| 05   | -35319.6953  | 3.37       | y_att=2.91, y_ali=1.59, y_f=4.86, d0_att=1.21, l_att=3.54, l_ali=3.31, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.57, y_acc=2.36, l_acc=2.75, d0_v=2.19 |
| 06   | -35428.6875  | 3.30       | y_att=2.01, y_ali=4.25, y_f=9.89, d0_att=1.56, l_att=4.34, l_ali=3.02, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.96, y_acc=1.04, l_acc=0.83, d0_v=0.72 |
| 07   | -35428.6875  | 3.30       | y_att=2.01, y_ali=4.25, y_f=9.89, d0_att=1.56, l_att=4.34, l_ali=3.02, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.96, y_acc=1.04, l_acc=0.83, d0_v=0.72 |
| 08   | -35470.8984  | 4.05       | y_att=1.80, y_ali=4.25, y_f=11.24, d0_att=1.41, l_att=6.85, l_ali=2.55, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.98, y_acc=1.35, l_acc=2.31, d0_v=0.68 |
| 09   | -35643.7539  | 3.47       | y_att=2.18, y_ali=0.24, y_f=11.24, d0_att=1.74, l_att=6.85, l_ali=2.86, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=1.35, l_acc=2.31, d0_v=0.56 |
| 10   | -35643.7539  | 3.39       | y_att=2.18, y_ali=0.24, y_f=11.24, d0_att=1.74, l_att=6.85, l_ali=2.86, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=1.35, l_acc=2.31, d0_v=0.56 |
| 11   | -35643.7539  | 3.35       | y_att=2.18, y_ali=0.24, y_f=11.24, d0_att=1.74, l_att=6.85, l_ali=2.86, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=1.35, l_acc=2.31, d0_v=0.56 |
| 12   | -35683.6836  | 4.20       | y_att=5.34, y_ali=3.80, y_f=13.40, d0_att=1.33, l_att=3.19, l_ali=3.74, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.31, y_acc=1.07, l_acc=1.17, d0_v=0.50 |
| 13   | -35683.6836  | 3.39       | y_att=5.34, y_ali=3.80, y_f=13.40, d0_att=1.33, l_att=3.19, l_ali=3.74, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.31, y_acc=1.07, l_acc=1.17, d0_v=0.50 |
| 14   | -35683.6836  | 3.36       | y_att=5.34, y_ali=3.80, y_f=13.40, d0_att=1.33, l_att=3.19, l_ali=3.74, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.31, y_acc=1.07, l_acc=1.17, d0_v=0.50 |
| 15   | -35710.1836  | 4.10       | y_att=4.94, y_ali=3.21, y_f=14.36, d0_att=1.26, l_att=4.72, l_ali=3.85, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.50, y_acc=2.33, l_acc=1.17, d0_v=0.22 |
| 16   | -35710.1836  | 3.37       | y_att=4.94, y_ali=3.21, y_f=14.36, d0_att=1.26, l_att=4.72, l_ali=3.85, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.50, y_acc=2.33, l_acc=1.17, d0_v=0.22 |
| 17   | -35710.1836  | 3.36       | y_att=4.94, y_ali=3.21, y_f=14.36, d0_att=1.26, l_att=4.72, l_ali=3.85, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.50, y_acc=2.33, l_acc=1.17, d0_v=0.22 |
| 18   | -35766.1641  | 3.35       | y_att=4.94, y_ali=1.85, y_f=14.36, d0_att=1.26, l_att=4.08, l_ali=3.85, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.73, y_acc=2.33, l_acc=1.17, d0_v=0.45 |
| 19   | -35766.1641  | 4.22       | y_att=4.94, y_ali=1.85, y_f=14.36, d0_att=1.26, l_att=4.08, l_ali=3.85, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.73, y_acc=2.33, l_acc=1.17, d0_v=0.45 |

**End of experiment.**
