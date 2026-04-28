# Experiment Report - PyTorch_CUDA (3D)
**Date:** 2026-04-21_22-21-24

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
| NB_DRONES            | 30         |
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
| 00   | -952.7410    | 4.35       | y_att=3.88, y_ali=1.58, y_f=0.87, d0_att=3.00, l_att=4.09, l_ali=1.51, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.96, y_acc=1.36, l_acc=3.60, d0_v=0.62 |
| 01   | -1064.7126   | 4.14       | y_att=3.36, y_ali=1.56, y_f=1.34, d0_att=2.57, l_att=4.60, l_ali=4.14, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.53, y_acc=1.38, l_acc=3.82, d0_v=0.47 |
| 02   | -1067.0338   | 4.14       | y_att=4.96, y_ali=0.55, y_f=1.15, d0_att=3.99, l_att=4.74, l_ali=3.72, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.89, y_acc=1.91, l_acc=2.79, d0_v=0.57 |
| 03   | -1147.4674   | 4.14       | y_att=2.92, y_ali=1.69, y_f=1.32, d0_att=1.22, l_att=3.52, l_ali=5.23, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.57, y_acc=1.64, l_acc=6.88, d0_v=0.94 |
| 04   | -1099.9417   | 4.14       | y_att=3.36, y_ali=1.56, y_f=1.34, d0_att=2.57, l_att=4.60, l_ali=4.14, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.28, y_acc=1.38, l_acc=3.82, d0_v=0.46 |
| 05   | -1236.5948   | 4.14       | y_att=3.23, y_ali=1.72, y_f=1.53, d0_att=1.97, l_att=4.75, l_ali=6.42, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.82, y_acc=1.38, l_acc=5.31, d0_v=0.55 |
| 06   | -1224.5028   | 4.14       | y_att=3.23, y_ali=1.72, y_f=1.53, d0_att=1.97, l_att=4.75, l_ali=6.42, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.82, y_acc=1.38, l_acc=5.31, d0_v=0.55 |
| 07   | -1304.0714   | 4.15       | y_att=3.16, y_ali=1.72, y_f=1.53, d0_att=1.97, l_att=4.75, l_ali=6.42, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.52, y_acc=1.38, l_acc=5.31, d0_v=0.55 |
| 08   | -1259.4862   | 4.15       | y_att=2.84, y_ali=2.67, y_f=1.41, d0_att=1.22, l_att=3.52, l_ali=7.32, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.16, y_acc=2.29, l_acc=6.99, d0_v=1.30 |
| 09   | -1273.9442   | 4.15       | y_att=2.64, y_ali=1.75, y_f=1.32, d0_att=1.14, l_att=3.52, l_ali=6.97, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.53, y_acc=1.64, l_acc=6.88, d0_v=0.95 |
| 10   | -1273.7283   | 4.15       | y_att=2.64, y_ali=1.75, y_f=1.32, d0_att=1.14, l_att=3.52, l_ali=6.97, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.53, y_acc=1.64, l_acc=6.88, d0_v=0.95 |
| 11   | -1280.8323   | 4.15       | y_att=3.20, y_ali=3.47, y_f=1.43, d0_att=1.22, l_att=3.52, l_ali=5.89, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.67, y_acc=2.25, l_acc=7.56, d0_v=1.30 |
| 12   | -1296.9683   | 4.15       | y_att=1.47, y_ali=2.32, y_f=1.21, d0_att=0.86, l_att=3.82, l_ali=7.76, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.57, y_acc=1.59, l_acc=7.97, d0_v=1.20 |
| 13   | -1331.8079   | 4.15       | y_att=3.19, y_ali=1.94, y_f=1.53, d0_att=1.38, l_att=3.56, l_ali=8.41, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=1.64, l_acc=7.18, d0_v=0.94 |
| 14   | -1320.3551   | 4.15       | y_att=1.47, y_ali=2.32, y_f=1.21, d0_att=0.86, l_att=3.82, l_ali=7.76, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.57, y_acc=1.59, l_acc=7.97, d0_v=1.20 |
| 15   | -1300.4596   | 4.15       | y_att=1.47, y_ali=2.32, y_f=1.21, d0_att=0.86, l_att=3.82, l_ali=7.76, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.57, y_acc=1.59, l_acc=7.97, d0_v=1.20 |
| 16   | -1314.5601   | 4.15       | y_att=1.14, y_ali=2.32, y_f=1.21, d0_att=0.86, l_att=4.36, l_ali=7.76, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.08, y_acc=1.59, l_acc=7.97, d0_v=1.20 |
| 17   | -1305.5389   | 4.16       | y_att=1.47, y_ali=2.32, y_f=1.21, d0_att=0.90, l_att=3.82, l_ali=7.76, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.23, y_acc=1.59, l_acc=7.97, d0_v=1.20 |
| 18   | -1365.6234   | 4.16       | y_att=1.47, y_ali=2.32, y_f=1.21, d0_att=0.90, l_att=3.82, l_ali=7.76, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.23, y_acc=1.59, l_acc=7.97, d0_v=1.20 |
| 19   | -1324.3839   | 4.16       | y_att=3.44, y_ali=1.69, y_f=1.67, d0_att=1.23, l_att=3.52, l_ali=9.40, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.01, y_acc=2.07, l_acc=6.83, d0_v=1.03 |

**End of experiment.**
