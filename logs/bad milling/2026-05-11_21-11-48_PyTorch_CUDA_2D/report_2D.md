# Experiment Report - PyTorch_CUDA (2D)
**Date:** 2026-05-11_21-11-48

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
| W_COLL               | 50.0       |
| W_DISP               | 10.0       |
| W_EFFORT             | 0          |
| W_EXPLO              | 0.0        |
| W_MILL               | -600.0     |
| W_POL                | 250.0      |
| W_STATIONARY         | 50         |
| Z_MAX                | 10.0       |
| Z_MIN                | 1.0        |

## 2. Optimization Evolution
| Gen  |  Best Cost   |  Time (s)  |                                                                All Parameters                                                                |
| :--: | :----------: | :--------: | :------------------------------------------------------------------------------------------------------------------------------------------ |
| 00   | 29663.7500   | 12.61      | y_att=0.05, y_ali=2.12, y_f=1.94, d0_att=4.55, l_att=9.88, l_ali=4.25, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.72, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.85, y_acc=0.04, l_acc=3.21, d0_v=1.52, y_explo=3.85 |
| 01   | 29663.7500   | 11.85      | y_att=0.05, y_ali=2.12, y_f=1.94, d0_att=4.55, l_att=9.88, l_ali=4.25, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.72, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.85, y_acc=0.04, l_acc=3.21, d0_v=1.52, y_explo=3.85 |
| 02   | -321305.5625 | 12.33      | y_att=3.36, y_ali=3.54, y_f=6.01, d0_att=5.94, l_att=2.77, l_ali=12.55, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.32, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.35, y_acc=0.04, l_acc=1.35, d0_v=0.58, y_explo=8.72 |
| 03   | -321305.5625 | 12.26      | y_att=3.36, y_ali=3.54, y_f=6.01, d0_att=5.94, l_att=2.77, l_ali=12.55, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.32, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.35, y_acc=0.04, l_acc=1.35, d0_v=0.58, y_explo=8.72 |
| 04   | -360164.6250 | 12.68      | y_att=0.10, y_ali=2.79, y_f=8.29, d0_att=4.47, l_att=1.56, l_ali=12.74, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.79, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.71, y_acc=0.11, l_acc=2.24, d0_v=0.96, y_explo=15.23 |
| 05   | -531939.8125 | 11.72      | y_att=0.59, y_ali=3.51, y_f=8.18, d0_att=2.72, l_att=1.22, l_ali=16.35, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=3.28, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.02, y_acc=0.21, l_acc=1.73, d0_v=2.21, y_explo=4.35 |
| 06   | -740965.8125 | 12.10      | y_att=0.10, y_ali=1.74, y_f=10.00, d0_att=5.07, l_att=10.58, l_ali=14.26, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.17, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.72, y_acc=0.12, l_acc=1.36, d0_v=1.49, y_explo=0.32 |
| 07   | -788285.6875 | 11.72      | y_att=2.11, y_ali=1.05, y_f=10.32, d0_att=3.86, l_att=0.22, l_ali=11.74, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.01, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.52, y_acc=0.24, l_acc=1.12, d0_v=1.56, y_explo=7.86 |
| 08   | -788285.6875 | 12.22      | y_att=2.11, y_ali=1.05, y_f=10.32, d0_att=3.86, l_att=0.22, l_ali=11.74, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.01, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.52, y_acc=0.24, l_acc=1.12, d0_v=1.56, y_explo=7.86 |
| 09   | -788285.6875 | 11.57      | y_att=2.11, y_ali=1.05, y_f=10.32, d0_att=3.86, l_att=0.22, l_ali=11.74, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.01, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.52, y_acc=0.24, l_acc=1.12, d0_v=1.56, y_explo=7.86 |
| 10   | -788285.6875 | 12.18      | y_att=2.11, y_ali=1.05, y_f=10.32, d0_att=3.86, l_att=0.22, l_ali=11.74, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.01, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.52, y_acc=0.24, l_acc=1.12, d0_v=1.56, y_explo=7.86 |
| 11   | -788285.6875 | 12.72      | y_att=2.11, y_ali=1.05, y_f=10.32, d0_att=3.86, l_att=0.22, l_ali=11.74, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.01, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.52, y_acc=0.24, l_acc=1.12, d0_v=1.56, y_explo=7.86 |
| 12   | -788285.6875 | 12.90      | y_att=2.11, y_ali=1.05, y_f=10.32, d0_att=3.86, l_att=0.22, l_ali=11.74, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.01, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.52, y_acc=0.24, l_acc=1.12, d0_v=1.56, y_explo=7.86 |
| 13   | -788285.6875 | 12.26      | y_att=2.11, y_ali=1.05, y_f=10.32, d0_att=3.86, l_att=0.22, l_ali=11.74, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.01, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.52, y_acc=0.24, l_acc=1.12, d0_v=1.56, y_explo=7.86 |
| 14   | -788285.6875 | 12.67      | y_att=2.11, y_ali=1.05, y_f=10.32, d0_att=3.86, l_att=0.22, l_ali=11.74, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.01, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.52, y_acc=0.24, l_acc=1.12, d0_v=1.56, y_explo=7.86 |
| 15   | -788285.6875 | 12.12      | y_att=2.11, y_ali=1.05, y_f=10.32, d0_att=3.86, l_att=0.22, l_ali=11.74, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.01, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.52, y_acc=0.24, l_acc=1.12, d0_v=1.56, y_explo=7.86 |
| 16   | -788285.6875 | 12.06      | y_att=2.11, y_ali=1.05, y_f=10.32, d0_att=3.86, l_att=0.22, l_ali=11.74, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.01, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.52, y_acc=0.24, l_acc=1.12, d0_v=1.56, y_explo=7.86 |
| 17   | -788285.6875 | 12.26      | y_att=2.11, y_ali=1.05, y_f=10.32, d0_att=3.86, l_att=0.22, l_ali=11.74, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.01, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.52, y_acc=0.24, l_acc=1.12, d0_v=1.56, y_explo=7.86 |
| 18   | -788285.6875 | 12.11      | y_att=2.11, y_ali=1.05, y_f=10.32, d0_att=3.86, l_att=0.22, l_ali=11.74, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.01, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.52, y_acc=0.24, l_acc=1.12, d0_v=1.56, y_explo=7.86 |
| 19   | -788285.6875 | 12.35      | y_att=2.11, y_ali=1.05, y_f=10.32, d0_att=3.86, l_att=0.22, l_ali=11.74, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.01, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.52, y_acc=0.24, l_acc=1.12, d0_v=1.56, y_explo=7.86 |

**End of experiment.**
