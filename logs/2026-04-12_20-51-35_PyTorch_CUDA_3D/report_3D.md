# Experiment Report - PyTorch_CUDA (3D)
**Date:** 2026-04-12_20-51-35

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
| 00   | -3118.0908   | 3.08       | y_att=2.77, y_ali=0.16, y_f=1.22, d0_att=3.65, l_att=1.53, l_ali=2.15, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.71, y_acc=0.44, l_acc=0.75, d0_v=2.44 |
| 01   | -3156.0605   | 2.67       | y_att=1.08, y_ali=2.59, y_f=1.70, d0_att=2.18, l_att=1.73, l_ali=3.53, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.50, y_acc=0.17, l_acc=1.41, d0_v=1.88 |
| 02   | -3310.1528   | 2.71       | y_att=4.95, y_ali=4.20, y_f=2.38, d0_att=3.90, l_att=1.35, l_ali=1.50, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.44, y_acc=0.73, l_acc=0.77, d0_v=3.43 |
| 03   | -3254.1917   | 2.73       | y_att=2.40, y_ali=2.02, y_f=1.98, d0_att=2.86, l_att=1.50, l_ali=3.22, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.39, y_acc=0.69, l_acc=0.61, d0_v=2.96 |
| 04   | -3353.7063   | 2.80       | y_att=3.63, y_ali=3.35, y_f=2.57, d0_att=3.65, l_att=1.75, l_ali=2.15, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.97, y_acc=0.20, l_acc=2.46, d0_v=2.09 |
| 05   | -3367.8643   | 2.74       | y_att=4.24, y_ali=0.98, y_f=2.85, d0_att=3.08, l_att=1.12, l_ali=3.22, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.74, y_acc=0.29, l_acc=0.63, d0_v=1.43 |
| 06   | -3312.5322   | 2.68       | y_att=0.80, y_ali=2.29, y_f=2.20, d0_att=4.11, l_att=3.14, l_ali=0.38, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.25, l_acc=0.93, d0_v=1.93 |
| 07   | -3341.6506   | 2.70       | y_att=2.21, y_ali=1.13, y_f=3.28, d0_att=3.70, l_att=2.31, l_ali=1.57, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.66, y_acc=0.14, l_acc=3.83, d0_v=2.38 |
| 08   | -3340.6990   | 2.71       | y_att=1.19, y_ali=1.40, y_f=2.58, d0_att=1.32, l_att=1.47, l_ali=4.16, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.54, y_acc=0.38, l_acc=2.10, d0_v=4.18 |
| 09   | -3361.9070   | 2.72       | y_att=5.51, y_ali=0.97, y_f=2.82, d0_att=3.00, l_att=1.22, l_ali=1.00, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.07, y_acc=0.18, l_acc=3.74, d0_v=2.86 |
| 10   | -3366.1028   | 2.68       | y_att=1.75, y_ali=3.84, y_f=4.27, d0_att=4.45, l_att=2.46, l_ali=2.27, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.06, y_acc=0.63, l_acc=0.38, d0_v=1.73 |
| 11   | -3339.9709   | 2.69       | y_att=0.86, y_ali=0.20, y_f=2.30, d0_att=2.29, l_att=2.29, l_ali=2.55, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.63, y_acc=0.03, l_acc=2.94, d0_v=0.68 |
| 12   | -3356.5142   | 2.70       | y_att=2.33, y_ali=1.73, y_f=1.96, d0_att=3.93, l_att=1.55, l_ali=1.81, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.24, y_acc=0.17, l_acc=1.26, d0_v=2.25 |
| 13   | -3356.2683   | 2.70       | y_att=0.49, y_ali=2.34, y_f=1.56, d0_att=3.36, l_att=3.05, l_ali=2.52, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.03, y_acc=0.12, l_acc=1.85, d0_v=2.41 |
| 14   | -3398.7197   | 2.68       | y_att=1.29, y_ali=0.70, y_f=1.74, d0_att=2.93, l_att=2.00, l_ali=2.20, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.30, y_acc=0.33, l_acc=1.04, d0_v=2.52 |
| 15   | -3368.3142   | 2.69       | y_att=3.63, y_ali=5.57, y_f=3.16, d0_att=3.86, l_att=1.75, l_ali=1.90, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.03, y_acc=0.27, l_acc=2.64, d0_v=3.49 |
| 16   | -3368.2852   | 2.69       | y_att=1.63, y_ali=1.93, y_f=2.42, d0_att=2.38, l_att=1.65, l_ali=0.55, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.91, y_acc=0.21, l_acc=1.29, d0_v=1.83 |
| 17   | -3364.1987   | 2.69       | y_att=3.70, y_ali=0.97, y_f=3.00, d0_att=3.51, l_att=1.29, l_ali=1.76, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.75, y_acc=0.49, l_acc=0.48, d0_v=1.97 |
| 18   | -3371.7876   | 2.68       | y_att=2.12, y_ali=0.90, y_f=2.77, d0_att=3.70, l_att=2.43, l_ali=1.66, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.91, y_acc=0.15, l_acc=3.71, d0_v=2.19 |
| 19   | -3392.3201   | 2.69       | y_att=4.37, y_ali=1.45, y_f=2.96, d0_att=3.05, l_att=1.17, l_ali=1.44, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.44, y_acc=0.49, l_acc=1.14, d0_v=3.70 |

**End of experiment.**
