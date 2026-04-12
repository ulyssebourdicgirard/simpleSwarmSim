# Experiment Report - PyTorch_CUDA (3D)
**Date:** 2026-04-12_21-39-50

## 1. Initial Configuration
| Parameter | Value |
| :--- | :--- |
| ALPHA_LPF            | 0.2        |
| ARENA_RADIUS         | 100.0      |
| COLLISION_DIST       | 0.4        |
| DT                   | 0.01       |
| ENABLE_3D            | True       |
| GEN_CPU              | 20         |
| GEN_GPU              | 20         |
| GRID_RES             | 5.0        |
| MAX_SPEED            | 20.0       |
| MAX_YAW_RATE         | 3.14       |
| NB_DRONES            | 30         |
| NEIGHBORS            | 3          |
| POP_SIZE_CPU         | 150        |
| POP_SIZE_GPU         | 5000       |
| SCENARIO             | exploration |
| SIM_STEPS            | 500        |
| SPOIL_ADD            | 0.05       |
| SPOIL_MULT           | 1.01       |
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
| 00   | -1059.7906   | 3.84       | y_att=4.21, y_ali=0.97, y_f=1.48, d0_att=3.17, l_att=4.77, l_ali=2.28, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.64, y_acc=1.85, l_acc=3.77, d0_v=0.58 |
| 01   | -1103.1400   | 3.92       | y_att=4.95, y_ali=0.09, y_f=1.29, d0_att=1.18, l_att=2.64, l_ali=1.65, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.25, y_acc=1.39, l_acc=3.33, d0_v=0.42 |
| 02   | -1062.6581   | 3.57       | y_att=1.17, y_ali=1.79, y_f=1.05, d0_att=1.24, l_att=5.19, l_ali=4.20, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.87, y_acc=1.27, l_acc=3.52, d0_v=0.49 |
| 03   | -1100.3685   | 3.43       | y_att=4.21, y_ali=0.97, y_f=1.48, d0_att=2.70, l_att=4.77, l_ali=2.28, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.64, y_acc=1.85, l_acc=3.77, d0_v=0.58 |
| 04   | -1201.4698   | 3.51       | y_att=4.95, y_ali=0.06, y_f=1.29, d0_att=1.40, l_att=2.70, l_ali=1.16, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.25, y_acc=1.39, l_acc=3.33, d0_v=0.42 |
| 05   | -1187.0712   | 3.55       | y_att=4.99, y_ali=0.94, y_f=1.52, d0_att=3.19, l_att=4.75, l_ali=1.38, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.03, y_acc=1.88, l_acc=3.10, d0_v=0.47 |
| 06   | -1164.6508   | 3.35       | y_att=4.99, y_ali=0.94, y_f=1.52, d0_att=3.19, l_att=4.75, l_ali=1.38, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.03, y_acc=1.88, l_acc=3.10, d0_v=0.47 |
| 07   | -1179.2208   | 3.40       | y_att=5.54, y_ali=0.08, y_f=1.51, d0_att=3.08, l_att=4.54, l_ali=2.80, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.18, y_acc=2.74, l_acc=3.41, d0_v=0.74 |
| 08   | -1199.0580   | 4.71       | y_att=4.15, y_ali=0.76, y_f=1.60, d0_att=2.93, l_att=4.95, l_ali=2.17, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.45, y_acc=2.05, l_acc=3.77, d0_v=0.58 |
| 09   | -1208.9987   | 3.56       | y_att=6.57, y_ali=0.08, y_f=1.51, d0_att=4.32, l_att=4.74, l_ali=1.27, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.23, y_acc=3.22, l_acc=3.50, d0_v=0.88 |
| 10   | -1236.1418   | 3.41       | y_att=6.57, y_ali=0.08, y_f=1.51, d0_att=4.32, l_att=4.95, l_ali=1.27, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.31, y_acc=3.22, l_acc=3.50, d0_v=0.88 |
| 11   | -1209.9288   | 3.76       | y_att=5.29, y_ali=0.05, y_f=1.50, d0_att=3.08, l_att=4.45, l_ali=2.80, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.06, y_acc=2.74, l_acc=3.45, d0_v=0.77 |
| 12   | -1230.6619   | 3.53       | y_att=6.57, y_ali=0.08, y_f=1.51, d0_att=4.32, l_att=4.95, l_ali=1.27, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.92, y_acc=3.22, l_acc=3.50, d0_v=0.88 |
| 13   | -1233.6473   | 3.35       | y_att=6.57, y_ali=0.06, y_f=1.51, d0_att=4.32, l_att=4.74, l_ali=1.07, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.79, y_acc=3.22, l_acc=3.50, d0_v=0.88 |
| 14   | -1249.4558   | 3.47       | y_att=4.99, y_ali=0.83, y_f=2.13, d0_att=2.84, l_att=5.29, l_ali=1.07, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.89, y_acc=1.76, l_acc=4.42, d0_v=0.45 |
| 15   | -1231.9312   | 3.61       | y_att=4.99, y_ali=0.88, y_f=2.06, d0_att=2.97, l_att=5.27, l_ali=1.31, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.97, y_acc=1.76, l_acc=5.46, d0_v=0.57 |
| 16   | -1244.8660   | 3.61       | y_att=4.99, y_ali=0.83, y_f=2.13, d0_att=2.84, l_att=5.29, l_ali=1.20, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.89, y_acc=1.76, l_acc=4.42, d0_v=0.45 |
| 17   | -1292.3031   | 3.34       | y_att=5.88, y_ali=0.94, y_f=2.20, d0_att=4.00, l_att=5.82, l_ali=0.93, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.10, y_acc=1.93, l_acc=4.36, d0_v=0.47 |
| 18   | -1310.7910   | 3.19       | y_att=5.88, y_ali=0.94, y_f=2.20, d0_att=4.00, l_att=5.82, l_ali=0.93, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.10, y_acc=1.93, l_acc=4.36, d0_v=0.47 |
| 19   | -1311.4241   | 3.33       | y_att=5.88, y_ali=0.94, y_f=2.20, d0_att=4.00, l_att=5.82, l_ali=0.93, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.10, y_acc=1.93, l_acc=4.36, d0_v=0.47 |

**End of experiment.**
