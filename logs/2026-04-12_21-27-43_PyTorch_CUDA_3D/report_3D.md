# Experiment Report - PyTorch_CUDA (3D)
**Date:** 2026-04-12_21-27-43

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
| 00   | -438.1315    | 3.35       | y_att=4.49, y_ali=2.08, y_f=1.23, d0_att=1.86, l_att=4.99, l_ali=3.42, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.34, y_acc=1.95, l_acc=3.15, d0_v=0.74 |
| 01   | -447.2105    | 3.21       | y_att=4.49, y_ali=2.08, y_f=1.23, d0_att=1.86, l_att=4.99, l_ali=3.42, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.34, y_acc=1.95, l_acc=3.15, d0_v=0.74 |
| 02   | -447.2105    | 3.66       | y_att=4.49, y_ali=2.08, y_f=1.23, d0_att=1.86, l_att=4.99, l_ali=3.42, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.34, y_acc=1.95, l_acc=3.15, d0_v=0.74 |
| 03   | -447.2105    | 4.12       | y_att=4.49, y_ali=2.08, y_f=1.23, d0_att=1.86, l_att=4.99, l_ali=3.42, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.34, y_acc=1.95, l_acc=3.15, d0_v=0.74 |
| 04   | -447.2105    | 3.23       | y_att=4.49, y_ali=2.08, y_f=1.23, d0_att=1.86, l_att=4.99, l_ali=3.42, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.34, y_acc=1.95, l_acc=3.15, d0_v=0.74 |
| 05   | -452.3356    | 3.32       | y_att=5.22, y_ali=2.08, y_f=1.87, d0_att=1.75, l_att=4.99, l_ali=3.19, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.64, y_acc=2.50, l_acc=3.36, d0_v=0.74 |
| 06   | -467.8674    | 2.95       | y_att=3.19, y_ali=0.58, y_f=1.72, d0_att=0.97, l_att=4.64, l_ali=3.55, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.34, y_acc=3.55, l_acc=2.11, d0_v=0.68 |
| 07   | -465.4612    | 3.98       | y_att=3.04, y_ali=1.05, y_f=1.72, d0_att=1.11, l_att=5.14, l_ali=2.76, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=3.40, l_acc=3.61, d0_v=1.10 |
| 08   | -472.6146    | 2.99       | y_att=3.19, y_ali=2.20, y_f=1.72, d0_att=0.97, l_att=4.64, l_ali=3.55, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.00, y_acc=2.95, l_acc=3.61, d0_v=0.96 |
| 09   | -474.7390    | 3.09       | y_att=3.32, y_ali=1.56, y_f=2.04, d0_att=1.11, l_att=5.14, l_ali=2.76, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=4.40, l_acc=3.23, d0_v=1.10 |
| 10   | -481.6386    | 3.14       | y_att=3.27, y_ali=2.72, y_f=2.26, d0_att=3.34, l_att=9.35, l_ali=3.58, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.67, y_acc=3.89, l_acc=2.71, d0_v=0.77 |
| 11   | -480.7007    | 3.97       | y_att=3.27, y_ali=2.72, y_f=2.26, d0_att=3.34, l_att=9.35, l_ali=3.58, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.67, y_acc=3.89, l_acc=2.71, d0_v=0.77 |
| 12   | -480.7007    | 3.23       | y_att=3.27, y_ali=2.72, y_f=2.26, d0_att=3.34, l_att=9.35, l_ali=3.58, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.67, y_acc=3.89, l_acc=2.71, d0_v=0.77 |
| 13   | -480.7007    | 3.19       | y_att=3.27, y_ali=2.72, y_f=2.26, d0_att=3.34, l_att=9.35, l_ali=3.58, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.67, y_acc=3.89, l_acc=2.71, d0_v=0.77 |
| 14   | -480.7007    | 3.16       | y_att=3.27, y_ali=2.72, y_f=2.26, d0_att=3.34, l_att=9.35, l_ali=3.58, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.67, y_acc=3.89, l_acc=2.71, d0_v=0.77 |
| 15   | -480.7007    | 4.29       | y_att=3.27, y_ali=2.72, y_f=2.26, d0_att=3.34, l_att=9.35, l_ali=3.58, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.67, y_acc=3.89, l_acc=2.71, d0_v=0.77 |
| 16   | -480.7007    | 3.21       | y_att=3.27, y_ali=2.72, y_f=2.26, d0_att=3.34, l_att=9.35, l_ali=3.58, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.67, y_acc=3.89, l_acc=2.71, d0_v=0.77 |
| 17   | -480.7007    | 3.32       | y_att=3.27, y_ali=2.72, y_f=2.26, d0_att=3.34, l_att=9.35, l_ali=3.58, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.67, y_acc=3.89, l_acc=2.71, d0_v=0.77 |
| 18   | -480.9476    | 4.22       | y_att=3.27, y_ali=2.72, y_f=2.26, d0_att=3.34, l_att=9.35, l_ali=3.60, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.30, y_acc=3.89, l_acc=2.71, d0_v=0.77 |
| 19   | -480.7455    | 3.15       | y_att=3.27, y_ali=2.72, y_f=2.26, d0_att=3.34, l_att=9.35, l_ali=3.60, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.30, y_acc=3.89, l_acc=2.71, d0_v=0.77 |

**End of experiment.**
