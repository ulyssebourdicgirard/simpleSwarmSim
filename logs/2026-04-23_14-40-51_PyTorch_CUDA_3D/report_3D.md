# Experiment Report - PyTorch_CUDA (3D)
**Date:** 2026-04-23_14-40-51

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
| NB_DRONES            | 5          |
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
| W_EFFORT             | 1.0        |
| W_EXPLO              | -50.0      |
| W_MILL               | 0          |
| W_POL                | -0.0       |
| Z_MAX                | 10.0       |
| Z_MIN                | 1.0        |

## 2. Optimization Evolution
| Gen  |  Best Cost   |  Time (s)  |                                                                All Parameters                                                                |
| :--: | :----------: | :--------: | :------------------------------------------------------------------------------------------------------------------------------------------ |
| 00   | -219.8972    | 4.25       | y_att=0.89, y_ali=3.12, y_f=1.76, d0_att=3.04, l_att=1.07, l_ali=4.49, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.58, y_acc=0.31, l_acc=3.31, d0_v=2.60 |
| 01   | -234.1791    | 3.34       | y_att=0.72, y_ali=1.21, y_f=1.01, d0_att=3.01, l_att=1.71, l_ali=3.17, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.07, y_acc=2.49, l_acc=0.30, d0_v=2.51 |
| 02   | -234.1791    | 3.37       | y_att=0.72, y_ali=1.21, y_f=1.01, d0_att=3.01, l_att=1.71, l_ali=3.17, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.07, y_acc=2.49, l_acc=0.30, d0_v=2.51 |
| 03   | -236.3237    | 3.14       | y_att=0.90, y_ali=3.69, y_f=0.80, d0_att=3.09, l_att=1.10, l_ali=4.31, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.59, y_acc=0.29, l_acc=2.15, d0_v=2.13 |
| 04   | -236.3237    | 4.47       | y_att=0.90, y_ali=3.69, y_f=0.80, d0_att=3.09, l_att=1.10, l_ali=4.31, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.59, y_acc=0.29, l_acc=2.15, d0_v=2.13 |
| 05   | -273.0354    | 3.18       | y_att=0.39, y_ali=2.08, y_f=0.11, d0_att=1.07, l_att=1.07, l_ali=1.78, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.64, y_acc=0.53, l_acc=0.49, d0_v=2.87 |
| 06   | -273.0354    | 3.22       | y_att=0.39, y_ali=2.08, y_f=0.11, d0_att=1.07, l_att=1.07, l_ali=1.78, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.64, y_acc=0.53, l_acc=0.49, d0_v=2.87 |
| 07   | -273.0354    | 3.12       | y_att=0.39, y_ali=2.08, y_f=0.11, d0_att=1.07, l_att=1.07, l_ali=1.78, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.64, y_acc=0.53, l_acc=0.49, d0_v=2.87 |
| 08   | -273.0354    | 4.05       | y_att=0.39, y_ali=2.08, y_f=0.11, d0_att=1.07, l_att=1.07, l_ali=1.78, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.64, y_acc=0.53, l_acc=0.49, d0_v=2.87 |
| 09   | -273.0354    | 2.80       | y_att=0.39, y_ali=2.08, y_f=0.11, d0_att=1.07, l_att=1.07, l_ali=1.78, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.64, y_acc=0.53, l_acc=0.49, d0_v=2.87 |
| 10   | -273.0354    | 2.83       | y_att=0.39, y_ali=2.08, y_f=0.11, d0_att=1.07, l_att=1.07, l_ali=1.78, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.64, y_acc=0.53, l_acc=0.49, d0_v=2.87 |
| 11   | -273.0354    | 2.77       | y_att=0.39, y_ali=2.08, y_f=0.11, d0_att=1.07, l_att=1.07, l_ali=1.78, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.64, y_acc=0.53, l_acc=0.49, d0_v=2.87 |
| 12   | -273.0354    | 4.01       | y_att=0.39, y_ali=2.08, y_f=0.11, d0_att=1.07, l_att=1.07, l_ali=1.78, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.64, y_acc=0.53, l_acc=0.49, d0_v=2.87 |
| 13   | -273.0354    | 2.84       | y_att=0.39, y_ali=2.08, y_f=0.11, d0_att=1.07, l_att=1.07, l_ali=1.78, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.64, y_acc=0.53, l_acc=0.49, d0_v=2.87 |
| 14   | -273.0354    | 2.74       | y_att=0.39, y_ali=2.08, y_f=0.11, d0_att=1.07, l_att=1.07, l_ali=1.78, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.64, y_acc=0.53, l_acc=0.49, d0_v=2.87 |
| 15   | -281.8730    | 2.75       | y_att=0.40, y_ali=1.23, y_f=0.10, d0_att=2.14, l_att=0.56, l_ali=2.91, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.96, y_acc=0.15, l_acc=1.66, d0_v=3.16 |
| 16   | -281.8730    | 3.92       | y_att=0.40, y_ali=1.23, y_f=0.10, d0_att=2.14, l_att=0.56, l_ali=2.91, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.96, y_acc=0.15, l_acc=1.66, d0_v=3.16 |
| 17   | -281.8730    | 2.78       | y_att=0.40, y_ali=1.23, y_f=0.10, d0_att=2.14, l_att=0.56, l_ali=2.91, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.96, y_acc=0.15, l_acc=1.66, d0_v=3.16 |
| 18   | -281.8730    | 2.77       | y_att=0.40, y_ali=1.23, y_f=0.10, d0_att=2.14, l_att=0.56, l_ali=2.91, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.96, y_acc=0.15, l_acc=1.66, d0_v=3.16 |
| 19   | -281.8730    | 2.74       | y_att=0.40, y_ali=1.23, y_f=0.10, d0_att=2.14, l_att=0.56, l_ali=2.91, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.96, y_acc=0.15, l_acc=1.66, d0_v=3.16 |

**End of experiment.**
