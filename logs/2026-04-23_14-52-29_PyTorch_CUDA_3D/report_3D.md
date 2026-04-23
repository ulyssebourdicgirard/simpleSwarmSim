# Experiment Report - PyTorch_CUDA (3D)
**Date:** 2026-04-23_14-52-29

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
| NB_DRONES            | 25         |
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
| 00   | -1064.9895   | 3.32       | y_att=4.63, y_ali=3.48, y_f=1.61, d0_att=3.10, l_att=1.20, l_ali=1.90, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.58, y_acc=0.38, l_acc=1.88, d0_v=2.73 |
| 01   | -1064.9895   | 2.77       | y_att=4.63, y_ali=3.48, y_f=1.61, d0_att=3.10, l_att=1.20, l_ali=1.90, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.58, y_acc=0.38, l_acc=1.88, d0_v=2.73 |
| 02   | -1196.8677   | 2.77       | y_att=2.94, y_ali=1.46, y_f=0.33, d0_att=2.75, l_att=1.63, l_ali=3.97, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.44, y_acc=0.15, l_acc=0.10, d0_v=1.03 |
| 03   | -1282.9052   | 3.87       | y_att=2.29, y_ali=0.79, y_f=0.27, d0_att=1.20, l_att=6.75, l_ali=2.16, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.08, l_acc=0.53, d0_v=2.42 |
| 04   | -1296.7130   | 2.77       | y_att=3.92, y_ali=2.99, y_f=0.23, d0_att=1.42, l_att=2.80, l_ali=4.64, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.65, y_acc=0.10, l_acc=0.57, d0_v=2.90 |
| 05   | -1306.2042   | 2.78       | y_att=3.92, y_ali=2.99, y_f=0.23, d0_att=1.42, l_att=2.80, l_ali=4.64, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.65, y_acc=0.10, l_acc=0.57, d0_v=2.90 |
| 06   | -1306.2042   | 2.81       | y_att=3.92, y_ali=2.99, y_f=0.23, d0_att=1.42, l_att=2.80, l_ali=4.64, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.65, y_acc=0.10, l_acc=0.57, d0_v=2.90 |
| 07   | -1306.2042   | 3.79       | y_att=3.92, y_ali=2.99, y_f=0.23, d0_att=1.42, l_att=2.80, l_ali=4.64, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.65, y_acc=0.10, l_acc=0.57, d0_v=2.90 |
| 08   | -1306.2042   | 2.79       | y_att=3.92, y_ali=2.99, y_f=0.23, d0_att=1.42, l_att=2.80, l_ali=4.64, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.65, y_acc=0.10, l_acc=0.57, d0_v=2.90 |
| 09   | -1310.1246   | 2.78       | y_att=3.92, y_ali=0.40, y_f=0.66, d0_att=1.42, l_att=3.53, l_ali=4.63, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.68, y_acc=0.00, l_acc=1.28, d0_v=2.90 |
| 10   | -1336.8636   | 2.78       | y_att=3.92, y_ali=0.40, y_f=0.66, d0_att=1.40, l_att=4.21, l_ali=2.40, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.53, y_acc=0.00, l_acc=1.90, d0_v=1.54 |
| 11   | -1336.8636   | 2.75       | y_att=3.92, y_ali=0.40, y_f=0.66, d0_att=1.40, l_att=4.21, l_ali=2.40, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.53, y_acc=0.00, l_acc=1.90, d0_v=1.54 |
| 12   | -1336.8636   | 2.74       | y_att=3.92, y_ali=0.40, y_f=0.66, d0_att=1.40, l_att=4.21, l_ali=2.40, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.53, y_acc=0.00, l_acc=1.90, d0_v=1.54 |
| 13   | -1336.8636   | 3.81       | y_att=3.92, y_ali=0.40, y_f=0.66, d0_att=1.40, l_att=4.21, l_ali=2.40, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.53, y_acc=0.00, l_acc=1.90, d0_v=1.54 |
| 14   | -1336.8636   | 2.81       | y_att=3.92, y_ali=0.40, y_f=0.66, d0_att=1.40, l_att=4.21, l_ali=2.40, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.53, y_acc=0.00, l_acc=1.90, d0_v=1.54 |
| 15   | -1336.8636   | 2.78       | y_att=3.92, y_ali=0.40, y_f=0.66, d0_att=1.40, l_att=4.21, l_ali=2.40, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.53, y_acc=0.00, l_acc=1.90, d0_v=1.54 |
| 16   | -1336.8636   | 2.78       | y_att=3.92, y_ali=0.40, y_f=0.66, d0_att=1.40, l_att=4.21, l_ali=2.40, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.53, y_acc=0.00, l_acc=1.90, d0_v=1.54 |
| 17   | -1336.8636   | 3.86       | y_att=3.92, y_ali=0.40, y_f=0.66, d0_att=1.40, l_att=4.21, l_ali=2.40, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.53, y_acc=0.00, l_acc=1.90, d0_v=1.54 |
| 18   | -1345.1145   | 2.79       | y_att=4.87, y_ali=5.24, y_f=0.59, d0_att=1.64, l_att=3.53, l_ali=0.62, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.76, y_acc=0.00, l_acc=0.99, d0_v=1.53 |
| 19   | -1364.2552   | 2.79       | y_att=1.54, y_ali=0.50, y_f=0.60, d0_att=0.53, l_att=3.39, l_ali=4.00, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.66, y_acc=0.00, l_acc=0.85, d0_v=1.96 |

**End of experiment.**
