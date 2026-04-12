# Experiment Report - PyTorch_CUDA (3D)
**Date:** 2026-04-12_21-24-41

## 1. Initial Configuration
| Parameter | Value |
| :--- | :--- |
| ARENA_RADIUS         | 100.0      |
| COLLISION_DIST       | 0.4        |
| DT                   | 0.01       |
| ENABLE_3D            | True       |
| GEN_CPU              | 20         |
| GEN_GPU              | 20         |
| GRID_RES             | 5.0        |
| MAX_SPEED            | 20.0       |
| NB_DRONES            | 5          |
| NEIGHBORS            | 3          |
| POP_SIZE_CPU         | 150        |
| POP_SIZE_GPU         | 5000       |
| SCENARIO             | exploration |
| SIM_STEPS            | 500        |
| VISU_STEPS           | 1000       |
| W_COLL               | 500.0      |
| W_DISP               | 0.0        |
| W_EFFORT             | 1          |
| W_EXPLO              | -50.0      |
| W_MILL               | 20.0       |
| W_POL                | -0.0       |
| Z_MAX                | 10.0       |
| Z_MIN                | 1.0        |

## 2. Optimization Evolution
| Gen  |  Best Cost   |  Time (s)  |                                                                All Parameters                                                                |
| :--: | :----------: | :--------: | :------------------------------------------------------------------------------------------------------------------------------------------ |
| 00   | 123.9168     | 4.53       | y_att=3.03, y_ali=2.43, y_f=1.23, d0_att=3.50, l_att=4.63, l_ali=3.13, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.71, y_acc=0.10, l_acc=0.77, d0_v=2.53 |
| 01   | 101.9149     | 3.40       | y_att=1.94, y_ali=3.26, y_f=2.12, d0_att=1.68, l_att=4.21, l_ali=2.22, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.90, y_acc=0.14, l_acc=0.58, d0_v=3.97 |
| 02   | 94.7322      | 4.36       | y_att=1.94, y_ali=3.59, y_f=2.31, d0_att=1.68, l_att=4.21, l_ali=2.22, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.90, y_acc=0.14, l_acc=0.33, d0_v=4.91 |
| 03   | 90.5545      | 3.42       | y_att=1.94, y_ali=4.13, y_f=2.31, d0_att=1.68, l_att=4.21, l_ali=2.22, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.90, y_acc=0.12, l_acc=0.33, d0_v=4.91 |
| 04   | 85.2873      | 3.35       | y_att=1.94, y_ali=3.59, y_f=3.24, d0_att=1.68, l_att=4.21, l_ali=1.61, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.39, y_acc=0.14, l_acc=0.33, d0_v=4.91 |
| 05   | 88.5786      | 3.28       | y_att=3.63, y_ali=0.18, y_f=2.66, d0_att=1.52, l_att=2.73, l_ali=1.59, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.31, y_acc=0.10, l_acc=0.37, d0_v=4.13 |
| 06   | 87.7738      | 4.08       | y_att=1.94, y_ali=2.12, y_f=3.37, d0_att=1.49, l_att=4.21, l_ali=1.89, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.69, y_acc=0.14, l_acc=0.24, d0_v=6.45 |
| 07   | 85.4823      | 3.89       | y_att=2.14, y_ali=2.68, y_f=2.42, d0_att=1.50, l_att=3.64, l_ali=3.06, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.90, y_acc=0.09, l_acc=0.44, d0_v=4.91 |
| 08   | 83.5704      | 3.18       | y_att=1.94, y_ali=3.84, y_f=4.14, d0_att=1.78, l_att=4.21, l_ali=3.37, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.56, y_acc=0.09, l_acc=0.22, d0_v=4.42 |
| 09   | 85.2551      | 3.20       | y_att=2.05, y_ali=5.48, y_f=1.99, d0_att=1.93, l_att=4.21, l_ali=2.01, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.03, y_acc=0.16, l_acc=0.11, d0_v=3.97 |
| 10   | 81.0437      | 4.22       | y_att=3.86, y_ali=0.21, y_f=4.34, d0_att=1.48, l_att=2.67, l_ali=1.59, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.31, y_acc=0.12, l_acc=0.31, d0_v=4.42 |
| 11   | 81.7323      | 3.14       | y_att=1.67, y_ali=4.51, y_f=6.08, d0_att=1.59, l_att=4.21, l_ali=1.43, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.00, y_acc=0.23, l_acc=0.19, d0_v=8.06 |
| 12   | 83.1919      | 3.33       | y_att=1.94, y_ali=1.99, y_f=3.30, d0_att=1.68, l_att=4.10, l_ali=2.91, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.64, y_acc=0.08, l_acc=0.28, d0_v=2.26 |
| 13   | 82.2253      | 3.20       | y_att=1.68, y_ali=2.26, y_f=5.14, d0_att=1.78, l_att=4.20, l_ali=3.43, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.31, y_acc=0.17, l_acc=0.28, d0_v=7.08 |
| 14   | 80.9910      | 4.04       | y_att=1.91, y_ali=1.52, y_f=5.16, d0_att=1.78, l_att=4.21, l_ali=2.26, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.00, y_acc=0.10, l_acc=0.38, d0_v=4.42 |
| 15   | 82.5209      | 3.16       | y_att=4.14, y_ali=0.11, y_f=4.44, d0_att=1.62, l_att=2.73, l_ali=0.63, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.31, y_acc=0.09, l_acc=0.49, d0_v=4.98 |
| 16   | 82.4799      | 3.20       | y_att=1.64, y_ali=4.15, y_f=4.46, d0_att=1.43, l_att=4.29, l_ali=2.13, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.98, y_acc=0.09, l_acc=0.56, d0_v=8.99 |
| 17   | 82.0620      | 2.77       | y_att=1.55, y_ali=5.05, y_f=5.87, d0_att=1.32, l_att=4.21, l_ali=1.71, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.29, y_acc=0.09, l_acc=0.44, d0_v=4.42 |
| 18   | 80.6252      | 3.85       | y_att=0.71, y_ali=0.30, y_f=10.15, d0_att=0.80, l_att=4.54, l_ali=0.95, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.95, y_acc=0.01, l_acc=0.84, d0_v=0.84 |
| 19   | 81.2943      | 2.77       | y_att=1.90, y_ali=3.15, y_f=6.55, d0_att=1.84, l_att=4.27, l_ali=1.33, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.04, y_acc=0.15, l_acc=0.24, d0_v=9.22 |

**End of experiment.**
