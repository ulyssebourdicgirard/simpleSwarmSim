# Experiment Report - PyTorch_CUDA (3D)
**Date:** 2026-04-12_21-36-49

## 1. Initial Configuration
| Parameter | Value |
| :--- | :--- |
| ALPHA_LPF            | 0.2        |
| ARENA_RADIUS         | 100.0      |
| COLLISION_DIST       | 0.4        |
| DT                   | 0.01       |
| ENABLE_3D            | True       |
| GEN_CPU              | 20         |
| GEN_GPU              | 20         |
| GRID_RES             | 5.0        |
| MAX_SPEED            | 20.0       |
| MAX_YAW_RATE         | 3.14       |
| NB_DRONES            | 25         |
| NEIGHBORS            | 3          |
| POP_SIZE_CPU         | 150        |
| POP_SIZE_GPU         | 5000       |
| SCENARIO             | exploration |
| SIM_STEPS            | 500        |
| SPOIL_ADD            | 0.05       |
| SPOIL_MULT           | 1.01       |
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
| 00   | -834.5906    | 3.24       | y_att=4.62, y_ali=3.91, y_f=0.80, d0_att=3.38, l_att=3.96, l_ali=3.15, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.69, y_acc=1.78, l_acc=3.18, d0_v=0.79 |
| 01   | -950.4534    | 3.17       | y_att=4.74, y_ali=3.49, y_f=1.33, d0_att=1.33, l_att=3.09, l_ali=2.05, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.53, y_acc=1.38, l_acc=4.91, d0_v=0.59 |
| 02   | -873.6002    | 4.15       | y_att=4.74, y_ali=3.49, y_f=1.33, d0_att=1.33, l_att=3.09, l_ali=2.05, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.53, y_acc=1.38, l_acc=4.91, d0_v=0.59 |
| 03   | -925.1555    | 3.17       | y_att=3.87, y_ali=3.65, y_f=1.71, d0_att=1.51, l_att=3.71, l_ali=4.00, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.15, y_acc=2.87, l_acc=3.55, d0_v=0.76 |
| 04   | -963.1527    | 3.25       | y_att=3.87, y_ali=2.23, y_f=1.88, d0_att=1.67, l_att=4.52, l_ali=2.52, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=2.87, l_acc=4.06, d0_v=0.76 |
| 05   | -995.1873    | 3.25       | y_att=3.87, y_ali=2.38, y_f=1.88, d0_att=1.67, l_att=4.52, l_ali=2.52, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=2.87, l_acc=4.06, d0_v=0.76 |
| 06   | -1016.8889   | 4.04       | y_att=5.10, y_ali=0.19, y_f=1.69, d0_att=1.07, l_att=2.97, l_ali=1.83, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.65, y_acc=1.74, l_acc=5.47, d0_v=0.67 |
| 07   | -1012.5065   | 3.10       | y_att=4.62, y_ali=1.92, y_f=1.94, d0_att=1.57, l_att=3.83, l_ali=2.42, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.96, y_acc=1.97, l_acc=4.03, d0_v=0.51 |
| 08   | -1008.0173   | 3.38       | y_att=4.04, y_ali=3.65, y_f=1.71, d0_att=1.51, l_att=4.02, l_ali=3.30, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.15, y_acc=2.87, l_acc=3.55, d0_v=0.72 |
| 09   | -1002.6608   | 3.81       | y_att=3.93, y_ali=3.87, y_f=1.60, d0_att=1.15, l_att=3.42, l_ali=0.99, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.29, y_acc=1.97, l_acc=3.42, d0_v=0.51 |
| 10   | -1014.9196   | 4.22       | y_att=4.04, y_ali=3.51, y_f=1.71, d0_att=1.51, l_att=4.02, l_ali=4.21, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.18, y_acc=2.84, l_acc=3.55, d0_v=0.72 |
| 11   | -1022.8510   | 2.99       | y_att=5.09, y_ali=6.68, y_f=2.29, d0_att=1.47, l_att=3.83, l_ali=1.76, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.29, y_acc=2.45, l_acc=4.29, d0_v=0.58 |
| 12   | -1014.6608   | 3.23       | y_att=4.85, y_ali=2.96, y_f=2.47, d0_att=1.26, l_att=3.70, l_ali=1.19, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.77, y_acc=1.87, l_acc=4.08, d0_v=0.39 |
| 13   | -1033.6887   | 3.16       | y_att=6.69, y_ali=2.35, y_f=1.88, d0_att=0.96, l_att=2.36, l_ali=9.61, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.74, y_acc=2.80, l_acc=3.46, d0_v=0.70 |
| 14   | -1030.7511   | 4.25       | y_att=5.09, y_ali=5.61, y_f=2.29, d0_att=1.47, l_att=3.83, l_ali=1.74, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.57, y_acc=2.45, l_acc=4.29, d0_v=0.58 |
| 15   | -1031.3395   | 3.25       | y_att=5.09, y_ali=5.53, y_f=2.29, d0_att=1.47, l_att=3.83, l_ali=1.76, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.29, y_acc=2.45, l_acc=4.29, d0_v=0.58 |
| 16   | -1061.1240   | 3.41       | y_att=6.69, y_ali=2.35, y_f=1.88, d0_att=0.96, l_att=2.36, l_ali=9.61, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.64, y_acc=2.82, l_acc=3.47, d0_v=0.70 |
| 17   | -1059.2559   | 3.22       | y_att=6.25, y_ali=1.99, y_f=1.88, d0_att=0.77, l_att=2.24, l_ali=8.18, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.51, y_acc=2.80, l_acc=4.43, d0_v=0.82 |
| 18   | -1051.3839   | 3.90       | y_att=6.25, y_ali=1.99, y_f=1.88, d0_att=0.77, l_att=2.24, l_ali=8.18, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.51, y_acc=2.80, l_acc=4.43, d0_v=0.82 |
| 19   | -1051.3839   | 3.29       | y_att=6.25, y_ali=1.99, y_f=1.88, d0_att=0.77, l_att=2.24, l_ali=8.18, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.51, y_acc=2.80, l_acc=4.43, d0_v=0.82 |

**End of experiment.**
