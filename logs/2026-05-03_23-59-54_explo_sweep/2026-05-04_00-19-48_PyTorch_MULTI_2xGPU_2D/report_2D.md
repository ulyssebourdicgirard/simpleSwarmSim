# Experiment Report - PyTorch_MULTI_2xGPU (2D)
**Date:** 2026-05-04_00-19-48

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
| 00   | -102755.4688 | 7.20       | y_att=0.16, y_ali=2.64, y_f=1.43, d0_att=4.18, l_att=2.07, l_ali=3.56, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.80, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.35, y_acc=0.24, l_acc=0.55, d0_v=1.43, y_explo=1.10 |
| 01   | -103815.6953 | 6.85       | y_att=0.30, y_ali=2.91, y_f=0.68, d0_att=1.36, l_att=1.17, l_ali=4.68, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.98, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.87, y_acc=0.01, l_acc=0.52, d0_v=2.18, y_explo=4.43 |
| 02   | -168752.6875 | 6.83       | y_att=0.10, y_ali=1.85, y_f=1.14, d0_att=7.37, l_att=0.24, l_ali=3.64, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.33, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.82, y_acc=0.02, l_acc=1.49, d0_v=2.68, y_explo=3.17 |
| 03   | -208794.1406 | 6.87       | y_att=1.30, y_ali=4.45, y_f=0.82, d0_att=5.27, l_att=1.13, l_ali=13.52, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.62, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.08, y_acc=0.06, l_acc=1.03, d0_v=1.74, y_explo=2.69 |
| 04   | -208794.1406 | 6.87       | y_att=1.30, y_ali=4.45, y_f=0.82, d0_att=5.27, l_att=1.13, l_ali=13.52, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.62, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.08, y_acc=0.06, l_acc=1.03, d0_v=1.74, y_explo=2.69 |
| 05   | -527494.4375 | 6.86       | y_att=0.25, y_ali=1.65, y_f=1.65, d0_att=3.49, l_att=2.24, l_ali=16.15, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.95, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.93, y_acc=0.20, l_acc=0.31, d0_v=2.93, y_explo=1.76 |
| 06   | -527494.4375 | 6.89       | y_att=0.25, y_ali=1.65, y_f=1.65, d0_att=3.49, l_att=2.24, l_ali=16.15, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.95, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.93, y_acc=0.20, l_acc=0.31, d0_v=2.93, y_explo=1.76 |
| 07   | -527494.4375 | 6.87       | y_att=0.25, y_ali=1.65, y_f=1.65, d0_att=3.49, l_att=2.24, l_ali=16.15, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.95, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.93, y_acc=0.20, l_acc=0.31, d0_v=2.93, y_explo=1.76 |
| 08   | -527494.4375 | 6.82       | y_att=0.25, y_ali=1.65, y_f=1.65, d0_att=3.49, l_att=2.24, l_ali=16.15, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.95, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.93, y_acc=0.20, l_acc=0.31, d0_v=2.93, y_explo=1.76 |
| 09   | -527494.4375 | 6.87       | y_att=0.25, y_ali=1.65, y_f=1.65, d0_att=3.49, l_att=2.24, l_ali=16.15, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.95, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.93, y_acc=0.20, l_acc=0.31, d0_v=2.93, y_explo=1.76 |
| 10   | -527494.4375 | 6.85       | y_att=0.25, y_ali=1.65, y_f=1.65, d0_att=3.49, l_att=2.24, l_ali=16.15, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.95, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.93, y_acc=0.20, l_acc=0.31, d0_v=2.93, y_explo=1.76 |
| 11   | -527494.4375 | 6.87       | y_att=0.25, y_ali=1.65, y_f=1.65, d0_att=3.49, l_att=2.24, l_ali=16.15, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.95, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.93, y_acc=0.20, l_acc=0.31, d0_v=2.93, y_explo=1.76 |
| 12   | -527494.4375 | 6.87       | y_att=0.25, y_ali=1.65, y_f=1.65, d0_att=3.49, l_att=2.24, l_ali=16.15, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.95, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.93, y_acc=0.20, l_acc=0.31, d0_v=2.93, y_explo=1.76 |
| 13   | -527494.4375 | 6.86       | y_att=0.25, y_ali=1.65, y_f=1.65, d0_att=3.49, l_att=2.24, l_ali=16.15, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.95, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.93, y_acc=0.20, l_acc=0.31, d0_v=2.93, y_explo=1.76 |
| 14   | -527494.4375 | 6.89       | y_att=0.25, y_ali=1.65, y_f=1.65, d0_att=3.49, l_att=2.24, l_ali=16.15, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.95, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.93, y_acc=0.20, l_acc=0.31, d0_v=2.93, y_explo=1.76 |
| 15   | -528484.8750 | 6.87       | y_att=0.20, y_ali=1.53, y_f=1.37, d0_att=2.75, l_att=0.32, l_ali=25.56, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.32, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.03, y_acc=0.06, l_acc=0.48, d0_v=0.78, y_explo=6.36 |
| 16   | -528484.8750 | 6.87       | y_att=0.20, y_ali=1.53, y_f=1.37, d0_att=2.75, l_att=0.32, l_ali=25.56, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.32, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.03, y_acc=0.06, l_acc=0.48, d0_v=0.78, y_explo=6.36 |
| 17   | -528484.8750 | 6.87       | y_att=0.20, y_ali=1.53, y_f=1.37, d0_att=2.75, l_att=0.32, l_ali=25.56, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.32, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.03, y_acc=0.06, l_acc=0.48, d0_v=0.78, y_explo=6.36 |
| 18   | -528484.8750 | 6.87       | y_att=0.20, y_ali=1.53, y_f=1.37, d0_att=2.75, l_att=0.32, l_ali=25.56, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.32, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.03, y_acc=0.06, l_acc=0.48, d0_v=0.78, y_explo=6.36 |
| 19   | -528484.8750 | 6.86       | y_att=0.20, y_ali=1.53, y_f=1.37, d0_att=2.75, l_att=0.32, l_ali=25.56, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.32, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.03, y_acc=0.06, l_acc=0.48, d0_v=0.78, y_explo=6.36 |

**End of experiment.**
