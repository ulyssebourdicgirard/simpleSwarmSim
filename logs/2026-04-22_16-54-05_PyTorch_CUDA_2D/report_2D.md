# Experiment Report - PyTorch_CUDA (2D)
**Date:** 2026-04-22_16-54-05

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
| 00   | -4381.6914   | 2.21       | y_att=0.62, y_ali=1.13, y_f=1.81, d0_att=3.13, l_att=1.41, l_ali=3.41, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.01, y_acc=0.11, l_acc=1.66, d0_v=0.56 |
| 01   | -4865.8047   | 1.83       | y_att=0.97, y_ali=2.65, y_f=1.74, d0_att=3.37, l_att=1.19, l_ali=2.70, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.85, y_acc=0.52, l_acc=0.57, d0_v=0.81 |
| 02   | -6185.3750   | 1.88       | y_att=0.63, y_ali=1.12, y_f=1.85, d0_att=3.06, l_att=1.07, l_ali=1.79, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.89, y_acc=0.14, l_acc=3.23, d0_v=1.68 |
| 03   | -5879.6406   | 1.82       | y_att=1.20, y_ali=3.21, y_f=1.56, d0_att=3.96, l_att=0.83, l_ali=2.15, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.54, y_acc=0.71, l_acc=1.54, d0_v=2.39 |
| 04   | -6183.6016   | 1.93       | y_att=0.83, y_ali=3.68, y_f=1.55, d0_att=8.04, l_att=0.99, l_ali=4.81, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.18, y_acc=0.20, l_acc=2.10, d0_v=1.57 |
| 05   | -6263.0991   | 1.81       | y_att=0.30, y_ali=4.16, y_f=1.58, d0_att=3.16, l_att=1.78, l_ali=3.08, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.45, y_acc=0.20, l_acc=1.18, d0_v=2.84 |
| 06   | -7149.8682   | 1.85       | y_att=0.39, y_ali=0.93, y_f=2.22, d0_att=3.87, l_att=0.43, l_ali=1.74, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.29, y_acc=0.10, l_acc=3.27, d0_v=1.63 |
| 07   | -6596.7534   | 1.78       | y_att=1.95, y_ali=1.03, y_f=1.40, d0_att=2.95, l_att=0.55, l_ali=2.34, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.73, y_acc=0.09, l_acc=2.01, d0_v=2.05 |
| 08   | -6308.9956   | 1.81       | y_att=1.06, y_ali=1.07, y_f=0.87, d0_att=6.53, l_att=0.79, l_ali=4.99, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.37, y_acc=0.31, l_acc=1.28, d0_v=3.48 |
| 09   | -6746.9043   | 1.84       | y_att=0.54, y_ali=0.88, y_f=0.81, d0_att=3.00, l_att=0.83, l_ali=2.50, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.64, y_acc=0.08, l_acc=2.74, d0_v=2.67 |
| 10   | -6808.5610   | 1.89       | y_att=1.19, y_ali=1.32, y_f=0.88, d0_att=5.47, l_att=0.44, l_ali=4.10, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.21, l_acc=1.73, d0_v=2.60 |
| 11   | -7332.1377   | 2.10       | y_att=0.65, y_ali=1.19, y_f=0.35, d0_att=2.89, l_att=0.11, l_ali=2.14, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.86, y_acc=0.03, l_acc=1.58, d0_v=1.81 |
| 12   | -7438.5542   | 2.14       | y_att=0.18, y_ali=2.51, y_f=3.55, d0_att=2.66, l_att=0.64, l_ali=3.51, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.40, y_acc=0.53, l_acc=0.26, d0_v=2.33 |
| 13   | -7104.9434   | 1.71       | y_att=0.50, y_ali=0.77, y_f=0.58, d0_att=2.76, l_att=0.77, l_ali=2.39, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.36, y_acc=0.07, l_acc=0.15, d0_v=0.75 |
| 14   | -7127.4106   | 1.72       | y_att=0.55, y_ali=0.71, y_f=1.14, d0_att=8.54, l_att=0.26, l_ali=2.61, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.52, y_acc=0.20, l_acc=1.29, d0_v=2.09 |
| 15   | -7390.9009   | 1.69       | y_att=0.36, y_ali=1.00, y_f=1.14, d0_att=3.26, l_att=0.55, l_ali=1.78, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.79, y_acc=0.02, l_acc=2.49, d0_v=2.09 |
| 16   | -7124.8833   | 1.68       | y_att=0.57, y_ali=3.05, y_f=7.17, d0_att=6.07, l_att=0.11, l_ali=2.64, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.37, y_acc=0.07, l_acc=0.86, d0_v=3.93 |
| 17   | -6756.3408   | 1.75       | y_att=0.71, y_ali=0.71, y_f=0.44, d0_att=2.25, l_att=0.10, l_ali=2.11, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.57, y_acc=0.05, l_acc=3.81, d0_v=5.05 |
| 18   | -7622.3418   | 1.79       | y_att=0.55, y_ali=3.66, y_f=4.22, d0_att=6.24, l_att=0.15, l_ali=2.14, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.84, y_acc=0.10, l_acc=0.52, d0_v=4.38 |
| 19   | -7259.3018   | 1.69       | y_att=0.41, y_ali=1.28, y_f=0.75, d0_att=4.45, l_att=0.28, l_ali=1.52, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.04, l_acc=2.79, d0_v=1.87 |

**End of experiment.**
