# Experiment Report - GPU
**Date:** 2026-02-19_21-36-37

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
| NEIGHBORS            | 3          |
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
| 00   | -3281.9110   | 8.37       | y_att=0.55, y_ali=3.31, y_f=0.62, d0_att=3.53, l_att=4.70, l_ali=4.30, alpha_att=1.00, alpha_ali=0.00                                        |
| 01   | -3972.2078   | 7.84       | y_att=0.85, y_ali=3.32, y_f=0.87, d0_att=4.71, l_att=3.64, l_ali=4.72, alpha_att=1.00, alpha_ali=0.00                                        |
| 02   | -5143.3781   | 8.25       | y_att=0.55, y_ali=3.23, y_f=0.62, d0_att=6.11, l_att=6.60, l_ali=4.30, alpha_att=1.00, alpha_ali=0.00                                        |
| 03   | -5178.5851   | 7.59       | y_att=0.55, y_ali=3.23, y_f=0.62, d0_att=6.11, l_att=7.03, l_ali=4.30, alpha_att=1.00, alpha_ali=0.00                                        |
| 04   | -5508.8489   | 7.32       | y_att=0.47, y_ali=3.31, y_f=0.35, d0_att=5.12, l_att=4.70, l_ali=4.61, alpha_att=1.00, alpha_ali=0.00                                        |
| 05   | -5661.5411   | 7.43       | y_att=0.55, y_ali=3.31, y_f=0.37, d0_att=4.73, l_att=5.96, l_ali=4.52, alpha_att=1.00, alpha_ali=0.00                                        |
| 06   | -5710.2246   | 7.35       | y_att=0.55, y_ali=3.31, y_f=0.37, d0_att=4.73, l_att=6.46, l_ali=4.52, alpha_att=1.00, alpha_ali=0.00                                        |
| 07   | -6052.7276   | 7.33       | y_att=0.55, y_ali=0.73, y_f=2.18, d0_att=3.25, l_att=0.43, l_ali=14.59, alpha_att=1.00, alpha_ali=0.00                                       |
| 08   | -6072.2497   | 7.37       | y_att=0.52, y_ali=0.69, y_f=1.35, d0_att=3.03, l_att=0.73, l_ali=15.12, alpha_att=1.00, alpha_ali=0.00                                       |
| 09   | -6078.7537   | 7.37       | y_att=0.50, y_ali=0.73, y_f=2.21, d0_att=3.11, l_att=0.37, l_ali=14.59, alpha_att=1.00, alpha_ali=0.00                                       |
| 10   | -6090.3656   | 7.46       | y_att=0.60, y_ali=0.73, y_f=2.18, d0_att=3.25, l_att=0.53, l_ali=14.95, alpha_att=1.00, alpha_ali=0.00                                       |
| 11   | -6108.8302   | 7.72       | y_att=0.25, y_ali=0.56, y_f=2.17, d0_att=2.42, l_att=0.58, l_ali=14.73, alpha_att=1.00, alpha_ali=0.00                                       |
| 12   | -6218.3268   | 7.49       | y_att=0.37, y_ali=3.22, y_f=0.27, d0_att=6.42, l_att=11.81, l_ali=4.37, alpha_att=1.00, alpha_ali=0.00                                       |
| 13   | -6266.7432   | 7.50       | y_att=0.37, y_ali=3.22, y_f=0.27, d0_att=6.47, l_att=19.85, l_ali=4.37, alpha_att=1.00, alpha_ali=0.00                                       |
| 14   | -6266.7432   | 7.50       | y_att=0.37, y_ali=3.22, y_f=0.27, d0_att=6.47, l_att=19.85, l_ali=4.37, alpha_att=1.00, alpha_ali=0.00                                       |
| 15   | -6266.7432   | 7.79       | y_att=0.37, y_ali=3.22, y_f=0.27, d0_att=6.47, l_att=19.85, l_ali=4.37, alpha_att=1.00, alpha_ali=0.00                                       |
| 16   | -6266.7432   | 7.61       | y_att=0.37, y_ali=3.22, y_f=0.27, d0_att=6.47, l_att=19.85, l_ali=4.37, alpha_att=1.00, alpha_ali=0.00                                       |
| 17   | -6270.0653   | 7.37       | y_att=0.37, y_ali=3.22, y_f=0.27, d0_att=6.47, l_att=19.50, l_ali=4.37, alpha_att=1.00, alpha_ali=0.00                                       |
| 18   | -6270.0653   | 7.45       | y_att=0.37, y_ali=3.22, y_f=0.27, d0_att=6.47, l_att=19.50, l_ali=4.37, alpha_att=1.00, alpha_ali=0.00                                       |
| 19   | -6270.8054   | 7.55       | y_att=0.37, y_ali=3.22, y_f=0.27, d0_att=6.47, l_att=19.45, l_ali=4.37, alpha_att=1.00, alpha_ali=0.00                                       |

**End of experiment.**
