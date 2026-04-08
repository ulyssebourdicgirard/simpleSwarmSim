# Experiment Report - PyTorch_CUDA (3D)
**Date:** 2026-04-08_15-54-00

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
| 00   | -6293.7544   | 3.55       | y_att=1.36, y_ali=3.65, y_f=1.86, d0_att=3.30, l_att=2.62, l_ali=4.11, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.58, y_acc=0.34, l_acc=1.44, d0_v=2.39 |
| 01   | -6148.7617   | 3.11       | y_att=0.63, y_ali=3.06, y_f=1.13, d0_att=3.65, l_att=1.77, l_ali=4.64, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.17, y_acc=0.48, l_acc=0.69, d0_v=2.50 |
| 02   | -6333.3521   | 3.13       | y_att=2.36, y_ali=3.88, y_f=1.89, d0_att=3.13, l_att=1.21, l_ali=3.03, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.78, y_acc=0.14, l_acc=1.65, d0_v=2.63 |
| 03   | -6392.2778   | 3.12       | y_att=0.99, y_ali=2.49, y_f=3.16, d0_att=3.71, l_att=3.10, l_ali=3.26, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.30, y_acc=0.97, l_acc=0.37, d0_v=2.22 |
| 04   | -6501.6499   | 3.09       | y_att=0.73, y_ali=1.76, y_f=1.16, d0_att=3.77, l_att=2.22, l_ali=3.11, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.88, y_acc=0.09, l_acc=0.64, d0_v=0.95 |
| 05   | -6352.6553   | 3.06       | y_att=4.80, y_ali=3.47, y_f=1.87, d0_att=1.97, l_att=0.82, l_ali=3.86, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.30, y_acc=0.16, l_acc=2.02, d0_v=1.87 |
| 06   | -6390.4819   | 3.09       | y_att=0.94, y_ali=2.90, y_f=1.73, d0_att=2.24, l_att=1.70, l_ali=3.54, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.93, y_acc=0.82, l_acc=0.26, d0_v=1.82 |
| 07   | -6512.6572   | 3.94       | y_att=1.77, y_ali=5.40, y_f=1.87, d0_att=3.10, l_att=1.31, l_ali=2.58, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.42, y_acc=0.14, l_acc=1.06, d0_v=2.10 |
| 08   | -6498.8291   | 3.83       | y_att=1.25, y_ali=1.04, y_f=1.35, d0_att=3.96, l_att=1.80, l_ali=3.44, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.38, y_acc=0.45, l_acc=0.35, d0_v=2.41 |
| 09   | -6435.6206   | 3.64       | y_att=2.28, y_ali=2.05, y_f=1.50, d0_att=3.13, l_att=1.13, l_ali=3.03, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.10, y_acc=0.11, l_acc=1.65, d0_v=2.77 |
| 10   | -6416.5122   | 3.37       | y_att=1.36, y_ali=2.80, y_f=2.30, d0_att=2.78, l_att=1.89, l_ali=3.17, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.37, y_acc=0.87, l_acc=0.27, d0_v=1.80 |
| 11   | -6434.4648   | 3.38       | y_att=2.39, y_ali=4.56, y_f=2.01, d0_att=3.51, l_att=1.21, l_ali=2.32, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.77, y_acc=0.15, l_acc=1.03, d0_v=2.10 |
| 12   | -6466.6104   | 3.32       | y_att=3.90, y_ali=0.87, y_f=0.85, d0_att=2.76, l_att=0.83, l_ali=4.04, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.96, y_acc=0.31, l_acc=0.62, d0_v=2.67 |
| 13   | -6440.5156   | 3.52       | y_att=1.14, y_ali=3.81, y_f=2.84, d0_att=2.25, l_att=1.63, l_ali=3.28, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.73, y_acc=0.12, l_acc=0.60, d0_v=0.64 |
| 14   | -6508.4219   | 3.56       | y_att=2.63, y_ali=0.41, y_f=1.14, d0_att=1.71, l_att=0.73, l_ali=4.44, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.54, y_acc=0.08, l_acc=0.68, d0_v=0.85 |
| 15   | -6468.8081   | 4.29       | y_att=1.43, y_ali=0.48, y_f=1.20, d0_att=1.86, l_att=0.81, l_ali=4.42, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.40, y_acc=0.11, l_acc=0.39, d0_v=0.69 |
| 16   | -6506.3555   | 3.93       | y_att=1.66, y_ali=0.65, y_f=0.62, d0_att=1.46, l_att=0.82, l_ali=4.52, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.62, y_acc=0.11, l_acc=0.95, d0_v=1.74 |
| 17   | -6484.9648   | 3.73       | y_att=2.71, y_ali=0.41, y_f=1.18, d0_att=1.71, l_att=0.73, l_ali=4.44, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.54, y_acc=0.08, l_acc=0.68, d0_v=0.85 |
| 18   | -6478.4038   | 3.39       | y_att=1.76, y_ali=0.25, y_f=0.19, d0_att=1.31, l_att=0.66, l_ali=5.36, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.50, y_acc=0.07, l_acc=0.68, d0_v=0.74 |
| 19   | -6588.7153   | 3.27       | y_att=1.76, y_ali=0.29, y_f=0.19, d0_att=1.31, l_att=0.66, l_ali=5.36, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.50, y_acc=0.07, l_acc=0.68, d0_v=0.74 |

**End of experiment.**
