# Experiment Report - PyTorch_CUDA (2D)
**Date:** 2026-04-22_17-03-28

## 1. Initial Configuration
| Parameter | Value |
| :--- | :--- |
| ALPHA_LPF            | 0.2        |
| ARENA_RADIUS         | 100.0      |
| COLLISION_DIST       | 0.4        |
| DT                   | 0.1        |
| ENABLE_3D            | False      |
| FULL_MILLING_MODE    | True       |
| GEN_CPU              | 20         |
| GEN_GPU              | 20         |
| GRID_RES             | 5.0        |
| MAX_SPEED            | 20.0       |
| MAX_YAW_RATE         | 3.14       |
| NB_DRONES            | 30         |
| NEIGHBORS            | 4          |
| POP_SIZE_CPU         | 150        |
| POP_SIZE_GPU         | 5000       |
| SCENARIO             | default    |
| SIM_STEPS            | 500        |
| SPOIL_ADD            | 0.05       |
| SPOIL_MULT           | 1.01       |
| VISU_STEPS           | 1000       |
| W_COLL               | 0          |
| W_DISP               | 0.0        |
| W_EFFORT             | 1.0        |
| W_EXPLO              | 0.0        |
| W_MILL               | -100.0     |
| W_POL                | 0.0        |
| Z_MAX                | 10.0       |
| Z_MIN                | 1.0        |

## 2. Optimization Evolution
| Gen  |  Best Cost   |  Time (s)  |                                                                All Parameters                                                                |
| :--: | :----------: | :--------: | :------------------------------------------------------------------------------------------------------------------------------------------ |
| 00   | -2838.0686   | 2.50       | y_att=4.51, y_ali=2.82, y_f=1.68, d0_att=1.57, l_att=4.14, l_ali=4.81, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.06, y_acc=1.78, l_acc=3.49, d0_v=0.60 |
| 01   | -5038.5742   | 2.28       | y_att=4.03, y_ali=0.15, y_f=1.58, d0_att=1.45, l_att=4.77, l_ali=1.22, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.70, y_acc=1.99, l_acc=3.49, d0_v=0.49 |
| 02   | -4603.9902   | 2.24       | y_att=4.03, y_ali=0.15, y_f=1.58, d0_att=1.45, l_att=4.77, l_ali=1.35, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.70, y_acc=2.01, l_acc=3.49, d0_v=0.49 |
| 03   | -4937.9248   | 2.24       | y_att=5.53, y_ali=2.82, y_f=1.84, d0_att=1.91, l_att=4.14, l_ali=4.79, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.93, y_acc=1.61, l_acc=3.92, d0_v=0.60 |
| 04   | -4044.8071   | 2.24       | y_att=4.00, y_ali=0.15, y_f=1.78, d0_att=1.38, l_att=4.77, l_ali=1.70, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.70, y_acc=2.88, l_acc=2.12, d0_v=0.53 |
| 05   | -3747.5142   | 2.24       | y_att=0.72, y_ali=3.24, y_f=0.56, d0_att=3.92, l_att=1.49, l_ali=2.90, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.63, y_acc=0.20, l_acc=0.48, d0_v=1.25 |
| 06   | -4057.6179   | 2.24       | y_att=2.26, y_ali=0.52, y_f=2.07, d0_att=4.10, l_att=0.67, l_ali=1.75, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.71, y_acc=0.12, l_acc=1.30, d0_v=2.38 |
| 07   | -3976.7253   | 2.24       | y_att=1.17, y_ali=1.45, y_f=2.86, d0_att=3.25, l_att=1.04, l_ali=4.65, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.37, y_acc=0.83, l_acc=0.33, d0_v=1.80 |
| 08   | -3805.9338   | 2.23       | y_att=0.72, y_ali=2.48, y_f=1.65, d0_att=3.57, l_att=0.62, l_ali=3.73, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.38, y_acc=0.26, l_acc=2.54, d0_v=5.34 |
| 09   | -3970.8159   | 2.24       | y_att=0.41, y_ali=4.12, y_f=1.08, d0_att=4.32, l_att=1.60, l_ali=3.86, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.63, y_acc=0.11, l_acc=0.76, d0_v=1.34 |
| 10   | -4160.1040   | 2.24       | y_att=0.12, y_ali=1.85, y_f=0.81, d0_att=1.24, l_att=0.69, l_ali=1.25, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.87, y_acc=0.14, l_acc=0.21, d0_v=2.77 |
| 11   | -4076.9209   | 2.24       | y_att=1.05, y_ali=2.74, y_f=1.47, d0_att=6.41, l_att=1.16, l_ali=2.98, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.59, y_acc=0.11, l_acc=0.95, d0_v=2.57 |
| 12   | -4038.6421   | 2.23       | y_att=0.76, y_ali=1.06, y_f=1.41, d0_att=3.42, l_att=0.44, l_ali=1.29, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.31, y_acc=0.14, l_acc=1.47, d0_v=3.85 |
| 13   | -4151.3999   | 2.24       | y_att=0.25, y_ali=2.30, y_f=1.14, d0_att=6.03, l_att=0.57, l_ali=0.83, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.91, y_acc=0.26, l_acc=0.18, d0_v=3.25 |
| 14   | -4187.9355   | 2.24       | y_att=0.53, y_ali=2.03, y_f=1.10, d0_att=3.22, l_att=0.39, l_ali=1.31, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.53, y_acc=0.15, l_acc=0.11, d0_v=3.60 |
| 15   | -4027.2729   | 2.24       | y_att=0.51, y_ali=1.33, y_f=1.86, d0_att=5.13, l_att=0.79, l_ali=1.65, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.57, y_acc=0.12, l_acc=0.26, d0_v=0.43 |
| 16   | -4112.6221   | 2.23       | y_att=1.76, y_ali=4.55, y_f=1.80, d0_att=3.61, l_att=0.52, l_ali=3.17, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.25, y_acc=0.07, l_acc=1.44, d0_v=2.90 |
| 17   | -4157.0293   | 2.24       | y_att=1.19, y_ali=0.75, y_f=1.08, d0_att=5.61, l_att=0.33, l_ali=0.48, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.74, y_acc=0.04, l_acc=0.78, d0_v=2.37 |
| 18   | -4178.7031   | 2.24       | y_att=0.24, y_ali=1.44, y_f=1.50, d0_att=6.67, l_att=1.29, l_ali=2.46, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.08, y_acc=0.03, l_acc=0.76, d0_v=3.21 |
| 19   | -4082.3091   | 2.25       | y_att=1.14, y_ali=0.25, y_f=3.15, d0_att=7.37, l_att=0.23, l_ali=1.66, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.57, y_acc=0.05, l_acc=0.73, d0_v=3.07 |

**End of experiment.**
