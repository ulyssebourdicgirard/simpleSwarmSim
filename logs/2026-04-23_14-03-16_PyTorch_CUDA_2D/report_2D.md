# Experiment Report - PyTorch_CUDA (2D)
**Date:** 2026-04-23_14-03-16

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
| NB_DRONES            | 30         |
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
| 00   | -2841.2090   | 3.32       | y_att=1.46, y_ali=3.02, y_f=1.91, d0_att=3.90, l_att=1.55, l_ali=3.82, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.74, y_acc=0.43, l_acc=0.54, d0_v=1.86 |
| 01   | -3219.8213   | 2.50       | y_att=2.76, y_ali=1.86, y_f=2.54, d0_att=3.71, l_att=1.38, l_ali=3.24, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.74, y_acc=1.01, l_acc=1.06, d0_v=3.75 |
| 02   | -3536.8064   | 2.53       | y_att=2.25, y_ali=3.29, y_f=1.87, d0_att=4.63, l_att=1.00, l_ali=2.66, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.93, y_acc=0.12, l_acc=2.44, d0_v=2.27 |
| 03   | -3536.8064   | 2.88       | y_att=2.25, y_ali=3.29, y_f=1.87, d0_att=4.63, l_att=1.00, l_ali=2.66, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.93, y_acc=0.12, l_acc=2.44, d0_v=2.27 |
| 04   | -3735.4309   | 2.56       | y_att=0.34, y_ali=1.80, y_f=2.55, d0_att=3.39, l_att=0.40, l_ali=1.78, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=1.00, l_acc=0.76, d0_v=2.55 |
| 05   | -3735.4309   | 3.54       | y_att=0.34, y_ali=1.80, y_f=2.55, d0_att=3.39, l_att=0.40, l_ali=1.78, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=1.00, l_acc=0.76, d0_v=2.55 |
| 06   | -3852.8635   | 2.91       | y_att=0.18, y_ali=0.95, y_f=0.55, d0_att=3.69, l_att=1.37, l_ali=0.78, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.52, y_acc=0.09, l_acc=0.34, d0_v=4.77 |
| 07   | -3852.8635   | 2.53       | y_att=0.18, y_ali=0.95, y_f=0.55, d0_att=3.69, l_att=1.37, l_ali=0.78, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.52, y_acc=0.09, l_acc=0.34, d0_v=4.77 |
| 08   | -3963.0796   | 2.52       | y_att=1.22, y_ali=3.11, y_f=1.69, d0_att=4.90, l_att=2.08, l_ali=1.34, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.46, y_acc=0.36, l_acc=0.50, d0_v=1.69 |
| 09   | -4178.1138   | 2.63       | y_att=1.70, y_ali=0.20, y_f=1.11, d0_att=7.17, l_att=0.19, l_ali=0.33, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.56, y_acc=0.01, l_acc=1.33, d0_v=2.37 |
| 10   | -4178.1138   | 3.08       | y_att=1.70, y_ali=0.20, y_f=1.11, d0_att=7.17, l_att=0.19, l_ali=0.33, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.56, y_acc=0.01, l_acc=1.33, d0_v=2.37 |
| 11   | -4178.1138   | 2.77       | y_att=1.70, y_ali=0.20, y_f=1.11, d0_att=7.17, l_att=0.19, l_ali=0.33, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.56, y_acc=0.01, l_acc=1.33, d0_v=2.37 |
| 12   | -4178.1138   | 2.57       | y_att=1.70, y_ali=0.20, y_f=1.11, d0_att=7.17, l_att=0.19, l_ali=0.33, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.56, y_acc=0.01, l_acc=1.33, d0_v=2.37 |
| 13   | -4178.1138   | 2.52       | y_att=1.70, y_ali=0.20, y_f=1.11, d0_att=7.17, l_att=0.19, l_ali=0.33, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.56, y_acc=0.01, l_acc=1.33, d0_v=2.37 |
| 14   | -4178.1138   | 2.64       | y_att=1.70, y_ali=0.20, y_f=1.11, d0_att=7.17, l_att=0.19, l_ali=0.33, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.56, y_acc=0.01, l_acc=1.33, d0_v=2.37 |
| 15   | -4178.1138   | 3.24       | y_att=1.70, y_ali=0.20, y_f=1.11, d0_att=7.17, l_att=0.19, l_ali=0.33, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.56, y_acc=0.01, l_acc=1.33, d0_v=2.37 |
| 16   | -4178.1138   | 2.56       | y_att=1.70, y_ali=0.20, y_f=1.11, d0_att=7.17, l_att=0.19, l_ali=0.33, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.56, y_acc=0.01, l_acc=1.33, d0_v=2.37 |
| 17   | -4178.1138   | 2.38       | y_att=1.70, y_ali=0.20, y_f=1.11, d0_att=7.17, l_att=0.19, l_ali=0.33, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.56, y_acc=0.01, l_acc=1.33, d0_v=2.37 |
| 18   | -4178.1138   | 2.55       | y_att=1.70, y_ali=0.20, y_f=1.11, d0_att=7.17, l_att=0.19, l_ali=0.33, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.56, y_acc=0.01, l_acc=1.33, d0_v=2.37 |
| 19   | -4178.1138   | 2.71       | y_att=1.70, y_ali=0.20, y_f=1.11, d0_att=7.17, l_att=0.19, l_ali=0.33, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.56, y_acc=0.01, l_acc=1.33, d0_v=2.37 |

**End of experiment.**
