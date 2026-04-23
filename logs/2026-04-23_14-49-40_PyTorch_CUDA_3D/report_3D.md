# Experiment Report - PyTorch_CUDA (3D)
**Date:** 2026-04-23_14-49-40

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
| NB_DRONES            | 20         |
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
| 00   | -853.1703    | 3.35       | y_att=4.09, y_ali=3.38, y_f=1.93, d0_att=3.72, l_att=1.28, l_ali=1.86, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.68, y_acc=0.13, l_acc=1.79, d0_v=0.68 |
| 01   | -853.1703    | 3.86       | y_att=4.09, y_ali=3.38, y_f=1.93, d0_att=3.72, l_att=1.28, l_ali=1.86, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.68, y_acc=0.13, l_acc=1.79, d0_v=0.68 |
| 02   | -971.3434    | 2.82       | y_att=3.92, y_ali=2.55, y_f=0.74, d0_att=2.52, l_att=3.52, l_ali=0.71, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.90, y_acc=0.00, l_acc=5.03, d0_v=2.68 |
| 03   | -1010.6121   | 2.83       | y_att=9.32, y_ali=4.47, y_f=0.95, d0_att=2.32, l_att=3.74, l_ali=5.51, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.81, y_acc=0.00, l_acc=1.49, d0_v=2.13 |
| 04   | -1012.5198   | 2.82       | y_att=4.82, y_ali=0.81, y_f=0.65, d0_att=2.52, l_att=4.79, l_ali=0.71, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.10, y_acc=0.00, l_acc=1.92, d0_v=2.68 |
| 05   | -1047.9365   | 3.80       | y_att=4.82, y_ali=0.81, y_f=0.65, d0_att=2.52, l_att=4.79, l_ali=0.71, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.10, y_acc=0.00, l_acc=1.92, d0_v=2.68 |
| 06   | -1047.9365   | 2.81       | y_att=4.82, y_ali=0.81, y_f=0.65, d0_att=2.52, l_att=4.79, l_ali=0.71, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.10, y_acc=0.00, l_acc=1.92, d0_v=2.68 |
| 07   | -1047.9365   | 2.83       | y_att=4.82, y_ali=0.81, y_f=0.65, d0_att=2.52, l_att=4.79, l_ali=0.71, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.10, y_acc=0.00, l_acc=1.92, d0_v=2.68 |
| 08   | -1047.9365   | 2.82       | y_att=4.82, y_ali=0.81, y_f=0.65, d0_att=2.52, l_att=4.79, l_ali=0.71, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.10, y_acc=0.00, l_acc=1.92, d0_v=2.68 |
| 09   | -1047.9365   | 3.66       | y_att=4.82, y_ali=0.81, y_f=0.65, d0_att=2.52, l_att=4.79, l_ali=0.71, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.10, y_acc=0.00, l_acc=1.92, d0_v=2.68 |
| 10   | -1047.9365   | 2.83       | y_att=4.82, y_ali=0.81, y_f=0.65, d0_att=2.52, l_att=4.79, l_ali=0.71, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.10, y_acc=0.00, l_acc=1.92, d0_v=2.68 |
| 11   | -1057.2961   | 2.84       | y_att=2.47, y_ali=1.06, y_f=0.65, d0_att=1.43, l_att=4.79, l_ali=1.22, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.09, y_acc=0.00, l_acc=1.41, d0_v=2.26 |
| 12   | -1058.9578   | 2.83       | y_att=4.75, y_ali=0.71, y_f=0.65, d0_att=2.17, l_att=3.81, l_ali=1.44, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.86, y_acc=0.00, l_acc=1.15, d0_v=2.12 |
| 13   | -1072.7351   | 3.64       | y_att=1.89, y_ali=0.33, y_f=0.60, d0_att=1.43, l_att=6.91, l_ali=2.08, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.61, y_acc=0.00, l_acc=0.52, d0_v=0.99 |
| 14   | -1084.3655   | 2.82       | y_att=6.16, y_ali=0.81, y_f=0.68, d0_att=0.50, l_att=1.79, l_ali=5.51, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.85, y_acc=0.00, l_acc=2.31, d0_v=3.17 |
| 15   | -1084.3655   | 2.83       | y_att=6.16, y_ali=0.81, y_f=0.68, d0_att=0.50, l_att=1.79, l_ali=5.51, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.85, y_acc=0.00, l_acc=2.31, d0_v=3.17 |
| 16   | -1091.9775   | 2.83       | y_att=5.87, y_ali=1.20, y_f=0.61, d0_att=4.99, l_att=6.07, l_ali=3.27, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.92, y_acc=0.00, l_acc=4.84, d0_v=1.87 |
| 17   | -1092.0957   | 3.83       | y_att=0.82, y_ali=0.07, y_f=0.63, d0_att=0.50, l_att=7.66, l_ali=4.26, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.01, y_acc=0.00, l_acc=1.27, d0_v=1.54 |
| 18   | -1092.0957   | 2.83       | y_att=0.82, y_ali=0.07, y_f=0.63, d0_att=0.50, l_att=7.66, l_ali=4.26, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.01, y_acc=0.00, l_acc=1.27, d0_v=1.54 |
| 19   | -1093.3740   | 2.82       | y_att=3.06, y_ali=0.37, y_f=0.63, d0_att=1.23, l_att=5.43, l_ali=1.95, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.00, y_acc=0.00, l_acc=1.49, d0_v=1.58 |

**End of experiment.**
