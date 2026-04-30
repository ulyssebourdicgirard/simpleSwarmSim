# Experiment Report - PyTorch_CUDA (3D)
**Date:** 2026-04-30_18-32-30

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
| 00   | -3323.5667   | 26.53      | y_att=0.35, y_ali=1.39, y_f=0.87, d0_att=3.05, l_att=8.08, l_ali=3.61, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.92, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.58, y_acc=0.40, l_acc=0.74, d0_v=2.09, y_explo=0.42 |
| 01   | -3465.5923   | 26.45      | y_att=1.66, y_ali=1.90, y_f=0.98, d0_att=6.62, l_att=1.87, l_ali=3.33, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.29, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.81, y_acc=0.11, l_acc=3.92, d0_v=1.44, y_explo=0.40 |
| 02   | -3494.0090   | 26.50      | y_att=0.82, y_ali=0.62, y_f=1.96, d0_att=3.05, l_att=2.12, l_ali=2.96, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.77, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.17, y_acc=0.25, l_acc=1.26, d0_v=2.84, y_explo=0.56 |
| 03   | -3533.6089   | 26.54      | y_att=0.76, y_ali=1.99, y_f=1.04, d0_att=1.14, l_att=3.46, l_ali=2.25, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.66, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.15, l_acc=1.15, d0_v=0.68, y_explo=0.49 |
| 04   | -3566.8652   | 26.51      | y_att=4.78, y_ali=3.45, y_f=0.62, d0_att=3.71, l_att=1.81, l_ali=1.85, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.55, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.23, y_acc=0.14, l_acc=0.72, d0_v=1.11, y_explo=0.21 |
| 05   | -3652.0020   | 26.57      | y_att=0.10, y_ali=0.16, y_f=1.11, d0_att=2.49, l_att=1.91, l_ali=4.36, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.22, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.37, l_acc=0.26, d0_v=1.36, y_explo=0.18 |
| 06   | -3782.1731   | 26.56      | y_att=1.05, y_ali=1.01, y_f=1.00, d0_att=1.27, l_att=2.86, l_ali=0.12, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.72, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.99, y_acc=0.89, l_acc=0.59, d0_v=1.85, y_explo=0.31 |
| 07   | -3782.1731   | 26.56      | y_att=1.05, y_ali=1.01, y_f=1.00, d0_att=1.27, l_att=2.86, l_ali=0.12, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.72, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.99, y_acc=0.89, l_acc=0.59, d0_v=1.85, y_explo=0.31 |
| 08   | -3782.1731   | 26.57      | y_att=1.05, y_ali=1.01, y_f=1.00, d0_att=1.27, l_att=2.86, l_ali=0.12, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.72, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.99, y_acc=0.89, l_acc=0.59, d0_v=1.85, y_explo=0.31 |
| 09   | -3782.1731   | 26.55      | y_att=1.05, y_ali=1.01, y_f=1.00, d0_att=1.27, l_att=2.86, l_ali=0.12, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.72, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.99, y_acc=0.89, l_acc=0.59, d0_v=1.85, y_explo=0.31 |

**End of experiment.**
