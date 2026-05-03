# Experiment Report - PyTorch_CUDA (2D)
**Date:** 2026-05-03_17-58-07

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
| GEN_GPU              | 10         |
| GRID_RES             | 5.0        |
| MAP_STRATEGY         | local_shared |
| MAX_SPEED            | 30.0       |
| MAX_YAW_RATE         | 3.14       |
| MIN_SPAWN_DIST       | 2.0        |
| NB_DRONES            | 5          |
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
| 00   | -4391.6958   | 3.33       | y_att=2.79, y_ali=1.89, y_f=1.36, d0_att=6.55, l_att=5.41, l_ali=2.83, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.85, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.13, y_acc=0.36, l_acc=2.47, d0_v=1.05, y_explo=3.66 |
| 01   | -4666.9985   | 3.23       | y_att=0.15, y_ali=0.66, y_f=0.41, d0_att=2.74, l_att=2.80, l_ali=2.66, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.69, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.19, y_acc=0.17, l_acc=0.66, d0_v=2.55, y_explo=3.42 |
| 02   | -4666.9985   | 3.96       | y_att=0.15, y_ali=0.66, y_f=0.41, d0_att=2.74, l_att=2.80, l_ali=2.66, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.69, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.19, y_acc=0.17, l_acc=0.66, d0_v=2.55, y_explo=3.42 |
| 03   | -5392.8901   | 3.13       | y_att=0.42, y_ali=0.00, y_f=1.05, d0_att=6.59, l_att=4.90, l_ali=5.26, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.21, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.52, y_acc=0.66, l_acc=1.60, d0_v=2.54, y_explo=4.29 |
| 04   | -7275.7661   | 3.12       | y_att=1.12, y_ali=3.24, y_f=3.17, d0_att=9.41, l_att=1.39, l_ali=3.80, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.26, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=1.24, l_acc=0.62, d0_v=1.42, y_explo=2.13 |
| 05   | -7275.7661   | 3.04       | y_att=1.12, y_ali=3.24, y_f=3.17, d0_att=9.41, l_att=1.39, l_ali=3.80, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.26, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=1.24, l_acc=0.62, d0_v=1.42, y_explo=2.13 |
| 06   | -7275.7661   | 3.78       | y_att=1.12, y_ali=3.24, y_f=3.17, d0_att=9.41, l_att=1.39, l_ali=3.80, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.26, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=1.24, l_acc=0.62, d0_v=1.42, y_explo=2.13 |
| 07   | -7275.7661   | 3.13       | y_att=1.12, y_ali=3.24, y_f=3.17, d0_att=9.41, l_att=1.39, l_ali=3.80, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.26, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=1.24, l_acc=0.62, d0_v=1.42, y_explo=2.13 |
| 08   | -7275.7661   | 3.26       | y_att=1.12, y_ali=3.24, y_f=3.17, d0_att=9.41, l_att=1.39, l_ali=3.80, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.26, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=1.24, l_acc=0.62, d0_v=1.42, y_explo=2.13 |
| 09   | -7275.7661   | 3.11       | y_att=1.12, y_ali=3.24, y_f=3.17, d0_att=9.41, l_att=1.39, l_ali=3.80, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.26, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=1.24, l_acc=0.62, d0_v=1.42, y_explo=2.13 |

**End of experiment.**
