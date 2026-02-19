# Experiment Report - GPU
**Date:** 2026-02-19_21-41-49

## 1. Initial Configuration
| Parameter | Value |
| :--- | :--- |
| ARENA_RADIUS         | 50.0       |
| COLLISION_DIST       | 0.4        |
| DT                   | 0.1        |
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
| 00   | 329.8612     | 6.70       | y_att=2.56, y_ali=1.59, y_f=1.91, d0_att=3.66, l_att=1.20, l_ali=2.06, alpha_att=1.00, alpha_ali=0.00                                        |
| 01   | 74.3169      | 6.25       | y_att=2.58, y_ali=0.28, y_f=1.24, d0_att=1.54, l_att=0.23, l_ali=3.93, alpha_att=1.00, alpha_ali=0.00                                        |
| 02   | -264.6960    | 6.26       | y_att=2.58, y_ali=0.28, y_f=1.24, d0_att=1.54, l_att=0.13, l_ali=3.93, alpha_att=1.00, alpha_ali=0.00                                        |
| 03   | -264.6960    | 6.28       | y_att=2.58, y_ali=0.28, y_f=1.24, d0_att=1.54, l_att=0.13, l_ali=3.93, alpha_att=1.00, alpha_ali=0.00                                        |
| 04   | -312.2351    | 6.35       | y_att=0.38, y_ali=3.24, y_f=1.98, d0_att=6.09, l_att=0.56, l_ali=1.37, alpha_att=1.00, alpha_ali=0.00                                        |
| 05   | -521.9329    | 6.32       | y_att=1.79, y_ali=0.80, y_f=0.10, d0_att=3.86, l_att=0.32, l_ali=4.17, alpha_att=1.00, alpha_ali=0.00                                        |
| 06   | -628.2314    | 6.26       | y_att=1.14, y_ali=0.40, y_f=0.15, d0_att=2.13, l_att=0.18, l_ali=3.05, alpha_att=1.00, alpha_ali=0.00                                        |
| 07   | -679.9784    | 6.37       | y_att=1.71, y_ali=0.40, y_f=0.10, d0_att=2.32, l_att=0.10, l_ali=3.05, alpha_att=1.00, alpha_ali=0.00                                        |
| 08   | -695.3200    | 6.34       | y_att=0.52, y_ali=0.58, y_f=0.11, d0_att=3.21, l_att=0.32, l_ali=2.94, alpha_att=1.00, alpha_ali=0.00                                        |
| 09   | -704.2595    | 6.28       | y_att=1.76, y_ali=0.80, y_f=0.10, d0_att=4.03, l_att=0.27, l_ali=2.84, alpha_att=1.00, alpha_ali=0.00                                        |
| 10   | -713.7289    | 6.29       | y_att=1.00, y_ali=0.54, y_f=0.10, d0_att=4.67, l_att=0.27, l_ali=1.71, alpha_att=1.00, alpha_ali=0.00                                        |
| 11   | -775.3892    | 6.29       | y_att=0.50, y_ali=0.54, y_f=0.10, d0_att=4.67, l_att=0.25, l_ali=1.71, alpha_att=1.00, alpha_ali=0.00                                        |
| 12   | -777.9315    | 6.28       | y_att=0.50, y_ali=0.54, y_f=0.10, d0_att=4.67, l_att=0.23, l_ali=1.71, alpha_att=1.00, alpha_ali=0.00                                        |
| 13   | -777.9315    | 6.33       | y_att=0.50, y_ali=0.54, y_f=0.10, d0_att=4.67, l_att=0.23, l_ali=1.71, alpha_att=1.00, alpha_ali=0.00                                        |
| 14   | -781.7818    | 6.49       | y_att=1.68, y_ali=0.10, y_f=0.10, d0_att=2.25, l_att=0.10, l_ali=3.00, alpha_att=1.00, alpha_ali=0.00                                        |
| 15   | -793.8516    | 6.20       | y_att=0.42, y_ali=0.38, y_f=0.10, d0_att=5.39, l_att=0.35, l_ali=2.18, alpha_att=1.00, alpha_ali=0.00                                        |
| 16   | -793.8516    | 6.29       | y_att=0.42, y_ali=0.38, y_f=0.10, d0_att=5.39, l_att=0.35, l_ali=2.18, alpha_att=1.00, alpha_ali=0.00                                        |
| 17   | -804.2683    | 6.37       | y_att=0.76, y_ali=0.19, y_f=0.11, d0_att=5.07, l_att=0.32, l_ali=3.06, alpha_att=1.00, alpha_ali=0.00                                        |
| 18   | -810.5176    | 6.43       | y_att=0.76, y_ali=0.17, y_f=0.11, d0_att=4.52, l_att=0.29, l_ali=3.06, alpha_att=1.00, alpha_ali=0.00                                        |
| 19   | -815.3614    | 6.42       | y_att=0.78, y_ali=0.17, y_f=0.10, d0_att=4.67, l_att=0.27, l_ali=3.09, alpha_att=1.00, alpha_ali=0.00                                        |

**End of experiment.**
