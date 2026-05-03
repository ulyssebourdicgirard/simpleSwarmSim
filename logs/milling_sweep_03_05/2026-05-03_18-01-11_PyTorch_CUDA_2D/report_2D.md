# Experiment Report - PyTorch_CUDA (2D)
**Date:** 2026-05-03_18-01-11

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
| NB_DRONES            | 15         |
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
| 00   | -4763.9771   | 3.17       | y_att=0.04, y_ali=1.79, y_f=1.55, d0_att=2.91, l_att=1.49, l_ali=3.62, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.62, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.18, y_acc=0.13, l_acc=1.20, d0_v=0.91, y_explo=1.67 |
| 01   | -4763.9771   | 4.02       | y_att=0.04, y_ali=1.79, y_f=1.55, d0_att=2.91, l_att=1.49, l_ali=3.62, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.62, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.18, y_acc=0.13, l_acc=1.20, d0_v=0.91, y_explo=1.67 |
| 02   | -4763.9771   | 3.09       | y_att=0.04, y_ali=1.79, y_f=1.55, d0_att=2.91, l_att=1.49, l_ali=3.62, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.62, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.18, y_acc=0.13, l_acc=1.20, d0_v=0.91, y_explo=1.67 |
| 03   | -4763.9771   | 3.09       | y_att=0.04, y_ali=1.79, y_f=1.55, d0_att=2.91, l_att=1.49, l_ali=3.62, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.62, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.18, y_acc=0.13, l_acc=1.20, d0_v=0.91, y_explo=1.67 |
| 04   | -4763.9771   | 3.11       | y_att=0.04, y_ali=1.79, y_f=1.55, d0_att=2.91, l_att=1.49, l_ali=3.62, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.62, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.18, y_acc=0.13, l_acc=1.20, d0_v=0.91, y_explo=1.67 |
| 05   | -4763.9771   | 4.29       | y_att=0.04, y_ali=1.79, y_f=1.55, d0_att=2.91, l_att=1.49, l_ali=3.62, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.62, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.18, y_acc=0.13, l_acc=1.20, d0_v=0.91, y_explo=1.67 |
| 06   | -5348.3276   | 3.15       | y_att=0.56, y_ali=2.28, y_f=2.48, d0_att=2.64, l_att=1.28, l_ali=5.13, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.04, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.22, y_acc=0.22, l_acc=0.79, d0_v=0.95, y_explo=5.26 |
| 07   | -5588.0444   | 3.07       | y_att=0.12, y_ali=1.98, y_f=1.54, d0_att=1.55, l_att=1.53, l_ali=4.89, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.35, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.02, l_acc=0.63, d0_v=0.87, y_explo=0.53 |
| 08   | -5588.0444   | 3.57       | y_att=0.12, y_ali=1.98, y_f=1.54, d0_att=1.55, l_att=1.53, l_ali=4.89, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.35, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.02, l_acc=0.63, d0_v=0.87, y_explo=0.53 |
| 09   | -5850.0049   | 3.97       | y_att=0.54, y_ali=1.12, y_f=0.97, d0_att=2.51, l_att=1.22, l_ali=7.88, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.06, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.27, y_acc=0.22, l_acc=1.90, d0_v=1.60, y_explo=1.11 |

**End of experiment.**
