# Experiment Report - PyTorch_CUDA (3D)
**Date:** 2026-03-15_16-35-15

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
| MAX_SPEED            | 10.0       |
| NB_DRONES            | 5          |
| NEIGHBORS            | 2          |
| POP_SIZE_CPU         | 150        |
| POP_SIZE_GPU         | 5000       |
| SCENARIO             | exploration |
| SIM_STEPS            | 5000       |
| VISU_STEPS           | 5000       |
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
| 00   | -4858.1870   | 28.20      | y_att=0.53, y_ali=3.97, y_f=1.33, d0_att=2.41, l_att=2.30, l_ali=1.51, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 01   | -6811.3652   | 28.51      | y_att=1.17, y_ali=0.03, y_f=0.96, d0_att=2.82, l_att=1.56, l_ali=4.44, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 02   | -6500.9014   | 28.30      | y_att=1.53, y_ali=0.37, y_f=1.42, d0_att=1.45, l_att=0.68, l_ali=0.87, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 03   | -6173.6157   | 29.56      | y_att=0.97, y_ali=0.02, y_f=1.21, d0_att=1.75, l_att=0.94, l_ali=4.84, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 04   | -7820.0894   | 28.85      | y_att=0.83, y_ali=0.08, y_f=1.00, d0_att=1.46, l_att=1.08, l_ali=1.48, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 05   | -9662.9062   | 29.43      | y_att=1.01, y_ali=0.04, y_f=2.06, d0_att=3.07, l_att=0.58, l_ali=2.51, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 06   | -8356.3076   | 29.08      | y_att=0.61, y_ali=0.08, y_f=1.35, d0_att=3.68, l_att=0.71, l_ali=1.80, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 07   | -11317.3535  | 28.78      | y_att=0.84, y_ali=0.00, y_f=0.66, d0_att=2.76, l_att=0.50, l_ali=1.24, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 08   | -10597.1465  | 28.58      | y_att=0.81, y_ali=0.00, y_f=0.60, d0_att=2.96, l_att=0.55, l_ali=0.75, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 09   | -10611.1318  | 29.16      | y_att=0.87, y_ali=0.00, y_f=0.61, d0_att=1.66, l_att=0.18, l_ali=0.65, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 10   | -11258.8740  | 29.08      | y_att=0.61, y_ali=0.00, y_f=0.61, d0_att=1.23, l_att=0.30, l_ali=0.65, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 11   | -11232.0586  | 29.40      | y_att=0.60, y_ali=0.00, y_f=0.61, d0_att=1.14, l_att=0.30, l_ali=0.65, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 12   | -11130.6309  | 29.24      | y_att=1.31, y_ali=0.01, y_f=0.57, d0_att=1.29, l_att=0.27, l_ali=1.89, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 13   | -10838.1514  | 29.32      | y_att=0.53, y_ali=0.00, y_f=0.81, d0_att=3.19, l_att=0.45, l_ali=0.89, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 14   | -11931.6318  | 29.91      | y_att=1.31, y_ali=0.01, y_f=0.57, d0_att=1.98, l_att=0.27, l_ali=1.89, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 15   | -11512.3887  | 29.52      | y_att=0.59, y_ali=0.00, y_f=1.10, d0_att=1.11, l_att=0.28, l_ali=0.65, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 16   | -11194.5137  | 29.73      | y_att=0.71, y_ali=0.00, y_f=0.61, d0_att=1.67, l_att=0.36, l_ali=2.78, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 17   | -11094.4580  | 29.46      | y_att=0.96, y_ali=0.00, y_f=0.63, d0_att=1.04, l_att=0.25, l_ali=0.66, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 18   | -11203.1680  | 29.31      | y_att=0.42, y_ali=0.00, y_f=0.34, d0_att=1.08, l_att=0.24, l_ali=1.13, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 19   | -11443.4248  | 29.35      | y_att=0.58, y_ali=0.00, y_f=0.96, d0_att=2.13, l_att=0.21, l_ali=0.26, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |

**End of experiment.**
