# Experiment Report - PyTorch_CUDA (3D)
**Date:** 2026-05-03_17-54-00

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
| NB_DRONES            | 25         |
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
| 00   | -1310.0551   | 4.52       | y_att=0.33, y_ali=3.03, y_f=1.96, d0_att=6.49, l_att=8.35, l_ali=3.22, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.08, y_acc=0.67, l_acc=2.92, d0_v=1.86, y_explo=2.77 |
| 01   | -1310.0551   | 5.40       | y_att=0.33, y_ali=3.03, y_f=1.96, d0_att=6.49, l_att=8.35, l_ali=3.22, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.08, y_acc=0.67, l_acc=2.92, d0_v=1.86, y_explo=2.77 |
| 02   | -1310.0551   | 4.33       | y_att=0.33, y_ali=3.03, y_f=1.96, d0_att=6.49, l_att=8.35, l_ali=3.22, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.08, y_acc=0.67, l_acc=2.92, d0_v=1.86, y_explo=2.77 |
| 03   | -1310.0551   | 4.62       | y_att=0.33, y_ali=3.03, y_f=1.96, d0_att=6.49, l_att=8.35, l_ali=3.22, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.08, y_acc=0.67, l_acc=2.92, d0_v=1.86, y_explo=2.77 |
| 04   | -1450.7252   | 4.94       | y_att=0.75, y_ali=2.14, y_f=1.81, d0_att=4.08, l_att=1.19, l_ali=6.06, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.21, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.55, y_acc=0.68, l_acc=2.77, d0_v=1.59, y_explo=0.63 |
| 05   | -1450.7252   | 4.37       | y_att=0.75, y_ali=2.14, y_f=1.81, d0_att=4.08, l_att=1.19, l_ali=6.06, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.21, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.55, y_acc=0.68, l_acc=2.77, d0_v=1.59, y_explo=0.63 |
| 06   | -2072.9097   | 5.27       | y_att=0.40, y_ali=1.69, y_f=1.18, d0_att=3.70, l_att=1.06, l_ali=5.89, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.92, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.12, y_acc=0.64, l_acc=0.66, d0_v=0.69, y_explo=3.14 |
| 07   | -2072.9097   | 4.24       | y_att=0.40, y_ali=1.69, y_f=1.18, d0_att=3.70, l_att=1.06, l_ali=5.89, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.92, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.12, y_acc=0.64, l_acc=0.66, d0_v=0.69, y_explo=3.14 |
| 08   | -2933.1785   | 4.33       | y_att=0.38, y_ali=2.88, y_f=2.11, d0_att=2.55, l_att=2.62, l_ali=4.89, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.40, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.12, y_acc=0.47, l_acc=0.70, d0_v=0.61, y_explo=1.55 |
| 09   | -3964.0630   | 5.40       | y_att=0.12, y_ali=1.69, y_f=1.18, d0_att=3.70, l_att=1.06, l_ali=5.89, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.28, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.12, y_acc=0.64, l_acc=0.33, d0_v=1.83, y_explo=3.14 |

**End of experiment.**
