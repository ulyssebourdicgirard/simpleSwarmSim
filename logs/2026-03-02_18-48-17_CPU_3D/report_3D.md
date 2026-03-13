# Experiment Report - CPU (3D)
**Date:** 2026-03-02_18-48-17

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
| 00   | 283.9926     | 2.98       | y_att=0.90, y_ali=1.28, y_f=1.09, d0_att=2.28, l_att=1.03, l_ali=4.52, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 01   | 264.2738     | 2.54       | y_att=0.90, y_ali=1.28, y_f=1.09, d0_att=3.05, l_att=1.03, l_ali=4.52, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 02   | 159.5282     | 2.52       | y_att=0.90, y_ali=2.15, y_f=1.09, d0_att=3.05, l_att=1.03, l_ali=4.52, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 03   | 101.5946     | 2.53       | y_att=1.01, y_ali=1.98, y_f=1.09, d0_att=3.76, l_att=1.03, l_ali=4.52, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 04   | -95.4093     | 2.53       | y_att=0.45, y_ali=1.68, y_f=1.09, d0_att=3.34, l_att=1.03, l_ali=4.52, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 05   | -178.4363    | 2.52       | y_att=0.23, y_ali=1.68, y_f=1.09, d0_att=4.66, l_att=1.03, l_ali=4.52, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 06   | -178.4363    | 2.53       | y_att=0.23, y_ali=1.68, y_f=1.09, d0_att=4.66, l_att=1.03, l_ali=4.52, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 07   | -202.1662    | 2.52       | y_att=0.26, y_ali=1.68, y_f=1.09, d0_att=3.47, l_att=1.03, l_ali=4.52, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 08   | -204.9840    | 2.55       | y_att=0.26, y_ali=1.68, y_f=1.09, d0_att=3.50, l_att=1.03, l_ali=4.52, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 09   | -214.7233    | 2.61       | y_att=0.10, y_ali=1.68, y_f=1.09, d0_att=4.66, l_att=1.03, l_ali=4.52, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 10   | -214.7233    | 2.63       | y_att=0.10, y_ali=1.68, y_f=1.09, d0_att=4.66, l_att=1.03, l_ali=4.52, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 11   | -220.7691    | 2.66       | y_att=0.10, y_ali=1.67, y_f=1.09, d0_att=4.66, l_att=1.03, l_ali=4.52, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 12   | -220.7691    | 2.71       | y_att=0.10, y_ali=1.67, y_f=1.09, d0_att=4.66, l_att=1.03, l_ali=4.52, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 13   | -222.0121    | 2.75       | y_att=0.10, y_ali=1.68, y_f=1.09, d0_att=4.78, l_att=1.03, l_ali=4.52, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 14   | -222.0121    | 2.77       | y_att=0.10, y_ali=1.68, y_f=1.09, d0_att=4.78, l_att=1.03, l_ali=4.52, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 15   | -222.0121    | 2.80       | y_att=0.10, y_ali=1.68, y_f=1.09, d0_att=4.78, l_att=1.03, l_ali=4.52, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 16   | -223.5924    | 2.83       | y_att=0.10, y_ali=1.66, y_f=1.09, d0_att=4.66, l_att=1.03, l_ali=4.52, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 17   | -223.5924    | 2.85       | y_att=0.10, y_ali=1.66, y_f=1.09, d0_att=4.66, l_att=1.03, l_ali=4.52, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 18   | -224.0003    | 2.84       | y_att=0.10, y_ali=1.69, y_f=1.09, d0_att=4.78, l_att=1.03, l_ali=4.52, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 19   | -224.0003    | 2.89       | y_att=0.10, y_ali=1.69, y_f=1.09, d0_att=4.78, l_att=1.03, l_ali=4.52, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |

**End of experiment.**
