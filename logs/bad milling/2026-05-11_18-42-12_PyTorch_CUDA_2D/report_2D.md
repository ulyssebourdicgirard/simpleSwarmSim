# Experiment Report - PyTorch_CUDA (2D)
**Date:** 2026-05-11_18-42-12

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
| NB_DRONES            | 5          |
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
| W_STATIONARY         | 1000       |
| Z_MAX                | 10.0       |
| Z_MIN                | 1.0        |

## 2. Optimization Evolution
| Gen  |  Best Cost   |  Time (s)  |                                                                All Parameters                                                                |
| :--: | :----------: | :--------: | :------------------------------------------------------------------------------------------------------------------------------------------ |
| 00   | -284527.6562 | 13.32      | y_att=0.20, y_ali=3.65, y_f=1.00, d0_att=6.39, l_att=1.60, l_ali=4.71, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.98, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.15, y_acc=0.02, l_acc=0.55, d0_v=1.67, y_explo=2.66 |
| 01   | -284527.6562 | 12.83      | y_att=0.20, y_ali=3.65, y_f=1.00, d0_att=6.39, l_att=1.60, l_ali=4.71, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.98, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.15, y_acc=0.02, l_acc=0.55, d0_v=1.67, y_explo=2.66 |
| 02   | -379972.9375 | 13.06      | y_att=0.20, y_ali=3.65, y_f=1.00, d0_att=3.93, l_att=1.29, l_ali=4.54, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.94, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.12, y_acc=0.02, l_acc=0.60, d0_v=2.34, y_explo=5.68 |
| 03   | -379972.9375 | 12.92      | y_att=0.20, y_ali=3.65, y_f=1.00, d0_att=3.93, l_att=1.29, l_ali=4.54, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.94, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.12, y_acc=0.02, l_acc=0.60, d0_v=2.34, y_explo=5.68 |
| 04   | -392478.9375 | 13.38      | y_att=0.10, y_ali=1.12, y_f=0.65, d0_att=11.65, l_att=7.32, l_ali=7.82, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.68, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.52, y_acc=0.13, l_acc=0.17, d0_v=3.90, y_explo=5.07 |
| 05   | -484120.9688 | 13.47      | y_att=4.85, y_ali=1.97, y_f=0.98, d0_att=10.18, l_att=7.66, l_ali=5.82, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.50, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.17, y_acc=0.00, l_acc=1.08, d0_v=1.71, y_explo=5.37 |
| 06   | -570822.2500 | 13.19      | y_att=1.89, y_ali=2.77, y_f=2.42, d0_att=9.58, l_att=1.60, l_ali=7.01, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.16, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.81, y_acc=0.01, l_acc=1.14, d0_v=2.51, y_explo=0.40 |
| 07   | -652378.5000 | 12.96      | y_att=0.18, y_ali=2.13, y_f=2.61, d0_att=5.69, l_att=1.86, l_ali=18.98, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.63, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.33, y_acc=0.07, l_acc=0.51, d0_v=2.32, y_explo=4.85 |
| 08   | -758219.0000 | 13.33      | y_att=0.18, y_ali=1.09, y_f=3.74, d0_att=11.14, l_att=14.72, l_ali=18.17, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.36, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.10, y_acc=0.12, l_acc=1.96, d0_v=4.32, y_explo=2.03 |
| 09   | -792867.3750 | 14.06      | y_att=0.93, y_ali=1.87, y_f=1.37, d0_att=8.52, l_att=3.04, l_ali=12.75, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.25, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.27, y_acc=0.00, l_acc=0.60, d0_v=2.43, y_explo=1.51 |
| 10   | -844525.5000 | 13.05      | y_att=0.11, y_ali=1.83, y_f=0.83, d0_att=9.28, l_att=2.84, l_ali=12.13, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.99, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.44, y_acc=0.01, l_acc=1.03, d0_v=2.42, y_explo=1.26 |
| 11   | -844525.5000 | 13.50      | y_att=0.11, y_ali=1.83, y_f=0.83, d0_att=9.28, l_att=2.84, l_ali=12.13, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.99, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.44, y_acc=0.01, l_acc=1.03, d0_v=2.42, y_explo=1.26 |
| 12   | -923978.4375 | 13.24      | y_att=0.17, y_ali=1.99, y_f=1.04, d0_att=10.62, l_att=0.11, l_ali=18.98, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.80, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.55, y_acc=0.09, l_acc=0.49, d0_v=2.96, y_explo=0.26 |
| 13   | -923978.4375 | 12.79      | y_att=0.17, y_ali=1.99, y_f=1.04, d0_att=10.62, l_att=0.11, l_ali=18.98, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.80, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.55, y_acc=0.09, l_acc=0.49, d0_v=2.96, y_explo=0.26 |
| 14   | -930610.7500 | 13.12      | y_att=0.14, y_ali=1.78, y_f=2.28, d0_att=22.17, l_att=1.11, l_ali=22.60, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.51, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.15, y_acc=0.01, l_acc=0.66, d0_v=4.17, y_explo=4.70 |
| 15   | -930610.7500 | 13.74      | y_att=0.14, y_ali=1.78, y_f=2.28, d0_att=22.17, l_att=1.11, l_ali=22.60, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.51, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.15, y_acc=0.01, l_acc=0.66, d0_v=4.17, y_explo=4.70 |
| 16   | -974523.5000 | 13.51      | y_att=0.17, y_ali=1.88, y_f=0.55, d0_att=3.71, l_att=0.10, l_ali=20.32, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.61, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.52, y_acc=0.00, l_acc=2.15, d0_v=3.60, y_explo=2.29 |
| 17   | -974523.5000 | 13.81      | y_att=0.17, y_ali=1.88, y_f=0.55, d0_att=3.71, l_att=0.10, l_ali=20.32, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.61, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.52, y_acc=0.00, l_acc=2.15, d0_v=3.60, y_explo=2.29 |
| 18   | -974523.5000 | 13.16      | y_att=0.17, y_ali=1.88, y_f=0.55, d0_att=3.71, l_att=0.10, l_ali=20.32, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.61, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.52, y_acc=0.00, l_acc=2.15, d0_v=3.60, y_explo=2.29 |
| 19   | -974523.5000 | 12.93      | y_att=0.17, y_ali=1.88, y_f=0.55, d0_att=3.71, l_att=0.10, l_ali=20.32, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.61, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.52, y_acc=0.00, l_acc=2.15, d0_v=3.60, y_explo=2.29 |

**End of experiment.**
