# Experiment Report - PyTorch_CUDA (3D)
**Date:** 2026-04-12_21-07-46

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
| NB_DRONES            | 15         |
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
| 00   | -243.5843    | 3.98       | y_att=3.27, y_ali=3.41, y_f=1.37, d0_att=1.73, l_att=4.77, l_ali=2.90, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.44, y_acc=1.74, l_acc=3.35, d0_v=0.69 |
| 01   | -328.7681    | 3.53       | y_att=3.27, y_ali=3.41, y_f=1.55, d0_att=1.73, l_att=4.77, l_ali=2.90, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.08, y_acc=1.74, l_acc=4.37, d0_v=0.69 |
| 02   | -381.6343    | 3.23       | y_att=4.68, y_ali=0.49, y_f=1.59, d0_att=1.43, l_att=4.21, l_ali=2.32, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.95, y_acc=1.40, l_acc=2.83, d0_v=0.34 |
| 03   | -431.2754    | 4.02       | y_att=2.54, y_ali=3.34, y_f=1.14, d0_att=1.39, l_att=5.09, l_ali=3.94, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.13, y_acc=2.82, l_acc=4.58, d0_v=1.46 |
| 04   | -489.1622    | 3.06       | y_att=6.48, y_ali=0.84, y_f=1.56, d0_att=2.30, l_att=4.63, l_ali=4.21, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.85, y_acc=2.37, l_acc=3.86, d0_v=0.82 |
| 05   | -471.2252    | 3.39       | y_att=1.69, y_ali=2.88, y_f=1.04, d0_att=0.74, l_att=4.37, l_ali=2.41, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.61, y_acc=2.12, l_acc=4.34, d0_v=1.09 |
| 06   | -506.3458    | 3.26       | y_att=4.14, y_ali=3.55, y_f=1.14, d0_att=2.20, l_att=5.08, l_ali=4.65, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.85, y_acc=0.99, l_acc=6.52, d0_v=0.69 |
| 07   | -501.3977    | 3.95       | y_att=4.14, y_ali=3.55, y_f=1.14, d0_att=2.20, l_att=5.08, l_ali=4.65, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.85, y_acc=0.99, l_acc=6.52, d0_v=0.69 |
| 08   | -515.8680    | 3.32       | y_att=4.14, y_ali=3.55, y_f=1.14, d0_att=2.20, l_att=5.08, l_ali=4.65, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.85, y_acc=0.99, l_acc=6.52, d0_v=0.69 |
| 09   | -514.8930    | 3.26       | y_att=4.14, y_ali=3.55, y_f=1.14, d0_att=2.20, l_att=5.08, l_ali=4.65, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.58, y_acc=0.99, l_acc=6.52, d0_v=0.69 |
| 10   | -522.6769    | 3.18       | y_att=4.14, y_ali=3.30, y_f=1.14, d0_att=2.20, l_att=5.08, l_ali=4.65, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.85, y_acc=0.99, l_acc=6.52, d0_v=0.69 |
| 11   | -519.2596    | 3.81       | y_att=4.49, y_ali=0.61, y_f=1.77, d0_att=1.39, l_att=4.63, l_ali=3.64, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.31, y_acc=1.75, l_acc=8.28, d0_v=1.05 |
| 12   | -517.6981    | 3.14       | y_att=4.49, y_ali=0.61, y_f=1.77, d0_att=1.39, l_att=4.63, l_ali=3.64, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.31, y_acc=1.75, l_acc=8.28, d0_v=1.05 |
| 13   | -505.6345    | 3.19       | y_att=4.24, y_ali=3.38, y_f=1.09, d0_att=2.02, l_att=4.69, l_ali=0.88, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.85, y_acc=1.37, l_acc=4.61, d0_v=0.72 |
| 14   | -541.0501    | 3.10       | y_att=7.62, y_ali=0.59, y_f=3.36, d0_att=1.16, l_att=4.13, l_ali=1.79, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.51, y_acc=1.54, l_acc=4.80, d0_v=0.32 |
| 15   | -502.3394    | 4.15       | y_att=3.52, y_ali=1.59, y_f=1.58, d0_att=1.46, l_att=4.97, l_ali=3.00, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.78, y_acc=1.90, l_acc=3.88, d0_v=0.65 |
| 16   | -516.7475    | 3.26       | y_att=5.48, y_ali=0.96, y_f=1.79, d0_att=1.36, l_att=4.11, l_ali=0.43, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.04, y_acc=0.79, l_acc=7.78, d0_v=0.46 |
| 17   | -521.8237    | 3.04       | y_att=7.62, y_ali=0.59, y_f=3.29, d0_att=1.16, l_att=4.13, l_ali=2.30, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.51, y_acc=1.54, l_acc=4.80, d0_v=0.32 |
| 18   | -552.8393    | 3.06       | y_att=11.59, y_ali=1.08, y_f=1.83, d0_att=1.70, l_att=3.16, l_ali=3.69, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.38, y_acc=2.46, l_acc=4.34, d0_v=0.80 |
| 19   | -548.4948    | 3.64       | y_att=11.59, y_ali=1.14, y_f=1.83, d0_att=1.70, l_att=3.16, l_ali=3.69, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.55, y_acc=2.46, l_acc=4.34, d0_v=0.80 |

**End of experiment.**
