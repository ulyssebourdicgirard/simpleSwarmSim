# Experiment Report - CPU (3D)
**Date:** 2026-03-13_13-15-03

## 1. Initial Configuration
| Parameter | Value |
| :--- | :--- |
| ARENA_RADIUS         | 50.0       |
| COLLISION_DIST       | 0.4        |
| DT                   | 0.1        |
| ENABLE_3D            | True       |
| GEN_CPU              | 20         |
| GEN_GPU              | 2          |
| GPU_AVAILABLE        | False      |
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
| Z_MAX                | 10.0       |
| Z_MIN                | 1.0        |

## 2. Optimization Evolution
| Gen  |  Best Cost   |  Time (s)  |                                                                All Parameters                                                                |
| :--: | :----------: | :--------: | :------------------------------------------------------------------------------------------------------------------------------------------ |
| 00   | 363.0117     | 2.90       | y_att=0.77, y_ali=1.15, y_f=1.41, d0_att=2.02, l_att=1.20, l_ali=4.63, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 01   | 330.6966     | 2.48       | y_att=0.77, y_ali=1.15, y_f=1.41, d0_att=2.38, l_att=1.20, l_ali=4.63, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 02   | 231.5675     | 2.46       | y_att=0.81, y_ali=2.33, y_f=1.46, d0_att=2.38, l_att=1.02, l_ali=3.60, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 03   | 143.3397     | 2.56       | y_att=0.27, y_ali=2.38, y_f=1.46, d0_att=1.86, l_att=1.02, l_ali=3.60, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 04   | 21.1669      | 2.46       | y_att=0.36, y_ali=1.15, y_f=1.41, d0_att=2.40, l_att=1.20, l_ali=4.63, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 05   | 21.1669      | 2.46       | y_att=0.36, y_ali=1.15, y_f=1.41, d0_att=2.40, l_att=1.20, l_ali=4.63, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 06   | -119.4061    | 2.47       | y_att=0.25, y_ali=1.89, y_f=1.46, d0_att=2.49, l_att=1.02, l_ali=3.60, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 07   | -139.2897    | 2.53       | y_att=0.23, y_ali=1.89, y_f=1.46, d0_att=2.49, l_att=1.02, l_ali=3.60, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 08   | -156.7086    | 2.55       | y_att=0.22, y_ali=1.89, y_f=1.46, d0_att=2.49, l_att=1.02, l_ali=3.60, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 09   | -196.7560    | 2.59       | y_att=0.16, y_ali=1.89, y_f=1.46, d0_att=2.49, l_att=1.02, l_ali=3.60, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 10   | -197.0238    | 2.62       | y_att=0.19, y_ali=1.96, y_f=1.46, d0_att=2.49, l_att=1.02, l_ali=3.60, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 11   | -209.0593    | 2.69       | y_att=0.15, y_ali=2.45, y_f=1.46, d0_att=4.91, l_att=1.02, l_ali=3.60, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 12   | -209.0593    | 2.69       | y_att=0.15, y_ali=2.45, y_f=1.46, d0_att=4.91, l_att=1.02, l_ali=3.60, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 13   | -217.6537    | 2.71       | y_att=0.10, y_ali=2.36, y_f=1.46, d0_att=4.38, l_att=1.02, l_ali=3.60, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 14   | -217.6537    | 2.71       | y_att=0.10, y_ali=2.36, y_f=1.46, d0_att=4.38, l_att=1.02, l_ali=3.60, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 15   | -220.7440    | 2.78       | y_att=0.10, y_ali=2.45, y_f=1.46, d0_att=4.47, l_att=1.02, l_ali=3.60, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 16   | -223.5841    | 2.77       | y_att=0.10, y_ali=2.43, y_f=1.46, d0_att=4.38, l_att=1.02, l_ali=3.60, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 17   | -223.5841    | 2.78       | y_att=0.10, y_ali=2.43, y_f=1.46, d0_att=4.38, l_att=1.02, l_ali=3.60, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 18   | -230.2351    | 2.80       | y_att=0.11, y_ali=2.72, y_f=1.46, d0_att=4.97, l_att=1.02, l_ali=3.60, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 19   | -230.2351    | 2.83       | y_att=0.11, y_ali=2.72, y_f=1.46, d0_att=4.97, l_att=1.02, l_ali=3.60, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |

**End of experiment.**
