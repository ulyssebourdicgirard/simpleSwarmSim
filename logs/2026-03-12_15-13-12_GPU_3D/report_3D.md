# Experiment Report - GPU (3D)
**Date:** 2026-03-12_15-13-12

## 1. Initial Configuration
| Parameter | Value |
| :--- | :--- |
| ARENA_RADIUS         | 50.0       |
| COLLISION_DIST       | 0.4        |
| DT                   | 0.1        |
| ENABLE_3D            | True       |
| GEN_CPU              | 20         |
| GEN_GPU              | 20         |
| GPU_AVAILABLE        | True       |
| GRID_RES             | 5.0        |
| MAX_SPEED            | 2.0        |
| NB_DRONES            | 20         |
| NEIGHBORS            | None       |
| POP_SIZE_CPU         | 150        |
| POP_SIZE_GPU         | 5000       |
| SCENARIO             | exploration |
| SIM_STEPS            | 500        |
| VISU_STEPS           | 1000       |
| W_COLL               | 500.0      |
| W_DISP               | 0.0        |
| W_EFFORT             | 1          |
| W_EXPLO              | -50.0      |
| W_MILL               | -20.0      |
| W_POL                | -0.0       |
| Z_MAX                | 10.0       |
| Z_MIN                | 1.0        |

## 2. Optimization Evolution
| Gen  |  Best Cost   |  Time (s)  |                                                                All Parameters                                                                |
| :--: | :----------: | :--------: | :------------------------------------------------------------------------------------------------------------------------------------------ |
| 00   | -5096.2193   | 11.58      | y_att=0.66, y_ali=0.48, y_f=1.55, d0_att=3.56, l_att=1.04, l_ali=4.84, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 01   | -5117.5770   | 11.34      | y_att=0.61, y_ali=2.80, y_f=1.11, d0_att=3.44, l_att=0.23, l_ali=2.22, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 02   | -5299.6995   | 11.20      | y_att=0.58, y_ali=1.01, y_f=1.97, d0_att=3.63, l_att=0.53, l_ali=2.26, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 03   | -5681.3230   | 11.29      | y_att=1.27, y_ali=1.46, y_f=1.74, d0_att=4.73, l_att=0.59, l_ali=3.17, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 04   | -5513.4932   | 11.34      | y_att=0.58, y_ali=2.97, y_f=1.40, d0_att=4.27, l_att=0.92, l_ali=1.45, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 05   | -5788.9481   | 11.28      | y_att=0.61, y_ali=2.80, y_f=0.98, d0_att=4.31, l_att=0.23, l_ali=2.22, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 06   | -5743.2326   | 11.21      | y_att=0.93, y_ali=0.54, y_f=1.74, d0_att=4.23, l_att=0.68, l_ali=4.66, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 07   | -5685.9148   | 11.22      | y_att=0.61, y_ali=2.41, y_f=1.17, d0_att=2.84, l_att=0.27, l_ali=1.92, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 08   | -5690.0504   | 11.22      | y_att=0.58, y_ali=2.36, y_f=1.99, d0_att=3.26, l_att=0.13, l_ali=2.22, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 09   | -5651.9078   | 11.22      | y_att=0.86, y_ali=1.24, y_f=1.19, d0_att=3.46, l_att=0.28, l_ali=2.82, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 10   | -5791.3261   | 11.22      | y_att=0.83, y_ali=1.09, y_f=2.34, d0_att=1.59, l_att=0.20, l_ali=2.06, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 11   | -5985.2623   | 11.22      | y_att=0.86, y_ali=1.51, y_f=2.41, d0_att=3.35, l_att=0.24, l_ali=2.43, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 12   | -5611.6224   | 11.22      | y_att=0.39, y_ali=0.67, y_f=1.47, d0_att=1.04, l_att=0.34, l_ali=1.43, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 13   | -5659.3637   | 11.22      | y_att=0.43, y_ali=2.81, y_f=1.49, d0_att=3.92, l_att=0.21, l_ali=2.02, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 14   | -5651.4119   | 11.29      | y_att=0.66, y_ali=2.69, y_f=1.99, d0_att=1.59, l_att=0.17, l_ali=1.37, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 15   | -5686.4418   | 11.73      | y_att=1.15, y_ali=1.09, y_f=5.55, d0_att=3.34, l_att=0.36, l_ali=2.06, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 16   | -5892.2273   | 11.79      | y_att=0.47, y_ali=4.48, y_f=2.44, d0_att=0.90, l_att=0.30, l_ali=0.78, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 17   | -5695.9750   | 11.86      | y_att=0.83, y_ali=2.68, y_f=3.45, d0_att=1.73, l_att=0.19, l_ali=1.49, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 18   | -5661.6861   | 11.55      | y_att=0.88, y_ali=1.09, y_f=4.13, d0_att=3.46, l_att=0.43, l_ali=2.86, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 19   | -5744.8735   | 11.48      | y_att=0.69, y_ali=4.36, y_f=1.88, d0_att=1.32, l_att=0.37, l_ali=1.00, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |

**End of experiment.**
