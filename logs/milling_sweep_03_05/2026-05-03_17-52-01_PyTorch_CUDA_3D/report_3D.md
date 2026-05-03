# Experiment Report - PyTorch_CUDA (3D)
**Date:** 2026-05-03_17-52-01

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
| FULL_MILLING_MODE    | True       |
| GEN_CPU              | 20         |
| GEN_GPU              | 10         |
| GRID_RES             | 5.0        |
| MAP_STRATEGY         | local_shared |
| MAX_SPEED            | 30.0       |
| MAX_YAW_RATE         | 3.14       |
| MIN_SPAWN_DIST       | 2.0        |
| NB_DRONES            | 20         |
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
| 00   | -1138.6438   | 4.13       | y_att=0.91, y_ali=3.80, y_f=1.79, d0_att=3.75, l_att=4.62, l_ali=3.16, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.80, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.83, y_acc=0.22, l_acc=3.02, d0_v=2.04, y_explo=2.92 |
| 01   | -1535.5621   | 5.30       | y_att=1.95, y_ali=3.26, y_f=1.39, d0_att=3.35, l_att=4.59, l_ali=5.03, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.16, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.24, y_acc=1.74, l_acc=0.59, d0_v=0.76, y_explo=3.96 |
| 02   | -1535.5621   | 4.57       | y_att=1.95, y_ali=3.26, y_f=1.39, d0_att=3.35, l_att=4.59, l_ali=5.03, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.16, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.24, y_acc=1.74, l_acc=0.59, d0_v=0.76, y_explo=3.96 |
| 03   | -1535.5621   | 4.27       | y_att=1.95, y_ali=3.26, y_f=1.39, d0_att=3.35, l_att=4.59, l_ali=5.03, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.16, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.24, y_acc=1.74, l_acc=0.59, d0_v=0.76, y_explo=3.96 |
| 04   | -1985.8062   | 5.29       | y_att=0.10, y_ali=2.85, y_f=2.06, d0_att=1.94, l_att=5.56, l_ali=7.18, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.93, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.95, y_acc=0.48, l_acc=0.68, d0_v=3.80, y_explo=3.57 |
| 05   | -1985.8062   | 4.29       | y_att=0.10, y_ali=2.85, y_f=2.06, d0_att=1.94, l_att=5.56, l_ali=7.18, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.93, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.95, y_acc=0.48, l_acc=0.68, d0_v=3.80, y_explo=3.57 |
| 06   | -3509.6499   | 4.41       | y_att=0.39, y_ali=2.42, y_f=2.82, d0_att=2.14, l_att=0.98, l_ali=4.95, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.15, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.94, y_acc=0.12, l_acc=1.66, d0_v=0.79, y_explo=2.52 |
| 07   | -3509.6499   | 5.19       | y_att=0.39, y_ali=2.42, y_f=2.82, d0_att=2.14, l_att=0.98, l_ali=4.95, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.15, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.94, y_acc=0.12, l_acc=1.66, d0_v=0.79, y_explo=2.52 |
| 08   | -3509.6499   | 4.32       | y_att=0.39, y_ali=2.42, y_f=2.82, d0_att=2.14, l_att=0.98, l_ali=4.95, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.15, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.94, y_acc=0.12, l_acc=1.66, d0_v=0.79, y_explo=2.52 |
| 09   | -3509.6499   | 4.42       | y_att=0.39, y_ali=2.42, y_f=2.82, d0_att=2.14, l_att=0.98, l_ali=4.95, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.15, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.94, y_acc=0.12, l_acc=1.66, d0_v=0.79, y_explo=2.52 |

**End of experiment.**
