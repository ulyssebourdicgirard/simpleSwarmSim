# Experiment Report - PyTorch_CUDA (2D)
**Date:** 2026-05-11_21-25-22

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
| 00   | -64100.2266  | 12.48      | y_att=0.14, y_ali=2.63, y_f=1.39, d0_att=1.42, l_att=1.29, l_ali=4.12, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.36, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.51, y_acc=0.01, l_acc=1.88, d0_v=2.19, y_explo=2.83 |
| 01   | -249703.6250 | 12.03      | y_att=3.05, y_ali=3.27, y_f=0.91, d0_att=2.12, l_att=1.92, l_ali=12.17, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.63, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.26, y_acc=0.03, l_acc=1.90, d0_v=2.61, y_explo=0.92 |
| 02   | -281625.0000 | 12.37      | y_att=0.47, y_ali=2.95, y_f=1.17, d0_att=3.44, l_att=11.08, l_ali=14.96, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.08, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.94, y_acc=0.03, l_acc=3.29, d0_v=2.88, y_explo=1.20 |
| 03   | -391103.5000 | 11.80      | y_att=0.10, y_ali=2.65, y_f=1.70, d0_att=1.90, l_att=1.17, l_ali=13.75, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.24, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.00, y_acc=0.16, l_acc=1.30, d0_v=2.58, y_explo=4.31 |
| 04   | -582976.7500 | 12.34      | y_att=0.22, y_ali=3.00, y_f=10.26, d0_att=5.98, l_att=0.93, l_ali=16.63, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=3.84, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.39, y_acc=0.10, l_acc=1.43, d0_v=0.59, y_explo=1.10 |
| 05   | -911942.8750 | 11.62      | y_att=0.10, y_ali=1.82, y_f=0.90, d0_att=3.44, l_att=4.16, l_ali=24.85, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.13, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.94, y_acc=0.03, l_acc=3.29, d0_v=3.54, y_explo=1.20 |
| 06   | -911942.8750 | 12.60      | y_att=0.10, y_ali=1.82, y_f=0.90, d0_att=3.44, l_att=4.16, l_ali=24.85, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.13, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.94, y_acc=0.03, l_acc=3.29, d0_v=3.54, y_explo=1.20 |
| 07   | -1031789.3750 | 11.98      | y_att=0.10, y_ali=0.80, y_f=10.95, d0_att=10.06, l_att=8.89, l_ali=15.80, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.07, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.94, y_acc=0.16, l_acc=0.91, d0_v=0.97, y_explo=1.37 |
| 08   | -1031789.3750 | 12.58      | y_att=0.10, y_ali=0.80, y_f=10.95, d0_att=10.06, l_att=8.89, l_ali=15.80, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.07, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.94, y_acc=0.16, l_acc=0.91, d0_v=0.97, y_explo=1.37 |
| 09   | -1031789.3750 | 11.84      | y_att=0.10, y_ali=0.80, y_f=10.95, d0_att=10.06, l_att=8.89, l_ali=15.80, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.07, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.94, y_acc=0.16, l_acc=0.91, d0_v=0.97, y_explo=1.37 |
| 10   | -1031789.3750 | 12.48      | y_att=0.10, y_ali=0.80, y_f=10.95, d0_att=10.06, l_att=8.89, l_ali=15.80, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.07, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.94, y_acc=0.16, l_acc=0.91, d0_v=0.97, y_explo=1.37 |
| 11   | -1031789.3750 | 12.26      | y_att=0.10, y_ali=0.80, y_f=10.95, d0_att=10.06, l_att=8.89, l_ali=15.80, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.07, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.94, y_acc=0.16, l_acc=0.91, d0_v=0.97, y_explo=1.37 |
| 12   | -1031789.3750 | 12.63      | y_att=0.10, y_ali=0.80, y_f=10.95, d0_att=10.06, l_att=8.89, l_ali=15.80, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.07, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.94, y_acc=0.16, l_acc=0.91, d0_v=0.97, y_explo=1.37 |
| 13   | -1031789.3750 | 12.70      | y_att=0.10, y_ali=0.80, y_f=10.95, d0_att=10.06, l_att=8.89, l_ali=15.80, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.07, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.94, y_acc=0.16, l_acc=0.91, d0_v=0.97, y_explo=1.37 |
| 14   | -1031789.3750 | 12.32      | y_att=0.10, y_ali=0.80, y_f=10.95, d0_att=10.06, l_att=8.89, l_ali=15.80, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.07, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.94, y_acc=0.16, l_acc=0.91, d0_v=0.97, y_explo=1.37 |
| 15   | -1031789.3750 | 12.62      | y_att=0.10, y_ali=0.80, y_f=10.95, d0_att=10.06, l_att=8.89, l_ali=15.80, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.07, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.94, y_acc=0.16, l_acc=0.91, d0_v=0.97, y_explo=1.37 |
| 16   | -1031789.3750 | 13.10      | y_att=0.10, y_ali=0.80, y_f=10.95, d0_att=10.06, l_att=8.89, l_ali=15.80, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.07, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.94, y_acc=0.16, l_acc=0.91, d0_v=0.97, y_explo=1.37 |
| 17   | -1031789.3750 | 12.50      | y_att=0.10, y_ali=0.80, y_f=10.95, d0_att=10.06, l_att=8.89, l_ali=15.80, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.07, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.94, y_acc=0.16, l_acc=0.91, d0_v=0.97, y_explo=1.37 |
| 18   | -1031789.3750 | 12.12      | y_att=0.10, y_ali=0.80, y_f=10.95, d0_att=10.06, l_att=8.89, l_ali=15.80, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.07, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.94, y_acc=0.16, l_acc=0.91, d0_v=0.97, y_explo=1.37 |
| 19   | -1031789.3750 | 12.22      | y_att=0.10, y_ali=0.80, y_f=10.95, d0_att=10.06, l_att=8.89, l_ali=15.80, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.07, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.94, y_acc=0.16, l_acc=0.91, d0_v=0.97, y_explo=1.37 |

**End of experiment.**
