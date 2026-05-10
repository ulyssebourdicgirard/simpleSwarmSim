# Experiment Report - PyTorch_MULTI_2xGPU (3D)
**Date:** 2026-05-10_09-35-15

## 1. Initial Configuration
| Parameter | Value |
| :--- | :--- |
| ALPHA_LPF            | 0.2        |
| ARENA_RADIUS         | 50.0       |
| COLLISION_DIST       | 0.4        |
| DT                   | 0.1        |
| ENABLE_3D            | True       |
| EXPLO_STRATEGY       | local_gradient |
| FOV_FACTOR           | 0.9        |
| FULL_MILLING_MODE    | False      |
| GEN_CPU              | 20         |
| GEN_GPU              | 20         |
| GRID_RES             | 5.0        |
| MAP_STRATEGY         | local_individual |
| MAX_SPEED            | 20.0       |
| MAX_YAW_RATE         | 3.14       |
| MIN_SPAWN_DIST       | 2.0        |
| NB_DRONES            | 10         |
| NEIGHBORS            | 2          |
| N_INIT_CONDITIONS    | 4          |
| POP_SIZE_CPU         | 150        |
| POP_SIZE_GPU         | 5000       |
| REFRESH_MAP_TICKS    | 100        |
| SCENARIO             | exploration |
| SIM_STEPS            | 3000       |
| SPOIL_ADD            | 0.02       |
| SPOIL_MULT           | 1.002      |
| VISU_STEPS           | 6000       |
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
| 00   | -120900.8828 | 30.54      | y_att=0.05, y_ali=0.05, y_f=0.00, d0_att=5.23, l_att=9.36, l_ali=1.29, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.37, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.17, y_acc=0.79, l_acc=3.31, d0_v=1.33, y_explo=0.33 |
| 01   | -128540.8906 | 30.27      | y_att=3.17, y_ali=1.27, y_f=0.31, d0_att=0.91, l_att=2.75, l_ali=3.56, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.87, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.24, y_acc=0.44, l_acc=1.04, d0_v=1.38, y_explo=0.86 |
| 02   | -128540.8906 | 30.29      | y_att=3.17, y_ali=1.27, y_f=0.31, d0_att=0.91, l_att=2.75, l_ali=3.56, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.87, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.24, y_acc=0.44, l_acc=1.04, d0_v=1.38, y_explo=0.86 |
| 03   | -128612.2891 | 30.32      | y_att=3.33, y_ali=0.93, y_f=0.31, d0_att=1.01, l_att=2.75, l_ali=3.56, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.73, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.24, y_acc=0.44, l_acc=1.04, d0_v=1.38, y_explo=0.71 |
| 04   | -128612.2891 | 30.29      | y_att=3.33, y_ali=0.93, y_f=0.31, d0_att=1.01, l_att=2.75, l_ali=3.56, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.73, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.24, y_acc=0.44, l_acc=1.04, d0_v=1.38, y_explo=0.71 |
| 05   | -128751.8203 | 30.29      | y_att=0.64, y_ali=0.16, y_f=0.31, d0_att=0.56, l_att=3.72, l_ali=3.10, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.47, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.85, y_acc=0.70, l_acc=0.50, d0_v=2.64, y_explo=1.20 |
| 06   | -132358.0312 | 30.28      | y_att=0.67, y_ali=0.16, y_f=1.29, d0_att=0.50, l_att=2.58, l_ali=1.81, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.59, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.75, y_acc=0.35, l_acc=1.56, d0_v=2.64, y_explo=0.55 |
| 07   | -132481.0938 | 30.28      | y_att=0.80, y_ali=0.16, y_f=0.34, d0_att=0.56, l_att=1.90, l_ali=3.70, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.27, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=1.14, l_acc=0.29, d0_v=4.21, y_explo=0.92 |
| 08   | -132809.6719 | 30.29      | y_att=1.64, y_ali=0.95, y_f=1.59, d0_att=0.71, l_att=2.75, l_ali=2.89, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.57, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.36, l_acc=1.23, d0_v=0.91, y_explo=0.21 |
| 09   | -134523.5469 | 30.28      | y_att=1.25, y_ali=0.93, y_f=0.10, d0_att=0.78, l_att=3.66, l_ali=5.42, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.94, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.82, y_acc=1.91, l_acc=0.84, d0_v=1.67, y_explo=0.13 |
| 10   | -134523.5469 | 30.29      | y_att=1.25, y_ali=0.93, y_f=0.10, d0_att=0.78, l_att=3.66, l_ali=5.42, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.94, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.82, y_acc=1.91, l_acc=0.84, d0_v=1.67, y_explo=0.13 |
| 11   | -135388.0469 | 30.28      | y_att=2.67, y_ali=2.03, y_f=0.80, d0_att=0.50, l_att=1.19, l_ali=1.86, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.81, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=9.78, y_acc=0.55, l_acc=0.59, d0_v=1.15, y_explo=0.19 |
| 12   | -136565.8906 | 30.28      | y_att=0.64, y_ali=0.10, y_f=0.10, d0_att=1.44, l_att=5.60, l_ali=1.77, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.93, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.78, l_acc=1.63, d0_v=1.73, y_explo=0.12 |
| 13   | -136565.8906 | 30.28      | y_att=0.64, y_ali=0.10, y_f=0.10, d0_att=1.44, l_att=5.60, l_ali=1.77, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.93, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.78, l_acc=1.63, d0_v=1.73, y_explo=0.12 |
| 14   | -136565.8906 | 30.27      | y_att=0.64, y_ali=0.10, y_f=0.10, d0_att=1.44, l_att=5.60, l_ali=1.77, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.93, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.78, l_acc=1.63, d0_v=1.73, y_explo=0.12 |
| 15   | -136565.8906 | 30.28      | y_att=0.64, y_ali=0.10, y_f=0.10, d0_att=1.44, l_att=5.60, l_ali=1.77, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.93, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.78, l_acc=1.63, d0_v=1.73, y_explo=0.12 |
| 16   | -136565.8906 | 30.25      | y_att=0.64, y_ali=0.10, y_f=0.10, d0_att=1.44, l_att=5.60, l_ali=1.77, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.93, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.78, l_acc=1.63, d0_v=1.73, y_explo=0.12 |
| 17   | -136565.8906 | 30.27      | y_att=0.64, y_ali=0.10, y_f=0.10, d0_att=1.44, l_att=5.60, l_ali=1.77, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.93, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.78, l_acc=1.63, d0_v=1.73, y_explo=0.12 |
| 18   | -136565.8906 | 30.25      | y_att=0.64, y_ali=0.10, y_f=0.10, d0_att=1.44, l_att=5.60, l_ali=1.77, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.93, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.78, l_acc=1.63, d0_v=1.73, y_explo=0.12 |
| 19   | -136565.8906 | 30.25      | y_att=0.64, y_ali=0.10, y_f=0.10, d0_att=1.44, l_att=5.60, l_ali=1.77, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.93, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.78, l_acc=1.63, d0_v=1.73, y_explo=0.12 |

**End of experiment.**
