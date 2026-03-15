# Experiment Report - PyTorch_CUDA (3D)
**Date:** 2026-03-15_15-52-22

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
| 00   | -771.9937    | 8.46       | y_att=0.70, y_ali=3.58, y_f=1.62, d0_att=3.44, l_att=1.14, l_ali=3.60, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 01   | -853.9453    | 8.12       | y_att=0.63, y_ali=3.53, y_f=1.77, d0_att=2.34, l_att=1.06, l_ali=3.55, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 02   | -924.4396    | 8.08       | y_att=0.32, y_ali=3.26, y_f=0.77, d0_att=3.86, l_att=0.96, l_ali=4.82, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 03   | -1021.9917   | 8.16       | y_att=1.36, y_ali=1.82, y_f=0.84, d0_att=3.05, l_att=0.38, l_ali=4.73, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 04   | -1060.9437   | 8.10       | y_att=0.73, y_ali=1.46, y_f=0.79, d0_att=2.26, l_att=0.88, l_ali=4.91, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 05   | -1054.6991   | 8.37       | y_att=0.67, y_ali=2.46, y_f=0.52, d0_att=1.55, l_att=0.44, l_ali=3.53, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 06   | -1085.4999   | 8.47       | y_att=1.05, y_ali=2.29, y_f=1.59, d0_att=3.58, l_att=0.53, l_ali=5.71, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 07   | -964.1646    | 8.16       | y_att=0.95, y_ali=3.48, y_f=0.70, d0_att=2.38, l_att=0.52, l_ali=7.22, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 08   | -1001.8871   | 8.02       | y_att=2.40, y_ali=3.48, y_f=1.62, d0_att=1.72, l_att=0.47, l_ali=5.82, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 09   | -1001.0540   | 8.09       | y_att=0.83, y_ali=2.58, y_f=1.61, d0_att=4.75, l_att=0.66, l_ali=5.07, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 10   | -999.4707    | 8.14       | y_att=0.10, y_ali=0.40, y_f=1.77, d0_att=1.51, l_att=0.74, l_ali=7.65, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 11   | -998.8839    | 8.73       | y_att=0.71, y_ali=3.17, y_f=1.35, d0_att=1.86, l_att=0.31, l_ali=6.61, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 12   | -1011.3354   | 8.75       | y_att=1.44, y_ali=7.04, y_f=1.01, d0_att=3.69, l_att=0.66, l_ali=6.16, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 13   | -1011.8908   | 8.86       | y_att=0.61, y_ali=3.32, y_f=0.58, d0_att=2.20, l_att=0.60, l_ali=4.05, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 14   | -959.2198    | 8.67       | y_att=0.57, y_ali=4.75, y_f=1.60, d0_att=1.84, l_att=0.25, l_ali=5.54, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 15   | -1038.7887   | 8.36       | y_att=0.29, y_ali=1.90, y_f=1.46, d0_att=4.80, l_att=1.04, l_ali=6.39, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 16   | -977.4261    | 8.60       | y_att=0.12, y_ali=3.31, y_f=0.35, d0_att=1.05, l_att=0.84, l_ali=4.54, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 17   | -960.1858    | 8.19       | y_att=0.44, y_ali=3.56, y_f=0.40, d0_att=2.56, l_att=0.67, l_ali=7.26, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 18   | -975.9830    | 8.17       | y_att=1.92, y_ali=2.85, y_f=1.55, d0_att=3.94, l_att=0.49, l_ali=10.00, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 19   | -1021.9410   | 8.14       | y_att=0.60, y_ali=4.75, y_f=1.00, d0_att=1.66, l_att=0.33, l_ali=2.45, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |

**End of experiment.**
