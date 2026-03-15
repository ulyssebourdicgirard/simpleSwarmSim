# Experiment Report - PyTorch_CUDA (3D)
**Date:** 2026-03-15_16-31-46

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
| MAX_SPEED            | 2.0        |
| NB_DRONES            | 5          |
| NEIGHBORS            | 2          |
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
| 00   | -998.1041    | 2.93       | y_att=0.95, y_ali=2.61, y_f=1.53, d0_att=2.35, l_att=1.92, l_ali=3.36, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 01   | -1048.2952   | 2.83       | y_att=4.77, y_ali=1.82, y_f=2.24, d0_att=3.87, l_att=1.44, l_ali=2.45, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 02   | -1037.5261   | 2.76       | y_att=2.57, y_ali=2.23, y_f=1.67, d0_att=3.05, l_att=1.87, l_ali=1.56, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 03   | -1052.5170   | 2.87       | y_att=2.34, y_ali=0.60, y_f=1.72, d0_att=2.10, l_att=1.47, l_ali=3.55, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 04   | -1031.4008   | 2.82       | y_att=4.11, y_ali=3.15, y_f=2.81, d0_att=5.18, l_att=1.48, l_ali=4.46, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 05   | -1067.5490   | 2.80       | y_att=2.33, y_ali=2.99, y_f=2.44, d0_att=1.51, l_att=1.17, l_ali=2.16, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 06   | -1055.1071   | 2.73       | y_att=2.86, y_ali=1.29, y_f=1.86, d0_att=1.62, l_att=1.27, l_ali=6.56, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 07   | -1028.7736   | 2.62       | y_att=1.26, y_ali=4.63, y_f=1.54, d0_att=1.77, l_att=2.12, l_ali=0.63, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 08   | -1047.0463   | 2.70       | y_att=3.31, y_ali=2.53, y_f=2.14, d0_att=3.64, l_att=1.52, l_ali=2.25, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 09   | -1039.4229   | 2.76       | y_att=0.89, y_ali=0.47, y_f=2.06, d0_att=1.15, l_att=1.89, l_ali=6.04, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 10   | -1032.6554   | 2.85       | y_att=1.02, y_ali=2.13, y_f=1.62, d0_att=2.17, l_att=1.02, l_ali=9.61, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 11   | -1044.5400   | 2.73       | y_att=1.75, y_ali=3.11, y_f=1.92, d0_att=4.90, l_att=2.05, l_ali=4.16, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 12   | -1041.6604   | 2.93       | y_att=1.68, y_ali=2.65, y_f=2.87, d0_att=1.93, l_att=1.36, l_ali=8.75, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 13   | -1041.9520   | 2.89       | y_att=1.07, y_ali=0.90, y_f=2.02, d0_att=0.62, l_att=1.16, l_ali=3.79, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 14   | -1031.1362   | 2.69       | y_att=0.70, y_ali=3.39, y_f=1.48, d0_att=3.29, l_att=2.57, l_ali=2.94, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 15   | -1064.6984   | 2.70       | y_att=1.91, y_ali=0.18, y_f=2.16, d0_att=2.02, l_att=1.36, l_ali=4.45, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 16   | -1045.7574   | 2.63       | y_att=0.99, y_ali=2.65, y_f=2.05, d0_att=1.00, l_att=1.53, l_ali=2.69, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 17   | -1040.6493   | 2.78       | y_att=2.83, y_ali=4.82, y_f=3.37, d0_att=2.42, l_att=1.47, l_ali=3.83, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 18   | -1062.6140   | 2.90       | y_att=0.61, y_ali=1.51, y_f=2.51, d0_att=0.72, l_att=1.32, l_ali=4.85, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 19   | -1046.3079   | 2.70       | y_att=0.29, y_ali=2.10, y_f=3.00, d0_att=1.94, l_att=2.99, l_ali=5.32, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |

**End of experiment.**
