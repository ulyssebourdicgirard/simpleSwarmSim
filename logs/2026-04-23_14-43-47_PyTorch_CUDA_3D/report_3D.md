# Experiment Report - PyTorch_CUDA (3D)
**Date:** 2026-04-23_14-43-47

## 1. Initial Configuration
| Parameter | Value |
| :--- | :--- |
| ALPHA_LPF            | 0.2        |
| ARENA_RADIUS         | 100.0      |
| COLLISION_DIST       | 0.4        |
| DT                   | 0.1        |
| ENABLE_3D            | True       |
| FULL_MILLING_MODE    | False      |
| GEN_CPU              | 20         |
| GEN_GPU              | 20         |
| GRID_RES             | 5.0        |
| MAX_SPEED            | 20.0       |
| MAX_YAW_RATE         | 3.14       |
| NB_DRONES            | 10         |
| NEIGHBORS            | 4          |
| POP_SIZE_CPU         | 150        |
| POP_SIZE_GPU         | 5000       |
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
| 00   | -792.8629    | 3.62       | y_att=0.88, y_ali=1.00, y_f=1.80, d0_att=1.90, l_att=4.31, l_ali=4.01, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.91, y_acc=0.48, l_acc=1.91, d0_v=1.82 |
| 01   | -792.8629    | 3.25       | y_att=0.88, y_ali=1.00, y_f=1.80, d0_att=1.90, l_att=4.31, l_ali=4.01, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.91, y_acc=0.48, l_acc=1.91, d0_v=1.82 |
| 02   | -792.8629    | 4.08       | y_att=0.88, y_ali=1.00, y_f=1.80, d0_att=1.90, l_att=4.31, l_ali=4.01, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.91, y_acc=0.48, l_acc=1.91, d0_v=1.82 |
| 03   | -792.8629    | 3.28       | y_att=0.88, y_ali=1.00, y_f=1.80, d0_att=1.90, l_att=4.31, l_ali=4.01, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.91, y_acc=0.48, l_acc=1.91, d0_v=1.82 |
| 04   | -792.8629    | 3.27       | y_att=0.88, y_ali=1.00, y_f=1.80, d0_att=1.90, l_att=4.31, l_ali=4.01, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.91, y_acc=0.48, l_acc=1.91, d0_v=1.82 |
| 05   | -792.8629    | 3.27       | y_att=0.88, y_ali=1.00, y_f=1.80, d0_att=1.90, l_att=4.31, l_ali=4.01, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.91, y_acc=0.48, l_acc=1.91, d0_v=1.82 |
| 06   | -792.8629    | 4.29       | y_att=0.88, y_ali=1.00, y_f=1.80, d0_att=1.90, l_att=4.31, l_ali=4.01, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.91, y_acc=0.48, l_acc=1.91, d0_v=1.82 |
| 07   | -792.8629    | 3.29       | y_att=0.88, y_ali=1.00, y_f=1.80, d0_att=1.90, l_att=4.31, l_ali=4.01, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.91, y_acc=0.48, l_acc=1.91, d0_v=1.82 |
| 08   | -792.8629    | 3.21       | y_att=0.88, y_ali=1.00, y_f=1.80, d0_att=1.90, l_att=4.31, l_ali=4.01, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.91, y_acc=0.48, l_acc=1.91, d0_v=1.82 |
| 09   | -792.8629    | 3.41       | y_att=0.88, y_ali=1.00, y_f=1.80, d0_att=1.90, l_att=4.31, l_ali=4.01, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.91, y_acc=0.48, l_acc=1.91, d0_v=1.82 |
| 10   | -792.8629    | 4.02       | y_att=0.88, y_ali=1.00, y_f=1.80, d0_att=1.90, l_att=4.31, l_ali=4.01, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.91, y_acc=0.48, l_acc=1.91, d0_v=1.82 |
| 11   | -792.8629    | 3.26       | y_att=0.88, y_ali=1.00, y_f=1.80, d0_att=1.90, l_att=4.31, l_ali=4.01, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.91, y_acc=0.48, l_acc=1.91, d0_v=1.82 |
| 12   | -792.8629    | 3.20       | y_att=0.88, y_ali=1.00, y_f=1.80, d0_att=1.90, l_att=4.31, l_ali=4.01, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.91, y_acc=0.48, l_acc=1.91, d0_v=1.82 |
| 13   | -792.8629    | 4.12       | y_att=0.88, y_ali=1.00, y_f=1.80, d0_att=1.90, l_att=4.31, l_ali=4.01, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.91, y_acc=0.48, l_acc=1.91, d0_v=1.82 |
| 14   | -792.8629    | 3.23       | y_att=0.88, y_ali=1.00, y_f=1.80, d0_att=1.90, l_att=4.31, l_ali=4.01, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.91, y_acc=0.48, l_acc=1.91, d0_v=1.82 |
| 15   | -810.4785    | 3.26       | y_att=2.74, y_ali=0.22, y_f=3.41, d0_att=0.93, l_att=2.19, l_ali=0.34, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.54, y_acc=0.40, l_acc=2.64, d0_v=1.15 |
| 16   | -810.4785    | 3.22       | y_att=2.74, y_ali=0.22, y_f=3.41, d0_att=0.93, l_att=2.19, l_ali=0.34, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.54, y_acc=0.40, l_acc=2.64, d0_v=1.15 |
| 17   | -810.4785    | 4.15       | y_att=2.74, y_ali=0.22, y_f=3.41, d0_att=0.93, l_att=2.19, l_ali=0.34, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.54, y_acc=0.40, l_acc=2.64, d0_v=1.15 |
| 18   | -810.4785    | 3.13       | y_att=2.74, y_ali=0.22, y_f=3.41, d0_att=0.93, l_att=2.19, l_ali=0.34, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.54, y_acc=0.40, l_acc=2.64, d0_v=1.15 |
| 19   | -810.4785    | 2.78       | y_att=2.74, y_ali=0.22, y_f=3.41, d0_att=0.93, l_att=2.19, l_ali=0.34, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.54, y_acc=0.40, l_acc=2.64, d0_v=1.15 |

**End of experiment.**
