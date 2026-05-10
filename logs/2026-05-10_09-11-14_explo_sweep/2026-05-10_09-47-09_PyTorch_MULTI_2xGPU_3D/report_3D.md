# Experiment Report - PyTorch_MULTI_2xGPU (3D)
**Date:** 2026-05-10_09-47-09

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
| FULL_MILLING_MODE    | False      |
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
| SCENARIO             | exploration |
| SIM_STEPS            | 3000       |
| SPOIL_ADD            | 0.02       |
| SPOIL_MULT           | 1.002      |
| VISU_STEPS           | 6000       |
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
| 00   | -121514.2266 | 44.40      | y_att=0.34, y_ali=0.57, y_f=0.00, d0_att=2.46, l_att=4.96, l_ali=2.28, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.72, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.95, y_acc=1.77, l_acc=2.69, d0_v=2.34, y_explo=4.90 |
| 01   | -124767.1094 | 44.18      | y_att=3.46, y_ali=0.70, y_f=0.10, d0_att=1.29, l_att=2.38, l_ali=4.55, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.76, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.91, y_acc=0.63, l_acc=0.66, d0_v=2.06, y_explo=0.90 |
| 02   | -124767.1094 | 44.18      | y_att=3.46, y_ali=0.70, y_f=0.10, d0_att=1.29, l_att=2.38, l_ali=4.55, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.76, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.91, y_acc=0.63, l_acc=0.66, d0_v=2.06, y_explo=0.90 |
| 03   | -131035.9453 | 44.16      | y_att=6.28, y_ali=1.26, y_f=0.19, d0_att=1.05, l_att=1.26, l_ali=1.93, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.23, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.21, l_acc=1.26, d0_v=1.76, y_explo=0.15 |
| 04   | -131035.9453 | 44.16      | y_att=6.28, y_ali=1.26, y_f=0.19, d0_att=1.05, l_att=1.26, l_ali=1.93, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.23, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.21, l_acc=1.26, d0_v=1.76, y_explo=0.15 |
| 05   | -132099.4062 | 44.15      | y_att=0.96, y_ali=0.28, y_f=0.10, d0_att=0.83, l_att=3.90, l_ali=3.36, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.09, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=1.90, l_acc=2.61, d0_v=2.93, y_explo=0.11 |
| 06   | -133517.2969 | 44.15      | y_att=0.60, y_ali=0.18, y_f=0.14, d0_att=1.07, l_att=6.24, l_ali=4.44, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.68, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.86, l_acc=0.97, d0_v=1.08, y_explo=0.10 |
| 07   | -133517.2969 | 44.14      | y_att=0.60, y_ali=0.18, y_f=0.14, d0_att=1.07, l_att=6.24, l_ali=4.44, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.68, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.86, l_acc=0.97, d0_v=1.08, y_explo=0.10 |
| 08   | -134476.8438 | 44.14      | y_att=2.27, y_ali=1.53, y_f=0.12, d0_att=1.04, l_att=3.16, l_ali=2.28, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.92, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.63, l_acc=0.98, d0_v=0.81, y_explo=0.10 |
| 09   | -135207.0156 | 44.14      | y_att=3.88, y_ali=2.91, y_f=0.10, d0_att=1.51, l_att=3.10, l_ali=2.73, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.90, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.72, l_acc=1.78, d0_v=1.06, y_explo=0.10 |
| 10   | -135221.2344 | 44.14      | y_att=2.63, y_ali=0.42, y_f=0.10, d0_att=0.95, l_att=2.37, l_ali=1.70, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.74, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.90, l_acc=0.59, d0_v=0.59, y_explo=0.10 |
| 11   | -135221.2344 | 44.14      | y_att=2.63, y_ali=0.42, y_f=0.10, d0_att=0.95, l_att=2.37, l_ali=1.70, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.74, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.90, l_acc=0.59, d0_v=0.59, y_explo=0.10 |
| 12   | -136039.6719 | 44.14      | y_att=0.66, y_ali=1.41, y_f=0.10, d0_att=0.87, l_att=4.63, l_ali=1.51, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.35, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.04, y_acc=0.73, l_acc=1.24, d0_v=0.66, y_explo=0.10 |
| 13   | -136039.6719 | 44.14      | y_att=0.66, y_ali=1.41, y_f=0.10, d0_att=0.87, l_att=4.63, l_ali=1.51, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.35, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.04, y_acc=0.73, l_acc=1.24, d0_v=0.66, y_explo=0.10 |
| 14   | -136039.6719 | 44.13      | y_att=0.66, y_ali=1.41, y_f=0.10, d0_att=0.87, l_att=4.63, l_ali=1.51, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.35, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.04, y_acc=0.73, l_acc=1.24, d0_v=0.66, y_explo=0.10 |
| 15   | -136039.6719 | 44.12      | y_att=0.66, y_ali=1.41, y_f=0.10, d0_att=0.87, l_att=4.63, l_ali=1.51, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.35, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.04, y_acc=0.73, l_acc=1.24, d0_v=0.66, y_explo=0.10 |
| 16   | -136710.6250 | 44.11      | y_att=2.82, y_ali=0.41, y_f=0.10, d0_att=0.50, l_att=1.70, l_ali=3.42, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.28, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.37, l_acc=1.18, d0_v=0.54, y_explo=0.12 |
| 17   | -136710.6250 | 44.11      | y_att=2.82, y_ali=0.41, y_f=0.10, d0_att=0.50, l_att=1.70, l_ali=3.42, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.28, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.37, l_acc=1.18, d0_v=0.54, y_explo=0.12 |
| 18   | -136710.6250 | 44.10      | y_att=2.82, y_ali=0.41, y_f=0.10, d0_att=0.50, l_att=1.70, l_ali=3.42, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.28, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.37, l_acc=1.18, d0_v=0.54, y_explo=0.12 |
| 19   | -136710.6250 | 44.10      | y_att=2.82, y_ali=0.41, y_f=0.10, d0_att=0.50, l_att=1.70, l_ali=3.42, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.28, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.37, l_acc=1.18, d0_v=0.54, y_explo=0.12 |

**End of experiment.**
