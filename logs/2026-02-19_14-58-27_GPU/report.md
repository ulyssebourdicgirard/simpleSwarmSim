# Experiment Report - GPU
**Date:** 2026-02-19_14-58-27

## 1. Initial Configuration
| Parameter | Value |
| :--- | :--- |
| ARENA_RADIUS         | 50.0       |
| COLLISION_DIST       | 0.6        |
| DT                   | 0.1        |
| GEN_CPU              | 20         |
| GEN_GPU              | 20         |
| GPU_AVAILABLE        | True       |
| MAX_SPEED            | 2.0        |
| NB_DRONES            | 40         |
| NEIGHBORS            | 3          |
| POP_SIZE_CPU         | 150        |
| POP_SIZE_GPU         | 100        |
| SIM_STEPS            | 500        |
| VISU_STEPS           | 1000       |
| W_COLL               | 5000.0     |
| W_DISP               | 1.0        |
| W_EFFORT             | 0.05       |
| W_MILL               | -2.0       |
| W_POL                | -2.0       |

## 2. Optimization Evolution
| Gen  |  Best Cost   |  Time (s)  |                                                                All Parameters                                                                |
| :--: | :----------: | :--------: | :------------------------------------------------------------------------------------------------------------------------------------------ |
| 00   | 12121.2002   | 3.01       | y_att=1.67, y_ali=2.55, y_f=1.44, d0_att=1.74, l_att=4.31, l_ali=1.72, alpha_att=1.00, alpha_ali=0.00                                        |
| 01   | 11954.7150   | 3.03       | y_att=1.67, y_ali=3.70, y_f=1.44, d0_att=1.74, l_att=4.31, l_ali=1.72, alpha_att=1.00, alpha_ali=0.00                                        |
| 02   | 11449.5259   | 3.01       | y_att=0.99, y_ali=2.07, y_f=1.14, d0_att=1.30, l_att=3.76, l_ali=2.93, alpha_att=1.00, alpha_ali=0.00                                        |
| 03   | 11367.9263   | 3.08       | y_att=1.11, y_ali=3.42, y_f=0.88, d0_att=1.59, l_att=4.67, l_ali=2.18, alpha_att=1.00, alpha_ali=0.00                                        |
| 04   | 10963.3595   | 2.96       | y_att=0.98, y_ali=2.07, y_f=0.46, d0_att=1.30, l_att=3.76, l_ali=2.93, alpha_att=1.00, alpha_ali=0.00                                        |
| 05   | 10888.4789   | 3.02       | y_att=0.98, y_ali=2.07, y_f=0.46, d0_att=1.30, l_att=3.32, l_ali=2.93, alpha_att=1.00, alpha_ali=0.00                                        |
| 06   | 10539.4733   | 2.87       | y_att=0.98, y_ali=2.07, y_f=0.29, d0_att=1.30, l_att=3.88, l_ali=2.93, alpha_att=1.00, alpha_ali=0.00                                        |
| 07   | 10298.6180   | 2.98       | y_att=1.29, y_ali=1.88, y_f=0.22, d0_att=1.30, l_att=2.02, l_ali=0.90, alpha_att=1.00, alpha_ali=0.00                                        |
| 08   | 8966.9136    | 2.83       | y_att=0.98, y_ali=2.27, y_f=0.13, d0_att=1.27, l_att=3.88, l_ali=2.93, alpha_att=1.00, alpha_ali=0.00                                        |
| 09   | 8371.9862    | 2.87       | y_att=1.29, y_ali=1.88, y_f=0.10, d0_att=1.30, l_att=2.02, l_ali=0.86, alpha_att=1.00, alpha_ali=0.00                                        |
| 10   | 8333.7693    | 3.04       | y_att=1.29, y_ali=1.82, y_f=0.10, d0_att=1.30, l_att=1.91, l_ali=0.86, alpha_att=1.00, alpha_ali=0.00                                        |
| 11   | 7976.3219    | 2.89       | y_att=0.98, y_ali=2.27, y_f=0.10, d0_att=1.27, l_att=3.88, l_ali=2.93, alpha_att=1.00, alpha_ali=0.00                                        |
| 12   | 7999.8543    | 2.91       | y_att=0.72, y_ali=2.27, y_f=0.10, d0_att=1.27, l_att=3.88, l_ali=2.93, alpha_att=1.00, alpha_ali=0.00                                        |
| 13   | 7927.7863    | 3.00       | y_att=0.98, y_ali=2.27, y_f=0.10, d0_att=1.30, l_att=4.03, l_ali=2.93, alpha_att=1.00, alpha_ali=0.00                                        |
| 14   | 7437.8452    | 3.18       | y_att=1.29, y_ali=3.08, y_f=0.10, d0_att=1.30, l_att=0.61, l_ali=1.19, alpha_att=1.00, alpha_ali=0.00                                        |
| 15   | 7490.2888    | 2.90       | y_att=1.29, y_ali=3.08, y_f=0.10, d0_att=1.30, l_att=0.61, l_ali=1.19, alpha_att=1.00, alpha_ali=0.00                                        |
| 16   | 7070.2157    | 2.87       | y_att=1.31, y_ali=3.67, y_f=0.10, d0_att=1.30, l_att=0.61, l_ali=1.23, alpha_att=1.00, alpha_ali=0.00                                        |
| 17   | 6709.0325    | 2.98       | y_att=1.37, y_ali=3.67, y_f=0.10, d0_att=1.30, l_att=0.40, l_ali=1.30, alpha_att=1.00, alpha_ali=0.00                                        |
| 18   | 6813.5697    | 2.82       | y_att=1.37, y_ali=3.67, y_f=0.10, d0_att=1.30, l_att=0.40, l_ali=1.30, alpha_att=1.00, alpha_ali=0.00                                        |
| 19   | 6309.8835    | 2.87       | y_att=0.83, y_ali=3.08, y_f=0.11, d0_att=1.15, l_att=0.48, l_ali=1.55, alpha_att=1.00, alpha_ali=0.00                                        |

**End of experiment.**
