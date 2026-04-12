# Experiment Report - PyTorch_CUDA (3D)
**Date:** 2026-04-12_21-13-40

## 1. Initial Configuration
| Parameter | Value |
| :--- | :--- |
| ARENA_RADIUS         | 100.0      |
| COLLISION_DIST       | 0.4        |
| DT                   | 0.01       |
| ENABLE_3D            | True       |
| GEN_CPU              | 20         |
| GEN_GPU              | 20         |
| GRID_RES             | 5.0        |
| MAX_SPEED            | 2.0        |
| NB_DRONES            | 25         |
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
| 00   | -884.9854    | 3.22       | y_att=4.87, y_ali=1.21, y_f=1.62, d0_att=2.22, l_att=4.57, l_ali=4.42, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.58, y_acc=1.80, l_acc=3.96, d0_v=0.54 |
| 01   | -814.3343    | 3.00       | y_att=4.87, y_ali=1.21, y_f=1.62, d0_att=2.22, l_att=4.57, l_ali=4.42, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.58, y_acc=1.80, l_acc=3.96, d0_v=0.54 |
| 02   | -956.1813    | 2.94       | y_att=4.87, y_ali=1.58, y_f=1.62, d0_att=2.61, l_att=4.57, l_ali=5.92, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.58, y_acc=1.20, l_acc=5.77, d0_v=0.52 |
| 03   | -962.6957    | 2.97       | y_att=4.87, y_ali=1.58, y_f=1.62, d0_att=2.61, l_att=4.57, l_ali=5.92, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.58, y_acc=1.20, l_acc=5.77, d0_v=0.52 |
| 04   | -962.6957    | 3.06       | y_att=4.87, y_ali=1.58, y_f=1.62, d0_att=2.61, l_att=4.57, l_ali=5.92, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.58, y_acc=1.20, l_acc=5.77, d0_v=0.52 |
| 05   | -987.5851    | 2.87       | y_att=4.87, y_ali=1.67, y_f=1.48, d0_att=2.44, l_att=4.52, l_ali=5.92, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.58, y_acc=1.20, l_acc=5.77, d0_v=0.56 |
| 06   | -1001.0010   | 2.93       | y_att=4.87, y_ali=1.58, y_f=1.54, d0_att=2.57, l_att=4.57, l_ali=5.92, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.58, y_acc=1.10, l_acc=6.08, d0_v=0.52 |
| 07   | -1006.4606   | 2.83       | y_att=1.58, y_ali=5.25, y_f=1.86, d0_att=1.07, l_att=5.29, l_ali=1.51, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.10, y_acc=2.12, l_acc=2.93, d0_v=0.43 |
| 08   | -1015.1808   | 2.81       | y_att=4.87, y_ali=1.21, y_f=1.95, d0_att=2.18, l_att=4.53, l_ali=4.49, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.58, y_acc=1.70, l_acc=3.99, d0_v=0.44 |
| 09   | -1022.8945   | 2.96       | y_att=5.31, y_ali=1.56, y_f=1.54, d0_att=2.57, l_att=4.23, l_ali=5.92, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.58, y_acc=1.10, l_acc=6.08, d0_v=0.51 |
| 10   | -1012.8860   | 2.94       | y_att=4.87, y_ali=1.62, y_f=1.95, d0_att=2.18, l_att=4.53, l_ali=4.49, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.58, y_acc=1.70, l_acc=3.99, d0_v=0.44 |
| 11   | -1134.7764   | 3.18       | y_att=5.36, y_ali=2.78, y_f=1.63, d0_att=2.64, l_att=4.57, l_ali=8.48, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.34, y_acc=1.16, l_acc=5.77, d0_v=0.52 |
| 12   | -1059.9332   | 2.92       | y_att=4.87, y_ali=1.85, y_f=1.62, d0_att=2.67, l_att=4.43, l_ali=9.07, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.22, y_acc=1.20, l_acc=5.38, d0_v=0.53 |
| 13   | -1109.7589   | 2.85       | y_att=4.87, y_ali=1.85, y_f=1.62, d0_att=2.67, l_att=4.43, l_ali=9.07, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.22, y_acc=1.20, l_acc=5.38, d0_v=0.53 |
| 14   | -1093.0063   | 2.97       | y_att=4.87, y_ali=1.85, y_f=1.62, d0_att=2.67, l_att=4.43, l_ali=9.07, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.46, y_acc=1.20, l_acc=5.38, d0_v=0.53 |
| 15   | -1081.4728   | 2.82       | y_att=5.75, y_ali=2.57, y_f=1.71, d0_att=2.61, l_att=4.57, l_ali=8.60, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.69, y_acc=1.40, l_acc=5.00, d0_v=0.51 |
| 16   | -1162.4308   | 2.86       | y_att=8.05, y_ali=2.07, y_f=1.79, d0_att=4.51, l_att=5.26, l_ali=8.27, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.58, y_acc=1.24, l_acc=6.39, d0_v=0.55 |
| 17   | -1061.9988   | 3.29       | y_att=8.05, y_ali=2.07, y_f=1.79, d0_att=4.51, l_att=5.26, l_ali=8.27, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.58, y_acc=1.24, l_acc=6.39, d0_v=0.55 |
| 18   | -1061.9988   | 3.25       | y_att=8.05, y_ali=2.07, y_f=1.79, d0_att=4.51, l_att=5.26, l_ali=8.27, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.58, y_acc=1.24, l_acc=6.39, d0_v=0.55 |
| 19   | -1064.6415   | 3.08       | y_att=7.96, y_ali=2.07, y_f=1.72, d0_att=4.51, l_att=5.41, l_ali=8.27, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.07, y_acc=1.20, l_acc=8.60, d0_v=0.73 |

**End of experiment.**
