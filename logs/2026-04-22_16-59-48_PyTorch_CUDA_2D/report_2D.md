# Experiment Report - PyTorch_CUDA (2D)
**Date:** 2026-04-22_16-59-48

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
| NB_DRONES            | 20         |
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
| 00   | -3312.8845   | 2.14       | y_att=1.16, y_ali=0.43, y_f=1.87, d0_att=2.39, l_att=1.77, l_ali=4.22, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.57, y_acc=0.50, l_acc=1.28, d0_v=1.18 |
| 01   | -3991.0017   | 1.77       | y_att=1.02, y_ali=1.72, y_f=1.78, d0_att=3.39, l_att=2.42, l_ali=3.83, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.28, y_acc=0.13, l_acc=1.29, d0_v=1.28 |
| 02   | -3798.5796   | 1.72       | y_att=2.34, y_ali=1.29, y_f=1.36, d0_att=4.99, l_att=1.24, l_ali=2.63, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.77, y_acc=0.39, l_acc=0.82, d0_v=2.46 |
| 03   | -4060.0046   | 1.82       | y_att=0.85, y_ali=1.72, y_f=2.70, d0_att=2.15, l_att=1.03, l_ali=5.22, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.83, y_acc=0.27, l_acc=0.47, d0_v=2.04 |
| 04   | -4140.2725   | 1.74       | y_att=1.02, y_ali=1.06, y_f=1.58, d0_att=5.07, l_att=2.42, l_ali=4.71, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.28, y_acc=0.13, l_acc=1.65, d0_v=1.87 |
| 05   | -4314.4473   | 1.71       | y_att=0.85, y_ali=2.51, y_f=2.37, d0_att=1.77, l_att=1.03, l_ali=5.19, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.76, y_acc=0.26, l_acc=0.31, d0_v=2.48 |
| 06   | -4384.3516   | 1.71       | y_att=1.79, y_ali=0.18, y_f=2.45, d0_att=3.78, l_att=0.77, l_ali=4.00, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.14, y_acc=0.18, l_acc=0.83, d0_v=1.71 |
| 07   | -4366.6299   | 1.74       | y_att=1.98, y_ali=3.57, y_f=1.98, d0_att=3.36, l_att=0.47, l_ali=1.28, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.99, y_acc=0.14, l_acc=2.16, d0_v=1.78 |
| 08   | -4512.9380   | 1.77       | y_att=2.34, y_ali=1.18, y_f=1.22, d0_att=4.43, l_att=1.10, l_ali=1.99, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.29, y_acc=0.29, l_acc=0.46, d0_v=2.64 |
| 09   | -4652.7402   | 1.72       | y_att=0.27, y_ali=0.48, y_f=1.03, d0_att=3.69, l_att=1.11, l_ali=1.69, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.80, y_acc=0.12, l_acc=0.20, d0_v=1.02 |
| 10   | -4346.8003   | 1.72       | y_att=0.30, y_ali=0.38, y_f=1.03, d0_att=2.83, l_att=1.30, l_ali=4.38, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.80, y_acc=0.08, l_acc=0.24, d0_v=1.02 |
| 11   | -4316.6587   | 1.72       | y_att=0.55, y_ali=1.72, y_f=3.01, d0_att=1.82, l_att=0.76, l_ali=6.96, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.14, y_acc=0.30, l_acc=0.23, d0_v=2.48 |
| 12   | -4640.9282   | 1.71       | y_att=0.39, y_ali=2.04, y_f=1.18, d0_att=2.37, l_att=1.02, l_ali=3.06, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.79, y_acc=0.08, l_acc=1.74, d0_v=5.59 |
| 13   | -4498.8535   | 1.71       | y_att=1.85, y_ali=2.59, y_f=2.06, d0_att=1.47, l_att=0.77, l_ali=1.48, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.12, l_acc=1.97, d0_v=3.61 |
| 14   | -4531.2280   | 1.76       | y_att=0.66, y_ali=1.52, y_f=2.45, d0_att=2.19, l_att=0.52, l_ali=5.22, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.87, y_acc=0.12, l_acc=0.38, d0_v=1.56 |
| 15   | -4689.3071   | 1.76       | y_att=0.82, y_ali=1.25, y_f=2.04, d0_att=1.72, l_att=0.54, l_ali=4.17, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.14, y_acc=0.34, l_acc=0.12, d0_v=1.82 |
| 16   | -4410.4751   | 1.75       | y_att=1.69, y_ali=6.08, y_f=2.12, d0_att=1.45, l_att=0.84, l_ali=3.23, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.10, l_acc=2.94, d0_v=2.76 |
| 17   | -4404.0762   | 1.75       | y_att=0.47, y_ali=1.38, y_f=3.16, d0_att=1.88, l_att=1.19, l_ali=2.95, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.88, y_acc=0.41, l_acc=0.84, d0_v=5.91 |
| 18   | -4661.1836   | 1.75       | y_att=0.39, y_ali=1.72, y_f=0.94, d0_att=7.27, l_att=1.24, l_ali=0.74, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.53, y_acc=0.10, l_acc=0.38, d0_v=1.88 |
| 19   | -4659.4824   | 1.75       | y_att=0.55, y_ali=1.71, y_f=2.74, d0_att=2.19, l_att=0.98, l_ali=3.34, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.00, y_acc=0.10, l_acc=0.62, d0_v=1.67 |

**End of experiment.**
