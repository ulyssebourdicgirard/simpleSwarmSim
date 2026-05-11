# Experiment Report - PyTorch_CUDA (2D)
**Date:** 2026-05-11_21-19-02

## 1. Initial Configuration
| Parameter | Value |
| :--- | :--- |
| ALPHA_LPF            | 0.2        |
| ARENA_RADIUS         | 50.0       |
| COLLISION_DIST       | 0.4        |
| DT                   | 0.1        |
| ENABLE_3D            | False      |
| EVAL_STRATEGY        | average    |
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
| W_STATIONARY         | 50         |
| Z_MAX                | 10.0       |
| Z_MIN                | 1.0        |

## 2. Optimization Evolution
| Gen  |  Best Cost   |  Time (s)  |                                                                All Parameters                                                                |
| :--: | :----------: | :--------: | :------------------------------------------------------------------------------------------------------------------------------------------ |
| 00   | 551196.1250  | 12.10      | y_att=2.35, y_ali=2.48, y_f=1.91, d0_att=6.91, l_att=6.50, l_ali=3.44, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.55, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.77, y_acc=0.05, l_acc=3.42, d0_v=2.83, y_explo=0.32 |
| 01   | -336445.1250 | 11.10      | y_att=3.86, y_ali=1.62, y_f=1.01, d0_att=3.71, l_att=0.99, l_ali=14.60, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.79, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.35, y_acc=0.06, l_acc=1.17, d0_v=1.92, y_explo=2.77 |
| 02   | -849162.6250 | 11.62      | y_att=2.15, y_ali=2.61, y_f=1.78, d0_att=8.41, l_att=2.83, l_ali=13.78, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=3.75, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.58, y_acc=0.00, l_acc=1.16, d0_v=2.19, y_explo=2.68 |
| 03   | -849162.6250 | 11.55      | y_att=2.15, y_ali=2.61, y_f=1.78, d0_att=8.41, l_att=2.83, l_ali=13.78, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=3.75, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.58, y_acc=0.00, l_acc=1.16, d0_v=2.19, y_explo=2.68 |
| 04   | -849162.6250 | 11.80      | y_att=2.15, y_ali=2.61, y_f=1.78, d0_att=8.41, l_att=2.83, l_ali=13.78, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=3.75, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.58, y_acc=0.00, l_acc=1.16, d0_v=2.19, y_explo=2.68 |
| 05   | -886400.5625 | 11.26      | y_att=0.10, y_ali=3.15, y_f=12.08, d0_att=4.31, l_att=7.82, l_ali=21.32, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=7.53, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.22, y_acc=0.09, l_acc=0.64, d0_v=1.10, y_explo=15.27 |
| 06   | -917537.8125 | 11.96      | y_att=2.88, y_ali=1.09, y_f=0.59, d0_att=10.18, l_att=3.22, l_ali=10.17, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.71, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.65, y_acc=0.00, l_acc=11.95, d0_v=13.33, y_explo=4.20 |
| 07   | -1182973.3750 | 11.48      | y_att=8.25, y_ali=5.22, y_f=1.43, d0_att=8.74, l_att=5.95, l_ali=19.56, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.45, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.36, y_acc=0.03, l_acc=1.83, d0_v=1.75, y_explo=3.73 |
| 08   | -1195596.7500 | 11.75      | y_att=2.99, y_ali=1.09, y_f=12.73, d0_att=14.68, l_att=9.31, l_ali=12.90, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.62, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.20, y_acc=0.00, l_acc=1.69, d0_v=14.40, y_explo=0.27 |
| 09   | -1195596.7500 | 11.50      | y_att=2.99, y_ali=1.09, y_f=12.73, d0_att=14.68, l_att=9.31, l_ali=12.90, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.62, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.20, y_acc=0.00, l_acc=1.69, d0_v=14.40, y_explo=0.27 |
| 10   | -1195596.7500 | 11.67      | y_att=2.99, y_ali=1.09, y_f=12.73, d0_att=14.68, l_att=9.31, l_ali=12.90, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.62, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.20, y_acc=0.00, l_acc=1.69, d0_v=14.40, y_explo=0.27 |
| 11   | -1195596.7500 | 11.70      | y_att=2.99, y_ali=1.09, y_f=12.73, d0_att=14.68, l_att=9.31, l_ali=12.90, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.62, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.20, y_acc=0.00, l_acc=1.69, d0_v=14.40, y_explo=0.27 |
| 12   | -1195596.7500 | 11.51      | y_att=2.99, y_ali=1.09, y_f=12.73, d0_att=14.68, l_att=9.31, l_ali=12.90, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.62, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.20, y_acc=0.00, l_acc=1.69, d0_v=14.40, y_explo=0.27 |
| 13   | -1195596.7500 | 11.35      | y_att=2.99, y_ali=1.09, y_f=12.73, d0_att=14.68, l_att=9.31, l_ali=12.90, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.62, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.20, y_acc=0.00, l_acc=1.69, d0_v=14.40, y_explo=0.27 |
| 14   | -1195596.7500 | 11.81      | y_att=2.99, y_ali=1.09, y_f=12.73, d0_att=14.68, l_att=9.31, l_ali=12.90, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.62, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.20, y_acc=0.00, l_acc=1.69, d0_v=14.40, y_explo=0.27 |
| 15   | -1195596.7500 | 11.65      | y_att=2.99, y_ali=1.09, y_f=12.73, d0_att=14.68, l_att=9.31, l_ali=12.90, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.62, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.20, y_acc=0.00, l_acc=1.69, d0_v=14.40, y_explo=0.27 |
| 16   | -1195596.7500 | 11.66      | y_att=2.99, y_ali=1.09, y_f=12.73, d0_att=14.68, l_att=9.31, l_ali=12.90, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.62, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.20, y_acc=0.00, l_acc=1.69, d0_v=14.40, y_explo=0.27 |
| 17   | -1195596.7500 | 11.32      | y_att=2.99, y_ali=1.09, y_f=12.73, d0_att=14.68, l_att=9.31, l_ali=12.90, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.62, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.20, y_acc=0.00, l_acc=1.69, d0_v=14.40, y_explo=0.27 |
| 18   | -1195596.7500 | 11.30      | y_att=2.99, y_ali=1.09, y_f=12.73, d0_att=14.68, l_att=9.31, l_ali=12.90, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.62, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.20, y_acc=0.00, l_acc=1.69, d0_v=14.40, y_explo=0.27 |
| 19   | -1195596.7500 | 11.53      | y_att=2.99, y_ali=1.09, y_f=12.73, d0_att=14.68, l_att=9.31, l_ali=12.90, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.62, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.20, y_acc=0.00, l_acc=1.69, d0_v=14.40, y_explo=0.27 |

**End of experiment.**
