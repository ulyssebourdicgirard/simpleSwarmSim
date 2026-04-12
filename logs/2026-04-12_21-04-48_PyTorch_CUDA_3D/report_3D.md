# Experiment Report - PyTorch_CUDA (3D)
**Date:** 2026-04-12_21-04-48

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
| 00   | -425.1820    | 3.32       | y_att=4.08, y_ali=0.54, y_f=1.77, d0_att=1.11, l_att=4.64, l_ali=2.69, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.15, y_acc=1.97, l_acc=3.30, d0_v=0.61 |
| 01   | -429.0918    | 3.45       | y_att=4.08, y_ali=0.54, y_f=1.77, d0_att=1.11, l_att=4.64, l_ali=2.69, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.15, y_acc=1.97, l_acc=3.30, d0_v=0.61 |
| 02   | -429.0918    | 4.28       | y_att=4.08, y_ali=0.54, y_f=1.77, d0_att=1.11, l_att=4.64, l_ali=2.69, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.15, y_acc=1.97, l_acc=3.30, d0_v=0.61 |
| 03   | -447.6794    | 3.08       | y_att=4.08, y_ali=0.48, y_f=1.68, d0_att=1.24, l_att=4.64, l_ali=2.69, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.68, y_acc=1.91, l_acc=3.29, d0_v=0.61 |
| 04   | -449.0399    | 3.02       | y_att=4.08, y_ali=0.48, y_f=1.68, d0_att=1.24, l_att=4.64, l_ali=2.69, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.68, y_acc=1.91, l_acc=3.29, d0_v=0.61 |
| 05   | -462.4814    | 3.07       | y_att=4.31, y_ali=1.55, y_f=1.61, d0_att=2.32, l_att=6.02, l_ali=4.63, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.00, y_acc=2.85, l_acc=2.80, d0_v=0.78 |
| 06   | -470.6270    | 4.00       | y_att=4.08, y_ali=0.54, y_f=2.57, d0_att=1.13, l_att=5.16, l_ali=2.58, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.66, y_acc=1.97, l_acc=3.30, d0_v=0.42 |
| 07   | -476.8786    | 3.02       | y_att=4.26, y_ali=0.66, y_f=2.13, d0_att=1.11, l_att=4.64, l_ali=2.69, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.61, y_acc=1.97, l_acc=3.33, d0_v=0.49 |
| 08   | -473.2908    | 3.29       | y_att=4.26, y_ali=0.66, y_f=2.13, d0_att=1.11, l_att=4.64, l_ali=2.69, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.61, y_acc=1.97, l_acc=3.33, d0_v=0.49 |
| 09   | -480.0836    | 3.45       | y_att=4.08, y_ali=0.23, y_f=2.48, d0_att=1.15, l_att=5.45, l_ali=3.35, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=1.91, l_acc=4.23, d0_v=0.53 |
| 10   | -489.5781    | 4.05       | y_att=3.69, y_ali=0.60, y_f=2.32, d0_att=1.11, l_att=5.16, l_ali=2.78, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.86, y_acc=1.97, l_acc=3.27, d0_v=0.45 |
| 11   | -480.8510    | 3.16       | y_att=4.08, y_ali=0.48, y_f=2.32, d0_att=1.11, l_att=5.16, l_ali=1.62, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.86, y_acc=1.97, l_acc=3.27, d0_v=0.45 |
| 12   | -478.2230    | 3.18       | y_att=6.31, y_ali=0.62, y_f=2.13, d0_att=1.59, l_att=4.74, l_ali=4.35, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.32, y_acc=2.03, l_acc=3.33, d0_v=0.51 |
| 13   | -483.8967    | 3.49       | y_att=3.92, y_ali=0.45, y_f=2.32, d0_att=1.11, l_att=5.16, l_ali=2.46, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.86, y_acc=1.97, l_acc=3.27, d0_v=0.45 |
| 14   | -484.6213    | 3.85       | y_att=5.00, y_ali=1.54, y_f=2.76, d0_att=2.32, l_att=7.27, l_ali=1.79, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.15, y_acc=2.11, l_acc=5.67, d0_v=0.68 |
| 15   | -485.2206    | 3.23       | y_att=5.00, y_ali=0.75, y_f=2.65, d0_att=2.49, l_att=7.06, l_ali=1.61, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.15, y_acc=2.11, l_acc=5.67, d0_v=0.72 |
| 16   | -486.4691    | 3.12       | y_att=5.00, y_ali=0.75, y_f=2.65, d0_att=2.49, l_att=7.06, l_ali=1.61, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.15, y_acc=2.11, l_acc=5.67, d0_v=0.72 |
| 17   | -486.4691    | 3.26       | y_att=5.00, y_ali=0.75, y_f=2.65, d0_att=2.49, l_att=7.06, l_ali=1.61, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.15, y_acc=2.11, l_acc=5.67, d0_v=0.72 |
| 18   | -488.1917    | 4.09       | y_att=5.00, y_ali=0.61, y_f=2.65, d0_att=2.49, l_att=7.06, l_ali=1.34, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.15, y_acc=2.11, l_acc=5.67, d0_v=0.72 |
| 19   | -489.0039    | 3.06       | y_att=5.12, y_ali=1.03, y_f=2.96, d0_att=2.19, l_att=7.14, l_ali=2.19, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.39, y_acc=2.16, l_acc=6.53, d0_v=0.75 |

**End of experiment.**
