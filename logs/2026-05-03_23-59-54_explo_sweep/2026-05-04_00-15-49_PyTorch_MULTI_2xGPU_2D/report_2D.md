# Experiment Report - PyTorch_MULTI_2xGPU (2D)
**Date:** 2026-05-04_00-15-49

## 1. Initial Configuration
| Parameter | Value |
| :--- | :--- |
| ALPHA_LPF            | 0.2        |
| ARENA_RADIUS         | 50.0       |
| COLLISION_DIST       | 0.4        |
| DT                   | 0.1        |
| ENABLE_3D            | False      |
| EXPLO_STRATEGY       | local_gradient |
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
| 00   | -113607.7266 | 7.09       | y_att=0.13, y_ali=1.93, y_f=0.67, d0_att=5.12, l_att=5.92, l_ali=4.71, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.77, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.40, y_acc=0.00, l_acc=1.89, d0_v=1.58, y_explo=3.46 |
| 01   | -113607.7266 | 6.79       | y_att=0.13, y_ali=1.93, y_f=0.67, d0_att=5.12, l_att=5.92, l_ali=4.71, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.77, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.40, y_acc=0.00, l_acc=1.89, d0_v=1.58, y_explo=3.46 |
| 02   | -262318.7188 | 6.81       | y_att=0.21, y_ali=0.61, y_f=0.96, d0_att=9.22, l_att=5.42, l_ali=3.25, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.49, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.55, y_acc=0.00, l_acc=0.10, d0_v=3.34, y_explo=2.02 |
| 03   | -262318.7188 | 6.80       | y_att=0.21, y_ali=0.61, y_f=0.96, d0_att=9.22, l_att=5.42, l_ali=3.25, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.49, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.55, y_acc=0.00, l_acc=0.10, d0_v=3.34, y_explo=2.02 |
| 04   | -262318.7188 | 6.81       | y_att=0.21, y_ali=0.61, y_f=0.96, d0_att=9.22, l_att=5.42, l_ali=3.25, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.49, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.55, y_acc=0.00, l_acc=0.10, d0_v=3.34, y_explo=2.02 |
| 05   | -268246.9062 | 6.79       | y_att=0.10, y_ali=3.22, y_f=2.16, d0_att=5.08, l_att=0.78, l_ali=2.66, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.58, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.91, y_acc=0.09, l_acc=0.26, d0_v=0.68, y_explo=2.39 |
| 06   | -268246.9062 | 6.79       | y_att=0.10, y_ali=3.22, y_f=2.16, d0_att=5.08, l_att=0.78, l_ali=2.66, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.58, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.91, y_acc=0.09, l_acc=0.26, d0_v=0.68, y_explo=2.39 |
| 07   | -276557.9062 | 6.81       | y_att=0.29, y_ali=2.11, y_f=1.58, d0_att=4.79, l_att=3.16, l_ali=16.06, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.43, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.22, y_acc=0.08, l_acc=1.93, d0_v=2.29, y_explo=2.15 |
| 08   | -338513.0000 | 6.82       | y_att=1.27, y_ali=2.25, y_f=1.20, d0_att=8.81, l_att=1.62, l_ali=14.61, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.90, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.36, y_acc=0.14, l_acc=1.27, d0_v=4.06, y_explo=2.48 |
| 09   | -434002.4375 | 6.83       | y_att=0.44, y_ali=1.23, y_f=0.64, d0_att=3.89, l_att=2.72, l_ali=29.30, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.37, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.04, l_acc=2.42, d0_v=4.43, y_explo=0.64 |
| 10   | -515884.1875 | 6.83       | y_att=0.12, y_ali=0.96, y_f=2.67, d0_att=6.71, l_att=0.46, l_ali=15.70, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.38, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.00, y_acc=0.15, l_acc=0.53, d0_v=3.66, y_explo=0.59 |
| 11   | -517428.8125 | 6.82       | y_att=0.10, y_ali=1.16, y_f=0.87, d0_att=8.31, l_att=1.10, l_ali=15.57, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.87, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.03, l_acc=1.22, d0_v=2.87, y_explo=2.90 |
| 12   | -517428.8125 | 6.81       | y_att=0.10, y_ali=1.16, y_f=0.87, d0_att=8.31, l_att=1.10, l_ali=15.57, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.87, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.03, l_acc=1.22, d0_v=2.87, y_explo=2.90 |
| 13   | -517428.8125 | 6.81       | y_att=0.10, y_ali=1.16, y_f=0.87, d0_att=8.31, l_att=1.10, l_ali=15.57, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.87, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.03, l_acc=1.22, d0_v=2.87, y_explo=2.90 |
| 14   | -517428.8125 | 6.84       | y_att=0.10, y_ali=1.16, y_f=0.87, d0_att=8.31, l_att=1.10, l_ali=15.57, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.87, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.03, l_acc=1.22, d0_v=2.87, y_explo=2.90 |
| 15   | -517428.8125 | 6.90       | y_att=0.10, y_ali=1.16, y_f=0.87, d0_att=8.31, l_att=1.10, l_ali=15.57, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.87, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.03, l_acc=1.22, d0_v=2.87, y_explo=2.90 |
| 16   | -517428.8125 | 6.86       | y_att=0.10, y_ali=1.16, y_f=0.87, d0_att=8.31, l_att=1.10, l_ali=15.57, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.87, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.03, l_acc=1.22, d0_v=2.87, y_explo=2.90 |
| 17   | -517428.8125 | 6.83       | y_att=0.10, y_ali=1.16, y_f=0.87, d0_att=8.31, l_att=1.10, l_ali=15.57, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.87, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.03, l_acc=1.22, d0_v=2.87, y_explo=2.90 |
| 18   | -517428.8125 | 6.85       | y_att=0.10, y_ali=1.16, y_f=0.87, d0_att=8.31, l_att=1.10, l_ali=15.57, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.87, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.03, l_acc=1.22, d0_v=2.87, y_explo=2.90 |
| 19   | -517428.8125 | 6.86       | y_att=0.10, y_ali=1.16, y_f=0.87, d0_att=8.31, l_att=1.10, l_ali=15.57, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.87, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.03, l_acc=1.22, d0_v=2.87, y_explo=2.90 |

**End of experiment.**
