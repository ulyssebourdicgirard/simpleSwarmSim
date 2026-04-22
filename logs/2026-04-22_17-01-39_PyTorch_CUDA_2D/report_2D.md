# Experiment Report - PyTorch_CUDA (2D)
**Date:** 2026-04-22_17-01-39

## 1. Initial Configuration
| Parameter | Value |
| :--- | :--- |
| ALPHA_LPF            | 0.2        |
| ARENA_RADIUS         | 100.0      |
| COLLISION_DIST       | 0.4        |
| DT                   | 0.1        |
| ENABLE_3D            | False      |
| FULL_MILLING_MODE    | True       |
| GEN_CPU              | 20         |
| GEN_GPU              | 20         |
| GRID_RES             | 5.0        |
| MAX_SPEED            | 20.0       |
| MAX_YAW_RATE         | 3.14       |
| NB_DRONES            | 25         |
| NEIGHBORS            | 4          |
| POP_SIZE_CPU         | 150        |
| POP_SIZE_GPU         | 5000       |
| SCENARIO             | default    |
| SIM_STEPS            | 500        |
| SPOIL_ADD            | 0.05       |
| SPOIL_MULT           | 1.01       |
| VISU_STEPS           | 1000       |
| W_COLL               | 0          |
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
| 00   | -3534.4011   | 1.99       | y_att=1.60, y_ali=0.60, y_f=1.61, d0_att=1.83, l_att=1.26, l_ali=4.54, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.17, y_acc=0.37, l_acc=1.00, d0_v=2.80 |
| 01   | -3896.6938   | 1.97       | y_att=2.13, y_ali=1.97, y_f=2.47, d0_att=2.09, l_att=1.56, l_ali=3.10, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.74, y_acc=0.26, l_acc=2.37, d0_v=2.03 |
| 02   | -4028.4292   | 1.74       | y_att=4.61, y_ali=3.35, y_f=2.54, d0_att=2.42, l_att=1.21, l_ali=1.66, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.10, y_acc=0.32, l_acc=1.28, d0_v=1.57 |
| 03   | -4020.1985   | 1.72       | y_att=0.62, y_ali=0.28, y_f=1.57, d0_att=3.95, l_att=2.86, l_ali=1.70, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.82, y_acc=0.30, l_acc=0.81, d0_v=2.46 |
| 04   | -4147.4331   | 1.70       | y_att=1.60, y_ali=0.33, y_f=1.61, d0_att=1.83, l_att=1.31, l_ali=5.31, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.58, y_acc=0.37, l_acc=1.00, d0_v=2.80 |
| 05   | -4042.2087   | 1.72       | y_att=2.76, y_ali=0.37, y_f=3.37, d0_att=3.82, l_att=1.28, l_ali=3.75, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.30, y_acc=0.88, l_acc=0.36, d0_v=2.94 |
| 06   | -4303.7148   | 1.72       | y_att=1.61, y_ali=1.86, y_f=2.20, d0_att=4.32, l_att=1.45, l_ali=4.63, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.33, y_acc=0.15, l_acc=1.22, d0_v=2.89 |
| 07   | -4340.8838   | 1.71       | y_att=3.96, y_ali=0.71, y_f=3.41, d0_att=3.41, l_att=2.62, l_ali=8.32, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.88, y_acc=1.72, l_acc=0.65, d0_v=1.45 |
| 08   | -4191.3794   | 1.72       | y_att=3.87, y_ali=0.68, y_f=4.49, d0_att=3.41, l_att=3.07, l_ali=6.52, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.58, y_acc=1.72, l_acc=0.71, d0_v=0.97 |
| 09   | -4716.2793   | 1.72       | y_att=3.99, y_ali=0.33, y_f=7.29, d0_att=3.41, l_att=2.96, l_ali=6.24, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.59, y_acc=2.31, l_acc=0.67, d0_v=0.89 |
| 10   | -4845.9512   | 1.70       | y_att=3.99, y_ali=0.67, y_f=5.87, d0_att=2.89, l_att=3.09, l_ali=8.47, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=3.25, l_acc=0.73, d0_v=1.00 |
| 11   | -5250.5298   | 1.70       | y_att=7.41, y_ali=0.42, y_f=12.33, d0_att=2.98, l_att=2.58, l_ali=5.78, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.49, y_acc=3.18, l_acc=0.67, d0_v=1.23 |
| 12   | -5076.1401   | 1.71       | y_att=3.73, y_ali=0.75, y_f=11.39, d0_att=1.60, l_att=2.49, l_ali=11.85, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.58, y_acc=3.25, l_acc=0.73, d0_v=1.20 |
| 13   | -5201.1982   | 1.74       | y_att=2.54, y_ali=0.99, y_f=7.74, d0_att=3.70, l_att=4.56, l_ali=8.47, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.71, y_acc=3.25, l_acc=0.34, d0_v=0.95 |
| 14   | -5199.2363   | 1.74       | y_att=3.54, y_ali=0.79, y_f=9.72, d0_att=4.76, l_att=5.22, l_ali=6.81, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.28, y_acc=4.71, l_acc=0.55, d0_v=1.11 |
| 15   | -5601.7173   | 1.76       | y_att=5.39, y_ali=1.17, y_f=9.88, d0_att=3.47, l_att=3.38, l_ali=9.25, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.94, y_acc=2.14, l_acc=0.63, d0_v=0.99 |
| 16   | -7641.9248   | 1.80       | y_att=3.73, y_ali=1.97, y_f=7.72, d0_att=2.57, l_att=3.98, l_ali=6.67, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.71, y_acc=3.25, l_acc=0.62, d0_v=0.66 |
| 17   | -7303.9204   | 1.80       | y_att=3.73, y_ali=1.97, y_f=7.72, d0_att=2.57, l_att=3.98, l_ali=6.67, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.71, y_acc=3.25, l_acc=0.62, d0_v=0.66 |
| 18   | -11961.8447  | 1.72       | y_att=5.41, y_ali=0.43, y_f=12.86, d0_att=2.86, l_att=5.07, l_ali=15.08, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.65, y_acc=3.79, l_acc=0.91, d0_v=0.67 |
| 19   | -7364.6309   | 1.71       | y_att=4.52, y_ali=0.36, y_f=8.85, d0_att=2.89, l_att=4.15, l_ali=8.35, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.48, y_acc=4.05, l_acc=0.51, d0_v=0.55 |

**End of experiment.**
