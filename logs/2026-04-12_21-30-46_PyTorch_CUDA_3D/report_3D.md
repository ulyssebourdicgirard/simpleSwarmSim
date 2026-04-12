# Experiment Report - PyTorch_CUDA (3D)
**Date:** 2026-04-12_21-30-46

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
| NB_DRONES            | 15         |
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
| 00   | -298.8158    | 4.57       | y_att=4.06, y_ali=2.28, y_f=1.23, d0_att=1.64, l_att=4.17, l_ali=3.11, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.54, y_acc=1.97, l_acc=3.78, d0_v=0.89 |
| 01   | -375.2332    | 3.32       | y_att=4.05, y_ali=0.30, y_f=1.08, d0_att=1.36, l_att=3.87, l_ali=4.92, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.27, y_acc=1.79, l_acc=3.11, d0_v=0.69 |
| 02   | -407.1418    | 3.19       | y_att=3.95, y_ali=2.30, y_f=0.80, d0_att=2.35, l_att=4.66, l_ali=3.03, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.06, y_acc=1.15, l_acc=3.32, d0_v=0.57 |
| 03   | -444.5003    | 3.36       | y_att=3.95, y_ali=2.30, y_f=0.80, d0_att=2.35, l_att=4.66, l_ali=3.03, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.06, y_acc=1.15, l_acc=3.32, d0_v=0.57 |
| 04   | -444.5003    | 4.11       | y_att=3.95, y_ali=2.30, y_f=0.80, d0_att=2.35, l_att=4.66, l_ali=3.03, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.06, y_acc=1.15, l_acc=3.32, d0_v=0.57 |
| 05   | -460.3533    | 3.13       | y_att=5.66, y_ali=1.67, y_f=1.57, d0_att=1.64, l_att=4.17, l_ali=2.11, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.52, y_acc=2.22, l_acc=3.64, d0_v=0.69 |
| 06   | -477.9745    | 3.27       | y_att=5.66, y_ali=1.46, y_f=1.30, d0_att=2.38, l_att=4.73, l_ali=3.49, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.45, y_acc=1.47, l_acc=4.34, d0_v=0.64 |
| 07   | -480.3853    | 4.10       | y_att=1.68, y_ali=3.26, y_f=1.24, d0_att=1.17, l_att=5.93, l_ali=3.46, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.43, y_acc=1.37, l_acc=5.38, d0_v=0.77 |
| 08   | -501.3823    | 3.44       | y_att=4.47, y_ali=0.64, y_f=1.19, d0_att=1.23, l_att=3.63, l_ali=2.67, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.23, y_acc=2.77, l_acc=3.61, d0_v=1.09 |
| 09   | -488.0379    | 3.13       | y_att=5.45, y_ali=0.27, y_f=1.52, d0_att=1.40, l_att=3.87, l_ali=4.32, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.13, y_acc=1.61, l_acc=4.48, d0_v=0.66 |
| 10   | -516.5742    | 3.32       | y_att=3.91, y_ali=0.57, y_f=1.52, d0_att=1.38, l_att=4.54, l_ali=4.02, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.81, y_acc=1.61, l_acc=4.55, d0_v=0.66 |
| 11   | -527.1320    | 4.28       | y_att=5.66, y_ali=1.67, y_f=1.57, d0_att=1.64, l_att=4.17, l_ali=2.17, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.04, y_acc=2.22, l_acc=3.64, d0_v=0.69 |
| 12   | -512.7603    | 3.21       | y_att=4.13, y_ali=1.92, y_f=1.34, d0_att=1.13, l_att=3.82, l_ali=0.51, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.71, y_acc=1.93, l_acc=4.35, d0_v=0.81 |
| 13   | -491.6068    | 3.13       | y_att=4.13, y_ali=1.92, y_f=1.34, d0_att=1.13, l_att=3.82, l_ali=0.51, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.71, y_acc=1.93, l_acc=4.35, d0_v=0.81 |
| 14   | -491.6068    | 3.20       | y_att=4.13, y_ali=1.92, y_f=1.34, d0_att=1.13, l_att=3.82, l_ali=0.51, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.71, y_acc=1.93, l_acc=4.35, d0_v=0.81 |
| 15   | -509.0972    | 4.36       | y_att=6.47, y_ali=3.19, y_f=1.93, d0_att=1.56, l_att=4.17, l_ali=2.16, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.53, y_acc=2.48, l_acc=5.04, d0_v=0.87 |
| 16   | -505.4851    | 3.26       | y_att=2.15, y_ali=1.54, y_f=1.70, d0_att=0.50, l_att=3.83, l_ali=2.70, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.53, y_acc=1.97, l_acc=4.50, d0_v=0.71 |
| 17   | -515.3525    | 3.27       | y_att=6.61, y_ali=1.83, y_f=1.91, d0_att=2.15, l_att=4.85, l_ali=2.57, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.42, y_acc=2.12, l_acc=4.68, d0_v=0.71 |
| 18   | -506.7485    | 3.52       | y_att=4.48, y_ali=1.09, y_f=1.38, d0_att=1.85, l_att=4.73, l_ali=5.19, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.51, y_acc=1.57, l_acc=3.44, d0_v=0.53 |
| 19   | -526.6595    | 3.81       | y_att=3.85, y_ali=6.06, y_f=1.51, d0_att=1.23, l_att=4.31, l_ali=0.54, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.32, y_acc=2.54, l_acc=5.04, d0_v=1.12 |

**End of experiment.**
