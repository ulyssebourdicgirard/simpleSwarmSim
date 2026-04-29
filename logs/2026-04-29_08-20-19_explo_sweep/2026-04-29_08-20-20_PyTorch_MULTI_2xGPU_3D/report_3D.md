# Experiment Report - PyTorch_MULTI_2xGPU (3D)
**Date:** 2026-04-29_08-20-20

## 1. Initial Configuration
| Parameter | Value |
| :--- | :--- |
| ALPHA_LPF            | 0.2        |
| ARENA_RADIUS         | 100.0      |
| COLLISION_DIST       | 0.4        |
| DT                   | 0.1        |
| ENABLE_3D            | True       |
| EXPLO_STRATEGY       | local_gradient |
| FOV_FACTOR           | 0.9        |
| FULL_MILLING_MODE    | False      |
| GEN_CPU              | 20         |
| GEN_GPU              | 20         |
| GRID_RES             | 5.0        |
| MAP_STRATEGY         | global     |
| MAX_SPEED            | 20.0       |
| MAX_YAW_RATE         | 3.14       |
| MIN_SPAWN_DIST       | 2.0        |
| NB_DRONES            | 15         |
| NEIGHBORS            | 2          |
| N_INIT_CONDITIONS    | 4          |
| POP_SIZE_CPU         | 150        |
| POP_SIZE_GPU         | 5000       |
| REFRESH_MAP_TICKS    | 50         |
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
| 00   | -5058.0059   | 17.51      | y_att=0.31, y_ali=3.39, y_f=1.83, d0_att=4.69, l_att=10.20, l_ali=2.34, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.49, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.75, y_acc=0.38, l_acc=1.78, d0_v=0.76, y_explo=0.14 |
| 01   | -5058.0059   | 17.19      | y_att=0.31, y_ali=3.39, y_f=1.83, d0_att=4.69, l_att=10.20, l_ali=2.34, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.49, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.75, y_acc=0.38, l_acc=1.78, d0_v=0.76, y_explo=0.14 |
| 02   | -5058.0059   | 17.19      | y_att=0.31, y_ali=3.39, y_f=1.83, d0_att=4.69, l_att=10.20, l_ali=2.34, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.49, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.75, y_acc=0.38, l_acc=1.78, d0_v=0.76, y_explo=0.14 |
| 03   | -5287.3198   | 17.19      | y_att=1.58, y_ali=3.89, y_f=1.64, d0_att=7.87, l_att=7.34, l_ali=4.48, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.46, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=1.32, l_acc=0.72, d0_v=2.06, y_explo=0.25 |
| 04   | -5287.3198   | 17.20      | y_att=1.58, y_ali=3.89, y_f=1.64, d0_att=7.87, l_att=7.34, l_ali=4.48, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.46, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=1.32, l_acc=0.72, d0_v=2.06, y_explo=0.25 |
| 05   | -5287.3198   | 17.20      | y_att=1.58, y_ali=3.89, y_f=1.64, d0_att=7.87, l_att=7.34, l_ali=4.48, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.46, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=1.32, l_acc=0.72, d0_v=2.06, y_explo=0.25 |
| 06   | -5287.3198   | 17.21      | y_att=1.58, y_ali=3.89, y_f=1.64, d0_att=7.87, l_att=7.34, l_ali=4.48, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.46, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=1.32, l_acc=0.72, d0_v=2.06, y_explo=0.25 |
| 07   | -5287.3198   | 17.21      | y_att=1.58, y_ali=3.89, y_f=1.64, d0_att=7.87, l_att=7.34, l_ali=4.48, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.46, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=1.32, l_acc=0.72, d0_v=2.06, y_explo=0.25 |
| 08   | -5287.3198   | 17.22      | y_att=1.58, y_ali=3.89, y_f=1.64, d0_att=7.87, l_att=7.34, l_ali=4.48, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.46, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=1.32, l_acc=0.72, d0_v=2.06, y_explo=0.25 |
| 09   | -5287.3198   | 17.22      | y_att=1.58, y_ali=3.89, y_f=1.64, d0_att=7.87, l_att=7.34, l_ali=4.48, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.46, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=1.32, l_acc=0.72, d0_v=2.06, y_explo=0.25 |
| 10   | -5287.3198   | 17.22      | y_att=1.58, y_ali=3.89, y_f=1.64, d0_att=7.87, l_att=7.34, l_ali=4.48, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.46, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=1.32, l_acc=0.72, d0_v=2.06, y_explo=0.25 |
| 11   | -5287.3198   | 17.22      | y_att=1.58, y_ali=3.89, y_f=1.64, d0_att=7.87, l_att=7.34, l_ali=4.48, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.46, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=1.32, l_acc=0.72, d0_v=2.06, y_explo=0.25 |
| 12   | -5287.3198   | 17.22      | y_att=1.58, y_ali=3.89, y_f=1.64, d0_att=7.87, l_att=7.34, l_ali=4.48, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.46, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=1.32, l_acc=0.72, d0_v=2.06, y_explo=0.25 |
| 13   | -5287.3198   | 17.22      | y_att=1.58, y_ali=3.89, y_f=1.64, d0_att=7.87, l_att=7.34, l_ali=4.48, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.46, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=1.32, l_acc=0.72, d0_v=2.06, y_explo=0.25 |
| 14   | -5287.3198   | 17.22      | y_att=1.58, y_ali=3.89, y_f=1.64, d0_att=7.87, l_att=7.34, l_ali=4.48, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.46, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=1.32, l_acc=0.72, d0_v=2.06, y_explo=0.25 |
| 15   | -5287.3198   | 17.22      | y_att=1.58, y_ali=3.89, y_f=1.64, d0_att=7.87, l_att=7.34, l_ali=4.48, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.46, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=1.32, l_acc=0.72, d0_v=2.06, y_explo=0.25 |
| 16   | -5287.3198   | 17.22      | y_att=1.58, y_ali=3.89, y_f=1.64, d0_att=7.87, l_att=7.34, l_ali=4.48, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.46, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=1.32, l_acc=0.72, d0_v=2.06, y_explo=0.25 |
| 17   | -5287.3198   | 17.22      | y_att=1.58, y_ali=3.89, y_f=1.64, d0_att=7.87, l_att=7.34, l_ali=4.48, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.46, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=1.32, l_acc=0.72, d0_v=2.06, y_explo=0.25 |
| 18   | -5287.3198   | 17.22      | y_att=1.58, y_ali=3.89, y_f=1.64, d0_att=7.87, l_att=7.34, l_ali=4.48, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.46, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=1.32, l_acc=0.72, d0_v=2.06, y_explo=0.25 |
| 19   | -5287.3198   | 17.22      | y_att=1.58, y_ali=3.89, y_f=1.64, d0_att=7.87, l_att=7.34, l_ali=4.48, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.46, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=1.32, l_acc=0.72, d0_v=2.06, y_explo=0.25 |

**End of experiment.**
