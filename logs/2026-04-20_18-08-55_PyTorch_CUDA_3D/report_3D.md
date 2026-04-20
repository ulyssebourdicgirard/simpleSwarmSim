# Experiment Report - PyTorch_CUDA (3D)
**Date:** 2026-04-20_18-08-55

## 1. Initial Configuration
| Parameter | Value |
| :--- | :--- |
| ALPHA_LPF            | 0.2        |
| ARENA_RADIUS         | 100.0      |
| COLLISION_DIST       | 0.4        |
| DT                   | 0.01       |
| ENABLE_3D            | True       |
| FULL_MILLING_MODE    | True       |
| GEN_CPU              | 20         |
| GEN_GPU              | 20         |
| GRID_RES             | 5.0        |
| MAX_SPEED            | 20.0       |
| MAX_YAW_RATE         | 3.14       |
| NB_DRONES            | 30         |
| NEIGHBORS            | 3          |
| POP_SIZE_CPU         | 150        |
| POP_SIZE_GPU         | 5000       |
| SCENARIO             | default    |
| SIM_STEPS            | 500        |
| SPOIL_ADD            | 0.05       |
| SPOIL_MULT           | 1.01       |
| VISU_STEPS           | 1000       |
| W_COLL               | 500.0      |
| W_DISP               | 0.0        |
| W_EFFORT             | 1.0        |
| W_EXPLO              | 0.0        |
| W_MILL               | -100.0     |
| W_POL                | 0.0        |
| Z_MAX                | 10.0       |
| Z_MIN                | 1.0        |

## 2. Optimization Evolution
| Gen  |  Best Cost   |  Time (s)  |                                                                All Parameters                                                                |
| :--: | :----------: | :--------: | :------------------------------------------------------------------------------------------------------------------------------------------ |
| 00   | -3758.2007   | 3.45       | y_att=3.69, y_ali=1.66, y_f=1.68, d0_att=3.99, l_att=1.36, l_ali=3.25, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.69, y_acc=0.14, l_acc=3.48, d0_v=1.97 |
| 01   | -3780.0774   | 3.18       | y_att=0.46, y_ali=2.10, y_f=1.27, d0_att=2.76, l_att=1.43, l_ali=4.02, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.95, y_acc=0.25, l_acc=0.51, d0_v=2.51 |
| 02   | -3770.4658   | 3.23       | y_att=0.68, y_ali=3.43, y_f=1.15, d0_att=3.70, l_att=2.90, l_ali=4.05, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.90, y_acc=0.11, l_acc=2.05, d0_v=1.17 |
| 03   | -3805.7761   | 3.05       | y_att=0.69, y_ali=2.10, y_f=0.40, d0_att=2.58, l_att=1.22, l_ali=5.11, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.95, y_acc=0.25, l_acc=0.51, d0_v=2.59 |
| 04   | -3838.5005   | 3.08       | y_att=0.46, y_ali=1.43, y_f=0.90, d0_att=2.76, l_att=1.43, l_ali=3.36, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.48, y_acc=0.25, l_acc=0.39, d0_v=3.17 |
| 05   | -3832.4563   | 2.94       | y_att=1.05, y_ali=3.34, y_f=0.82, d0_att=3.66, l_att=1.08, l_ali=2.10, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.81, y_acc=0.10, l_acc=1.00, d0_v=1.79 |
| 06   | -3859.4004   | 2.99       | y_att=1.14, y_ali=2.10, y_f=0.26, d0_att=2.88, l_att=0.60, l_ali=5.11, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.59, y_acc=0.25, l_acc=0.55, d0_v=2.59 |
| 07   | -3889.9229   | 2.90       | y_att=0.65, y_ali=5.87, y_f=0.57, d0_att=2.13, l_att=1.34, l_ali=2.53, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.90, y_acc=0.07, l_acc=0.91, d0_v=1.21 |
| 08   | -3872.3030   | 3.03       | y_att=0.61, y_ali=1.98, y_f=0.56, d0_att=2.80, l_att=1.60, l_ali=2.00, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.71, y_acc=0.31, l_acc=0.69, d0_v=2.59 |
| 09   | -3887.2996   | 3.14       | y_att=0.44, y_ali=1.76, y_f=0.16, d0_att=1.94, l_att=0.66, l_ali=5.11, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.21, l_acc=0.55, d0_v=2.59 |
| 10   | -3927.4304   | 3.05       | y_att=2.68, y_ali=1.33, y_f=0.20, d0_att=4.52, l_att=0.54, l_ali=1.53, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.40, y_acc=0.20, l_acc=0.23, d0_v=1.73 |
| 11   | -3983.3298   | 2.99       | y_att=0.54, y_ali=1.64, y_f=0.14, d0_att=2.85, l_att=1.06, l_ali=4.37, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.84, y_acc=0.27, l_acc=0.28, d0_v=4.67 |
| 12   | -3918.4395   | 3.07       | y_att=0.60, y_ali=2.34, y_f=0.29, d0_att=3.34, l_att=1.60, l_ali=4.09, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.22, y_acc=0.31, l_acc=0.46, d0_v=2.59 |
| 13   | -3964.3342   | 2.95       | y_att=0.69, y_ali=0.94, y_f=0.13, d0_att=3.91, l_att=1.35, l_ali=5.11, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.81, y_acc=0.24, l_acc=0.24, d0_v=3.71 |
| 14   | -3943.3032   | 2.99       | y_att=0.69, y_ali=1.51, y_f=0.10, d0_att=3.24, l_att=1.52, l_ali=3.47, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.90, y_acc=0.15, l_acc=0.27, d0_v=2.81 |
| 15   | -3981.8867   | 2.99       | y_att=0.25, y_ali=1.43, y_f=0.18, d0_att=4.25, l_att=1.11, l_ali=3.87, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.85, y_acc=0.13, l_acc=0.11, d0_v=2.34 |
| 16   | -4000.1987   | 3.02       | y_att=5.24, y_ali=0.29, y_f=0.15, d0_att=17.05, l_att=1.55, l_ali=5.49, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.21, y_acc=0.40, l_acc=0.15, d0_v=2.09 |
| 17   | -4033.1218   | 3.19       | y_att=5.24, y_ali=0.24, y_f=0.13, d0_att=20.63, l_att=2.16, l_ali=5.49, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.21, y_acc=0.26, l_acc=0.17, d0_v=2.00 |
| 18   | -4327.0029   | 3.23       | y_att=6.75, y_ali=0.16, y_f=0.13, d0_att=22.88, l_att=2.98, l_ali=5.05, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.21, y_acc=0.26, l_acc=0.17, d0_v=2.00 |
| 19   | -4255.4736   | 3.05       | y_att=6.75, y_ali=0.16, y_f=0.13, d0_att=22.88, l_att=2.98, l_ali=5.05, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.09, y_acc=0.26, l_acc=0.17, d0_v=2.00 |

**End of experiment.**
