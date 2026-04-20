# Experiment Report - PyTorch_CUDA (3D)
**Date:** 2026-04-20_18-12-16

## 1. Initial Configuration
| Parameter | Value |
| :--- | :--- |
| ALPHA_LPF            | 0.2        |
| ARENA_RADIUS         | 100.0      |
| COLLISION_DIST       | 0.4        |
| DT                   | 0.1        |
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
| 00   | -7135.7275   | 3.37       | y_att=1.56, y_ali=2.38, y_f=0.61, d0_att=1.81, l_att=4.34, l_ali=2.64, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.13, y_acc=1.87, l_acc=3.73, d0_v=2.63 |
| 01   | -6106.5005   | 3.14       | y_att=4.14, y_ali=3.40, y_f=0.98, d0_att=2.30, l_att=3.17, l_ali=1.73, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.37, y_acc=1.22, l_acc=1.59, d0_v=0.76 |
| 02   | -8356.7432   | 3.19       | y_att=3.99, y_ali=0.04, y_f=1.22, d0_att=2.22, l_att=3.71, l_ali=3.21, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.52, y_acc=1.03, l_acc=2.25, d0_v=0.75 |
| 03   | -6104.3906   | 3.01       | y_att=3.99, y_ali=0.04, y_f=1.22, d0_att=2.22, l_att=3.71, l_ali=3.21, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.52, y_acc=1.03, l_acc=2.25, d0_v=0.75 |
| 04   | -6835.2822   | 3.00       | y_att=2.75, y_ali=1.66, y_f=1.83, d0_att=1.12, l_att=3.49, l_ali=2.34, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.86, y_acc=1.01, l_acc=3.17, d0_v=0.89 |
| 05   | -7542.0747   | 3.01       | y_att=4.99, y_ali=0.80, y_f=1.28, d0_att=1.96, l_att=3.21, l_ali=3.10, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.35, y_acc=1.29, l_acc=2.91, d0_v=0.79 |
| 06   | -6703.8638   | 2.95       | y_att=4.86, y_ali=0.33, y_f=0.92, d0_att=3.46, l_att=4.78, l_ali=4.66, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.07, y_acc=1.01, l_acc=3.95, d0_v=0.57 |
| 07   | -5675.3682   | 2.99       | y_att=6.04, y_ali=0.80, y_f=1.28, d0_att=1.96, l_att=3.21, l_ali=3.10, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.35, y_acc=1.29, l_acc=2.91, d0_v=0.79 |
| 08   | -6506.0063   | 2.91       | y_att=4.56, y_ali=2.59, y_f=1.95, d0_att=1.54, l_att=3.54, l_ali=1.11, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.83, y_acc=1.21, l_acc=3.62, d0_v=0.64 |
| 09   | -5212.2427   | 3.17       | y_att=5.09, y_ali=1.73, y_f=1.79, d0_att=1.63, l_att=3.34, l_ali=2.34, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.00, y_acc=1.43, l_acc=3.28, d0_v=0.68 |
| 10   | -5512.9092   | 3.15       | y_att=5.09, y_ali=1.73, y_f=1.79, d0_att=1.63, l_att=3.34, l_ali=2.34, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.00, y_acc=1.43, l_acc=3.28, d0_v=0.68 |
| 11   | -7079.3008   | 2.97       | y_att=3.34, y_ali=2.02, y_f=1.14, d0_att=1.05, l_att=2.45, l_ali=1.35, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=1.06, l_acc=1.62, d0_v=0.63 |
| 12   | -5348.5391   | 3.06       | y_att=5.09, y_ali=1.73, y_f=1.83, d0_att=1.63, l_att=3.34, l_ali=2.93, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.00, y_acc=1.43, l_acc=3.28, d0_v=0.68 |
| 13   | -5746.3530   | 3.02       | y_att=5.09, y_ali=1.73, y_f=1.37, d0_att=1.63, l_att=3.34, l_ali=2.93, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.00, y_acc=1.43, l_acc=3.28, d0_v=0.68 |
| 14   | -4412.4248   | 3.00       | y_att=5.09, y_ali=1.73, y_f=1.37, d0_att=1.70, l_att=3.34, l_ali=2.93, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.00, y_acc=1.27, l_acc=3.28, d0_v=0.68 |
| 15   | -4295.9995   | 2.92       | y_att=5.09, y_ali=1.73, y_f=1.37, d0_att=1.63, l_att=3.34, l_ali=2.93, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.00, y_acc=1.43, l_acc=3.28, d0_v=0.61 |
| 16   | -4266.7544   | 2.96       | y_att=5.09, y_ali=1.73, y_f=1.37, d0_att=1.63, l_att=3.34, l_ali=2.93, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.07, y_acc=1.21, l_acc=3.28, d0_v=0.61 |
| 17   | -4158.4746   | 3.13       | y_att=1.09, y_ali=0.38, y_f=1.26, d0_att=1.78, l_att=0.59, l_ali=3.91, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.13, y_acc=0.07, l_acc=0.25, d0_v=0.84 |
| 18   | -4002.3040   | 3.13       | y_att=0.65, y_ali=0.70, y_f=3.04, d0_att=1.21, l_att=0.79, l_ali=3.52, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.54, y_acc=0.23, l_acc=0.32, d0_v=0.90 |
| 19   | -4145.8838   | 3.04       | y_att=0.35, y_ali=3.75, y_f=4.11, d0_att=3.02, l_att=0.13, l_ali=1.29, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.15, y_acc=1.37, l_acc=0.20, d0_v=3.86 |

**End of experiment.**
