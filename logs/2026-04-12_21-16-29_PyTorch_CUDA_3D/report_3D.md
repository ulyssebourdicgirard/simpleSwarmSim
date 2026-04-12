# Experiment Report - PyTorch_CUDA (3D)
**Date:** 2026-04-12_21-16-29

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
| NB_DRONES            | 30         |
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
| 00   | -914.0203    | 4.55       | y_att=3.93, y_ali=1.61, y_f=0.98, d0_att=1.57, l_att=2.63, l_ali=3.65, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.56, y_acc=1.41, l_acc=3.40, d0_v=0.63 |
| 01   | -1044.3009   | 3.58       | y_att=1.82, y_ali=3.35, y_f=1.39, d0_att=1.40, l_att=4.62, l_ali=2.58, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.75, y_acc=1.52, l_acc=3.19, d0_v=0.44 |
| 02   | -1076.3962   | 3.48       | y_att=1.82, y_ali=3.47, y_f=1.39, d0_att=1.40, l_att=4.62, l_ali=3.15, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.90, y_acc=1.52, l_acc=3.19, d0_v=0.44 |
| 03   | -1109.7985   | 4.19       | y_att=3.58, y_ali=2.14, y_f=1.29, d0_att=1.36, l_att=3.35, l_ali=3.94, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.93, y_acc=1.92, l_acc=3.43, d0_v=0.61 |
| 04   | -1214.3966   | 3.41       | y_att=4.00, y_ali=3.51, y_f=1.69, d0_att=1.56, l_att=3.61, l_ali=3.78, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.20, y_acc=1.66, l_acc=5.91, d0_v=0.67 |
| 05   | -1195.1514   | 3.47       | y_att=4.09, y_ali=4.01, y_f=1.73, d0_att=1.56, l_att=3.81, l_ali=3.04, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.09, y_acc=1.66, l_acc=5.18, d0_v=0.59 |
| 06   | -1239.8412   | 3.40       | y_att=4.00, y_ali=3.51, y_f=1.69, d0_att=1.56, l_att=3.61, l_ali=5.14, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.20, y_acc=1.89, l_acc=5.04, d0_v=0.67 |
| 07   | -1236.0615   | 4.37       | y_att=4.00, y_ali=3.51, y_f=1.69, d0_att=1.56, l_att=3.61, l_ali=5.14, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.20, y_acc=1.89, l_acc=5.04, d0_v=0.67 |
| 08   | -1244.3733   | 3.84       | y_att=4.00, y_ali=3.51, y_f=1.69, d0_att=1.56, l_att=3.61, l_ali=5.14, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.20, y_acc=1.89, l_acc=5.04, d0_v=0.67 |
| 09   | -1253.9607   | 3.51       | y_att=4.22, y_ali=2.82, y_f=1.99, d0_att=2.04, l_att=4.28, l_ali=6.69, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.79, y_acc=2.13, l_acc=4.48, d0_v=0.60 |
| 10   | -1259.8748   | 3.28       | y_att=4.00, y_ali=5.43, y_f=1.68, d0_att=1.67, l_att=3.93, l_ali=5.14, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.20, y_acc=1.89, l_acc=5.04, d0_v=0.67 |
| 11   | -1269.1311   | 3.24       | y_att=3.48, y_ali=4.01, y_f=1.69, d0_att=1.33, l_att=3.61, l_ali=5.78, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.15, y_acc=1.80, l_acc=5.32, d0_v=0.67 |
| 12   | -1335.8966   | 4.45       | y_att=4.22, y_ali=2.82, y_f=1.96, d0_att=2.04, l_att=4.28, l_ali=5.95, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.79, y_acc=1.59, l_acc=5.15, d0_v=0.50 |
| 13   | -1315.3483   | 3.59       | y_att=4.17, y_ali=4.01, y_f=1.69, d0_att=2.18, l_att=4.07, l_ali=6.90, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.53, y_acc=1.79, l_acc=5.00, d0_v=0.67 |
| 14   | -1327.9872   | 3.66       | y_att=4.90, y_ali=4.56, y_f=1.23, d0_att=1.82, l_att=3.15, l_ali=6.69, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.25, y_acc=1.84, l_acc=3.85, d0_v=0.69 |
| 15   | -1307.1172   | 4.38       | y_att=4.14, y_ali=4.26, y_f=1.99, d0_att=1.82, l_att=4.28, l_ali=6.69, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.16, y_acc=2.13, l_acc=4.60, d0_v=0.60 |
| 16   | -1299.6758   | 3.42       | y_att=2.97, y_ali=2.61, y_f=1.45, d0_att=2.27, l_att=4.94, l_ali=7.29, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.57, y_acc=2.20, l_acc=3.36, d0_v=0.66 |
| 17   | -1319.0172   | 3.49       | y_att=3.23, y_ali=5.39, y_f=1.76, d0_att=1.56, l_att=4.10, l_ali=6.78, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.96, y_acc=1.79, l_acc=5.25, d0_v=0.67 |
| 18   | -1335.5782   | 3.46       | y_att=3.48, y_ali=6.71, y_f=1.76, d0_att=1.56, l_att=4.10, l_ali=6.56, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.75, y_acc=1.79, l_acc=5.25, d0_v=0.67 |
| 19   | -1353.3206   | 3.30       | y_att=3.42, y_ali=6.92, y_f=1.70, d0_att=1.61, l_att=4.10, l_ali=6.46, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.75, y_acc=1.79, l_acc=5.25, d0_v=0.67 |

**End of experiment.**
