# Experiment Report - PyTorch_MULTI_2xGPU (2D)
**Date:** 2026-05-04_00-11-49

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
| MAP_STRATEGY         | local_individual |
| MAX_SPEED            | 20.0       |
| MAX_YAW_RATE         | 3.14       |
| MIN_SPAWN_DIST       | 2.0        |
| NB_DRONES            | 10         |
| NEIGHBORS            | 2          |
| N_INIT_CONDITIONS    | 4          |
| POP_SIZE_CPU         | 150        |
| POP_SIZE_GPU         | 5000       |
| REFRESH_MAP_TICKS    | 100        |
| SCENARIO             | default    |
| SIM_STEPS            | 3000       |
| SPOIL_ADD            | 0.02       |
| SPOIL_MULT           | 1.002      |
| VISU_STEPS           | 6000       |
| W_COLL               | 10.0       |
| W_DISP               | 2.0        |
| W_EFFORT             | 0.5        |
| W_EXPLO              | 0.0        |
| W_MILL               | -300.0     |
| W_POL                | 0.0        |
| Z_MAX                | 10.0       |
| Z_MIN                | 1.0        |

## 2. Optimization Evolution
| Gen  |  Best Cost   |  Time (s)  |                                                                All Parameters                                                                |
| :--: | :----------: | :--------: | :------------------------------------------------------------------------------------------------------------------------------------------ |
| 00   | -169689.7969 | 7.20       | y_att=0.02, y_ali=0.46, y_f=1.51, d0_att=3.49, l_att=5.14, l_ali=4.01, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.82, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.09, y_acc=0.01, l_acc=2.71, d0_v=2.92, y_explo=0.34 |
| 01   | -169689.7969 | 6.88       | y_att=0.02, y_ali=0.46, y_f=1.51, d0_att=3.49, l_att=5.14, l_ali=4.01, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.82, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.09, y_acc=0.01, l_acc=2.71, d0_v=2.92, y_explo=0.34 |
| 02   | -169689.7969 | 6.99       | y_att=0.02, y_ali=0.46, y_f=1.51, d0_att=3.49, l_att=5.14, l_ali=4.01, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.82, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.09, y_acc=0.01, l_acc=2.71, d0_v=2.92, y_explo=0.34 |
| 03   | -225313.8281 | 6.91       | y_att=0.13, y_ali=1.73, y_f=2.46, d0_att=6.73, l_att=2.52, l_ali=3.66, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.75, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.66, y_acc=0.05, l_acc=1.36, d0_v=0.80, y_explo=2.93 |
| 04   | -250378.1094 | 6.90       | y_att=0.13, y_ali=1.73, y_f=2.46, d0_att=6.73, l_att=2.52, l_ali=3.66, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.82, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.66, y_acc=0.05, l_acc=1.36, d0_v=0.80, y_explo=2.93 |
| 05   | -250378.1094 | 6.90       | y_att=0.13, y_ali=1.73, y_f=2.46, d0_att=6.73, l_att=2.52, l_ali=3.66, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.82, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.66, y_acc=0.05, l_acc=1.36, d0_v=0.80, y_explo=2.93 |
| 06   | -282657.8438 | 6.89       | y_att=1.29, y_ali=2.13, y_f=1.93, d0_att=9.39, l_att=0.70, l_ali=3.34, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.25, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.76, y_acc=0.05, l_acc=0.98, d0_v=0.54, y_explo=4.12 |
| 07   | -288675.0938 | 6.88       | y_att=0.32, y_ali=2.76, y_f=1.70, d0_att=5.75, l_att=0.70, l_ali=3.39, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.30, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.15, y_acc=0.05, l_acc=0.58, d0_v=0.54, y_explo=3.15 |
| 08   | -316256.2500 | 6.91       | y_att=0.11, y_ali=1.34, y_f=1.75, d0_att=3.80, l_att=6.38, l_ali=11.81, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.77, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.65, y_acc=0.02, l_acc=0.56, d0_v=2.20, y_explo=0.15 |
| 09   | -352446.2812 | 6.87       | y_att=0.10, y_ali=1.06, y_f=1.20, d0_att=3.68, l_att=2.21, l_ali=10.92, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.26, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.46, y_acc=0.00, l_acc=1.32, d0_v=4.09, y_explo=3.39 |
| 10   | -573400.1875 | 6.92       | y_att=0.30, y_ali=1.28, y_f=0.72, d0_att=6.22, l_att=3.87, l_ali=36.08, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.48, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.30, y_acc=0.08, l_acc=0.73, d0_v=2.65, y_explo=0.14 |
| 11   | -573400.1875 | 6.92       | y_att=0.30, y_ali=1.28, y_f=0.72, d0_att=6.22, l_att=3.87, l_ali=36.08, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.48, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.30, y_acc=0.08, l_acc=0.73, d0_v=2.65, y_explo=0.14 |
| 12   | -573400.1875 | 6.92       | y_att=0.30, y_ali=1.28, y_f=0.72, d0_att=6.22, l_att=3.87, l_ali=36.08, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.48, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.30, y_acc=0.08, l_acc=0.73, d0_v=2.65, y_explo=0.14 |
| 13   | -573400.1875 | 6.90       | y_att=0.30, y_ali=1.28, y_f=0.72, d0_att=6.22, l_att=3.87, l_ali=36.08, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.48, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.30, y_acc=0.08, l_acc=0.73, d0_v=2.65, y_explo=0.14 |
| 14   | -573400.1875 | 6.91       | y_att=0.30, y_ali=1.28, y_f=0.72, d0_att=6.22, l_att=3.87, l_ali=36.08, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.48, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.30, y_acc=0.08, l_acc=0.73, d0_v=2.65, y_explo=0.14 |
| 15   | -573400.1875 | 6.91       | y_att=0.30, y_ali=1.28, y_f=0.72, d0_att=6.22, l_att=3.87, l_ali=36.08, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.48, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.30, y_acc=0.08, l_acc=0.73, d0_v=2.65, y_explo=0.14 |
| 16   | -573400.1875 | 6.90       | y_att=0.30, y_ali=1.28, y_f=0.72, d0_att=6.22, l_att=3.87, l_ali=36.08, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.48, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.30, y_acc=0.08, l_acc=0.73, d0_v=2.65, y_explo=0.14 |
| 17   | -578034.6875 | 6.89       | y_att=0.13, y_ali=1.33, y_f=0.78, d0_att=3.40, l_att=0.32, l_ali=27.25, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.99, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.17, y_acc=0.10, l_acc=0.44, d0_v=2.74, y_explo=4.35 |
| 18   | -578034.6875 | 6.89       | y_att=0.13, y_ali=1.33, y_f=0.78, d0_att=3.40, l_att=0.32, l_ali=27.25, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.99, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.17, y_acc=0.10, l_acc=0.44, d0_v=2.74, y_explo=4.35 |
| 19   | -578034.6875 | 6.89       | y_att=0.13, y_ali=1.33, y_f=0.78, d0_att=3.40, l_att=0.32, l_ali=27.25, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.99, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.17, y_acc=0.10, l_acc=0.44, d0_v=2.74, y_explo=4.35 |

**End of experiment.**
