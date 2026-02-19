# Experiment Report - GPU
**Date:** 2026-02-19_15-07-51

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
| W_COLL               | 500.0      |
| W_DISP               | 1.0        |
| W_EFFORT             | 1          |
| W_MILL               | -20.0      |
| W_POL                | -2.0       |

## 2. Optimization Evolution
| Gen  |  Best Cost   |  Time (s)  |                                                                All Parameters                                                                |
| :--: | :----------: | :--------: | :------------------------------------------------------------------------------------------------------------------------------------------ |
| 00   | 210.8048     | 3.85       | y_att=0.97, y_ali=2.74, y_f=1.80, d0_att=2.15, l_att=1.16, l_ali=2.61, alpha_att=1.00, alpha_ali=0.00                                        |
| 01   | 6.0854       | 3.71       | y_att=0.51, y_ali=1.61, y_f=1.29, d0_att=1.39, l_att=1.02, l_ali=2.91, alpha_att=1.00, alpha_ali=0.00                                        |
| 02   | -373.7000    | 3.65       | y_att=1.12, y_ali=1.03, y_f=0.67, d0_att=1.47, l_att=1.11, l_ali=4.44, alpha_att=1.00, alpha_ali=0.00                                        |
| 03   | -2026.0618   | 3.62       | y_att=0.90, y_ali=2.90, y_f=0.25, d0_att=3.45, l_att=1.70, l_ali=4.38, alpha_att=1.00, alpha_ali=0.00                                        |
| 04   | -2499.2199   | 3.61       | y_att=0.90, y_ali=2.90, y_f=0.25, d0_att=4.81, l_att=1.70, l_ali=4.73, alpha_att=1.00, alpha_ali=0.00                                        |
| 05   | -2618.5183   | 3.65       | y_att=0.91, y_ali=2.55, y_f=0.19, d0_att=3.65, l_att=1.70, l_ali=4.73, alpha_att=1.00, alpha_ali=0.00                                        |
| 06   | -3039.2988   | 3.69       | y_att=0.55, y_ali=2.90, y_f=0.11, d0_att=4.43, l_att=1.62, l_ali=3.93, alpha_att=1.00, alpha_ali=0.00                                        |
| 07   | -3473.9617   | 3.65       | y_att=0.90, y_ali=2.16, y_f=0.16, d0_att=3.86, l_att=1.87, l_ali=5.44, alpha_att=1.00, alpha_ali=0.00                                        |
| 08   | -4031.1298   | 3.64       | y_att=0.55, y_ali=2.75, y_f=0.10, d0_att=4.43, l_att=1.62, l_ali=6.49, alpha_att=1.00, alpha_ali=0.00                                        |
| 09   | -4031.1298   | 3.71       | y_att=0.55, y_ali=2.75, y_f=0.10, d0_att=4.43, l_att=1.62, l_ali=6.49, alpha_att=1.00, alpha_ali=0.00                                        |
| 10   | -4031.1298   | 3.67       | y_att=0.55, y_ali=2.75, y_f=0.10, d0_att=4.43, l_att=1.62, l_ali=6.49, alpha_att=1.00, alpha_ali=0.00                                        |
| 11   | -4203.2390   | 3.56       | y_att=1.02, y_ali=2.74, y_f=0.10, d0_att=5.07, l_att=1.30, l_ali=6.78, alpha_att=1.00, alpha_ali=0.00                                        |
| 12   | -4203.2390   | 3.64       | y_att=1.02, y_ali=2.74, y_f=0.10, d0_att=5.07, l_att=1.30, l_ali=6.78, alpha_att=1.00, alpha_ali=0.00                                        |
| 13   | -4206.5063   | 3.67       | y_att=1.50, y_ali=2.74, y_f=0.10, d0_att=5.07, l_att=0.94, l_ali=6.78, alpha_att=1.00, alpha_ali=0.00                                        |
| 14   | -4217.4888   | 3.66       | y_att=1.45, y_ali=2.74, y_f=0.10, d0_att=5.07, l_att=0.94, l_ali=6.78, alpha_att=1.00, alpha_ali=0.00                                        |
| 15   | -4235.5701   | 3.62       | y_att=1.50, y_ali=2.74, y_f=0.10, d0_att=5.07, l_att=1.01, l_ali=6.63, alpha_att=1.00, alpha_ali=0.00                                        |
| 16   | -4236.5747   | 3.58       | y_att=1.50, y_ali=2.77, y_f=0.10, d0_att=5.07, l_att=0.94, l_ali=6.78, alpha_att=1.00, alpha_ali=0.00                                        |
| 17   | -4236.5747   | 3.65       | y_att=1.50, y_ali=2.77, y_f=0.10, d0_att=5.07, l_att=0.94, l_ali=6.78, alpha_att=1.00, alpha_ali=0.00                                        |
| 18   | -4274.0825   | 3.63       | y_att=0.51, y_ali=2.90, y_f=0.10, d0_att=7.70, l_att=2.04, l_ali=6.74, alpha_att=1.00, alpha_ali=0.00                                        |
| 19   | -4287.1703   | 3.61       | y_att=0.38, y_ali=2.75, y_f=0.10, d0_att=6.13, l_att=3.13, l_ali=6.49, alpha_att=1.00, alpha_ali=0.00                                        |
| 20   | -4287.1703   | 3.61       | y_att=0.38, y_ali=2.75, y_f=0.10, d0_att=6.13, l_att=3.13, l_ali=6.49, alpha_att=1.00, alpha_ali=0.00                                        |
| 21   | -4287.1703   | 3.60       | y_att=0.38, y_ali=2.75, y_f=0.10, d0_att=6.13, l_att=3.13, l_ali=6.49, alpha_att=1.00, alpha_ali=0.00                                        |
| 22   | -4295.0471   | 3.56       | y_att=2.16, y_ali=2.74, y_f=0.10, d0_att=5.07, l_att=0.80, l_ali=6.78, alpha_att=1.00, alpha_ali=0.00                                        |
| 23   | -4295.0471   | 3.58       | y_att=2.16, y_ali=2.74, y_f=0.10, d0_att=5.07, l_att=0.80, l_ali=6.78, alpha_att=1.00, alpha_ali=0.00                                        |
| 24   | -4302.6629   | 3.63       | y_att=0.38, y_ali=2.75, y_f=0.10, d0_att=6.13, l_att=3.39, l_ali=6.49, alpha_att=1.00, alpha_ali=0.00                                        |
| 25   | -4302.7244   | 3.58       | y_att=0.38, y_ali=2.75, y_f=0.10, d0_att=6.13, l_att=3.39, l_ali=6.49, alpha_att=1.00, alpha_ali=0.00                                        |
| 26   | -4318.9986   | 3.62       | y_att=0.39, y_ali=2.77, y_f=0.10, d0_att=6.70, l_att=3.16, l_ali=6.49, alpha_att=1.00, alpha_ali=0.00                                        |
| 27   | -4318.9986   | 3.57       | y_att=0.39, y_ali=2.77, y_f=0.10, d0_att=6.70, l_att=3.16, l_ali=6.49, alpha_att=1.00, alpha_ali=0.00                                        |
| 28   | -4321.8307   | 3.65       | y_att=0.38, y_ali=2.75, y_f=0.10, d0_att=6.48, l_att=3.30, l_ali=6.49, alpha_att=1.00, alpha_ali=0.00                                        |
| 29   | -4321.8307   | 3.71       | y_att=0.38, y_ali=2.75, y_f=0.10, d0_att=6.48, l_att=3.30, l_ali=6.49, alpha_att=1.00, alpha_ali=0.00                                        |

**End of experiment.**
