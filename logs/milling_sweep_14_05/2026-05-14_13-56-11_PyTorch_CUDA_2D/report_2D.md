# Experiment Report - PyTorch_CUDA (2D)
**Date:** 2026-05-14_13-56-11

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
| GEN_GPU              | 10         |
| GRID_RES             | 5.0        |
| MAP_STRATEGY         | local_shared |
| MAX_SPEED            | 20.0       |
| MAX_YAW_RATE         | 3.14       |
| MIN_SPAWN_DIST       | 2.0        |
| NB_DRONES            | 15         |
| NEIGHBORS            | 2          |
| N_INIT_CONDITIONS    | 4          |
| POP_SIZE_CPU         | 150        |
| POP_SIZE_GPU         | 5000       |
| REFRESH_MAP_TICKS    | 100        |
| SCENARIO             | default    |
| SIM_STEPS            | 400        |
| SPOIL_ADD            | 0.02       |
| SPOIL_MULT           | 1.002      |
| VISU_STEPS           | 800        |
| W_COLL               | 0          |
| W_DISP               | 0          |
| W_EFFORT             | 0          |
| W_EXPLO              | 0.0        |
| W_MILL               | -600.0     |
| W_POL                | 0          |
| W_STATIONARY         | 0          |
| Z_MAX                | 10.0       |
| Z_MIN                | 1.0        |

## 2. Optimization Evolution
| Gen  |  Best Cost   |  Time (s)  |                                                                All Parameters                                                                |
| :--: | :----------: | :--------: | :------------------------------------------------------------------------------------------------------------------------------------------ |
| 00   | -124327.1875 | 2.72       | y_att=4.29, y_ali=1.24, y_f=1.49, d0_att=6.27, l_att=5.80, l_ali=1.55, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.79, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.93, y_acc=0.38, l_acc=2.61, d0_v=2.63, y_explo=3.31 |
| 01   | -124327.1875 | 2.08       | y_att=4.29, y_ali=1.24, y_f=1.49, d0_att=6.27, l_att=5.80, l_ali=1.55, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.79, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.93, y_acc=0.38, l_acc=2.61, d0_v=2.63, y_explo=3.31 |
| 02   | -135155.4844 | 2.12       | y_att=3.94, y_ali=0.77, y_f=11.92, d0_att=7.95, l_att=6.77, l_ali=1.55, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.86, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.04, l_acc=0.82, d0_v=2.72, y_explo=0.76 |
| 03   | -186729.9844 | 2.09       | y_att=28.42, y_ali=5.27, y_f=0.94, d0_att=18.86, l_att=8.58, l_ali=3.90, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.35, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.56, y_acc=0.67, l_acc=0.65, d0_v=2.93, y_explo=4.13 |
| 04   | -186729.9844 | 2.05       | y_att=28.42, y_ali=5.27, y_f=0.94, d0_att=18.86, l_att=8.58, l_ali=3.90, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.35, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.56, y_acc=0.67, l_acc=0.65, d0_v=2.93, y_explo=4.13 |
| 05   | -188157.6719 | 2.04       | y_att=13.48, y_ali=2.46, y_f=1.85, d0_att=10.42, l_att=10.91, l_ali=3.50, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.61, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.70, y_acc=0.01, l_acc=1.02, d0_v=1.62, y_explo=0.28 |
| 06   | -188157.6719 | 2.49       | y_att=13.48, y_ali=2.46, y_f=1.85, d0_att=10.42, l_att=10.91, l_ali=3.50, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.61, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.70, y_acc=0.01, l_acc=1.02, d0_v=1.62, y_explo=0.28 |
| 07   | -188157.6719 | 2.04       | y_att=13.48, y_ali=2.46, y_f=1.85, d0_att=10.42, l_att=10.91, l_ali=3.50, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.61, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.70, y_acc=0.01, l_acc=1.02, d0_v=1.62, y_explo=0.28 |
| 08   | -188157.6719 | 2.07       | y_att=13.48, y_ali=2.46, y_f=1.85, d0_att=10.42, l_att=10.91, l_ali=3.50, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.61, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.70, y_acc=0.01, l_acc=1.02, d0_v=1.62, y_explo=0.28 |
| 09   | -188157.6719 | 2.05       | y_att=13.48, y_ali=2.46, y_f=1.85, d0_att=10.42, l_att=10.91, l_ali=3.50, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.61, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.70, y_acc=0.01, l_acc=1.02, d0_v=1.62, y_explo=0.28 |

**End of experiment.**
