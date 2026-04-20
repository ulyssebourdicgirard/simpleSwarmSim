# Experiment Report - PyTorch_CUDA (2D)
**Date:** 2026-04-20_18-15-29

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
| 00   | -6183.8115   | 2.55       | y_att=4.93, y_ali=0.11, y_f=0.71, d0_att=2.09, l_att=2.64, l_ali=1.73, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.88, y_acc=1.84, l_acc=1.94, d0_v=1.39 |
| 01   | -5113.0654   | 2.41       | y_att=4.51, y_ali=2.06, y_f=1.45, d0_att=1.39, l_att=2.79, l_ali=4.49, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.61, y_acc=1.08, l_acc=2.72, d0_v=0.77 |
| 02   | -7407.5771   | 2.53       | y_att=2.43, y_ali=3.84, y_f=1.49, d0_att=1.29, l_att=4.42, l_ali=1.64, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.59, y_acc=0.92, l_acc=3.28, d0_v=0.60 |
| 03   | -8265.1689   | 2.53       | y_att=6.63, y_ali=1.39, y_f=1.74, d0_att=3.24, l_att=3.99, l_ali=3.60, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.12, y_acc=1.15, l_acc=2.81, d0_v=0.64 |
| 04   | -5926.0156   | 2.45       | y_att=2.37, y_ali=2.20, y_f=1.36, d0_att=0.75, l_att=3.80, l_ali=4.64, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.30, y_acc=0.95, l_acc=3.70, d0_v=0.34 |
| 05   | -6563.1875   | 2.37       | y_att=3.17, y_ali=3.47, y_f=1.56, d0_att=0.96, l_att=3.25, l_ali=1.45, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.59, y_acc=1.85, l_acc=1.86, d0_v=0.57 |
| 06   | -6762.0430   | 2.42       | y_att=6.63, y_ali=1.81, y_f=1.66, d0_att=3.86, l_att=4.49, l_ali=4.98, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.69, y_acc=1.15, l_acc=2.90, d0_v=0.72 |
| 07   | -7246.8872   | 2.40       | y_att=2.09, y_ali=1.87, y_f=1.58, d0_att=1.14, l_att=4.96, l_ali=1.95, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.02, y_acc=1.06, l_acc=5.93, d0_v=0.60 |
| 08   | -7087.6230   | 2.33       | y_att=1.50, y_ali=2.91, y_f=1.52, d0_att=1.14, l_att=4.60, l_ali=0.93, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.96, y_acc=1.37, l_acc=2.32, d0_v=0.65 |
| 09   | -4144.4307   | 2.32       | y_att=3.17, y_ali=3.83, y_f=1.18, d0_att=0.96, l_att=3.25, l_ali=2.77, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.59, y_acc=1.94, l_acc=2.60, d0_v=0.57 |
| 10   | -8813.7656   | 2.35       | y_att=3.17, y_ali=2.33, y_f=1.32, d0_att=1.11, l_att=3.25, l_ali=2.77, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.59, y_acc=2.24, l_acc=1.75, d0_v=0.70 |
| 11   | -6502.4199   | 2.40       | y_att=2.06, y_ali=4.50, y_f=1.45, d0_att=0.65, l_att=3.25, l_ali=1.45, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.55, y_acc=2.14, l_acc=1.98, d0_v=0.64 |
| 12   | -5637.7222   | 2.56       | y_att=2.23, y_ali=1.97, y_f=1.49, d0_att=1.14, l_att=3.81, l_ali=1.45, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.22, y_acc=1.02, l_acc=2.33, d0_v=0.52 |
| 13   | -5274.9043   | 2.43       | y_att=6.02, y_ali=1.31, y_f=1.40, d0_att=1.62, l_att=3.09, l_ali=2.77, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.45, y_acc=1.53, l_acc=2.27, d0_v=0.77 |
| 14   | -6030.4653   | 2.36       | y_att=4.90, y_ali=1.95, y_f=1.40, d0_att=1.92, l_att=3.34, l_ali=6.14, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.57, y_acc=1.52, l_acc=2.65, d0_v=0.77 |
| 15   | -5569.3994   | 2.38       | y_att=6.11, y_ali=1.37, y_f=1.40, d0_att=1.92, l_att=3.34, l_ali=5.10, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.57, y_acc=1.38, l_acc=2.65, d0_v=0.77 |
| 16   | -4906.5435   | 2.39       | y_att=6.02, y_ali=1.31, y_f=1.40, d0_att=2.04, l_att=3.09, l_ali=3.15, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.34, y_acc=1.53, l_acc=2.27, d0_v=0.58 |
| 17   | -5894.5181   | 2.37       | y_att=7.06, y_ali=2.20, y_f=1.40, d0_att=1.39, l_att=2.33, l_ali=5.19, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.30, y_acc=1.53, l_acc=2.65, d0_v=0.73 |
| 18   | -5204.1343   | 2.35       | y_att=6.38, y_ali=1.52, y_f=1.46, d0_att=1.74, l_att=3.07, l_ali=4.39, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.30, y_acc=1.59, l_acc=2.97, d0_v=1.15 |
| 19   | -4147.5166   | 2.32       | y_att=5.61, y_ali=2.20, y_f=1.55, d0_att=1.41, l_att=2.78, l_ali=3.66, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.30, y_acc=1.73, l_acc=3.15, d0_v=0.85 |

**End of experiment.**
