# Experiment Report - PyTorch_CUDA (3D)
**Date:** 2026-04-23_14-55-19

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
| NB_DRONES            | 30         |
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
| 00   | -1280.1294   | 4.38       | y_att=0.64, y_ali=0.89, y_f=1.03, d0_att=1.51, l_att=1.86, l_ali=3.92, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.28, y_acc=0.31, l_acc=1.26, d0_v=1.88 |
| 01   | -1280.1294   | 3.20       | y_att=0.64, y_ali=0.89, y_f=1.03, d0_att=1.51, l_att=1.86, l_ali=3.92, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.28, y_acc=0.31, l_acc=1.26, d0_v=1.88 |
| 02   | -1505.3894   | 3.19       | y_att=1.02, y_ali=2.92, y_f=0.45, d0_att=1.64, l_att=2.29, l_ali=2.37, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.08, y_acc=0.03, l_acc=0.44, d0_v=3.56 |
| 03   | -1513.2567   | 4.14       | y_att=4.04, y_ali=0.21, y_f=0.36, d0_att=1.34, l_att=3.39, l_ali=1.88, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.54, y_acc=0.06, l_acc=0.82, d0_v=3.25 |
| 04   | -1513.2567   | 3.16       | y_att=4.04, y_ali=0.21, y_f=0.36, d0_att=1.34, l_att=3.39, l_ali=1.88, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.54, y_acc=0.06, l_acc=0.82, d0_v=3.25 |
| 05   | -1524.8436   | 3.15       | y_att=0.46, y_ali=0.00, y_f=0.57, d0_att=1.29, l_att=1.19, l_ali=2.74, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.68, y_acc=0.00, l_acc=0.73, d0_v=2.28 |
| 06   | -1524.8436   | 3.18       | y_att=0.46, y_ali=0.00, y_f=0.57, d0_att=1.29, l_att=1.19, l_ali=2.74, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.68, y_acc=0.00, l_acc=0.73, d0_v=2.28 |
| 07   | -1531.7579   | 4.15       | y_att=5.73, y_ali=0.04, y_f=0.43, d0_att=2.35, l_att=6.00, l_ali=3.33, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.41, y_acc=0.05, l_acc=0.49, d0_v=1.85 |
| 08   | -1531.7579   | 3.20       | y_att=5.73, y_ali=0.04, y_f=0.43, d0_att=2.35, l_att=6.00, l_ali=3.33, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.41, y_acc=0.05, l_acc=0.49, d0_v=1.85 |
| 09   | -1531.7579   | 3.17       | y_att=5.73, y_ali=0.04, y_f=0.43, d0_att=2.35, l_att=6.00, l_ali=3.33, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.41, y_acc=0.05, l_acc=0.49, d0_v=1.85 |
| 10   | -1531.7579   | 3.17       | y_att=5.73, y_ali=0.04, y_f=0.43, d0_att=2.35, l_att=6.00, l_ali=3.33, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.41, y_acc=0.05, l_acc=0.49, d0_v=1.85 |
| 11   | -1538.6577   | 4.15       | y_att=0.48, y_ali=11.28, y_f=0.45, d0_att=3.85, l_att=0.42, l_ali=0.50, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.57, y_acc=0.00, l_acc=1.11, d0_v=0.93 |
| 12   | -1538.6577   | 3.17       | y_att=0.48, y_ali=11.28, y_f=0.45, d0_att=3.85, l_att=0.42, l_ali=0.50, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.57, y_acc=0.00, l_acc=1.11, d0_v=0.93 |
| 13   | -1555.4576   | 3.15       | y_att=0.33, y_ali=1.74, y_f=0.55, d0_att=4.38, l_att=0.70, l_ali=1.23, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.00, y_acc=0.00, l_acc=0.68, d0_v=1.51 |
| 14   | -1555.4576   | 3.15       | y_att=0.33, y_ali=1.74, y_f=0.55, d0_att=4.38, l_att=0.70, l_ali=1.23, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.00, y_acc=0.00, l_acc=0.68, d0_v=1.51 |
| 15   | -1555.4576   | 4.11       | y_att=0.33, y_ali=1.74, y_f=0.55, d0_att=4.38, l_att=0.70, l_ali=1.23, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.00, y_acc=0.00, l_acc=0.68, d0_v=1.51 |
| 16   | -1555.4576   | 3.16       | y_att=0.33, y_ali=1.74, y_f=0.55, d0_att=4.38, l_att=0.70, l_ali=1.23, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.00, y_acc=0.00, l_acc=0.68, d0_v=1.51 |
| 17   | -1555.4576   | 3.12       | y_att=0.33, y_ali=1.74, y_f=0.55, d0_att=4.38, l_att=0.70, l_ali=1.23, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.00, y_acc=0.00, l_acc=0.68, d0_v=1.51 |
| 18   | -1559.3025   | 4.06       | y_att=0.47, y_ali=2.60, y_f=0.54, d0_att=1.31, l_att=0.11, l_ali=3.14, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.00, y_acc=0.00, l_acc=0.41, d0_v=4.13 |
| 19   | -1559.3025   | 3.13       | y_att=0.47, y_ali=2.60, y_f=0.54, d0_att=1.31, l_att=0.11, l_ali=3.14, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.00, y_acc=0.00, l_acc=0.41, d0_v=4.13 |

**End of experiment.**
