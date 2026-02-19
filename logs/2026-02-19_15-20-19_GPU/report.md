# Experiment Report - GPU
**Date:** 2026-02-19_15-20-19

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
| 00   | -2257.5616   | 7.92       | y_att=1.93, y_ali=1.20, y_f=1.61, d0_att=1.80, l_att=2.39, l_ali=1.88, alpha_att=1.00, alpha_ali=0.00                                        |
| 01   | -2257.5616   | 7.50       | y_att=1.93, y_ali=1.20, y_f=1.61, d0_att=1.80, l_att=2.39, l_ali=1.88, alpha_att=1.00, alpha_ali=0.00                                        |
| 02   | -2413.4784   | 7.44       | y_att=0.72, y_ali=3.58, y_f=1.22, d0_att=1.99, l_att=4.94, l_ali=1.33, alpha_att=1.00, alpha_ali=0.00                                        |
| 03   | -2740.1047   | 7.46       | y_att=3.32, y_ali=1.51, y_f=2.30, d0_att=1.74, l_att=1.41, l_ali=1.72, alpha_att=1.00, alpha_ali=0.00                                        |
| 04   | -2740.1047   | 7.42       | y_att=3.32, y_ali=1.51, y_f=2.30, d0_att=1.74, l_att=1.41, l_ali=1.72, alpha_att=1.00, alpha_ali=0.00                                        |
| 05   | -2740.1047   | 7.50       | y_att=3.32, y_ali=1.51, y_f=2.30, d0_att=1.74, l_att=1.41, l_ali=1.72, alpha_att=1.00, alpha_ali=0.00                                        |
| 06   | -2740.1047   | 7.43       | y_att=3.32, y_ali=1.51, y_f=2.30, d0_att=1.74, l_att=1.41, l_ali=1.72, alpha_att=1.00, alpha_ali=0.00                                        |
| 07   | -2959.2892   | 7.47       | y_att=1.83, y_ali=0.25, y_f=1.74, d0_att=1.06, l_att=1.15, l_ali=3.33, alpha_att=1.00, alpha_ali=0.00                                        |
| 08   | -3010.4328   | 7.40       | y_att=3.11, y_ali=0.31, y_f=1.22, d0_att=0.72, l_att=0.68, l_ali=2.33, alpha_att=1.00, alpha_ali=0.00                                        |
| 09   | -3010.4328   | 7.40       | y_att=3.11, y_ali=0.31, y_f=1.22, d0_att=0.72, l_att=0.68, l_ali=2.33, alpha_att=1.00, alpha_ali=0.00                                        |
| 10   | -3010.4328   | 7.41       | y_att=3.11, y_ali=0.31, y_f=1.22, d0_att=0.72, l_att=0.68, l_ali=2.33, alpha_att=1.00, alpha_ali=0.00                                        |
| 11   | -3115.3848   | 7.45       | y_att=1.91, y_ali=0.29, y_f=2.37, d0_att=1.05, l_att=1.18, l_ali=3.80, alpha_att=1.00, alpha_ali=0.00                                        |
| 12   | -3115.3848   | 7.40       | y_att=1.91, y_ali=0.29, y_f=2.37, d0_att=1.05, l_att=1.18, l_ali=3.80, alpha_att=1.00, alpha_ali=0.00                                        |
| 13   | -3115.3848   | 7.45       | y_att=1.91, y_ali=0.29, y_f=2.37, d0_att=1.05, l_att=1.18, l_ali=3.80, alpha_att=1.00, alpha_ali=0.00                                        |
| 14   | -3115.3848   | 7.45       | y_att=1.91, y_ali=0.29, y_f=2.37, d0_att=1.05, l_att=1.18, l_ali=3.80, alpha_att=1.00, alpha_ali=0.00                                        |
| 15   | -3115.3848   | 7.47       | y_att=1.91, y_ali=0.29, y_f=2.37, d0_att=1.05, l_att=1.18, l_ali=3.80, alpha_att=1.00, alpha_ali=0.00                                        |
| 16   | -3115.3848   | 7.39       | y_att=1.91, y_ali=0.29, y_f=2.37, d0_att=1.05, l_att=1.18, l_ali=3.80, alpha_att=1.00, alpha_ali=0.00                                        |
| 17   | -3119.4547   | 7.40       | y_att=3.75, y_ali=0.25, y_f=2.41, d0_att=1.38, l_att=0.95, l_ali=3.74, alpha_att=1.00, alpha_ali=0.00                                        |
| 18   | -3119.4547   | 7.47       | y_att=3.75, y_ali=0.25, y_f=2.41, d0_att=1.38, l_att=0.95, l_ali=3.74, alpha_att=1.00, alpha_ali=0.00                                        |
| 19   | -3119.4547   | 7.41       | y_att=3.75, y_ali=0.25, y_f=2.41, d0_att=1.38, l_att=0.95, l_ali=3.74, alpha_att=1.00, alpha_ali=0.00                                        |

**End of experiment.**
