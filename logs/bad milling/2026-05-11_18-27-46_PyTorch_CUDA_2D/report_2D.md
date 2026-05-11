# Experiment Report - PyTorch_CUDA (2D)
**Date:** 2026-05-11_18-27-46

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
| NB_DRONES            | 15         |
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
| W_COLL               | 500.0      |
| W_DISP               | 10.0       |
| W_EFFORT             | 0.3        |
| W_EXPLO              | 0.0        |
| W_MILL               | -600.0     |
| W_POL                | 250.0      |
| W_STATIONARY         | 400        |
| Z_MAX                | 10.0       |
| Z_MIN                | 1.0        |

## 2. Optimization Evolution
| Gen  |  Best Cost   |  Time (s)  |                                                                All Parameters                                                                |
| :--: | :----------: | :--------: | :------------------------------------------------------------------------------------------------------------------------------------------ |
| 00   | 561387.5625  | 17.17      | y_att=4.17, y_ali=2.44, y_f=0.41, d0_att=7.31, l_att=9.27, l_ali=1.87, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.39, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.45, y_acc=1.17, l_acc=1.44, d0_v=0.70, y_explo=1.77 |
| 01   | 561387.5625  | 17.56      | y_att=4.17, y_ali=2.44, y_f=0.41, d0_att=7.31, l_att=9.27, l_ali=1.87, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.39, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.45, y_acc=1.17, l_acc=1.44, d0_v=0.70, y_explo=1.77 |
| 02   | 309959.6250  | 17.76      | y_att=3.27, y_ali=3.64, y_f=1.39, d0_att=4.48, l_att=3.12, l_ali=6.14, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.53, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.16, y_acc=0.03, l_acc=1.85, d0_v=2.13, y_explo=5.15 |
| 03   | -192325.4844 | 18.51      | y_att=0.10, y_ali=1.98, y_f=0.74, d0_att=3.50, l_att=1.11, l_ali=3.80, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.36, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.79, y_acc=0.02, l_acc=1.00, d0_v=1.45, y_explo=0.97 |
| 04   | -192325.4844 | 18.61      | y_att=0.10, y_ali=1.98, y_f=0.74, d0_att=3.50, l_att=1.11, l_ali=3.80, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.36, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.79, y_acc=0.02, l_acc=1.00, d0_v=1.45, y_explo=0.97 |
| 05   | -233201.7500 | 16.24      | y_att=0.10, y_ali=2.39, y_f=0.97, d0_att=2.25, l_att=1.18, l_ali=3.90, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.01, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.85, y_acc=0.01, l_acc=0.63, d0_v=1.05, y_explo=0.16 |
| 06   | -236524.8281 | 15.97      | y_att=0.11, y_ali=2.77, y_f=1.55, d0_att=3.29, l_att=1.11, l_ali=3.18, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.17, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.08, y_acc=0.02, l_acc=0.28, d0_v=1.16, y_explo=0.38 |
| 07   | -390943.4688 | 16.06      | y_att=0.19, y_ali=1.99, y_f=1.69, d0_att=1.50, l_att=0.21, l_ali=3.66, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.91, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.39, y_acc=0.01, l_acc=1.83, d0_v=0.51, y_explo=0.35 |
| 08   | -390943.4688 | 15.53      | y_att=0.19, y_ali=1.99, y_f=1.69, d0_att=1.50, l_att=0.21, l_ali=3.66, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.91, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.39, y_acc=0.01, l_acc=1.83, d0_v=0.51, y_explo=0.35 |
| 09   | -448685.8750 | 17.84      | y_att=0.10, y_ali=1.30, y_f=0.75, d0_att=1.59, l_att=1.20, l_ali=15.57, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.47, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.68, y_acc=0.03, l_acc=0.28, d0_v=1.14, y_explo=6.64 |
| 10   | -633678.1875 | 16.36      | y_att=0.60, y_ali=1.05, y_f=0.61, d0_att=1.13, l_att=0.12, l_ali=21.93, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.79, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.00, y_acc=0.01, l_acc=0.70, d0_v=1.60, y_explo=4.80 |
| 11   | -767145.3125 | 16.66      | y_att=0.60, y_ali=1.05, y_f=0.29, d0_att=1.54, l_att=0.12, l_ali=21.93, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.19, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.00, y_acc=0.01, l_acc=1.03, d0_v=1.83, y_explo=1.68 |
| 12   | -767145.3125 | 15.87      | y_att=0.60, y_ali=1.05, y_f=0.29, d0_att=1.54, l_att=0.12, l_ali=21.93, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.19, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.00, y_acc=0.01, l_acc=1.03, d0_v=1.83, y_explo=1.68 |
| 13   | -767145.3125 | 17.87      | y_att=0.60, y_ali=1.05, y_f=0.29, d0_att=1.54, l_att=0.12, l_ali=21.93, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.19, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.00, y_acc=0.01, l_acc=1.03, d0_v=1.83, y_explo=1.68 |
| 14   | -767145.3125 | 16.35      | y_att=0.60, y_ali=1.05, y_f=0.29, d0_att=1.54, l_att=0.12, l_ali=21.93, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.19, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.00, y_acc=0.01, l_acc=1.03, d0_v=1.83, y_explo=1.68 |
| 15   | -936118.7500 | 16.50      | y_att=0.10, y_ali=0.99, y_f=0.81, d0_att=0.94, l_att=0.13, l_ali=29.49, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.37, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.90, y_acc=0.01, l_acc=2.15, d0_v=1.56, y_explo=0.89 |
| 16   | -1100254.1250 | 19.47      | y_att=0.17, y_ali=0.89, y_f=2.75, d0_att=2.07, l_att=0.11, l_ali=23.67, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.89, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.53, y_acc=0.07, l_acc=0.69, d0_v=0.95, y_explo=0.51 |
| 17   | -1100254.1250 | 17.00      | y_att=0.17, y_ali=0.89, y_f=2.75, d0_att=2.07, l_att=0.11, l_ali=23.67, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.89, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.53, y_acc=0.07, l_acc=0.69, d0_v=0.95, y_explo=0.51 |
| 18   | -1159458.2500 | 16.62      | y_att=0.12, y_ali=0.66, y_f=2.41, d0_att=1.64, l_att=1.36, l_ali=52.64, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.65, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.43, y_acc=0.11, l_acc=1.16, d0_v=1.74, y_explo=1.39 |
| 19   | -1159458.2500 | 16.72      | y_att=0.12, y_ali=0.66, y_f=2.41, d0_att=1.64, l_att=1.36, l_ali=52.64, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.65, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.43, y_acc=0.11, l_acc=1.16, d0_v=1.74, y_explo=1.39 |

**End of experiment.**
