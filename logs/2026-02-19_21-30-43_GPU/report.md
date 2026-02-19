# Experiment Report - GPU
**Date:** 2026-02-19_21-30-43

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
| W_DISP               | 0.0        |
| W_EFFORT             | 1          |
| W_MILL               | -20.0      |
| W_POL                | -0.0       |

## 2. Optimization Evolution
| Gen  |  Best Cost   |  Time (s)  |                                                                All Parameters                                                                |
| :--: | :----------: | :--------: | :------------------------------------------------------------------------------------------------------------------------------------------ |
| 00   | -3783.9587   | 8.55       | y_att=0.89, y_ali=0.62, y_f=1.12, d0_att=1.64, l_att=3.12, l_ali=3.46, alpha_att=1.00, alpha_ali=0.00                                        |
| 01   | -4059.3942   | 7.58       | y_att=1.25, y_ali=2.29, y_f=1.81, d0_att=2.40, l_att=3.14, l_ali=2.12, alpha_att=1.00, alpha_ali=0.00                                        |
| 02   | -4059.3942   | 7.61       | y_att=1.25, y_ali=2.29, y_f=1.81, d0_att=2.40, l_att=3.14, l_ali=2.12, alpha_att=1.00, alpha_ali=0.00                                        |
| 03   | -4112.6164   | 7.64       | y_att=1.10, y_ali=2.12, y_f=1.98, d0_att=2.28, l_att=4.85, l_ali=3.12, alpha_att=1.00, alpha_ali=0.00                                        |
| 04   | -4325.8317   | 7.62       | y_att=1.49, y_ali=1.68, y_f=3.58, d0_att=2.32, l_att=4.07, l_ali=2.66, alpha_att=1.00, alpha_ali=0.00                                        |
| 05   | -4560.6891   | 7.63       | y_att=1.99, y_ali=3.54, y_f=1.54, d0_att=2.54, l_att=3.71, l_ali=1.79, alpha_att=1.00, alpha_ali=0.00                                        |
| 06   | -4560.6891   | 7.74       | y_att=1.99, y_ali=3.54, y_f=1.54, d0_att=2.54, l_att=3.71, l_ali=1.79, alpha_att=1.00, alpha_ali=0.00                                        |
| 07   | -4560.6891   | 7.52       | y_att=1.99, y_ali=3.54, y_f=1.54, d0_att=2.54, l_att=3.71, l_ali=1.79, alpha_att=1.00, alpha_ali=0.00                                        |
| 08   | -4560.6891   | 7.78       | y_att=1.99, y_ali=3.54, y_f=1.54, d0_att=2.54, l_att=3.71, l_ali=1.79, alpha_att=1.00, alpha_ali=0.00                                        |
| 09   | -4603.6103   | 8.00       | y_att=1.49, y_ali=2.26, y_f=1.63, d0_att=2.72, l_att=4.37, l_ali=2.66, alpha_att=1.00, alpha_ali=0.00                                        |
| 10   | -4603.6103   | 7.80       | y_att=1.49, y_ali=2.26, y_f=1.63, d0_att=2.72, l_att=4.37, l_ali=2.66, alpha_att=1.00, alpha_ali=0.00                                        |
| 11   | -4603.6103   | 8.02       | y_att=1.49, y_ali=2.26, y_f=1.63, d0_att=2.72, l_att=4.37, l_ali=2.66, alpha_att=1.00, alpha_ali=0.00                                        |
| 12   | -4626.3753   | 7.63       | y_att=1.24, y_ali=3.54, y_f=3.66, d0_att=2.54, l_att=4.10, l_ali=1.34, alpha_att=1.00, alpha_ali=0.00                                        |
| 13   | -4626.3753   | 7.38       | y_att=1.24, y_ali=3.54, y_f=3.66, d0_att=2.54, l_att=4.10, l_ali=1.34, alpha_att=1.00, alpha_ali=0.00                                        |
| 14   | -4626.3753   | 7.93       | y_att=1.24, y_ali=3.54, y_f=3.66, d0_att=2.54, l_att=4.10, l_ali=1.34, alpha_att=1.00, alpha_ali=0.00                                        |
| 15   | -4626.3753   | 7.89       | y_att=1.24, y_ali=3.54, y_f=3.66, d0_att=2.54, l_att=4.10, l_ali=1.34, alpha_att=1.00, alpha_ali=0.00                                        |
| 16   | -4734.8256   | 7.83       | y_att=1.41, y_ali=1.46, y_f=2.03, d0_att=2.32, l_att=4.07, l_ali=2.81, alpha_att=1.00, alpha_ali=0.00                                        |
| 17   | -4734.8256   | 7.72       | y_att=1.41, y_ali=1.46, y_f=2.03, d0_att=2.32, l_att=4.07, l_ali=2.81, alpha_att=1.00, alpha_ali=0.00                                        |
| 18   | -4734.8256   | 7.46       | y_att=1.41, y_ali=1.46, y_f=2.03, d0_att=2.32, l_att=4.07, l_ali=2.81, alpha_att=1.00, alpha_ali=0.00                                        |
| 19   | -4734.8256   | 7.31       | y_att=1.41, y_ali=1.46, y_f=2.03, d0_att=2.32, l_att=4.07, l_ali=2.81, alpha_att=1.00, alpha_ali=0.00                                        |

**End of experiment.**
