# Experiment Report - PyTorch_MULTI_2xGPU (3D)
**Date:** 2026-04-28_09-11-43

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
| NB_DRONES            | 25         |
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
| 00   | -2963.3223   | 40.77      | y_att=0.60, y_ali=2.71, y_f=0.74, d0_att=5.16, l_att=4.18, l_ali=3.54, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.70, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.63, y_acc=0.04, l_acc=2.74, d0_v=2.29, y_explo=0.18 |
| 01   | -2963.3223   | 40.42      | y_att=0.60, y_ali=2.71, y_f=0.74, d0_att=5.16, l_att=4.18, l_ali=3.54, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.70, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.63, y_acc=0.04, l_acc=2.74, d0_v=2.29, y_explo=0.18 |
| 02   | -2963.3223   | 40.41      | y_att=0.60, y_ali=2.71, y_f=0.74, d0_att=5.16, l_att=4.18, l_ali=3.54, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.70, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.63, y_acc=0.04, l_acc=2.74, d0_v=2.29, y_explo=0.18 |
| 03   | -3077.7324   | 40.41      | y_att=0.53, y_ali=2.25, y_f=1.46, d0_att=1.14, l_att=1.75, l_ali=2.10, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.55, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.04, l_acc=0.77, d0_v=0.72, y_explo=0.18 |
| 04   | -3235.2976   | 40.40      | y_att=1.35, y_ali=0.22, y_f=2.06, d0_att=0.96, l_att=1.41, l_ali=4.52, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.07, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.72, y_acc=0.49, l_acc=1.29, d0_v=3.33, y_explo=0.10 |
| 05   | -3235.2976   | 40.39      | y_att=1.35, y_ali=0.22, y_f=2.06, d0_att=0.96, l_att=1.41, l_ali=4.52, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.07, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.72, y_acc=0.49, l_acc=1.29, d0_v=3.33, y_explo=0.10 |
| 06   | -3247.6089   | 40.39      | y_att=0.62, y_ali=2.71, y_f=0.81, d0_att=1.08, l_att=1.53, l_ali=1.14, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.46, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.00, l_acc=1.26, d0_v=1.77, y_explo=0.10 |
| 07   | -3337.7937   | 40.38      | y_att=1.04, y_ali=0.04, y_f=1.36, d0_att=1.33, l_att=1.75, l_ali=1.91, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.39, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.82, y_acc=1.05, l_acc=0.47, d0_v=2.34, y_explo=0.10 |
| 08   | -3342.2896   | 40.38      | y_att=0.54, y_ali=1.07, y_f=1.49, d0_att=0.85, l_att=1.23, l_ali=1.40, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.74, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.82, y_acc=0.28, l_acc=0.77, d0_v=3.70, y_explo=0.12 |
| 09   | -3357.7698   | 40.38      | y_att=0.12, y_ali=0.05, y_f=1.77, d0_att=0.55, l_att=2.33, l_ali=2.79, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.57, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.10, l_acc=0.62, d0_v=1.13, y_explo=0.14 |
| 10   | -3433.7861   | 40.38      | y_att=0.16, y_ali=2.60, y_f=1.50, d0_att=0.70, l_att=1.87, l_ali=0.12, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.67, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.10, l_acc=0.47, d0_v=1.53, y_explo=0.10 |
| 11   | -3433.7861   | 40.38      | y_att=0.16, y_ali=2.60, y_f=1.50, d0_att=0.70, l_att=1.87, l_ali=0.12, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.67, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.10, l_acc=0.47, d0_v=1.53, y_explo=0.10 |
| 12   | -3433.7861   | 40.37      | y_att=0.16, y_ali=2.60, y_f=1.50, d0_att=0.70, l_att=1.87, l_ali=0.12, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.67, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.10, l_acc=0.47, d0_v=1.53, y_explo=0.10 |
| 13   | -3442.2566   | 40.37      | y_att=0.30, y_ali=0.04, y_f=1.45, d0_att=0.72, l_att=1.41, l_ali=2.01, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.22, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.10, l_acc=1.00, d0_v=1.50, y_explo=0.10 |
| 14   | -3496.1787   | 40.37      | y_att=0.10, y_ali=1.99, y_f=1.06, d0_att=0.50, l_att=1.43, l_ali=0.79, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.70, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.03, l_acc=0.54, d0_v=1.70, y_explo=0.10 |
| 15   | -3496.1787   | 40.37      | y_att=0.10, y_ali=1.99, y_f=1.06, d0_att=0.50, l_att=1.43, l_ali=0.79, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.70, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.03, l_acc=0.54, d0_v=1.70, y_explo=0.10 |
| 16   | -3496.1787   | 40.37      | y_att=0.10, y_ali=1.99, y_f=1.06, d0_att=0.50, l_att=1.43, l_ali=0.79, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.70, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.03, l_acc=0.54, d0_v=1.70, y_explo=0.10 |
| 17   | -3497.4973   | 40.37      | y_att=0.29, y_ali=0.12, y_f=0.74, d0_att=1.38, l_att=0.94, l_ali=2.13, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.67, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.06, l_acc=1.16, d0_v=0.46, y_explo=0.10 |
| 18   | -3524.7515   | 40.37      | y_att=0.94, y_ali=2.95, y_f=1.77, d0_att=0.54, l_att=1.02, l_ali=1.34, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.08, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.09, l_acc=0.51, d0_v=0.66, y_explo=0.10 |
| 19   | -3524.7515   | 40.37      | y_att=0.94, y_ali=2.95, y_f=1.77, d0_att=0.54, l_att=1.02, l_ali=1.34, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.08, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.09, l_acc=0.51, d0_v=0.66, y_explo=0.10 |

**End of experiment.**
