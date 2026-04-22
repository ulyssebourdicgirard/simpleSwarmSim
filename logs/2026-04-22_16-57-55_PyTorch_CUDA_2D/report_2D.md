# Experiment Report - PyTorch_CUDA (2D)
**Date:** 2026-04-22_16-57-55

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
| NB_DRONES            | 15         |
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
| 00   | -14638.6709  | 2.05       | y_att=3.83, y_ali=1.79, y_f=1.69, d0_att=3.18, l_att=4.31, l_ali=3.42, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.80, y_acc=1.57, l_acc=1.04, d0_v=1.13 |
| 01   | -32716.2129  | 1.88       | y_att=1.75, y_ali=3.75, y_f=1.63, d0_att=4.99, l_att=3.86, l_ali=1.57, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.66, y_acc=0.38, l_acc=0.46, d0_v=0.58 |
| 02   | -29688.5547  | 1.74       | y_att=1.75, y_ali=3.75, y_f=1.63, d0_att=4.99, l_att=3.86, l_ali=1.57, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.66, y_acc=0.38, l_acc=0.46, d0_v=0.58 |
| 03   | -37048.4336  | 1.72       | y_att=1.75, y_ali=3.78, y_f=1.63, d0_att=4.99, l_att=3.86, l_ali=1.57, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.91, y_acc=0.38, l_acc=0.46, d0_v=0.58 |
| 04   | -39672.1055  | 1.71       | y_att=1.30, y_ali=0.85, y_f=2.62, d0_att=2.08, l_att=3.89, l_ali=1.49, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.86, y_acc=0.75, l_acc=0.41, d0_v=0.39 |
| 05   | -39886.4570  | 1.71       | y_att=1.64, y_ali=0.88, y_f=3.38, d0_att=2.08, l_att=3.37, l_ali=1.07, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.17, y_acc=0.75, l_acc=0.45, d0_v=0.55 |
| 06   | -39871.5039  | 1.72       | y_att=1.64, y_ali=0.88, y_f=3.38, d0_att=2.08, l_att=3.37, l_ali=1.07, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.17, y_acc=0.75, l_acc=0.45, d0_v=0.55 |
| 07   | -39843.0820  | 1.71       | y_att=1.64, y_ali=0.88, y_f=3.38, d0_att=2.08, l_att=3.37, l_ali=1.07, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.17, y_acc=0.75, l_acc=0.45, d0_v=0.55 |
| 08   | -39917.9766  | 1.71       | y_att=2.04, y_ali=0.08, y_f=3.64, d0_att=2.93, l_att=4.43, l_ali=7.73, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=1.61, l_acc=0.40, d0_v=0.57 |
| 09   | -39996.7656  | 1.71       | y_att=0.96, y_ali=1.10, y_f=4.54, d0_att=2.54, l_att=5.35, l_ali=1.49, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.43, y_acc=0.75, l_acc=0.41, d0_v=0.45 |
| 10   | -40017.5117  | 1.71       | y_att=4.13, y_ali=3.39, y_f=4.31, d0_att=3.25, l_att=3.80, l_ali=2.36, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.83, y_acc=2.91, l_acc=0.26, d0_v=0.39 |
| 11   | -40011.0664  | 1.72       | y_att=4.13, y_ali=3.39, y_f=4.31, d0_att=3.25, l_att=3.80, l_ali=2.36, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.83, y_acc=2.91, l_acc=0.26, d0_v=0.39 |
| 12   | -40017.5977  | 1.72       | y_att=2.45, y_ali=0.12, y_f=4.75, d0_att=3.33, l_att=5.84, l_ali=5.35, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.02, y_acc=1.39, l_acc=0.39, d0_v=0.15 |
| 13   | -40057.1602  | 1.73       | y_att=4.10, y_ali=7.60, y_f=7.41, d0_att=2.70, l_att=3.82, l_ali=5.85, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.14, y_acc=1.79, l_acc=0.29, d0_v=0.31 |
| 14   | -40095.3789  | 1.71       | y_att=1.30, y_ali=0.65, y_f=7.27, d0_att=2.06, l_att=4.36, l_ali=0.99, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.26, y_acc=1.10, l_acc=0.25, d0_v=0.39 |
| 15   | -40083.4258  | 1.71       | y_att=2.45, y_ali=0.10, y_f=5.23, d0_att=3.58, l_att=6.20, l_ali=6.26, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.52, y_acc=2.02, l_acc=0.39, d0_v=0.24 |
| 16   | -40130.6367  | 1.72       | y_att=2.20, y_ali=0.30, y_f=6.64, d0_att=3.02, l_att=5.95, l_ali=2.16, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.09, y_acc=0.99, l_acc=0.45, d0_v=0.18 |
| 17   | -40146.3320  | 1.75       | y_att=1.86, y_ali=0.10, y_f=5.77, d0_att=2.56, l_att=5.42, l_ali=6.05, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.80, y_acc=2.04, l_acc=0.41, d0_v=0.43 |
| 18   | -40171.2461  | 1.79       | y_att=4.25, y_ali=7.60, y_f=8.07, d0_att=2.61, l_att=3.82, l_ali=4.42, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.81, y_acc=1.69, l_acc=0.36, d0_v=0.31 |
| 19   | -40184.3242  | 1.79       | y_att=4.25, y_ali=7.60, y_f=8.07, d0_att=2.61, l_att=3.82, l_ali=2.28, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.81, y_acc=1.69, l_acc=0.36, d0_v=0.31 |

**End of experiment.**
