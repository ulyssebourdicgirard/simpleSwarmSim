# Experiment Report - PyTorch_CUDA (3D)
**Date:** 2026-05-03_17-50-02

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
| NB_DRONES            | 15         |
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
| 00   | -1838.1553   | 4.30       | y_att=1.58, y_ali=3.61, y_f=1.93, d0_att=4.45, l_att=5.14, l_ali=4.11, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.78, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.51, y_acc=0.97, l_acc=2.54, d0_v=2.34, y_explo=2.71 |
| 01   | -2024.5585   | 5.46       | y_att=0.35, y_ali=2.83, y_f=1.83, d0_att=1.32, l_att=8.48, l_ali=4.51, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.73, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.64, y_acc=1.18, l_acc=2.44, d0_v=1.10, y_explo=2.76 |
| 02   | -2075.4226   | 4.36       | y_att=1.45, y_ali=2.38, y_f=1.67, d0_att=1.14, l_att=1.46, l_ali=4.60, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.57, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.61, y_acc=0.38, l_acc=2.45, d0_v=0.85, y_explo=2.49 |
| 03   | -2859.5039   | 4.38       | y_att=0.29, y_ali=2.73, y_f=1.39, d0_att=3.17, l_att=2.56, l_ali=3.79, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.62, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=1.16, l_acc=1.85, d0_v=4.07, y_explo=3.82 |
| 04   | -2859.5039   | 5.78       | y_att=0.29, y_ali=2.73, y_f=1.39, d0_att=3.17, l_att=2.56, l_ali=3.79, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.62, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=1.16, l_acc=1.85, d0_v=4.07, y_explo=3.82 |
| 05   | -3189.6072   | 4.26       | y_att=0.20, y_ali=1.51, y_f=1.30, d0_att=1.04, l_att=5.55, l_ali=2.62, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.67, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.00, y_acc=0.54, l_acc=2.35, d0_v=0.85, y_explo=2.85 |
| 06   | -3278.9158   | 5.40       | y_att=0.96, y_ali=1.90, y_f=2.87, d0_att=5.37, l_att=0.80, l_ali=5.00, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.67, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.25, y_acc=0.55, l_acc=1.63, d0_v=1.80, y_explo=0.10 |
| 07   | -3278.9158   | 4.37       | y_att=0.96, y_ali=1.90, y_f=2.87, d0_att=5.37, l_att=0.80, l_ali=5.00, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.67, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.25, y_acc=0.55, l_acc=1.63, d0_v=1.80, y_explo=0.10 |
| 08   | -3278.9158   | 4.17       | y_att=0.96, y_ali=1.90, y_f=2.87, d0_att=5.37, l_att=0.80, l_ali=5.00, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.67, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.25, y_acc=0.55, l_acc=1.63, d0_v=1.80, y_explo=0.10 |
| 09   | -5623.7817   | 5.24       | y_att=0.14, y_ali=1.38, y_f=1.54, d0_att=3.47, l_att=3.68, l_ali=8.49, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.85, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.86, y_acc=0.33, l_acc=0.29, d0_v=0.54, y_explo=0.59 |

**End of experiment.**
