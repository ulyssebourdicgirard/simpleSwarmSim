# Experiment Report - PyTorch_CUDA (3D)
**Date:** 2026-04-12_20-49-03

## 1. Initial Configuration
| Parameter | Value |
| :--- | :--- |
| ARENA_RADIUS         | 50.0       |
| COLLISION_DIST       | 0.4        |
| DT                   | 0.1        |
| ENABLE_3D            | True       |
| GEN_CPU              | 20         |
| GEN_GPU              | 20         |
| GRID_RES             | 5.0        |
| MAX_SPEED            | 2.0        |
| NB_DRONES            | 10         |
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
| 00   | -2061.8071   | 3.08       | y_att=0.84, y_ali=1.55, y_f=1.76, d0_att=2.07, l_att=2.07, l_ali=2.33, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.15, y_acc=0.34, l_acc=0.95, d0_v=2.44 |
| 01   | -2140.3196   | 3.15       | y_att=3.97, y_ali=3.76, y_f=1.62, d0_att=2.75, l_att=1.00, l_ali=1.93, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.18, y_acc=0.19, l_acc=0.77, d0_v=1.76 |
| 02   | -2192.1724   | 3.31       | y_att=2.29, y_ali=1.22, y_f=1.74, d0_att=3.82, l_att=1.82, l_ali=2.02, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.29, y_acc=0.86, l_acc=0.40, d0_v=2.69 |
| 03   | -2227.3362   | 3.25       | y_att=3.15, y_ali=0.74, y_f=1.64, d0_att=2.22, l_att=1.01, l_ali=5.40, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.54, y_acc=0.15, l_acc=0.65, d0_v=2.28 |
| 04   | -2188.7876   | 3.14       | y_att=4.46, y_ali=3.00, y_f=1.62, d0_att=3.14, l_att=1.00, l_ali=1.56, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.40, y_acc=0.11, l_acc=0.77, d0_v=1.27 |
| 05   | -2222.7795   | 2.94       | y_att=1.37, y_ali=2.41, y_f=1.97, d0_att=3.30, l_att=1.64, l_ali=3.22, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.94, y_acc=0.22, l_acc=0.47, d0_v=1.73 |
| 06   | -2235.6030   | 2.89       | y_att=1.05, y_ali=1.63, y_f=2.30, d0_att=4.02, l_att=1.44, l_ali=4.25, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.43, y_acc=0.33, l_acc=1.18, d0_v=3.01 |
| 07   | -2228.7432   | 2.81       | y_att=2.72, y_ali=0.39, y_f=2.17, d0_att=2.45, l_att=1.15, l_ali=1.65, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.52, y_acc=0.41, l_acc=0.51, d0_v=2.29 |
| 08   | -2227.6160   | 2.95       | y_att=1.87, y_ali=4.28, y_f=2.04, d0_att=2.21, l_att=0.90, l_ali=1.95, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.80, y_acc=0.07, l_acc=1.00, d0_v=2.02 |
| 09   | -2187.3079   | 3.22       | y_att=2.18, y_ali=1.18, y_f=1.59, d0_att=2.60, l_att=1.54, l_ali=2.20, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.48, y_acc=0.67, l_acc=0.59, d0_v=2.77 |
| 10   | -2223.6357   | 3.10       | y_att=2.98, y_ali=4.15, y_f=1.65, d0_att=3.65, l_att=1.36, l_ali=0.87, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.61, y_acc=0.37, l_acc=0.48, d0_v=2.58 |
| 11   | -2223.1179   | 2.73       | y_att=3.63, y_ali=0.78, y_f=2.01, d0_att=2.54, l_att=1.08, l_ali=2.04, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.90, y_acc=0.29, l_acc=1.16, d0_v=2.08 |
| 12   | -2251.7712   | 2.67       | y_att=0.70, y_ali=1.46, y_f=2.15, d0_att=2.72, l_att=2.28, l_ali=0.92, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.62, y_acc=0.40, l_acc=0.45, d0_v=1.86 |
| 13   | -2210.5166   | 2.65       | y_att=0.63, y_ali=1.49, y_f=2.46, d0_att=2.87, l_att=2.66, l_ali=1.36, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.88, y_acc=0.36, l_acc=0.78, d0_v=2.99 |
| 14   | -2272.4885   | 2.65       | y_att=2.84, y_ali=5.53, y_f=1.37, d0_att=9.83, l_att=2.69, l_ali=3.08, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.64, y_acc=0.24, l_acc=0.26, d0_v=1.04 |
| 15   | -2208.9561   | 2.63       | y_att=3.06, y_ali=0.86, y_f=3.62, d0_att=0.70, l_att=0.56, l_ali=3.20, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.17, y_acc=0.17, l_acc=0.64, d0_v=1.82 |
| 16   | -2232.9075   | 2.64       | y_att=1.16, y_ali=2.17, y_f=1.95, d0_att=5.75, l_att=2.98, l_ali=2.07, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.69, y_acc=0.42, l_acc=2.42, d0_v=8.90 |
| 17   | -2215.7290   | 2.65       | y_att=1.51, y_ali=0.81, y_f=1.69, d0_att=2.07, l_att=1.36, l_ali=2.94, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.18, y_acc=0.24, l_acc=0.88, d0_v=3.47 |
| 18   | -2217.5469   | 2.64       | y_att=2.47, y_ali=3.02, y_f=3.57, d0_att=4.67, l_att=2.09, l_ali=9.37, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.50, y_acc=0.29, l_acc=0.33, d0_v=0.54 |
| 19   | -2219.7991   | 2.65       | y_att=0.81, y_ali=2.04, y_f=2.97, d0_att=2.13, l_att=2.58, l_ali=3.01, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.71, y_acc=0.23, l_acc=2.20, d0_v=2.53 |

**End of experiment.**
