# Experiment Report - GPU (3D)
**Date:** 2026-02-22_18-05-36

## 1. Initial Configuration
| Parameter | Value |
| :--- | :--- |
| ARENA_RADIUS         | 50.0       |
| COLLISION_DIST       | 0.4        |
| DT                   | 0.1        |
| ENABLE_3D            | True       |
| GEN_CPU              | 20         |
| GEN_GPU              | 20         |
| GPU_AVAILABLE        | True       |
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
| 00   | 143.0283     | 13.04      | y_att=0.55, y_ali=2.72, y_f=1.95, d0_att=2.77, l_att=1.17, l_ali=3.09, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00 |
| 01   | -170.2547    | 12.26      | y_att=0.57, y_ali=2.26, y_f=1.79, d0_att=3.68, l_att=0.92, l_ali=3.74, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00 |
| 02   | -253.5705    | 12.48      | y_att=1.16, y_ali=2.60, y_f=0.48, d0_att=2.23, l_att=0.36, l_ali=2.76, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00 |
| 03   | -288.6727    | 12.46      | y_att=1.14, y_ali=1.94, y_f=0.97, d0_att=3.99, l_att=0.50, l_ali=2.74, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00 |
| 04   | -478.6606    | 11.21      | y_att=0.64, y_ali=2.56, y_f=1.31, d0_att=3.03, l_att=0.49, l_ali=1.87, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00 |
| 05   | -401.5668    | 11.23      | y_att=0.66, y_ali=1.94, y_f=0.89, d0_att=4.46, l_att=1.04, l_ali=2.38, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00 |
| 06   | -453.6795    | 11.21      | y_att=0.51, y_ali=1.03, y_f=0.53, d0_att=1.35, l_att=0.31, l_ali=2.02, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00 |
| 07   | -515.1671    | 11.23      | y_att=0.82, y_ali=2.18, y_f=1.02, d0_att=3.15, l_att=0.49, l_ali=1.97, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00 |
| 08   | -549.2085    | 11.98      | y_att=1.15, y_ali=2.47, y_f=0.65, d0_att=3.09, l_att=0.32, l_ali=1.80, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00 |
| 09   | -399.2123    | 12.19      | y_att=0.54, y_ali=4.03, y_f=1.29, d0_att=2.47, l_att=0.38, l_ali=1.41, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00 |
| 10   | -554.4881    | 11.77      | y_att=0.62, y_ali=1.31, y_f=0.79, d0_att=5.03, l_att=0.26, l_ali=3.45, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00 |
| 11   | -656.4157    | 10.99      | y_att=0.67, y_ali=1.31, y_f=1.06, d0_att=7.32, l_att=0.30, l_ali=3.64, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00 |
| 12   | -677.2960    | 11.04      | y_att=0.98, y_ali=1.65, y_f=0.18, d0_att=3.69, l_att=0.26, l_ali=2.11, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00 |
| 13   | -579.0055    | 12.46      | y_att=0.21, y_ali=0.58, y_f=0.55, d0_att=4.14, l_att=0.65, l_ali=4.37, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00 |
| 14   | -637.8917    | 12.57      | y_att=0.72, y_ali=2.93, y_f=0.12, d0_att=3.55, l_att=0.28, l_ali=1.49, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00 |
| 15   | -488.4882    | 11.98      | y_att=1.00, y_ali=2.19, y_f=0.14, d0_att=2.23, l_att=0.14, l_ali=1.65, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00 |
| 16   | -548.3186    | 11.31      | y_att=0.36, y_ali=2.32, y_f=0.18, d0_att=7.73, l_att=0.38, l_ali=2.82, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00 |
| 17   | -596.0695    | 11.16      | y_att=0.62, y_ali=1.56, y_f=0.12, d0_att=2.97, l_att=0.14, l_ali=2.16, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00 |
| 18   | -583.8012    | 11.51      | y_att=1.12, y_ali=2.00, y_f=0.18, d0_att=3.16, l_att=0.21, l_ali=1.99, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00 |
| 19   | -705.2261    | 11.02      | y_att=0.60, y_ali=2.75, y_f=0.17, d0_att=6.74, l_att=0.16, l_ali=2.15, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00 |

**End of experiment.**
