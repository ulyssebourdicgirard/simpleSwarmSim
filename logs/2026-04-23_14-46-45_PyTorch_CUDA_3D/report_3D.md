# Experiment Report - PyTorch_CUDA (3D)
**Date:** 2026-04-23_14-46-45

## 1. Initial Configuration
| Parameter | Value |
| :--- | :--- |
| ALPHA_LPF            | 0.2        |
| ARENA_RADIUS         | 100.0      |
| COLLISION_DIST       | 0.4        |
| DT                   | 0.1        |
| ENABLE_3D            | True       |
| FULL_MILLING_MODE    | False      |
| GEN_CPU              | 20         |
| GEN_GPU              | 20         |
| GRID_RES             | 5.0        |
| MAX_SPEED            | 20.0       |
| MAX_YAW_RATE         | 3.14       |
| NB_DRONES            | 15         |
| NEIGHBORS            | 4          |
| POP_SIZE_CPU         | 150        |
| POP_SIZE_GPU         | 5000       |
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
| 00   | -639.5192    | 3.86       | y_att=1.55, y_ali=3.88, y_f=1.58, d0_att=3.41, l_att=2.17, l_ali=3.68, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.07, y_acc=0.18, l_acc=2.65, d0_v=1.56 |
| 01   | -639.5192    | 3.07       | y_att=1.55, y_ali=3.88, y_f=1.58, d0_att=3.41, l_att=2.17, l_ali=3.68, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.07, y_acc=0.18, l_acc=2.65, d0_v=1.56 |
| 02   | -675.2536    | 3.66       | y_att=2.48, y_ali=0.57, y_f=0.44, d0_att=3.11, l_att=1.10, l_ali=1.62, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.34, y_acc=0.24, l_acc=0.84, d0_v=2.28 |
| 03   | -741.1205    | 3.81       | y_att=2.06, y_ali=4.76, y_f=0.30, d0_att=3.83, l_att=2.22, l_ali=0.59, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.52, y_acc=0.10, l_acc=0.16, d0_v=1.81 |
| 04   | -743.2307    | 2.99       | y_att=0.96, y_ali=0.38, y_f=0.71, d0_att=3.09, l_att=1.32, l_ali=0.87, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.44, y_acc=0.00, l_acc=0.35, d0_v=2.87 |
| 05   | -745.2991    | 3.12       | y_att=2.06, y_ali=3.32, y_f=0.29, d0_att=1.74, l_att=2.22, l_ali=2.64, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.45, y_acc=0.10, l_acc=0.16, d0_v=1.81 |
| 06   | -745.2991    | 4.00       | y_att=2.06, y_ali=3.32, y_f=0.29, d0_att=1.74, l_att=2.22, l_ali=2.64, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.45, y_acc=0.10, l_acc=0.16, d0_v=1.81 |
| 07   | -748.6351    | 2.97       | y_att=1.38, y_ali=0.62, y_f=0.10, d0_att=2.94, l_att=1.35, l_ali=0.94, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.10, y_acc=0.16, l_acc=0.38, d0_v=0.95 |
| 08   | -767.8753    | 3.00       | y_att=0.72, y_ali=1.99, y_f=0.10, d0_att=3.94, l_att=0.10, l_ali=3.35, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.22, y_acc=0.11, l_acc=0.79, d0_v=1.63 |
| 09   | -770.2071    | 2.97       | y_att=1.96, y_ali=2.44, y_f=0.42, d0_att=1.53, l_att=0.56, l_ali=3.01, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.82, y_acc=0.01, l_acc=0.74, d0_v=6.06 |
| 10   | -770.2071    | 4.03       | y_att=1.96, y_ali=2.44, y_f=0.42, d0_att=1.53, l_att=0.56, l_ali=3.01, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.82, y_acc=0.01, l_acc=0.74, d0_v=6.06 |
| 11   | -770.9797    | 2.96       | y_att=0.63, y_ali=0.39, y_f=0.10, d0_att=3.59, l_att=0.13, l_ali=3.33, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.37, y_acc=0.16, l_acc=0.78, d0_v=2.11 |
| 12   | -812.8140    | 2.96       | y_att=1.22, y_ali=3.79, y_f=0.10, d0_att=4.71, l_att=0.89, l_ali=1.42, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.33, y_acc=0.11, l_acc=1.08, d0_v=1.85 |
| 13   | -812.8140    | 2.97       | y_att=1.22, y_ali=3.79, y_f=0.10, d0_att=4.71, l_att=0.89, l_ali=1.42, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.33, y_acc=0.11, l_acc=1.08, d0_v=1.85 |
| 14   | -812.8140    | 4.10       | y_att=1.22, y_ali=3.79, y_f=0.10, d0_att=4.71, l_att=0.89, l_ali=1.42, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.33, y_acc=0.11, l_acc=1.08, d0_v=1.85 |
| 15   | -812.8140    | 3.14       | y_att=1.22, y_ali=3.79, y_f=0.10, d0_att=4.71, l_att=0.89, l_ali=1.42, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.33, y_acc=0.11, l_acc=1.08, d0_v=1.85 |
| 16   | -812.8140    | 3.09       | y_att=1.22, y_ali=3.79, y_f=0.10, d0_att=4.71, l_att=0.89, l_ali=1.42, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.33, y_acc=0.11, l_acc=1.08, d0_v=1.85 |
| 17   | -812.8140    | 2.88       | y_att=1.22, y_ali=3.79, y_f=0.10, d0_att=4.71, l_att=0.89, l_ali=1.42, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.33, y_acc=0.11, l_acc=1.08, d0_v=1.85 |
| 18   | -812.8140    | 3.96       | y_att=1.22, y_ali=3.79, y_f=0.10, d0_att=4.71, l_att=0.89, l_ali=1.42, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.33, y_acc=0.11, l_acc=1.08, d0_v=1.85 |
| 19   | -812.8140    | 2.91       | y_att=1.22, y_ali=3.79, y_f=0.10, d0_att=4.71, l_att=0.89, l_ali=1.42, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.33, y_acc=0.11, l_acc=1.08, d0_v=1.85 |

**End of experiment.**
