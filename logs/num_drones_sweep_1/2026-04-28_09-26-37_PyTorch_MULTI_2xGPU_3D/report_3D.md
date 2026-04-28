# Experiment Report - PyTorch_MULTI_2xGPU (3D)
**Date:** 2026-04-28_09-26-37

## 1. Initial Configuration
| Parameter | Value |
| :--- | :--- |
| ALPHA_LPF            | 0.2        |
| ARENA_RADIUS         | 100.0      |
| COLLISION_DIST       | 0.4        |
| DT                   | 0.1        |
| ENABLE_3D            | True       |
| EXPLO_STRATEGY       | local_gradient |
| FOV_FACTOR           | 0.577      |
| FULL_MILLING_MODE    | False      |
| GEN_CPU              | 20         |
| GEN_GPU              | 20         |
| GRID_RES             | 5.0        |
| MAP_STRATEGY         | local_shared |
| MAX_SPEED            | 20.0       |
| MAX_YAW_RATE         | 3.14       |
| MIN_SPAWN_DIST       | 2.0        |
| NB_DRONES            | 30         |
| NEIGHBORS            | 2          |
| N_INIT_CONDITIONS    | 4          |
| POP_SIZE_CPU         | 150        |
| POP_SIZE_GPU         | 5000       |
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
| 00   | -3162.8464   | 49.77      | y_att=0.02, y_ali=3.23, y_f=1.74, d0_att=2.25, l_att=3.90, l_ali=2.25, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.53, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.87, y_acc=0.05, l_acc=2.22, d0_v=2.97, y_explo=0.12 |
| 01   | -3537.9573   | 49.42      | y_att=0.10, y_ali=3.23, y_f=1.74, d0_att=2.25, l_att=3.90, l_ali=2.25, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.79, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.87, y_acc=0.05, l_acc=2.22, d0_v=2.97, y_explo=0.12 |
| 02   | -3537.9573   | 49.41      | y_att=0.10, y_ali=3.23, y_f=1.74, d0_att=2.25, l_att=3.90, l_ali=2.25, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.79, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.87, y_acc=0.05, l_acc=2.22, d0_v=2.97, y_explo=0.12 |
| 03   | -3537.9573   | 49.41      | y_att=0.10, y_ali=3.23, y_f=1.74, d0_att=2.25, l_att=3.90, l_ali=2.25, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.79, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.87, y_acc=0.05, l_acc=2.22, d0_v=2.97, y_explo=0.12 |
| 04   | -3537.9573   | 49.40      | y_att=0.10, y_ali=3.23, y_f=1.74, d0_att=2.25, l_att=3.90, l_ali=2.25, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.79, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.87, y_acc=0.05, l_acc=2.22, d0_v=2.97, y_explo=0.12 |
| 05   | -3537.9573   | 49.39      | y_att=0.10, y_ali=3.23, y_f=1.74, d0_att=2.25, l_att=3.90, l_ali=2.25, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.79, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.87, y_acc=0.05, l_acc=2.22, d0_v=2.97, y_explo=0.12 |
| 06   | -3659.1252   | 49.38      | y_att=0.10, y_ali=0.09, y_f=0.71, d0_att=0.83, l_att=4.93, l_ali=4.58, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.97, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.70, y_acc=0.03, l_acc=2.33, d0_v=2.56, y_explo=0.11 |
| 07   | -3782.5383   | 49.37      | y_att=0.30, y_ali=0.03, y_f=0.80, d0_att=0.87, l_att=2.41, l_ali=0.40, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.88, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.94, y_acc=0.16, l_acc=0.62, d0_v=1.02, y_explo=0.10 |
| 08   | -3836.9785   | 49.36      | y_att=0.30, y_ali=0.03, y_f=0.80, d0_att=0.87, l_att=2.41, l_ali=0.40, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.90, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.94, y_acc=0.16, l_acc=0.62, d0_v=1.02, y_explo=0.10 |
| 09   | -3896.5193   | 49.35      | y_att=0.25, y_ali=0.74, y_f=1.37, d0_att=1.22, l_att=2.97, l_ali=1.34, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.28, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.00, l_acc=1.51, d0_v=0.41, y_explo=0.10 |
| 10   | -3896.5193   | 49.35      | y_att=0.25, y_ali=0.74, y_f=1.37, d0_att=1.22, l_att=2.97, l_ali=1.34, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.28, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.00, l_acc=1.51, d0_v=0.41, y_explo=0.10 |
| 11   | -3934.4773   | 49.35      | y_att=0.83, y_ali=0.25, y_f=1.74, d0_att=0.89, l_att=1.50, l_ali=1.78, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.54, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.45, y_acc=0.02, l_acc=1.53, d0_v=0.32, y_explo=0.11 |
| 12   | -4004.1946   | 49.35      | y_att=0.81, y_ali=2.23, y_f=5.86, d0_att=1.02, l_att=1.21, l_ali=1.60, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.33, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.05, l_acc=0.28, d0_v=1.79, y_explo=0.11 |
| 13   | -4004.1946   | 49.35      | y_att=0.81, y_ali=2.23, y_f=5.86, d0_att=1.02, l_att=1.21, l_ali=1.60, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.33, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.05, l_acc=0.28, d0_v=1.79, y_explo=0.11 |
| 14   | -4004.1946   | 49.35      | y_att=0.81, y_ali=2.23, y_f=5.86, d0_att=1.02, l_att=1.21, l_ali=1.60, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.33, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.05, l_acc=0.28, d0_v=1.79, y_explo=0.11 |
| 15   | -4004.1946   | 49.34      | y_att=0.81, y_ali=2.23, y_f=5.86, d0_att=1.02, l_att=1.21, l_ali=1.60, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.33, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.05, l_acc=0.28, d0_v=1.79, y_explo=0.11 |
| 16   | -4019.6152   | 49.34      | y_att=0.51, y_ali=2.76, y_f=9.02, d0_att=0.55, l_att=0.97, l_ali=0.45, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.04, l_acc=1.41, d0_v=1.39, y_explo=0.11 |
| 17   | -4049.5930   | 49.34      | y_att=0.18, y_ali=0.94, y_f=1.56, d0_att=0.64, l_att=1.73, l_ali=0.65, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.93, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.04, l_acc=0.42, d0_v=0.50, y_explo=0.10 |
| 18   | -6482.4775   | 49.33      | y_att=0.58, y_ali=0.02, y_f=17.71, d0_att=0.68, l_att=1.11, l_ali=2.61, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.97, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.00, l_acc=0.65, d0_v=2.12, y_explo=0.10 |
| 19   | -7029.8115   | 49.33      | y_att=0.58, y_ali=0.00, y_f=17.71, d0_att=0.51, l_att=1.95, l_ali=2.61, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.63, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.00, l_acc=0.98, d0_v=7.28, y_explo=0.10 |

**End of experiment.**
