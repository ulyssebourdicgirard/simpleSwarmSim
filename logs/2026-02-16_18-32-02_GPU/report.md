# Experiment Report - GPU
**Date:** 2026-02-16_18-32-02

## 1. Initial Configuration
| Parameter | Value |
| :--- | :--- |
| ARENA_RADIUS         | 50.0       |
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
| W_POL                | -2.0       |

## 2. Optimization Evolution
| Gen  |  Best Cost   |  Time (s)  |                                                                All Parameters                                                                |
| :--: | :----------: | :--------: | :------------------------------------------------------------------------------------------------------------------------------------------ |
| 00   | 11064.9672   | 2.69       | y_att=3.62, y_ali=3.98, y_f=0.54, d0_att=1.15, l_att=1.10, l_ali=1.45, alpha_att=1.00, alpha_ali=0.00                                        |
| 01   | 11051.0370   | 2.69       | y_att=3.62, y_ali=3.98, y_f=0.54, d0_att=1.15, l_att=1.10, l_ali=1.45, alpha_att=1.00, alpha_ali=0.00                                        |
| 02   | 10882.1185   | 2.63       | y_att=3.62, y_ali=3.57, y_f=0.42, d0_att=1.18, l_att=1.10, l_ali=1.45, alpha_att=1.00, alpha_ali=0.00                                        |
| 03   | 10093.1200   | 2.87       | y_att=0.86, y_ali=2.28, y_f=0.59, d0_att=1.23, l_att=0.51, l_ali=1.81, alpha_att=1.00, alpha_ali=0.00                                        |
| 04   | 8501.0495    | 2.63       | y_att=1.16, y_ali=2.28, y_f=0.56, d0_att=1.23, l_att=0.10, l_ali=2.24, alpha_att=1.00, alpha_ali=0.00                                        |
| 05   | 8774.7036    | 2.65       | y_att=0.86, y_ali=3.04, y_f=0.59, d0_att=1.23, l_att=0.51, l_ali=1.81, alpha_att=1.00, alpha_ali=0.00                                        |
| 06   | 8182.5244    | 2.76       | y_att=4.38, y_ali=2.62, y_f=0.10, d0_att=1.01, l_att=0.71, l_ali=1.05, alpha_att=1.00, alpha_ali=0.00                                        |
| 07   | 8178.7364    | 2.73       | y_att=4.38, y_ali=2.62, y_f=0.10, d0_att=1.01, l_att=0.71, l_ali=1.05, alpha_att=1.00, alpha_ali=0.00                                        |
| 08   | 8127.0414    | 2.53       | y_att=4.38, y_ali=2.62, y_f=0.10, d0_att=1.01, l_att=0.46, l_ali=1.05, alpha_att=1.00, alpha_ali=0.00                                        |
| 09   | 7918.8225    | 2.73       | y_att=2.60, y_ali=3.33, y_f=0.10, d0_att=0.91, l_att=0.29, l_ali=1.05, alpha_att=1.00, alpha_ali=0.00                                        |
| 10   | 7694.3852    | 2.51       | y_att=2.60, y_ali=4.45, y_f=0.10, d0_att=1.25, l_att=0.29, l_ali=1.15, alpha_att=1.00, alpha_ali=0.00                                        |
| 11   | 7029.5476    | 2.56       | y_att=5.35, y_ali=2.23, y_f=0.11, d0_att=0.91, l_att=0.22, l_ali=1.64, alpha_att=1.00, alpha_ali=0.00                                        |
| 12   | 6545.8072    | 2.71       | y_att=2.60, y_ali=4.45, y_f=0.10, d0_att=1.25, l_att=0.29, l_ali=1.15, alpha_att=1.00, alpha_ali=0.00                                        |
| 13   | 6297.4593    | 2.70       | y_att=2.18, y_ali=3.33, y_f=0.10, d0_att=0.91, l_att=0.24, l_ali=1.27, alpha_att=1.00, alpha_ali=0.00                                        |
| 14   | 6171.1388    | 2.69       | y_att=2.17, y_ali=3.01, y_f=0.10, d0_att=0.91, l_att=0.30, l_ali=1.46, alpha_att=1.00, alpha_ali=0.00                                        |
| 15   | 5810.6104    | 2.75       | y_att=4.96, y_ali=2.47, y_f=0.10, d0_att=0.91, l_att=0.18, l_ali=1.93, alpha_att=1.00, alpha_ali=0.00                                        |
| 16   | 5965.8633    | 2.68       | y_att=3.39, y_ali=2.39, y_f=0.10, d0_att=0.91, l_att=0.27, l_ali=1.93, alpha_att=1.00, alpha_ali=0.00                                        |
| 17   | 5784.5692    | 2.73       | y_att=5.08, y_ali=2.47, y_f=0.10, d0_att=0.91, l_att=0.18, l_ali=1.93, alpha_att=1.00, alpha_ali=0.00                                        |
| 18   | 5659.3649    | 2.72       | y_att=3.39, y_ali=2.39, y_f=0.10, d0_att=0.91, l_att=0.20, l_ali=1.93, alpha_att=1.00, alpha_ali=0.00                                        |
| 19   | 5771.7533    | 2.71       | y_att=2.00, y_ali=1.91, y_f=0.10, d0_att=0.55, l_att=0.17, l_ali=1.64, alpha_att=1.00, alpha_ali=0.00                                        |

**End of experiment.**
