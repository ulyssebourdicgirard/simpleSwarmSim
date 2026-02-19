# Experiment Report - GPU
**Date:** 2026-02-19_15-02-46

## 1. Initial Configuration
| Parameter | Value |
| :--- | :--- |
| ARENA_RADIUS         | 25.0       |
| COLLISION_DIST       | 0.4        |
| DT                   | 0.1        |
| GEN_CPU              | 20         |
| GEN_GPU              | 30         |
| GPU_AVAILABLE        | True       |
| MAX_SPEED            | 2.0        |
| NB_DRONES            | 20         |
| NEIGHBORS            | 3          |
| POP_SIZE_CPU         | 150        |
| POP_SIZE_GPU         | 2000       |
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
| 00   | 1584.7785    | 8.68       | y_att=0.55, y_ali=2.73, y_f=1.93, d0_att=3.26, l_att=2.41, l_ali=4.76, alpha_att=1.00, alpha_ali=0.00                                        |
| 01   | 1637.3370    | 3.67       | y_att=1.00, y_ali=3.55, y_f=1.40, d0_att=2.90, l_att=1.56, l_ali=3.06, alpha_att=1.00, alpha_ali=0.00                                        |
| 02   | 1371.1821    | 3.82       | y_att=0.35, y_ali=3.26, y_f=0.96, d0_att=3.72, l_att=2.31, l_ali=3.51, alpha_att=1.00, alpha_ali=0.00                                        |
| 03   | 1282.7834    | 3.72       | y_att=0.65, y_ali=3.33, y_f=0.95, d0_att=5.86, l_att=1.36, l_ali=3.88, alpha_att=1.00, alpha_ali=0.00                                        |
| 04   | 1070.6393    | 3.64       | y_att=0.61, y_ali=2.63, y_f=0.52, d0_att=2.98, l_att=1.64, l_ali=6.25, alpha_att=1.00, alpha_ali=0.00                                        |
| 05   | 920.5929     | 3.75       | y_att=0.61, y_ali=2.63, y_f=0.52, d0_att=2.98, l_att=1.64, l_ali=6.25, alpha_att=1.00, alpha_ali=0.00                                        |
| 06   | 302.8456     | 3.61       | y_att=0.98, y_ali=2.14, y_f=0.48, d0_att=2.45, l_att=0.58, l_ali=6.54, alpha_att=1.00, alpha_ali=0.00                                        |
| 07   | 109.2941     | 3.58       | y_att=0.85, y_ali=2.14, y_f=0.18, d0_att=2.45, l_att=0.57, l_ali=6.62, alpha_att=1.00, alpha_ali=0.00                                        |
| 08   | 239.7927     | 3.58       | y_att=1.07, y_ali=2.41, y_f=0.37, d0_att=3.54, l_att=0.49, l_ali=7.16, alpha_att=1.00, alpha_ali=0.00                                        |
| 09   | -26.7247     | 3.55       | y_att=0.14, y_ali=2.39, y_f=0.16, d0_att=2.54, l_att=1.38, l_ali=5.91, alpha_att=1.00, alpha_ali=0.00                                        |
| 10   | -44.4140     | 3.63       | y_att=1.16, y_ali=2.45, y_f=0.24, d0_att=3.51, l_att=0.30, l_ali=8.00, alpha_att=1.00, alpha_ali=0.00                                        |
| 11   | -80.9012     | 3.54       | y_att=0.87, y_ali=1.86, y_f=0.23, d0_att=2.20, l_att=0.58, l_ali=7.16, alpha_att=1.00, alpha_ali=0.00                                        |
| 12   | -130.3786    | 3.57       | y_att=0.32, y_ali=2.40, y_f=0.10, d0_att=4.29, l_att=1.08, l_ali=7.79, alpha_att=1.00, alpha_ali=0.00                                        |
| 13   | -164.2931    | 3.54       | y_att=0.48, y_ali=2.92, y_f=0.12, d0_att=4.50, l_att=0.70, l_ali=6.00, alpha_att=1.00, alpha_ali=0.00                                        |
| 14   | -128.0579    | 3.60       | y_att=0.45, y_ali=2.66, y_f=0.13, d0_att=5.28, l_att=0.51, l_ali=8.73, alpha_att=1.00, alpha_ali=0.00                                        |
| 15   | -140.7145    | 3.53       | y_att=0.29, y_ali=2.40, y_f=0.12, d0_att=4.50, l_att=1.08, l_ali=7.79, alpha_att=1.00, alpha_ali=0.00                                        |
| 16   | -185.5307    | 3.61       | y_att=0.48, y_ali=2.51, y_f=0.16, d0_att=4.32, l_att=0.50, l_ali=9.07, alpha_att=1.00, alpha_ali=0.00                                        |
| 17   | -155.7092    | 3.64       | y_att=0.64, y_ali=2.29, y_f=0.11, d0_att=3.15, l_att=0.47, l_ali=6.25, alpha_att=1.00, alpha_ali=0.00                                        |
| 18   | -170.5786    | 3.66       | y_att=0.60, y_ali=2.38, y_f=0.10, d0_att=5.02, l_att=0.68, l_ali=8.10, alpha_att=1.00, alpha_ali=0.00                                        |
| 19   | -116.1791    | 3.55       | y_att=0.25, y_ali=2.45, y_f=0.11, d0_att=4.71, l_att=0.22, l_ali=8.08, alpha_att=1.00, alpha_ali=0.00                                        |
| 20   | -175.2688    | 3.70       | y_att=0.72, y_ali=2.14, y_f=0.11, d0_att=4.38, l_att=0.29, l_ali=11.52, alpha_att=1.00, alpha_ali=0.00                                       |
| 21   | -149.8938    | 3.71       | y_att=0.46, y_ali=1.94, y_f=0.14, d0_att=3.09, l_att=1.11, l_ali=9.14, alpha_att=1.00, alpha_ali=0.00                                        |
| 22   | -175.2688    | 3.57       | y_att=0.72, y_ali=2.14, y_f=0.11, d0_att=4.38, l_att=0.29, l_ali=11.52, alpha_att=1.00, alpha_ali=0.00                                       |
| 23   | -186.6270    | 3.51       | y_att=0.72, y_ali=1.87, y_f=0.13, d0_att=3.04, l_att=0.33, l_ali=9.62, alpha_att=1.00, alpha_ali=0.00                                        |
| 24   | -153.3383    | 3.72       | y_att=0.72, y_ali=2.14, y_f=0.11, d0_att=4.38, l_att=0.23, l_ali=11.52, alpha_att=1.00, alpha_ali=0.00                                       |
| 25   | -187.9768    | 3.59       | y_att=0.66, y_ali=2.09, y_f=0.10, d0_att=4.45, l_att=0.21, l_ali=10.62, alpha_att=1.00, alpha_ali=0.00                                       |
| 26   | -119.8467    | 3.54       | y_att=0.66, y_ali=2.23, y_f=0.14, d0_att=4.20, l_att=0.15, l_ali=12.24, alpha_att=1.00, alpha_ali=0.00                                       |
| 27   | -152.1581    | 3.59       | y_att=0.66, y_ali=2.23, y_f=0.11, d0_att=4.20, l_att=0.14, l_ali=8.35, alpha_att=1.00, alpha_ali=0.00                                        |
| 28   | -193.3269    | 3.60       | y_att=0.50, y_ali=2.28, y_f=0.13, d0_att=5.36, l_att=0.10, l_ali=19.19, alpha_att=1.00, alpha_ali=0.00                                       |
| 29   | -179.4113    | 3.61       | y_att=0.38, y_ali=2.44, y_f=0.11, d0_att=7.75, l_att=0.50, l_ali=16.06, alpha_att=1.00, alpha_ali=0.00                                       |

**End of experiment.**
