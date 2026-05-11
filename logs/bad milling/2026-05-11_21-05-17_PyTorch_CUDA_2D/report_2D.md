# Experiment Report - PyTorch_CUDA (2D)
**Date:** 2026-05-11_21-05-17

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
| 00   | 1606.1488    | 11.99      | y_att=3.58, y_ali=0.05, y_f=1.26, d0_att=7.97, l_att=11.06, l_ali=1.03, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.94, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.55, y_acc=1.35, l_acc=1.99, d0_v=1.27, y_explo=4.68 |
| 01   | 1606.1488    | 11.52      | y_att=3.58, y_ali=0.05, y_f=1.26, d0_att=7.97, l_att=11.06, l_ali=1.03, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.94, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.55, y_acc=1.35, l_acc=1.99, d0_v=1.27, y_explo=4.68 |
| 02   | 1606.1488    | 11.86      | y_att=3.58, y_ali=0.05, y_f=1.26, d0_att=7.97, l_att=11.06, l_ali=1.03, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.94, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.55, y_acc=1.35, l_acc=1.99, d0_v=1.27, y_explo=4.68 |
| 03   | 1606.1488    | 11.38      | y_att=3.58, y_ali=0.05, y_f=1.26, d0_att=7.97, l_att=11.06, l_ali=1.03, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.94, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.55, y_acc=1.35, l_acc=1.99, d0_v=1.27, y_explo=4.68 |
| 04   | 1606.1488    | 11.66      | y_att=3.58, y_ali=0.05, y_f=1.26, d0_att=7.97, l_att=11.06, l_ali=1.03, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.94, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.55, y_acc=1.35, l_acc=1.99, d0_v=1.27, y_explo=4.68 |
| 05   | 1606.1488    | 11.59      | y_att=3.58, y_ali=0.05, y_f=1.26, d0_att=7.97, l_att=11.06, l_ali=1.03, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.94, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.55, y_acc=1.35, l_acc=1.99, d0_v=1.27, y_explo=4.68 |
| 06   | 1606.1488    | 11.70      | y_att=3.58, y_ali=0.05, y_f=1.26, d0_att=7.97, l_att=11.06, l_ali=1.03, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.94, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.55, y_acc=1.35, l_acc=1.99, d0_v=1.27, y_explo=4.68 |
| 07   | 1606.1488    | 11.49      | y_att=3.58, y_ali=0.05, y_f=1.26, d0_att=7.97, l_att=11.06, l_ali=1.03, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.94, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.55, y_acc=1.35, l_acc=1.99, d0_v=1.27, y_explo=4.68 |
| 08   | 1606.1488    | 11.52      | y_att=3.58, y_ali=0.05, y_f=1.26, d0_att=7.97, l_att=11.06, l_ali=1.03, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.94, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.55, y_acc=1.35, l_acc=1.99, d0_v=1.27, y_explo=4.68 |
| 09   | 1606.1488    | 11.60      | y_att=3.58, y_ali=0.05, y_f=1.26, d0_att=7.97, l_att=11.06, l_ali=1.03, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.94, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.55, y_acc=1.35, l_acc=1.99, d0_v=1.27, y_explo=4.68 |
| 10   | 1606.1488    | 11.77      | y_att=3.58, y_ali=0.05, y_f=1.26, d0_att=7.97, l_att=11.06, l_ali=1.03, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.94, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.55, y_acc=1.35, l_acc=1.99, d0_v=1.27, y_explo=4.68 |
| 11   | 1606.1488    | 11.37      | y_att=3.58, y_ali=0.05, y_f=1.26, d0_att=7.97, l_att=11.06, l_ali=1.03, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.94, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.55, y_acc=1.35, l_acc=1.99, d0_v=1.27, y_explo=4.68 |
| 12   | 1606.1488    | 11.32      | y_att=3.58, y_ali=0.05, y_f=1.26, d0_att=7.97, l_att=11.06, l_ali=1.03, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.94, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.55, y_acc=1.35, l_acc=1.99, d0_v=1.27, y_explo=4.68 |
| 13   | 1606.1488    | 11.30      | y_att=3.58, y_ali=0.05, y_f=1.26, d0_att=7.97, l_att=11.06, l_ali=1.03, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.94, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.55, y_acc=1.35, l_acc=1.99, d0_v=1.27, y_explo=4.68 |
| 14   | 1606.1488    | 11.60      | y_att=3.58, y_ali=0.05, y_f=1.26, d0_att=7.97, l_att=11.06, l_ali=1.03, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.94, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.55, y_acc=1.35, l_acc=1.99, d0_v=1.27, y_explo=4.68 |
| 15   | 1606.1488    | 11.50      | y_att=3.58, y_ali=0.05, y_f=1.26, d0_att=7.97, l_att=11.06, l_ali=1.03, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.94, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.55, y_acc=1.35, l_acc=1.99, d0_v=1.27, y_explo=4.68 |
| 16   | 1606.1488    | 11.56      | y_att=3.58, y_ali=0.05, y_f=1.26, d0_att=7.97, l_att=11.06, l_ali=1.03, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.94, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.55, y_acc=1.35, l_acc=1.99, d0_v=1.27, y_explo=4.68 |
| 17   | 1606.1488    | 11.43      | y_att=3.58, y_ali=0.05, y_f=1.26, d0_att=7.97, l_att=11.06, l_ali=1.03, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.94, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.55, y_acc=1.35, l_acc=1.99, d0_v=1.27, y_explo=4.68 |
| 18   | 1606.1488    | 11.82      | y_att=3.58, y_ali=0.05, y_f=1.26, d0_att=7.97, l_att=11.06, l_ali=1.03, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.94, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.55, y_acc=1.35, l_acc=1.99, d0_v=1.27, y_explo=4.68 |
| 19   | 1606.1488    | 11.38      | y_att=3.58, y_ali=0.05, y_f=1.26, d0_att=7.97, l_att=11.06, l_ali=1.03, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.94, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.55, y_acc=1.35, l_acc=1.99, d0_v=1.27, y_explo=4.68 |

**End of experiment.**
