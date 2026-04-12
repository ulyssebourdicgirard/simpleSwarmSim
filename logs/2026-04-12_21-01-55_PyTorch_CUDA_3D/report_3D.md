# Experiment Report - PyTorch_CUDA (3D)
**Date:** 2026-04-12_21-01-55

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
| MAX_SPEED            | 2.0        |
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
| 00   | 112.7868     | 3.07       | y_att=2.61, y_ali=0.45, y_f=1.96, d0_att=2.48, l_att=4.08, l_ali=3.99, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.98, y_acc=0.14, l_acc=0.58, d0_v=2.35 |
| 01   | 104.6190     | 3.26       | y_att=2.61, y_ali=0.56, y_f=2.45, d0_att=2.05, l_att=4.08, l_ali=3.99, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.17, y_acc=0.14, l_acc=0.66, d0_v=2.35 |
| 02   | 102.1842     | 3.97       | y_att=2.62, y_ali=4.12, y_f=1.52, d0_att=1.69, l_att=3.73, l_ali=2.97, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.67, y_acc=0.03, l_acc=1.38, d0_v=2.21 |
| 03   | 95.9215      | 3.19       | y_att=3.20, y_ali=3.16, y_f=1.81, d0_att=0.96, l_att=2.61, l_ali=4.56, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.23, y_acc=0.18, l_acc=0.31, d0_v=3.98 |
| 04   | 91.4820      | 3.33       | y_att=3.20, y_ali=1.89, y_f=1.81, d0_att=1.18, l_att=2.57, l_ali=4.56, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.63, y_acc=0.18, l_acc=0.14, d0_v=3.26 |
| 05   | 89.6155      | 4.22       | y_att=4.67, y_ali=1.33, y_f=2.92, d0_att=1.22, l_att=2.31, l_ali=3.79, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.07, l_acc=0.35, d0_v=4.04 |
| 06   | 86.3322      | 3.22       | y_att=3.20, y_ali=1.43, y_f=3.59, d0_att=0.78, l_att=2.21, l_ali=5.56, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.23, y_acc=0.14, l_acc=0.34, d0_v=2.89 |
| 07   | 85.2391      | 3.23       | y_att=6.67, y_ali=1.23, y_f=3.33, d0_att=1.22, l_att=2.03, l_ali=3.93, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.60, y_acc=0.12, l_acc=0.37, d0_v=3.94 |
| 08   | 83.0111      | 3.08       | y_att=4.04, y_ali=2.38, y_f=4.10, d0_att=0.99, l_att=2.21, l_ali=5.63, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.14, y_acc=0.18, l_acc=0.15, d0_v=3.43 |
| 09   | 84.5014      | 3.30       | y_att=2.29, y_ali=4.10, y_f=4.55, d0_att=1.56, l_att=3.73, l_ali=1.52, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.33, y_acc=0.01, l_acc=1.68, d0_v=3.32 |
| 10   | 81.8306      | 3.78       | y_att=8.45, y_ali=1.09, y_f=3.83, d0_att=1.64, l_att=1.90, l_ali=5.70, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.16, y_acc=0.12, l_acc=0.19, d0_v=3.32 |
| 11   | 83.0920      | 3.18       | y_att=4.41, y_ali=0.19, y_f=4.22, d0_att=0.79, l_att=1.83, l_ali=3.98, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.57, y_acc=0.08, l_acc=0.40, d0_v=4.14 |
| 12   | 83.1248      | 3.44       | y_att=4.67, y_ali=1.93, y_f=2.50, d0_att=1.30, l_att=2.31, l_ali=5.86, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.25, y_acc=0.13, l_acc=0.17, d0_v=4.29 |
| 13   | 82.5302      | 3.35       | y_att=2.14, y_ali=3.21, y_f=4.45, d0_att=1.53, l_att=3.74, l_ali=2.08, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.47, y_acc=0.00, l_acc=0.34, d0_v=1.80 |
| 14   | 76.0390      | 2.89       | y_att=4.49, y_ali=1.65, y_f=5.49, d0_att=1.29, l_att=2.39, l_ali=25.81, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.65, y_acc=0.11, l_acc=0.19, d0_v=2.50 |
| 15   | 69.5737      | 3.02       | y_att=4.49, y_ali=1.65, y_f=5.49, d0_att=1.29, l_att=2.39, l_ali=25.81, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.65, y_acc=0.11, l_acc=0.19, d0_v=2.50 |
| 16   | 69.0152      | 3.33       | y_att=4.79, y_ali=1.65, y_f=4.78, d0_att=1.29, l_att=2.39, l_ali=32.27, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.65, y_acc=0.10, l_acc=0.19, d0_v=2.73 |
| 17   | 66.2400      | 3.97       | y_att=4.79, y_ali=1.65, y_f=4.78, d0_att=1.29, l_att=2.39, l_ali=32.27, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.65, y_acc=0.10, l_acc=0.19, d0_v=2.73 |
| 18   | 35.3159      | 3.11       | y_att=4.79, y_ali=1.65, y_f=4.78, d0_att=1.29, l_att=2.39, l_ali=37.72, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.65, y_acc=0.10, l_acc=0.19, d0_v=2.10 |
| 19   | 24.2012      | 3.43       | y_att=4.79, y_ali=1.65, y_f=4.78, d0_att=1.29, l_att=2.39, l_ali=37.72, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.65, y_acc=0.10, l_acc=0.19, d0_v=2.10 |

**End of experiment.**
