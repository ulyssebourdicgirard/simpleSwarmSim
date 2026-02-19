# Experiment Report - GPU
**Date:** 2026-02-19_15-28-19

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
| 00   | -2273.2619   | 7.63       | y_att=1.73, y_ali=3.73, y_f=1.84, d0_att=2.84, l_att=3.66, l_ali=1.88, alpha_att=1.00, alpha_ali=0.00                                        |
| 01   | -2273.2619   | 7.44       | y_att=1.73, y_ali=3.73, y_f=1.84, d0_att=2.84, l_att=3.66, l_ali=1.88, alpha_att=1.00, alpha_ali=0.00                                        |
| 02   | -2273.2619   | 7.41       | y_att=1.73, y_ali=3.73, y_f=1.84, d0_att=2.84, l_att=3.66, l_ali=1.88, alpha_att=1.00, alpha_ali=0.00                                        |
| 03   | -2408.9907   | 7.44       | y_att=0.99, y_ali=2.58, y_f=1.56, d0_att=2.79, l_att=5.64, l_ali=2.51, alpha_att=1.00, alpha_ali=0.00                                        |
| 04   | -2408.9907   | 7.44       | y_att=0.99, y_ali=2.58, y_f=1.56, d0_att=2.79, l_att=5.64, l_ali=2.51, alpha_att=1.00, alpha_ali=0.00                                        |
| 05   | -2427.2180   | 7.41       | y_att=1.70, y_ali=3.90, y_f=1.69, d0_att=2.71, l_att=3.78, l_ali=1.93, alpha_att=1.00, alpha_ali=0.00                                        |
| 06   | -2683.0842   | 7.43       | y_att=1.13, y_ali=1.88, y_f=2.24, d0_att=2.79, l_att=4.34, l_ali=2.62, alpha_att=1.00, alpha_ali=0.00                                        |
| 07   | -2683.0842   | 7.43       | y_att=1.13, y_ali=1.88, y_f=2.24, d0_att=2.79, l_att=4.34, l_ali=2.62, alpha_att=1.00, alpha_ali=0.00                                        |
| 08   | -2683.0842   | 7.46       | y_att=1.13, y_ali=1.88, y_f=2.24, d0_att=2.79, l_att=4.34, l_ali=2.62, alpha_att=1.00, alpha_ali=0.00                                        |
| 09   | -2683.0842   | 7.45       | y_att=1.13, y_ali=1.88, y_f=2.24, d0_att=2.79, l_att=4.34, l_ali=2.62, alpha_att=1.00, alpha_ali=0.00                                        |
| 10   | -2731.8401   | 7.44       | y_att=0.95, y_ali=2.33, y_f=1.96, d0_att=2.79, l_att=4.91, l_ali=1.63, alpha_att=1.00, alpha_ali=0.00                                        |
| 11   | -2839.5530   | 7.46       | y_att=0.68, y_ali=2.41, y_f=1.71, d0_att=2.78, l_att=7.41, l_ali=2.28, alpha_att=1.00, alpha_ali=0.00                                        |
| 12   | -2981.3105   | 7.44       | y_att=0.92, y_ali=6.18, y_f=2.60, d0_att=2.85, l_att=4.60, l_ali=1.29, alpha_att=1.00, alpha_ali=0.00                                        |
| 13   | -2981.3105   | 7.45       | y_att=0.92, y_ali=6.18, y_f=2.60, d0_att=2.85, l_att=4.60, l_ali=1.29, alpha_att=1.00, alpha_ali=0.00                                        |
| 14   | -2981.3105   | 7.46       | y_att=0.92, y_ali=6.18, y_f=2.60, d0_att=2.85, l_att=4.60, l_ali=1.29, alpha_att=1.00, alpha_ali=0.00                                        |
| 15   | -2981.3105   | 7.47       | y_att=0.92, y_ali=6.18, y_f=2.60, d0_att=2.85, l_att=4.60, l_ali=1.29, alpha_att=1.00, alpha_ali=0.00                                        |
| 16   | -2981.3105   | 7.47       | y_att=0.92, y_ali=6.18, y_f=2.60, d0_att=2.85, l_att=4.60, l_ali=1.29, alpha_att=1.00, alpha_ali=0.00                                        |
| 17   | -2981.3105   | 7.51       | y_att=0.92, y_ali=6.18, y_f=2.60, d0_att=2.85, l_att=4.60, l_ali=1.29, alpha_att=1.00, alpha_ali=0.00                                        |
| 18   | -2981.3105   | 7.42       | y_att=0.92, y_ali=6.18, y_f=2.60, d0_att=2.85, l_att=4.60, l_ali=1.29, alpha_att=1.00, alpha_ali=0.00                                        |
| 19   | -2981.3105   | 7.51       | y_att=0.92, y_ali=6.18, y_f=2.60, d0_att=2.85, l_att=4.60, l_ali=1.29, alpha_att=1.00, alpha_ali=0.00                                        |

**End of experiment.**
