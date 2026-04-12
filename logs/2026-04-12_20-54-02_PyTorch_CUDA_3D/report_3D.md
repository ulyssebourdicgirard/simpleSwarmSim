# Experiment Report - PyTorch_CUDA (3D)
**Date:** 2026-04-12_20-54-02

## 1. Initial Configuration
| Parameter | Value |
| :--- | :--- |
| ARENA_RADIUS         | 50.0       |
| COLLISION_DIST       | 0.4        |
| DT                   | 0.1        |
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
| 00   | -4201.1855   | 3.41       | y_att=0.54, y_ali=1.87, y_f=1.93, d0_att=2.09, l_att=2.17, l_ali=1.19, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.58, y_acc=0.15, l_acc=1.58, d0_v=1.07 |
| 01   | -4310.7788   | 2.91       | y_att=0.53, y_ali=3.56, y_f=1.10, d0_att=2.97, l_att=2.51, l_ali=2.75, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.69, y_acc=0.17, l_acc=1.57, d0_v=2.74 |
| 02   | -4285.4893   | 2.94       | y_att=3.34, y_ali=3.79, y_f=1.69, d0_att=3.12, l_att=1.18, l_ali=4.54, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.60, y_acc=0.40, l_acc=0.35, d0_v=1.82 |
| 03   | -4382.1309   | 3.04       | y_att=1.28, y_ali=0.90, y_f=2.35, d0_att=2.17, l_att=1.66, l_ali=1.43, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.32, y_acc=0.29, l_acc=1.03, d0_v=2.06 |
| 04   | -4413.7344   | 3.08       | y_att=2.14, y_ali=0.82, y_f=2.21, d0_att=2.14, l_att=1.08, l_ali=1.43, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.84, y_acc=0.20, l_acc=0.67, d0_v=1.56 |
| 05   | -4463.9253   | 3.23       | y_att=1.33, y_ali=2.04, y_f=3.01, d0_att=1.02, l_att=1.01, l_ali=3.05, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.75, y_acc=0.12, l_acc=2.00, d0_v=1.50 |
| 06   | -4428.0259   | 2.87       | y_att=0.99, y_ali=3.52, y_f=1.77, d0_att=2.90, l_att=2.05, l_ali=3.07, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.59, y_acc=0.42, l_acc=0.44, d0_v=1.51 |
| 07   | -4458.6948   | 3.00       | y_att=2.78, y_ali=1.35, y_f=2.14, d0_att=4.56, l_att=1.43, l_ali=4.54, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.23, y_acc=0.30, l_acc=0.40, d0_v=1.99 |
| 08   | -4418.3560   | 3.06       | y_att=3.17, y_ali=2.44, y_f=2.54, d0_att=6.38, l_att=1.83, l_ali=3.39, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.26, y_acc=0.20, l_acc=0.53, d0_v=1.65 |
| 09   | -4423.8823   | 3.14       | y_att=0.46, y_ali=3.19, y_f=1.71, d0_att=2.09, l_att=2.05, l_ali=2.09, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.42, y_acc=0.23, l_acc=1.10, d0_v=2.81 |
| 10   | -4431.2622   | 3.15       | y_att=0.92, y_ali=0.76, y_f=1.39, d0_att=1.84, l_att=1.14, l_ali=2.45, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.96, y_acc=0.13, l_acc=1.64, d0_v=2.99 |
| 11   | -4487.3257   | 3.33       | y_att=0.63, y_ali=0.80, y_f=2.90, d0_att=2.09, l_att=2.14, l_ali=1.62, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.80, y_acc=0.08, l_acc=1.95, d0_v=1.09 |
| 12   | -4474.3491   | 3.08       | y_att=1.37, y_ali=1.03, y_f=2.59, d0_att=1.84, l_att=1.35, l_ali=2.02, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.54, y_acc=0.30, l_acc=1.21, d0_v=2.45 |
| 13   | -4429.8042   | 3.13       | y_att=3.83, y_ali=0.17, y_f=2.13, d0_att=2.86, l_att=1.09, l_ali=1.41, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.50, y_acc=0.34, l_acc=0.90, d0_v=2.03 |
| 14   | -4441.1890   | 3.02       | y_att=0.67, y_ali=3.19, y_f=2.04, d0_att=1.95, l_att=1.62, l_ali=2.69, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.73, y_acc=0.17, l_acc=1.26, d0_v=2.56 |
| 15   | -4511.8447   | 3.05       | y_att=0.60, y_ali=0.41, y_f=1.17, d0_att=3.39, l_att=1.81, l_ali=2.22, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.02, y_acc=0.31, l_acc=0.51, d0_v=3.77 |
| 16   | -4432.9888   | 2.91       | y_att=1.58, y_ali=0.41, y_f=3.29, d0_att=3.02, l_att=1.57, l_ali=2.98, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.13, y_acc=0.23, l_acc=0.94, d0_v=2.12 |
| 17   | -4447.0488   | 3.48       | y_att=0.51, y_ali=5.35, y_f=2.04, d0_att=1.96, l_att=1.83, l_ali=2.21, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.59, y_acc=0.17, l_acc=1.26, d0_v=2.85 |
| 18   | -4471.9092   | 3.15       | y_att=2.78, y_ali=0.80, y_f=2.87, d0_att=2.40, l_att=0.77, l_ali=1.69, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.54, y_acc=0.16, l_acc=1.00, d0_v=2.56 |
| 19   | -4525.6406   | 3.10       | y_att=2.56, y_ali=1.24, y_f=2.32, d0_att=3.06, l_att=1.19, l_ali=0.64, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.39, y_acc=0.12, l_acc=2.03, d0_v=2.56 |

**End of experiment.**
