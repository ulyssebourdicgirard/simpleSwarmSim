# Experiment Report - PyTorch_CUDA (3D)
**Date:** 2026-04-12_20-46-30

## 1. Initial Configuration
| Parameter | Value |
| :--- | :--- |
| ARENA_RADIUS         | 50.0       |
| COLLISION_DIST       | 0.4        |
| DT                   | 0.1        |
| ENABLE_3D            | True       |
| GEN_CPU              | 20         |
| GEN_GPU              | 20         |
| GRID_RES             | 5.0        |
| MAX_SPEED            | 2.0        |
| NB_DRONES            | 5          |
| NEIGHBORS            | 3          |
| POP_SIZE_CPU         | 150        |
| POP_SIZE_GPU         | 5000       |
| SCENARIO             | exploration |
| SIM_STEPS            | 500        |
| VISU_STEPS           | 1000       |
| W_COLL               | 500.0      |
| W_DISP               | 0.0        |
| W_EFFORT             | 1          |
| W_EXPLO              | -50.0      |
| W_MILL               | 20.0       |
| W_POL                | -0.0       |
| Z_MAX                | 10.0       |
| Z_MIN                | 1.0        |

## 2. Optimization Evolution
| Gen  |  Best Cost   |  Time (s)  |                                                                All Parameters                                                                |
| :--: | :----------: | :--------: | :------------------------------------------------------------------------------------------------------------------------------------------ |
| 00   | -990.9689    | 3.40       | y_att=2.20, y_ali=0.81, y_f=0.74, d0_att=2.27, l_att=1.83, l_ali=3.83, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.02, y_acc=0.19, l_acc=0.69, d0_v=2.11 |
| 01   | -1028.9166   | 3.26       | y_att=0.87, y_ali=3.37, y_f=1.57, d0_att=2.57, l_att=3.60, l_ali=1.90, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.33, y_acc=0.29, l_acc=0.50, d0_v=2.04 |
| 02   | -1014.0897   | 3.46       | y_att=1.04, y_ali=1.92, y_f=0.70, d0_att=3.20, l_att=4.20, l_ali=4.29, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.01, y_acc=0.38, l_acc=0.80, d0_v=2.51 |
| 03   | -1095.2141   | 3.08       | y_att=1.72, y_ali=1.51, y_f=0.56, d0_att=2.16, l_att=2.19, l_ali=3.45, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.21, y_acc=0.11, l_acc=0.80, d0_v=1.11 |
| 04   | -1073.5968   | 3.02       | y_att=4.75, y_ali=1.07, y_f=1.03, d0_att=3.81, l_att=1.31, l_ali=2.39, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.27, y_acc=0.22, l_acc=0.50, d0_v=3.04 |
| 05   | -1069.2927   | 2.72       | y_att=0.57, y_ali=4.34, y_f=1.04, d0_att=5.58, l_att=4.64, l_ali=1.86, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.38, y_acc=0.22, l_acc=2.14, d0_v=6.16 |
| 06   | -1073.8584   | 2.75       | y_att=0.65, y_ali=0.03, y_f=0.62, d0_att=1.05, l_att=2.78, l_ali=2.24, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.27, y_acc=0.17, l_acc=0.75, d0_v=1.34 |
| 07   | -1098.4448   | 2.80       | y_att=3.44, y_ali=2.02, y_f=0.49, d0_att=5.36, l_att=2.38, l_ali=2.94, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.71, y_acc=0.17, l_acc=0.47, d0_v=1.31 |
| 08   | -1084.0105   | 2.80       | y_att=2.65, y_ali=1.30, y_f=0.54, d0_att=2.35, l_att=1.79, l_ali=3.97, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.21, y_acc=0.11, l_acc=0.74, d0_v=1.19 |
| 09   | -1123.7213   | 2.71       | y_att=3.55, y_ali=4.94, y_f=0.58, d0_att=8.77, l_att=3.23, l_ali=3.95, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.70, y_acc=0.16, l_acc=0.58, d0_v=1.42 |
| 10   | -1130.7281   | 3.00       | y_att=3.37, y_ali=3.05, y_f=0.60, d0_att=5.14, l_att=2.59, l_ali=2.03, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.59, y_acc=0.16, l_acc=0.47, d0_v=1.03 |
| 11   | -1097.3832   | 3.30       | y_att=1.27, y_ali=1.64, y_f=0.50, d0_att=3.91, l_att=3.54, l_ali=4.14, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.56, y_acc=0.19, l_acc=0.47, d0_v=1.10 |
| 12   | -1114.2906   | 3.19       | y_att=4.10, y_ali=4.94, y_f=0.58, d0_att=10.89, l_att=3.23, l_ali=3.95, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.70, y_acc=0.16, l_acc=0.58, d0_v=1.67 |
| 13   | -1103.7041   | 3.00       | y_att=2.82, y_ali=2.08, y_f=0.56, d0_att=4.99, l_att=2.78, l_ali=3.01, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.69, y_acc=0.20, l_acc=0.31, d0_v=0.82 |
| 14   | -1115.3265   | 2.97       | y_att=2.85, y_ali=2.82, y_f=0.56, d0_att=4.54, l_att=2.56, l_ali=2.19, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.41, y_acc=0.16, l_acc=0.45, d0_v=1.03 |
| 15   | -1130.3623   | 3.13       | y_att=1.81, y_ali=6.94, y_f=0.88, d0_att=3.68, l_att=2.00, l_ali=11.23, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.43, y_acc=0.22, l_acc=0.78, d0_v=1.15 |
| 16   | -1097.9751   | 2.92       | y_att=2.48, y_ali=1.75, y_f=0.51, d0_att=2.63, l_att=2.19, l_ali=3.35, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.00, y_acc=0.13, l_acc=0.66, d0_v=1.04 |
| 17   | -1094.9705   | 3.23       | y_att=2.14, y_ali=2.07, y_f=0.42, d0_att=3.59, l_att=2.38, l_ali=2.38, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.54, y_acc=0.23, l_acc=0.38, d0_v=1.78 |
| 18   | -1158.2816   | 3.23       | y_att=3.37, y_ali=3.50, y_f=0.88, d0_att=2.65, l_att=1.07, l_ali=12.23, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.95, y_acc=0.10, l_acc=0.85, d0_v=0.69 |
| 19   | -1121.0634   | 3.03       | y_att=2.07, y_ali=3.58, y_f=1.54, d0_att=3.31, l_att=1.34, l_ali=11.90, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.95, y_acc=0.13, l_acc=0.68, d0_v=0.69 |

**End of experiment.**
