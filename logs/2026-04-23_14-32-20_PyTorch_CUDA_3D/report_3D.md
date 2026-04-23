# Experiment Report - PyTorch_CUDA (3D)
**Date:** 2026-04-23_14-32-20

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
| NB_DRONES            | 30         |
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
| W_EFFORT             | 1          |
| W_EXPLO              | -50.0      |
| W_MILL               | 20.0       |
| W_POL                | -0.0       |
| Z_MAX                | 10.0       |
| Z_MIN                | 1.0        |

## 2. Optimization Evolution
| Gen  |  Best Cost   |  Time (s)  |                                                                All Parameters                                                                |
| :--: | :----------: | :--------: | :------------------------------------------------------------------------------------------------------------------------------------------ |
| 00   | -1060.6536   | 4.84       | y_att=0.89, y_ali=3.50, y_f=0.84, d0_att=3.04, l_att=2.47, l_ali=3.02, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.18, y_acc=0.67, l_acc=0.85, d0_v=2.98 |
| 01   | -1296.7242   | 3.79       | y_att=3.56, y_ali=2.34, y_f=0.55, d0_att=1.49, l_att=3.27, l_ali=0.92, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.44, y_acc=0.45, l_acc=0.10, d0_v=2.98 |
| 02   | -1491.4513   | 3.72       | y_att=3.85, y_ali=0.97, y_f=0.73, d0_att=1.49, l_att=6.44, l_ali=1.56, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.86, y_acc=0.02, l_acc=0.72, d0_v=1.82 |
| 03   | -1491.4513   | 3.47       | y_att=3.85, y_ali=0.97, y_f=0.73, d0_att=1.49, l_att=6.44, l_ali=1.56, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.86, y_acc=0.02, l_acc=0.72, d0_v=1.82 |
| 04   | -1491.4513   | 3.46       | y_att=3.85, y_ali=0.97, y_f=0.73, d0_att=1.49, l_att=6.44, l_ali=1.56, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.86, y_acc=0.02, l_acc=0.72, d0_v=1.82 |
| 05   | -1510.3080   | 3.35       | y_att=4.59, y_ali=2.39, y_f=0.58, d0_att=2.02, l_att=4.95, l_ali=1.66, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.90, y_acc=0.00, l_acc=0.36, d0_v=2.90 |
| 06   | -1513.3375   | 3.35       | y_att=4.59, y_ali=2.39, y_f=0.58, d0_att=2.02, l_att=4.95, l_ali=1.66, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.90, y_acc=0.00, l_acc=0.36, d0_v=2.90 |
| 07   | -1523.0597   | 4.42       | y_att=2.70, y_ali=0.65, y_f=0.54, d0_att=0.80, l_att=4.26, l_ali=6.42, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.32, y_acc=0.04, l_acc=1.08, d0_v=4.19 |
| 08   | -1523.0597   | 3.79       | y_att=2.70, y_ali=0.65, y_f=0.54, d0_att=0.80, l_att=4.26, l_ali=6.42, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.32, y_acc=0.04, l_acc=1.08, d0_v=4.19 |
| 09   | -1534.1870   | 3.67       | y_att=4.34, y_ali=1.34, y_f=0.52, d0_att=1.63, l_att=3.98, l_ali=1.83, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.46, y_acc=0.24, l_acc=0.10, d0_v=3.74 |
| 10   | -1534.1870   | 4.67       | y_att=4.34, y_ali=1.34, y_f=0.52, d0_att=1.63, l_att=3.98, l_ali=1.83, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.46, y_acc=0.24, l_acc=0.10, d0_v=3.74 |
| 11   | -1550.5953   | 3.63       | y_att=4.25, y_ali=0.61, y_f=0.58, d0_att=1.24, l_att=5.30, l_ali=2.19, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.00, y_acc=0.16, l_acc=0.14, d0_v=2.80 |
| 12   | -1550.5953   | 3.65       | y_att=4.25, y_ali=0.61, y_f=0.58, d0_att=1.24, l_att=5.30, l_ali=2.19, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.00, y_acc=0.16, l_acc=0.14, d0_v=2.80 |
| 13   | -1550.5953   | 3.61       | y_att=4.25, y_ali=0.61, y_f=0.58, d0_att=1.24, l_att=5.30, l_ali=2.19, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.00, y_acc=0.16, l_acc=0.14, d0_v=2.80 |
| 14   | -1550.5953   | 3.50       | y_att=4.25, y_ali=0.61, y_f=0.58, d0_att=1.24, l_att=5.30, l_ali=2.19, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.00, y_acc=0.16, l_acc=0.14, d0_v=2.80 |
| 15   | -1554.7167   | 3.51       | y_att=4.67, y_ali=5.20, y_f=0.63, d0_att=0.74, l_att=3.07, l_ali=1.22, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.56, y_acc=0.06, l_acc=0.19, d0_v=3.29 |
| 16   | -1554.7167   | 3.48       | y_att=4.67, y_ali=5.20, y_f=0.63, d0_att=0.74, l_att=3.07, l_ali=1.22, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.56, y_acc=0.06, l_acc=0.19, d0_v=3.29 |
| 17   | -1554.7167   | 3.73       | y_att=4.67, y_ali=5.20, y_f=0.63, d0_att=0.74, l_att=3.07, l_ali=1.22, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.56, y_acc=0.06, l_acc=0.19, d0_v=3.29 |
| 18   | -1554.7167   | 4.31       | y_att=4.67, y_ali=5.20, y_f=0.63, d0_att=0.74, l_att=3.07, l_ali=1.22, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.56, y_acc=0.06, l_acc=0.19, d0_v=3.29 |
| 19   | -1556.8551   | 3.53       | y_att=3.81, y_ali=1.38, y_f=0.80, d0_att=1.92, l_att=7.05, l_ali=1.61, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.14, y_acc=0.01, l_acc=0.26, d0_v=3.48 |

**End of experiment.**
