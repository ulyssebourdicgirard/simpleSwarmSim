# Experiment Report - GPU
**Date:** 2026-02-19_15-11-45

## 1. Initial Configuration
| Parameter | Value |
| :--- | :--- |
| ARENA_RADIUS         | 15.0       |
| COLLISION_DIST       | 0.4        |
| DT                   | 0.1        |
| GEN_CPU              | 20         |
| GEN_GPU              | 20         |
| GPU_AVAILABLE        | True       |
| MAX_SPEED            | 2.0        |
| NB_DRONES            | 20         |
| NEIGHBORS            | 3          |
| POP_SIZE_CPU         | 150        |
| POP_SIZE_GPU         | 5000       |
| SIM_STEPS            | 500        |
| VISU_STEPS           | 1000       |
| W_COLL               | 500.0      |
| W_DISP               | 1.0        |
| W_EFFORT             | 1          |
| W_MILL               | -20.0      |
| W_POL                | -2.0       |

## 2. Optimization Evolution
| Gen  |  Best Cost   |  Time (s)  |                                                                All Parameters                                                                |
| :--: | :----------: | :--------: | :------------------------------------------------------------------------------------------------------------------------------------------ |
| 00   | -2675.3981   | 8.08       | y_att=1.88, y_ali=1.97, y_f=1.18, d0_att=2.60, l_att=2.64, l_ali=2.40, alpha_att=1.00, alpha_ali=0.00                                        |
| 01   | -2675.3981   | 7.52       | y_att=1.88, y_ali=1.97, y_f=1.18, d0_att=2.60, l_att=2.64, l_ali=2.40, alpha_att=1.00, alpha_ali=0.00                                        |
| 02   | -2675.3981   | 7.83       | y_att=1.88, y_ali=1.97, y_f=1.18, d0_att=2.60, l_att=2.64, l_ali=2.40, alpha_att=1.00, alpha_ali=0.00                                        |
| 03   | -2965.2759   | 7.76       | y_att=1.57, y_ali=1.77, y_f=1.80, d0_att=2.52, l_att=3.28, l_ali=2.13, alpha_att=1.00, alpha_ali=0.00                                        |
| 04   | -2965.2759   | 7.89       | y_att=1.57, y_ali=1.77, y_f=1.80, d0_att=2.52, l_att=3.28, l_ali=2.13, alpha_att=1.00, alpha_ali=0.00                                        |
| 05   | -2996.8936   | 7.86       | y_att=1.62, y_ali=2.56, y_f=2.70, d0_att=2.77, l_att=3.16, l_ali=2.17, alpha_att=1.00, alpha_ali=0.00                                        |
| 06   | -2996.8936   | 7.92       | y_att=1.62, y_ali=2.56, y_f=2.70, d0_att=2.77, l_att=3.16, l_ali=2.17, alpha_att=1.00, alpha_ali=0.00                                        |
| 07   | -2996.8936   | 7.71       | y_att=1.62, y_ali=2.56, y_f=2.70, d0_att=2.77, l_att=3.16, l_ali=2.17, alpha_att=1.00, alpha_ali=0.00                                        |
| 08   | -2996.8936   | 7.78       | y_att=1.62, y_ali=2.56, y_f=2.70, d0_att=2.77, l_att=3.16, l_ali=2.17, alpha_att=1.00, alpha_ali=0.00                                        |
| 09   | -2996.8936   | 7.62       | y_att=1.62, y_ali=2.56, y_f=2.70, d0_att=2.77, l_att=3.16, l_ali=2.17, alpha_att=1.00, alpha_ali=0.00                                        |
| 10   | -2996.8936   | 7.79       | y_att=1.62, y_ali=2.56, y_f=2.70, d0_att=2.77, l_att=3.16, l_ali=2.17, alpha_att=1.00, alpha_ali=0.00                                        |
| 11   | -3034.2938   | 7.77       | y_att=0.40, y_ali=2.03, y_f=1.02, d0_att=1.10, l_att=1.70, l_ali=1.15, alpha_att=1.00, alpha_ali=0.00                                        |
| 12   | -3186.0454   | 7.74       | y_att=0.30, y_ali=4.98, y_f=1.22, d0_att=1.23, l_att=2.40, l_ali=0.79, alpha_att=1.00, alpha_ali=0.00                                        |
| 13   | -3186.0454   | 7.67       | y_att=0.30, y_ali=4.98, y_f=1.22, d0_att=1.23, l_att=2.40, l_ali=0.79, alpha_att=1.00, alpha_ali=0.00                                        |
| 14   | -3186.0454   | 7.92       | y_att=0.30, y_ali=4.98, y_f=1.22, d0_att=1.23, l_att=2.40, l_ali=0.79, alpha_att=1.00, alpha_ali=0.00                                        |
| 15   | -3191.4672   | 7.73       | y_att=0.33, y_ali=4.12, y_f=1.81, d0_att=1.12, l_att=2.09, l_ali=0.82, alpha_att=1.00, alpha_ali=0.00                                        |
| 16   | -3300.3925   | 7.49       | y_att=0.46, y_ali=2.03, y_f=1.36, d0_att=1.10, l_att=1.59, l_ali=1.15, alpha_att=1.00, alpha_ali=0.00                                        |
| 17   | -3300.5655   | 7.47       | y_att=0.40, y_ali=4.43, y_f=1.86, d0_att=1.53, l_att=2.51, l_ali=0.94, alpha_att=1.00, alpha_ali=0.00                                        |
| 18   | -3300.5655   | 7.24       | y_att=0.40, y_ali=4.43, y_f=1.86, d0_att=1.53, l_att=2.51, l_ali=0.94, alpha_att=1.00, alpha_ali=0.00                                        |
| 19   | -3342.0229   | 7.36       | y_att=0.31, y_ali=4.38, y_f=1.72, d0_att=1.76, l_att=3.59, l_ali=1.04, alpha_att=1.00, alpha_ali=0.00                                        |

**End of experiment.**
