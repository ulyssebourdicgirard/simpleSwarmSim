# Experiment Report - PyTorch_CUDA (2D)
**Date:** 2026-05-03_18-48-55

## 1. Initial Configuration
| Parameter | Value |
| :--- | :--- |
| ALPHA_LPF            | 0.2        |
| ARENA_RADIUS         | 50.0       |
| COLLISION_DIST       | 0.4        |
| DT                   | 0.1        |
| ENABLE_3D            | False      |
| EXPLO_STRATEGY       | global_best |
| FOV_FACTOR           | 0.9        |
| FULL_MILLING_MODE    | True       |
| GEN_CPU              | 20         |
| GEN_GPU              | 20         |
| GRID_RES             | 5.0        |
| MAP_STRATEGY         | local_shared |
| MAX_SPEED            | 30.0       |
| MAX_YAW_RATE         | 3.14       |
| MIN_SPAWN_DIST       | 2.0        |
| NB_DRONES            | 5          |
| NEIGHBORS            | 4          |
| N_INIT_CONDITIONS    | 4          |
| POP_SIZE_CPU         | 150        |
| POP_SIZE_GPU         | 5000       |
| REFRESH_MAP_TICKS    | 100        |
| SCENARIO             | default    |
| SIM_STEPS            | 800        |
| SPOIL_ADD            | 0.02       |
| SPOIL_MULT           | 1.002      |
| VISU_STEPS           | 2000       |
| W_COLL               | 1.0        |
| W_DISP               | 20.0       |
| W_EFFORT             | 0.0        |
| W_EXPLO              | 0.0        |
| W_MILL               | -300.0     |
| W_POL                | 0.0        |
| Z_MAX                | 10.0       |
| Z_MIN                | 1.0        |

## 2. Optimization Evolution
| Gen  |  Best Cost   |  Time (s)  |                                                                All Parameters                                                                |
| :--: | :----------: | :--------: | :------------------------------------------------------------------------------------------------------------------------------------------ |
| 00   | 10579.3994   | 3.03       | y_att=4.11, y_ali=1.26, y_f=0.41, d0_att=7.91, l_att=8.17, l_ali=1.84, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.15, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.54, y_acc=0.40, l_acc=2.93, d0_v=0.58, y_explo=4.36 |
| 01   | -8992.0029   | 2.97       | y_att=2.00, y_ali=2.39, y_f=0.22, d0_att=11.44, l_att=7.57, l_ali=2.77, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.44, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.68, y_acc=0.73, l_acc=1.79, d0_v=2.54, y_explo=2.71 |
| 02   | -12008.0830  | 3.14       | y_att=4.72, y_ali=0.17, y_f=1.67, d0_att=9.97, l_att=8.74, l_ali=2.72, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.98, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.21, y_acc=0.77, l_acc=3.42, d0_v=0.72, y_explo=1.46 |
| 03   | -12008.0830  | 3.04       | y_att=4.72, y_ali=0.17, y_f=1.67, d0_att=9.97, l_att=8.74, l_ali=2.72, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.98, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.21, y_acc=0.77, l_acc=3.42, d0_v=0.72, y_explo=1.46 |
| 04   | -12008.0830  | 2.85       | y_att=4.72, y_ali=0.17, y_f=1.67, d0_att=9.97, l_att=8.74, l_ali=2.72, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.98, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.21, y_acc=0.77, l_acc=3.42, d0_v=0.72, y_explo=1.46 |
| 05   | -12008.0830  | 2.85       | y_att=4.72, y_ali=0.17, y_f=1.67, d0_att=9.97, l_att=8.74, l_ali=2.72, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.98, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.21, y_acc=0.77, l_acc=3.42, d0_v=0.72, y_explo=1.46 |
| 06   | -12008.0830  | 2.83       | y_att=4.72, y_ali=0.17, y_f=1.67, d0_att=9.97, l_att=8.74, l_ali=2.72, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.98, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.21, y_acc=0.77, l_acc=3.42, d0_v=0.72, y_explo=1.46 |
| 07   | -28316.6406  | 2.80       | y_att=0.28, y_ali=0.84, y_f=0.40, d0_att=12.04, l_att=17.73, l_ali=3.66, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.11, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.00, l_acc=1.49, d0_v=2.23, y_explo=0.75 |
| 08   | -28316.6406  | 2.80       | y_att=0.28, y_ali=0.84, y_f=0.40, d0_att=12.04, l_att=17.73, l_ali=3.66, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.11, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.00, l_acc=1.49, d0_v=2.23, y_explo=0.75 |
| 09   | -28316.6406  | 3.04       | y_att=0.28, y_ali=0.84, y_f=0.40, d0_att=12.04, l_att=17.73, l_ali=3.66, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.11, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.00, l_acc=1.49, d0_v=2.23, y_explo=0.75 |
| 10   | -28316.6406  | 3.02       | y_att=0.28, y_ali=0.84, y_f=0.40, d0_att=12.04, l_att=17.73, l_ali=3.66, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.11, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.00, l_acc=1.49, d0_v=2.23, y_explo=0.75 |
| 11   | -28316.6406  | 2.95       | y_att=0.28, y_ali=0.84, y_f=0.40, d0_att=12.04, l_att=17.73, l_ali=3.66, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.11, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.00, l_acc=1.49, d0_v=2.23, y_explo=0.75 |
| 12   | -28316.6406  | 2.82       | y_att=0.28, y_ali=0.84, y_f=0.40, d0_att=12.04, l_att=17.73, l_ali=3.66, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.11, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.00, l_acc=1.49, d0_v=2.23, y_explo=0.75 |
| 13   | -41108.6250  | 2.90       | y_att=0.24, y_ali=0.48, y_f=0.94, d0_att=21.42, l_att=7.58, l_ali=3.71, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.16, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.91, y_acc=0.01, l_acc=1.32, d0_v=2.10, y_explo=1.76 |
| 14   | -41108.6250  | 2.91       | y_att=0.24, y_ali=0.48, y_f=0.94, d0_att=21.42, l_att=7.58, l_ali=3.71, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.16, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.91, y_acc=0.01, l_acc=1.32, d0_v=2.10, y_explo=1.76 |
| 15   | -41108.6250  | 2.81       | y_att=0.24, y_ali=0.48, y_f=0.94, d0_att=21.42, l_att=7.58, l_ali=3.71, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.16, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.91, y_acc=0.01, l_acc=1.32, d0_v=2.10, y_explo=1.76 |
| 16   | -41108.6250  | 2.84       | y_att=0.24, y_ali=0.48, y_f=0.94, d0_att=21.42, l_att=7.58, l_ali=3.71, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.16, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.91, y_acc=0.01, l_acc=1.32, d0_v=2.10, y_explo=1.76 |
| 17   | -41108.6250  | 2.85       | y_att=0.24, y_ali=0.48, y_f=0.94, d0_att=21.42, l_att=7.58, l_ali=3.71, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.16, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.91, y_acc=0.01, l_acc=1.32, d0_v=2.10, y_explo=1.76 |
| 18   | -41108.6250  | 3.12       | y_att=0.24, y_ali=0.48, y_f=0.94, d0_att=21.42, l_att=7.58, l_ali=3.71, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.16, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.91, y_acc=0.01, l_acc=1.32, d0_v=2.10, y_explo=1.76 |
| 19   | -41108.6250  | 3.01       | y_att=0.24, y_ali=0.48, y_f=0.94, d0_att=21.42, l_att=7.58, l_ali=3.71, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.16, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.91, y_acc=0.01, l_acc=1.32, d0_v=2.10, y_explo=1.76 |

**End of experiment.**
