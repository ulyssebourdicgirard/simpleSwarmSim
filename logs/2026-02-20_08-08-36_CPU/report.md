# Experiment Report - CPU
**Date:** 2026-02-20_08-08-36

## 1. Initial Configuration
| Parameter | Value |
| :--- | :--- |
| ARENA_RADIUS         | 50.0       |
| COLLISION_DIST       | 0.4        |
| DT                   | 0.1        |
| GEN_CPU              | 20         |
| GEN_GPU              | 20         |
| GPU_AVAILABLE        | False      |
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
| 00   | 493.6055     | 4.52       | y_att=1.84, y_ali=0.58, y_f=1.54, d0_att=2.54, l_att=1.51, l_ali=3.54, alpha_att=1.00, alpha_ali=0.00                                        |
| 01   | 493.0259     | 2.65       | y_att=1.58, y_ali=0.80, y_f=1.71, d0_att=3.06, l_att=1.11, l_ali=4.21, alpha_att=1.00, alpha_ali=0.00                                        |
| 02   | 361.9638     | 2.64       | y_att=1.58, y_ali=0.69, y_f=1.71, d0_att=3.06, l_att=1.11, l_ali=4.21, alpha_att=1.00, alpha_ali=0.00                                        |
| 03   | 357.5471     | 2.43       | y_att=1.58, y_ali=0.68, y_f=1.71, d0_att=3.06, l_att=1.11, l_ali=4.21, alpha_att=1.00, alpha_ali=0.00                                        |
| 04   | 350.8659     | 2.50       | y_att=0.86, y_ali=0.69, y_f=1.71, d0_att=3.06, l_att=1.11, l_ali=4.21, alpha_att=1.00, alpha_ali=0.00                                        |
| 05   | 323.4608     | 4.11       | y_att=1.71, y_ali=0.80, y_f=1.71, d0_att=4.70, l_att=1.11, l_ali=4.21, alpha_att=1.00, alpha_ali=0.00                                        |
| 06   | 274.1971     | 4.77       | y_att=0.74, y_ali=0.68, y_f=1.71, d0_att=3.81, l_att=1.11, l_ali=4.21, alpha_att=1.00, alpha_ali=0.00                                        |
| 07   | 208.1206     | 4.69       | y_att=0.48, y_ali=0.69, y_f=1.71, d0_att=3.06, l_att=1.11, l_ali=4.21, alpha_att=1.00, alpha_ali=0.00                                        |
| 08   | 68.0303      | 4.64       | y_att=0.36, y_ali=0.69, y_f=1.71, d0_att=3.06, l_att=1.11, l_ali=4.21, alpha_att=1.00, alpha_ali=0.00                                        |
| 09   | -234.5305    | 4.79       | y_att=0.19, y_ali=0.57, y_f=1.71, d0_att=4.09, l_att=1.11, l_ali=4.21, alpha_att=1.00, alpha_ali=0.00                                        |
| 10   | -271.8111    | 4.64       | y_att=0.15, y_ali=0.57, y_f=1.71, d0_att=4.09, l_att=1.11, l_ali=4.21, alpha_att=1.00, alpha_ali=0.00                                        |
| 11   | -290.1118    | 4.62       | y_att=0.31, y_ali=0.98, y_f=1.71, d0_att=6.53, l_att=1.11, l_ali=4.21, alpha_att=1.00, alpha_ali=0.00                                        |
| 12   | -334.0778    | 4.80       | y_att=0.10, y_ali=0.57, y_f=1.71, d0_att=4.64, l_att=1.11, l_ali=4.21, alpha_att=1.00, alpha_ali=0.00                                        |
| 13   | -334.0778    | 5.30       | y_att=0.10, y_ali=0.57, y_f=1.71, d0_att=4.64, l_att=1.11, l_ali=4.21, alpha_att=1.00, alpha_ali=0.00                                        |
| 14   | -350.8538    | 5.17       | y_att=0.10, y_ali=0.70, y_f=1.71, d0_att=4.73, l_att=1.11, l_ali=4.21, alpha_att=1.00, alpha_ali=0.00                                        |
| 15   | -356.3111    | 5.16       | y_att=0.10, y_ali=0.70, y_f=1.71, d0_att=4.73, l_att=1.11, l_ali=4.21, alpha_att=1.00, alpha_ali=0.00                                        |
| 16   | -360.2879    | 4.82       | y_att=0.11, y_ali=0.70, y_f=1.71, d0_att=4.73, l_att=1.11, l_ali=4.21, alpha_att=1.00, alpha_ali=0.00                                        |
| 17   | -363.3744    | 4.56       | y_att=0.12, y_ali=0.73, y_f=1.71, d0_att=4.97, l_att=1.11, l_ali=4.21, alpha_att=1.00, alpha_ali=0.00                                        |
| 18   | -363.3744    | 4.45       | y_att=0.12, y_ali=0.73, y_f=1.71, d0_att=4.97, l_att=1.11, l_ali=4.21, alpha_att=1.00, alpha_ali=0.00                                        |
| 19   | -363.3744    | 4.67       | y_att=0.12, y_ali=0.73, y_f=1.71, d0_att=4.97, l_att=1.11, l_ali=4.21, alpha_att=1.00, alpha_ali=0.00                                        |

**End of experiment.**
