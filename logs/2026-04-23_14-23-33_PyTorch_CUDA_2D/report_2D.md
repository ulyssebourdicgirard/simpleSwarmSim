# Experiment Report - PyTorch_CUDA (2D)
**Date:** 2026-04-23_14-23-33

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
| NB_DRONES            | 25         |
| NEIGHBORS            | 4          |
| POP_SIZE_CPU         | 150        |
| POP_SIZE_GPU         | 50000      |
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
| 00   | -4433.7993   | 22.10      | y_att=3.42, y_ali=3.35, y_f=1.82, d0_att=3.02, l_att=1.48, l_ali=3.62, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.63, y_acc=1.99, l_acc=0.52, d0_v=2.89 |
| 01   | -4433.7993   | 23.82      | y_att=3.42, y_ali=3.35, y_f=1.82, d0_att=3.02, l_att=1.48, l_ali=3.62, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.63, y_acc=1.99, l_acc=0.52, d0_v=2.89 |
| 02   | -4433.7993   | 22.50      | y_att=3.42, y_ali=3.35, y_f=1.82, d0_att=3.02, l_att=1.48, l_ali=3.62, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.63, y_acc=1.99, l_acc=0.52, d0_v=2.89 |
| 03   | -4433.7993   | 22.52      | y_att=3.42, y_ali=3.35, y_f=1.82, d0_att=3.02, l_att=1.48, l_ali=3.62, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.63, y_acc=1.99, l_acc=0.52, d0_v=2.89 |
| 04   | -4484.1177   | 22.08      | y_att=2.10, y_ali=0.57, y_f=1.86, d0_att=3.44, l_att=1.02, l_ali=4.26, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.12, y_acc=0.15, l_acc=1.96, d0_v=2.29 |
| 05   | -4552.8623   | 22.58      | y_att=1.76, y_ali=3.57, y_f=6.00, d0_att=2.95, l_att=2.05, l_ali=4.56, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.44, l_acc=0.50, d0_v=0.93 |
| 06   | -4552.8623   | 21.74      | y_att=1.76, y_ali=3.57, y_f=6.00, d0_att=2.95, l_att=2.05, l_ali=4.56, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.44, l_acc=0.50, d0_v=0.93 |
| 07   | -4722.3682   | 21.76      | y_att=0.72, y_ali=0.69, y_f=1.80, d0_att=5.32, l_att=1.24, l_ali=2.61, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.89, y_acc=0.38, l_acc=1.55, d0_v=6.86 |
| 08   | -4722.3682   | 21.77      | y_att=0.72, y_ali=0.69, y_f=1.80, d0_att=5.32, l_att=1.24, l_ali=2.61, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.89, y_acc=0.38, l_acc=1.55, d0_v=6.86 |
| 09   | -4797.0698   | 21.69      | y_att=0.59, y_ali=0.76, y_f=1.60, d0_att=10.32, l_att=0.63, l_ali=1.84, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.99, y_acc=0.19, l_acc=0.76, d0_v=2.91 |
| 10   | -4797.0698   | 21.65      | y_att=0.59, y_ali=0.76, y_f=1.60, d0_att=10.32, l_att=0.63, l_ali=1.84, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.99, y_acc=0.19, l_acc=0.76, d0_v=2.91 |
| 11   | -4797.0698   | 21.71      | y_att=0.59, y_ali=0.76, y_f=1.60, d0_att=10.32, l_att=0.63, l_ali=1.84, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.99, y_acc=0.19, l_acc=0.76, d0_v=2.91 |
| 12   | -4915.5190   | 21.82      | y_att=0.16, y_ali=0.77, y_f=2.49, d0_att=3.15, l_att=0.43, l_ali=1.90, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.51, y_acc=0.35, l_acc=0.10, d0_v=3.07 |
| 13   | -4915.5190   | 21.88      | y_att=0.16, y_ali=0.77, y_f=2.49, d0_att=3.15, l_att=0.43, l_ali=1.90, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.51, y_acc=0.35, l_acc=0.10, d0_v=3.07 |
| 14   | -4915.5190   | 22.15      | y_att=0.16, y_ali=0.77, y_f=2.49, d0_att=3.15, l_att=0.43, l_ali=1.90, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.51, y_acc=0.35, l_acc=0.10, d0_v=3.07 |
| 15   | -4915.5190   | 22.09      | y_att=0.16, y_ali=0.77, y_f=2.49, d0_att=3.15, l_att=0.43, l_ali=1.90, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.51, y_acc=0.35, l_acc=0.10, d0_v=3.07 |
| 16   | -4915.5190   | 22.18      | y_att=0.16, y_ali=0.77, y_f=2.49, d0_att=3.15, l_att=0.43, l_ali=1.90, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.51, y_acc=0.35, l_acc=0.10, d0_v=3.07 |
| 17   | -4915.5190   | 24.16      | y_att=0.16, y_ali=0.77, y_f=2.49, d0_att=3.15, l_att=0.43, l_ali=1.90, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.51, y_acc=0.35, l_acc=0.10, d0_v=3.07 |
| 18   | -4915.5190   | 23.12      | y_att=0.16, y_ali=0.77, y_f=2.49, d0_att=3.15, l_att=0.43, l_ali=1.90, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.51, y_acc=0.35, l_acc=0.10, d0_v=3.07 |
| 19   | -4915.5190   | 23.65      | y_att=0.16, y_ali=0.77, y_f=2.49, d0_att=3.15, l_att=0.43, l_ali=1.90, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.51, y_acc=0.35, l_acc=0.10, d0_v=3.07 |

**End of experiment.**
