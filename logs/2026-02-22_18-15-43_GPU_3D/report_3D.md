# Experiment Report - GPU (3D)
**Date:** 2026-02-22_18-15-43

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
| MAX_SPEED            | 2.0        |
| NB_DRONES            | 20         |
| NEIGHBORS            | None       |
| POP_SIZE_CPU         | 150        |
| POP_SIZE_GPU         | 5000       |
| SIM_STEPS            | 500        |
| VISU_STEPS           | 1000       |
| W_COLL               | 500.0      |
| W_DISP               | 0.0        |
| W_EFFORT             | 1          |
| W_MILL               | -20.0      |
| W_POL                | -0.0       |

## 2. Optimization Evolution
| Gen  |  Best Cost   |  Time (s)  |                                                                All Parameters                                                                |
| :--: | :----------: | :--------: | :------------------------------------------------------------------------------------------------------------------------------------------ |
| 00   | 121.0177     | 12.15      | y_att=1.07, y_ali=2.96, y_f=1.76, d0_att=3.88, l_att=1.06, l_ali=3.98, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00 |
| 01   | -157.2263    | 12.25      | y_att=0.39, y_ali=3.68, y_f=1.36, d0_att=3.93, l_att=1.18, l_ali=3.77, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00 |
| 02   | -383.9365    | 12.20      | y_att=0.76, y_ali=2.72, y_f=1.87, d0_att=5.48, l_att=0.33, l_ali=2.64, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00 |
| 03   | -458.9941    | 12.23      | y_att=0.58, y_ali=2.89, y_f=1.61, d0_att=5.85, l_att=0.33, l_ali=2.64, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00 |
| 04   | -407.5706    | 12.26      | y_att=0.23, y_ali=2.35, y_f=2.37, d0_att=5.22, l_att=1.11, l_ali=2.62, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00 |
| 05   | -578.6781    | 11.56      | y_att=0.66, y_ali=2.72, y_f=1.83, d0_att=5.48, l_att=0.41, l_ali=2.32, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00 |
| 06   | -696.1524    | 11.36      | y_att=0.77, y_ali=3.80, y_f=0.48, d0_att=5.61, l_att=0.70, l_ali=1.80, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00 |
| 07   | -447.0710    | 12.02      | y_att=0.51, y_ali=3.56, y_f=0.38, d0_att=3.30, l_att=0.50, l_ali=1.69, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00 |
| 08   | -412.1358    | 11.74      | y_att=0.88, y_ali=2.72, y_f=2.38, d0_att=6.61, l_att=0.24, l_ali=2.82, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00 |
| 09   | -542.8375    | 11.45      | y_att=0.32, y_ali=2.57, y_f=3.18, d0_att=5.75, l_att=0.37, l_ali=2.51, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00 |
| 10   | -477.8732    | 11.16      | y_att=0.42, y_ali=2.82, y_f=0.52, d0_att=3.59, l_att=0.34, l_ali=2.07, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00 |
| 11   | -497.8910    | 11.42      | y_att=2.17, y_ali=2.73, y_f=0.98, d0_att=6.48, l_att=0.21, l_ali=2.71, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00 |
| 12   | -578.2247    | 11.24      | y_att=0.32, y_ali=0.71, y_f=0.47, d0_att=1.90, l_att=0.24, l_ali=2.71, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00 |
| 13   | -729.6474    | 11.11      | y_att=1.00, y_ali=2.64, y_f=0.29, d0_att=7.16, l_att=0.33, l_ali=2.39, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00 |
| 14   | -723.0194    | 11.81      | y_att=0.83, y_ali=3.56, y_f=0.29, d0_att=2.79, l_att=0.20, l_ali=1.36, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00 |
| 15   | -579.9878    | 12.04      | y_att=0.83, y_ali=3.59, y_f=0.29, d0_att=2.79, l_att=0.20, l_ali=1.36, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00 |
| 16   | -639.4607    | 11.70      | y_att=1.55, y_ali=1.26, y_f=0.85, d0_att=5.54, l_att=0.22, l_ali=3.40, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00 |
| 17   | -641.8284    | 11.54      | y_att=0.84, y_ali=1.76, y_f=0.23, d0_att=12.23, l_att=0.26, l_ali=4.25, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00 |
| 18   | -796.7441    | 11.36      | y_att=1.33, y_ali=3.72, y_f=0.17, d0_att=21.12, l_att=0.15, l_ali=2.90, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00 |
| 19   | -667.8801    | 11.16      | y_att=0.71, y_ali=1.59, y_f=0.12, d0_att=2.62, l_att=0.12, l_ali=1.84, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00 |

**End of experiment.**
