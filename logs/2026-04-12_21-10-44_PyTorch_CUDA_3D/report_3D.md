# Experiment Report - PyTorch_CUDA (3D)
**Date:** 2026-04-12_21-10-44

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
| NB_DRONES            | 20         |
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
| 00   | -540.0643    | 3.30       | y_att=3.56, y_ali=3.63, y_f=1.15, d0_att=1.49, l_att=3.44, l_ali=3.34, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.03, y_acc=1.92, l_acc=2.66, d0_v=0.62 |
| 01   | -644.5728    | 3.67       | y_att=3.03, y_ali=1.58, y_f=1.81, d0_att=1.27, l_att=4.25, l_ali=2.49, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.06, y_acc=1.70, l_acc=3.97, d0_v=0.54 |
| 02   | -796.7109    | 3.58       | y_att=4.92, y_ali=3.46, y_f=1.19, d0_att=3.23, l_att=5.23, l_ali=4.34, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.11, y_acc=1.47, l_acc=6.09, d0_v=0.89 |
| 03   | -774.2035    | 3.13       | y_att=3.09, y_ali=1.58, y_f=1.81, d0_att=1.27, l_att=4.25, l_ali=2.49, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.06, y_acc=1.85, l_acc=3.97, d0_v=0.54 |
| 04   | -777.6892    | 3.07       | y_att=3.09, y_ali=1.58, y_f=1.81, d0_att=1.27, l_att=4.25, l_ali=2.49, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.74, y_acc=2.16, l_acc=3.37, d0_v=0.54 |
| 05   | -788.1632    | 3.85       | y_att=4.48, y_ali=3.44, y_f=1.18, d0_att=3.47, l_att=5.13, l_ali=1.10, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.00, y_acc=1.71, l_acc=4.96, d0_v=0.86 |
| 06   | -813.8020    | 3.07       | y_att=4.13, y_ali=2.16, y_f=2.12, d0_att=1.27, l_att=4.30, l_ali=1.97, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.06, y_acc=1.70, l_acc=3.65, d0_v=0.39 |
| 07   | -868.1631    | 3.14       | y_att=1.08, y_ali=0.20, y_f=1.92, d0_att=0.83, l_att=6.16, l_ali=3.87, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.09, y_acc=2.65, l_acc=2.88, d0_v=0.51 |
| 08   | -857.0873    | 3.38       | y_att=1.08, y_ali=0.20, y_f=1.92, d0_att=0.83, l_att=6.16, l_ali=3.87, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.09, y_acc=2.94, l_acc=4.06, d0_v=0.80 |
| 09   | -861.9652    | 4.10       | y_att=1.08, y_ali=0.20, y_f=1.92, d0_att=0.83, l_att=6.16, l_ali=3.87, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.09, y_acc=2.94, l_acc=4.06, d0_v=0.80 |
| 10   | -868.1941    | 3.09       | y_att=1.08, y_ali=0.26, y_f=1.92, d0_att=0.83, l_att=6.16, l_ali=3.87, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.93, y_acc=2.94, l_acc=4.06, d0_v=0.80 |
| 11   | -862.1794    | 3.14       | y_att=1.08, y_ali=0.26, y_f=1.92, d0_att=0.83, l_att=6.16, l_ali=3.87, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.93, y_acc=2.94, l_acc=4.06, d0_v=0.80 |
| 12   | -870.5472    | 3.11       | y_att=1.08, y_ali=0.25, y_f=1.92, d0_att=0.83, l_att=6.16, l_ali=3.87, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.93, y_acc=2.94, l_acc=4.06, d0_v=0.80 |
| 13   | -862.1794    | 3.87       | y_att=1.08, y_ali=0.25, y_f=1.92, d0_att=0.83, l_att=6.16, l_ali=3.87, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.93, y_acc=2.94, l_acc=4.06, d0_v=0.80 |
| 14   | -877.6102    | 3.16       | y_att=1.65, y_ali=0.32, y_f=2.74, d0_att=0.83, l_att=6.16, l_ali=3.76, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.80, y_acc=1.61, l_acc=3.40, d0_v=0.27 |
| 15   | -902.4805    | 3.24       | y_att=1.65, y_ali=0.32, y_f=2.74, d0_att=0.83, l_att=6.16, l_ali=3.76, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=1.61, l_acc=3.40, d0_v=0.27 |
| 16   | -889.4094    | 3.16       | y_att=1.65, y_ali=0.32, y_f=2.74, d0_att=0.83, l_att=6.16, l_ali=3.76, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.26, y_acc=1.61, l_acc=3.40, d0_v=0.27 |
| 17   | -894.7972    | 3.87       | y_att=4.22, y_ali=2.20, y_f=1.79, d0_att=1.08, l_att=3.54, l_ali=9.67, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.24, y_acc=1.55, l_acc=4.97, d0_v=0.54 |
| 18   | -893.2566    | 3.26       | y_att=3.09, y_ali=1.07, y_f=2.13, d0_att=0.99, l_att=4.34, l_ali=2.52, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.72, y_acc=2.47, l_acc=4.83, d0_v=0.71 |
| 19   | -890.9550    | 3.07       | y_att=5.89, y_ali=2.19, y_f=1.84, d0_att=4.09, l_att=6.16, l_ali=0.75, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.83, y_acc=0.60, l_acc=13.73, d0_v=0.51 |

**End of experiment.**
