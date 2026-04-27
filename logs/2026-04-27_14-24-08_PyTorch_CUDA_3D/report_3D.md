# Experiment Report - PyTorch_CUDA (3D)
**Date:** 2026-04-27_14-24-08

## 1. Initial Configuration
| Parameter | Value |
| :--- | :--- |
| ALPHA_LPF            | 0.2        |
| ARENA_RADIUS         | 100.0      |
| COLLISION_DIST       | 0.4        |
| DT                   | 0.1        |
| ENABLE_3D            | True       |
| EXPLO_STRATEGY       | local_gradient |
| FOV_FACTOR           | 1.0        |
| FULL_MILLING_MODE    | False      |
| GEN_CPU              | 20         |
| GEN_GPU              | 20         |
| GRID_RES             | 5.0        |
| MAP_STRATEGY         | local_shared |
| MAX_SPEED            | 20.0       |
| MAX_YAW_RATE         | 3.14       |
| MIN_SPAWN_DIST       | 2.0        |
| NB_DRONES            | 30         |
| NEIGHBORS            | 2          |
| N_INIT_CONDITIONS    | 4          |
| POP_SIZE_CPU         | 150        |
| POP_SIZE_GPU         | 5000       |
| REFRESH_MAP_TICKS    | 50         |
| SCENARIO             | exploration |
| SIM_STEPS            | 500        |
| SPOIL_ADD            | 0.05       |
| SPOIL_MULT           | 1.01       |
| VISU_STEPS           | 1000       |
| W_COLL               | 500.0      |
| W_DISP               | 0.0        |
| W_EFFORT             | 1.0        |
| W_EXPLO              | -50.0      |
| W_MILL               | 0          |
| W_POL                | -0.0       |
| Z_MAX                | 10.0       |
| Z_MIN                | 1.0        |

## 2. Optimization Evolution
| Gen  |  Best Cost   |  Time (s)  |                                                                All Parameters                                                                |
| :--: | :----------: | :--------: | :------------------------------------------------------------------------------------------------------------------------------------------ |
| 00   | -8139.8501   | 112.79     | y_att=2.22, y_ali=0.68, y_f=0.97, d0_att=1.89, l_att=1.54, l_ali=1.98, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.13, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.94, y_acc=0.20, l_acc=0.71, d0_v=2.29, y_explo=0.55 |
| 01   | -8506.9365   | 113.26     | y_att=3.11, y_ali=0.92, y_f=1.57, d0_att=1.61, l_att=3.49, l_ali=1.13, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.65, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.27, y_acc=0.48, l_acc=1.08, d0_v=2.51, y_explo=0.42 |
| 02   | -8648.2012   | 114.97     | y_att=3.20, y_ali=1.75, y_f=1.32, d0_att=1.30, l_att=1.36, l_ali=2.14, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.47, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.29, y_acc=0.01, l_acc=2.48, d0_v=1.37, y_explo=0.10 |
| 03   | -8770.7461   | 114.71     | y_att=2.58, y_ali=1.38, y_f=0.82, d0_att=1.10, l_att=1.46, l_ali=1.43, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.76, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.20, l_acc=1.09, d0_v=1.43, y_explo=0.65 |
| 04   | -8770.7461   | 111.95     | y_att=2.58, y_ali=1.38, y_f=0.82, d0_att=1.10, l_att=1.46, l_ali=1.43, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.76, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.20, l_acc=1.09, d0_v=1.43, y_explo=0.65 |
| 05   | -8888.8438   | 113.66     | y_att=1.05, y_ali=0.16, y_f=0.54, d0_att=1.93, l_att=3.77, l_ali=2.96, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.55, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.44, y_acc=0.05, l_acc=1.41, d0_v=2.53, y_explo=0.27 |
| 06   | -9012.5723   | 116.98     | y_att=0.21, y_ali=2.11, y_f=1.61, d0_att=0.50, l_att=4.99, l_ali=4.99, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.23, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.91, y_acc=0.43, l_acc=0.66, d0_v=0.88, y_explo=0.25 |
| 07   | -9232.9268   | 116.81     | y_att=4.39, y_ali=0.50, y_f=0.95, d0_att=0.57, l_att=0.89, l_ali=3.74, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.39, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.02, l_acc=4.29, d0_v=0.95, y_explo=0.12 |
| 08   | -9232.9268   | 116.91     | y_att=4.39, y_ali=0.50, y_f=0.95, d0_att=0.57, l_att=0.89, l_ali=3.74, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.39, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.02, l_acc=4.29, d0_v=0.95, y_explo=0.12 |
| 09   | -9232.9268   | 116.74     | y_att=4.39, y_ali=0.50, y_f=0.95, d0_att=0.57, l_att=0.89, l_ali=3.74, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.39, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.02, l_acc=4.29, d0_v=0.95, y_explo=0.12 |
| 10   | -9283.4307   | 115.53     | y_att=0.97, y_ali=1.23, y_f=1.75, d0_att=1.53, l_att=2.52, l_ali=3.87, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.63, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.13, l_acc=0.29, d0_v=1.38, y_explo=0.37 |
| 11   | -9283.4307   | 115.50     | y_att=0.97, y_ali=1.23, y_f=1.75, d0_att=1.53, l_att=2.52, l_ali=3.87, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.63, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.13, l_acc=0.29, d0_v=1.38, y_explo=0.37 |
| 12   | -9296.1943   | 116.62     | y_att=0.37, y_ali=0.80, y_f=1.84, d0_att=0.51, l_att=2.64, l_ali=3.91, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.63, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.01, l_acc=0.32, d0_v=0.53, y_explo=0.37 |
| 13   | -9296.1943   | 115.70     | y_att=0.37, y_ali=0.80, y_f=1.84, d0_att=0.51, l_att=2.64, l_ali=3.91, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.63, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.01, l_acc=0.32, d0_v=0.53, y_explo=0.37 |
| 14   | -9463.5107   | 117.76     | y_att=0.36, y_ali=0.56, y_f=0.56, d0_att=0.85, l_att=2.38, l_ali=2.58, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.63, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.07, l_acc=1.72, d0_v=2.54, y_explo=0.30 |
| 15   | -9463.5107   | 115.48     | y_att=0.36, y_ali=0.56, y_f=0.56, d0_att=0.85, l_att=2.38, l_ali=2.58, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.63, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.07, l_acc=1.72, d0_v=2.54, y_explo=0.30 |
| 16   | -9477.5967   | 115.47     | y_att=0.57, y_ali=1.71, y_f=1.73, d0_att=0.50, l_att=1.61, l_ali=2.23, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.17, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.21, l_acc=0.95, d0_v=2.11, y_explo=0.10 |
| 17   | -9531.7568   | 116.02     | y_att=2.30, y_ali=0.89, y_f=1.72, d0_att=1.02, l_att=1.66, l_ali=1.50, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.63, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.59, y_acc=0.20, l_acc=0.93, d0_v=0.93, y_explo=0.13 |
| 18   | -9531.7568   | 115.31     | y_att=2.30, y_ali=0.89, y_f=1.72, d0_att=1.02, l_att=1.66, l_ali=1.50, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.63, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.59, y_acc=0.20, l_acc=0.93, d0_v=0.93, y_explo=0.13 |
| 19   | -9601.8779   | 115.39     | y_att=0.69, y_ali=0.11, y_f=2.04, d0_att=0.89, l_att=2.11, l_ali=1.62, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.83, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.02, l_acc=1.64, d0_v=0.35, y_explo=0.10 |

**End of experiment.**
