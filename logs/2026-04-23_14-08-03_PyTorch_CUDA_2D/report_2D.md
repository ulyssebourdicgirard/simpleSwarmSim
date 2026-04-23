# Experiment Report - PyTorch_CUDA (2D)
**Date:** 2026-04-23_14-08-03

## 1. Initial Configuration
| Parameter | Value |
| :--- | :--- |
| ALPHA_LPF            | 0.2        |
| ARENA_RADIUS         | 100.0      |
| COLLISION_DIST       | 0.4        |
| DT                   | 0.1        |
| ENABLE_3D            | False      |
| FULL_MILLING_MODE    | True       |
| GEN_CPU              | 20         |
| GEN_GPU              | 20         |
| GRID_RES             | 5.0        |
| MAX_SPEED            | 20.0       |
| MAX_YAW_RATE         | 3.14       |
| NB_DRONES            | 5          |
| NEIGHBORS            | 4          |
| POP_SIZE_CPU         | 150        |
| POP_SIZE_GPU         | 5000       |
| SCENARIO             | default    |
| SIM_STEPS            | 500        |
| SPOIL_ADD            | 0.05       |
| SPOIL_MULT           | 1.01       |
| VISU_STEPS           | 1000       |
| W_COLL               | 0          |
| W_DISP               | 0.0        |
| W_EFFORT             | 1.0        |
| W_EXPLO              | 0.0        |
| W_MILL               | -100.0     |
| W_POL                | 0.0        |
| Z_MAX                | 10.0       |
| Z_MIN                | 1.0        |

## 2. Optimization Evolution
| Gen  |  Best Cost   |  Time (s)  |                                                                All Parameters                                                                |
| :--: | :----------: | :--------: | :------------------------------------------------------------------------------------------------------------------------------------------ |
| 00   | -4138.0859   | 2.07       | y_att=0.64, y_ali=2.74, y_f=1.52, d0_att=2.99, l_att=1.03, l_ali=4.35, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.20, y_acc=0.17, l_acc=2.19, d0_v=2.68 |
| 01   | -4797.1646   | 1.89       | y_att=0.69, y_ali=1.42, y_f=1.70, d0_att=3.17, l_att=0.75, l_ali=2.54, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.33, y_acc=0.21, l_acc=4.00, d0_v=2.85 |
| 02   | -5520.8408   | 2.04       | y_att=0.64, y_ali=2.77, y_f=0.63, d0_att=3.52, l_att=0.69, l_ali=1.85, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.68, y_acc=0.07, l_acc=2.26, d0_v=3.37 |
| 03   | -5520.8408   | 2.01       | y_att=0.64, y_ali=2.77, y_f=0.63, d0_att=3.52, l_att=0.69, l_ali=1.85, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.68, y_acc=0.07, l_acc=2.26, d0_v=3.37 |
| 04   | -5712.8745   | 1.85       | y_att=0.27, y_ali=5.68, y_f=1.13, d0_att=5.54, l_att=1.15, l_ali=1.77, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.06, y_acc=0.74, l_acc=1.19, d0_v=2.00 |
| 05   | -6417.2148   | 1.90       | y_att=0.48, y_ali=4.28, y_f=1.87, d0_att=3.74, l_att=0.39, l_ali=5.84, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.86, y_acc=0.22, l_acc=0.76, d0_v=1.91 |
| 06   | -6417.2148   | 1.85       | y_att=0.48, y_ali=4.28, y_f=1.87, d0_att=3.74, l_att=0.39, l_ali=5.84, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.86, y_acc=0.22, l_acc=0.76, d0_v=1.91 |
| 07   | -6951.7285   | 3.07       | y_att=0.31, y_ali=3.93, y_f=1.69, d0_att=1.64, l_att=0.26, l_ali=3.49, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.08, l_acc=0.53, d0_v=1.58 |
| 08   | -6951.7285   | 2.02       | y_att=0.31, y_ali=3.93, y_f=1.69, d0_att=1.64, l_att=0.26, l_ali=3.49, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.08, l_acc=0.53, d0_v=1.58 |
| 09   | -6951.7285   | 2.03       | y_att=0.31, y_ali=3.93, y_f=1.69, d0_att=1.64, l_att=0.26, l_ali=3.49, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.08, l_acc=0.53, d0_v=1.58 |
| 10   | -7409.9146   | 2.03       | y_att=0.26, y_ali=0.20, y_f=1.32, d0_att=6.40, l_att=0.75, l_ali=1.95, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.03, y_acc=0.08, l_acc=1.25, d0_v=2.52 |
| 11   | -7409.9146   | 1.91       | y_att=0.26, y_ali=0.20, y_f=1.32, d0_att=6.40, l_att=0.75, l_ali=1.95, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.03, y_acc=0.08, l_acc=1.25, d0_v=2.52 |
| 12   | -7409.9146   | 1.99       | y_att=0.26, y_ali=0.20, y_f=1.32, d0_att=6.40, l_att=0.75, l_ali=1.95, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.03, y_acc=0.08, l_acc=1.25, d0_v=2.52 |
| 13   | -7515.3936   | 2.38       | y_att=0.66, y_ali=5.09, y_f=1.00, d0_att=9.09, l_att=0.21, l_ali=6.70, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.25, y_acc=0.28, l_acc=0.15, d0_v=1.66 |
| 14   | -7529.6802   | 2.16       | y_att=0.86, y_ali=1.37, y_f=4.08, d0_att=2.22, l_att=0.14, l_ali=1.70, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.83, y_acc=0.12, l_acc=1.34, d0_v=2.55 |
| 15   | -7544.0063   | 2.05       | y_att=1.38, y_ali=1.43, y_f=3.90, d0_att=5.80, l_att=0.25, l_ali=7.20, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.14, y_acc=0.13, l_acc=0.91, d0_v=4.00 |
| 16   | -7544.0063   | 2.13       | y_att=1.38, y_ali=1.43, y_f=3.90, d0_att=5.80, l_att=0.25, l_ali=7.20, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.14, y_acc=0.13, l_acc=0.91, d0_v=4.00 |
| 17   | -7601.8262   | 1.93       | y_att=0.62, y_ali=0.78, y_f=5.24, d0_att=4.41, l_att=0.10, l_ali=5.10, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.16, l_acc=0.69, d0_v=3.16 |
| 18   | -7601.8262   | 1.97       | y_att=0.62, y_ali=0.78, y_f=5.24, d0_att=4.41, l_att=0.10, l_ali=5.10, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.16, l_acc=0.69, d0_v=3.16 |
| 19   | -7601.8262   | 1.94       | y_att=0.62, y_ali=0.78, y_f=5.24, d0_att=4.41, l_att=0.10, l_ali=5.10, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.16, l_acc=0.69, d0_v=3.16 |

**End of experiment.**
