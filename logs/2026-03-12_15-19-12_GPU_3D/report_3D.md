# Experiment Report - GPU (3D)
**Date:** 2026-03-12_15-19-12

## 1. Initial Configuration
| Parameter | Value |
| :--- | :--- |
| ARENA_RADIUS         | 500.0      |
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
| 00   | -678.5094    | 19.59      | y_att=0.71, y_ali=3.58, y_f=1.48, d0_att=3.14, l_att=1.32, l_ali=4.25, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 01   | -762.9767    | 19.08      | y_att=0.91, y_ali=3.38, y_f=1.89, d0_att=3.16, l_att=0.86, l_ali=4.32, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 02   | -868.4720    | 18.60      | y_att=0.74, y_ali=2.23, y_f=2.36, d0_att=3.74, l_att=0.68, l_ali=4.01, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 03   | -966.9760    | 18.66      | y_att=0.74, y_ali=2.23, y_f=2.98, d0_att=3.68, l_att=0.68, l_ali=4.01, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 04   | -995.7964    | 18.64      | y_att=0.49, y_ali=2.13, y_f=0.88, d0_att=5.17, l_att=0.77, l_ali=4.78, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 05   | -1012.9393   | 18.58      | y_att=0.49, y_ali=2.13, y_f=0.88, d0_att=5.17, l_att=0.68, l_ali=4.78, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 06   | -1035.8015   | 18.63      | y_att=0.41, y_ali=1.70, y_f=0.55, d0_att=2.25, l_att=0.30, l_ali=3.54, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 07   | -1049.9573   | 18.62      | y_att=0.37, y_ali=0.64, y_f=3.05, d0_att=1.81, l_att=0.26, l_ali=5.22, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 08   | -1058.6864   | 18.90      | y_att=0.18, y_ali=3.88, y_f=0.70, d0_att=3.14, l_att=0.39, l_ali=2.78, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 09   | -1057.4069   | 18.67      | y_att=0.18, y_ali=3.88, y_f=0.70, d0_att=3.14, l_att=0.39, l_ali=2.78, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 10   | -1065.4506   | 18.57      | y_att=0.33, y_ali=1.70, y_f=0.34, d0_att=2.25, l_att=0.10, l_ali=3.54, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 11   | -1067.0654   | 18.59      | y_att=0.33, y_ali=1.70, y_f=0.34, d0_att=2.25, l_att=0.10, l_ali=3.54, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 12   | -1068.0391   | 18.53      | y_att=0.29, y_ali=1.70, y_f=0.34, d0_att=2.25, l_att=0.10, l_ali=3.54, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 13   | -1068.9860   | 18.76      | y_att=0.27, y_ali=1.70, y_f=0.32, d0_att=2.25, l_att=0.12, l_ali=3.54, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 14   | -1068.6400   | 18.76      | y_att=0.27, y_ali=1.70, y_f=0.18, d0_att=2.26, l_att=0.10, l_ali=3.54, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 15   | -1068.9108   | 18.61      | y_att=0.33, y_ali=1.70, y_f=0.34, d0_att=2.25, l_att=0.10, l_ali=3.54, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 16   | -1070.3056   | 23.07      | y_att=0.28, y_ali=1.70, y_f=0.16, d0_att=2.26, l_att=0.10, l_ali=3.54, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 17   | -1070.5541   | 60.16      | y_att=0.33, y_ali=1.70, y_f=0.17, d0_att=2.25, l_att=0.10, l_ali=3.54, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 18   | -1071.5423   | 111.25     | y_att=0.17, y_ali=1.70, y_f=0.18, d0_att=2.26, l_att=0.10, l_ali=3.54, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 19   | -1071.5956   | 242.10     | y_att=0.17, y_ali=2.14, y_f=0.19, d0_att=5.17, l_att=0.10, l_ali=4.78, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |

**End of experiment.**
