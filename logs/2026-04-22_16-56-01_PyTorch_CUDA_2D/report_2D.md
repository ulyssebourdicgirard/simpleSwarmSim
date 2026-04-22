# Experiment Report - PyTorch_CUDA (2D)
**Date:** 2026-04-22_16-56-01

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
| NB_DRONES            | 10         |
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
| 00   | -34332.7578  | 2.34       | y_att=3.12, y_ali=2.52, y_f=2.00, d0_att=3.00, l_att=2.96, l_ali=3.35, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.13, y_acc=0.62, l_acc=1.74, d0_v=2.16 |
| 01   | -34756.9844  | 1.86       | y_att=2.67, y_ali=0.69, y_f=2.80, d0_att=1.22, l_att=3.05, l_ali=2.19, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.43, y_acc=1.95, l_acc=2.00, d0_v=1.82 |
| 02   | -34765.7930  | 1.80       | y_att=2.67, y_ali=0.56, y_f=2.80, d0_att=1.22, l_att=3.05, l_ali=2.19, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.43, y_acc=1.95, l_acc=2.00, d0_v=1.82 |
| 03   | -34901.4688  | 1.83       | y_att=4.70, y_ali=0.72, y_f=2.56, d0_att=1.32, l_att=1.98, l_ali=6.96, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.13, y_acc=1.36, l_acc=1.65, d0_v=1.93 |
| 04   | -35002.8086  | 1.80       | y_att=2.53, y_ali=2.79, y_f=3.44, d0_att=1.11, l_att=2.99, l_ali=6.10, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.55, y_acc=0.80, l_acc=1.35, d0_v=0.51 |
| 05   | -35250.6367  | 1.82       | y_att=3.00, y_ali=0.77, y_f=4.22, d0_att=1.22, l_att=3.11, l_ali=1.93, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.91, y_acc=1.95, l_acc=2.18, d0_v=1.82 |
| 06   | -35228.2969  | 1.88       | y_att=3.00, y_ali=0.77, y_f=4.22, d0_att=1.22, l_att=3.11, l_ali=1.93, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.03, y_acc=1.95, l_acc=2.18, d0_v=1.82 |
| 07   | -35271.8047  | 1.84       | y_att=4.57, y_ali=1.67, y_f=5.00, d0_att=2.45, l_att=3.87, l_ali=0.89, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.57, y_acc=1.48, l_acc=1.26, d0_v=0.69 |
| 08   | -35342.4766  | 1.84       | y_att=2.96, y_ali=0.73, y_f=5.26, d0_att=1.47, l_att=3.45, l_ali=2.61, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.93, y_acc=1.56, l_acc=2.23, d0_v=2.05 |
| 09   | -35573.5508  | 1.83       | y_att=2.75, y_ali=0.68, y_f=7.95, d0_att=0.78, l_att=3.50, l_ali=3.28, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.91, y_acc=2.70, l_acc=2.18, d0_v=1.35 |
| 10   | -35567.2734  | 1.80       | y_att=2.75, y_ali=0.68, y_f=7.95, d0_att=0.78, l_att=3.50, l_ali=3.28, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.91, y_acc=2.70, l_acc=2.18, d0_v=1.35 |
| 11   | -35587.4922  | 1.77       | y_att=2.75, y_ali=0.68, y_f=7.89, d0_att=0.78, l_att=3.50, l_ali=3.28, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.91, y_acc=2.70, l_acc=2.18, d0_v=1.35 |
| 12   | -35569.5664  | 1.79       | y_att=2.75, y_ali=0.68, y_f=7.95, d0_att=0.78, l_att=3.43, l_ali=3.93, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.91, y_acc=2.58, l_acc=2.18, d0_v=1.35 |
| 13   | -35593.7227  | 1.76       | y_att=8.38, y_ali=3.17, y_f=8.74, d0_att=1.68, l_att=3.03, l_ali=2.07, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=1.46, l_acc=2.52, d0_v=0.86 |
| 14   | -35629.5625  | 1.77       | y_att=3.43, y_ali=0.31, y_f=9.78, d0_att=1.53, l_att=4.30, l_ali=5.63, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.86, y_acc=1.50, l_acc=3.29, d0_v=1.63 |
| 15   | -35715.1367  | 1.75       | y_att=2.22, y_ali=1.03, y_f=13.37, d0_att=1.21, l_att=6.09, l_ali=1.32, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=1.96, l_acc=1.64, d0_v=0.41 |
| 16   | -35689.9961  | 1.76       | y_att=2.22, y_ali=1.03, y_f=13.37, d0_att=1.19, l_att=6.09, l_ali=1.32, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=1.96, l_acc=1.69, d0_v=0.41 |
| 17   | -35731.0391  | 1.75       | y_att=5.95, y_ali=3.33, y_f=12.58, d0_att=1.25, l_att=3.52, l_ali=3.77, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.98, l_acc=3.41, d0_v=0.64 |
| 18   | -35752.2344  | 1.76       | y_att=4.53, y_ali=2.75, y_f=12.50, d0_att=1.03, l_att=3.52, l_ali=2.52, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.86, y_acc=1.03, l_acc=3.41, d0_v=0.71 |
| 19   | -35766.6836  | 1.76       | y_att=2.65, y_ali=0.85, y_f=12.98, d0_att=0.61, l_att=3.83, l_ali=2.99, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.25, y_acc=1.97, l_acc=2.75, d0_v=0.92 |

**End of experiment.**
