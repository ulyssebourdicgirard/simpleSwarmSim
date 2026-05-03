# Experiment Report - PyTorch_CUDA (2D)
**Date:** 2026-05-03_17-59-40

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
| NB_DRONES            | 10         |
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
| 00   | -3347.5369   | 3.22       | y_att=1.08, y_ali=2.43, y_f=0.99, d0_att=7.73, l_att=6.13, l_ali=2.04, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.91, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.25, y_acc=0.43, l_acc=2.44, d0_v=2.59, y_explo=2.22 |
| 01   | -3347.5369   | 4.12       | y_att=1.08, y_ali=2.43, y_f=0.99, d0_att=7.73, l_att=6.13, l_ali=2.04, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.91, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.25, y_acc=0.43, l_acc=2.44, d0_v=2.59, y_explo=2.22 |
| 02   | -5105.0425   | 3.17       | y_att=0.10, y_ali=3.18, y_f=1.59, d0_att=9.22, l_att=1.71, l_ali=6.99, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.54, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.71, y_acc=0.09, l_acc=0.83, d0_v=1.37, y_explo=0.18 |
| 03   | -5105.0425   | 3.13       | y_att=0.10, y_ali=3.18, y_f=1.59, d0_att=9.22, l_att=1.71, l_ali=6.99, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.54, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.71, y_acc=0.09, l_acc=0.83, d0_v=1.37, y_explo=0.18 |
| 04   | -5570.9800   | 3.13       | y_att=1.15, y_ali=2.59, y_f=2.29, d0_att=4.02, l_att=6.71, l_ali=3.06, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.04, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.72, y_acc=1.08, l_acc=0.65, d0_v=0.80, y_explo=1.22 |
| 05   | -5570.9800   | 4.07       | y_att=1.15, y_ali=2.59, y_f=2.29, d0_att=4.02, l_att=6.71, l_ali=3.06, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.04, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.72, y_acc=1.08, l_acc=0.65, d0_v=0.80, y_explo=1.22 |
| 06   | -5570.9800   | 3.17       | y_att=1.15, y_ali=2.59, y_f=2.29, d0_att=4.02, l_att=6.71, l_ali=3.06, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.04, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.72, y_acc=1.08, l_acc=0.65, d0_v=0.80, y_explo=1.22 |
| 07   | -5570.9800   | 3.11       | y_att=1.15, y_ali=2.59, y_f=2.29, d0_att=4.02, l_att=6.71, l_ali=3.06, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.04, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.72, y_acc=1.08, l_acc=0.65, d0_v=0.80, y_explo=1.22 |
| 08   | -7671.6367   | 3.98       | y_att=0.13, y_ali=3.00, y_f=2.52, d0_att=0.99, l_att=0.46, l_ali=9.28, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.17, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.01, y_acc=0.62, l_acc=0.93, d0_v=1.61, y_explo=1.44 |
| 09   | -8349.3750   | 3.12       | y_att=0.12, y_ali=2.09, y_f=2.32, d0_att=4.99, l_att=1.89, l_ali=4.03, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.52, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.63, y_acc=0.12, l_acc=1.36, d0_v=0.57, y_explo=3.14 |

**End of experiment.**
