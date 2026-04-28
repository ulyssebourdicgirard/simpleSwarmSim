# Experiment Report - PyTorch_MULTI_2xGPU (3D)
**Date:** 2026-04-28_08-44-12

## 1. Initial Configuration
| Parameter | Value |
| :--- | :--- |
| ALPHA_LPF            | 0.2        |
| ARENA_RADIUS         | 100.0      |
| COLLISION_DIST       | 0.4        |
| DT                   | 0.1        |
| ENABLE_3D            | True       |
| EXPLO_STRATEGY       | local_gradient |
| FOV_FACTOR           | 0.577      |
| FULL_MILLING_MODE    | False      |
| GEN_CPU              | 20         |
| GEN_GPU              | 20         |
| GRID_RES             | 5.0        |
| MAP_STRATEGY         | local_shared |
| MAX_SPEED            | 20.0       |
| MAX_YAW_RATE         | 3.14       |
| MIN_SPAWN_DIST       | 2.0        |
| NB_DRONES            | 10         |
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
| 00   | -1440.2814   | 15.79      | y_att=0.22, y_ali=3.84, y_f=0.88, d0_att=2.48, l_att=6.07, l_ali=3.66, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.36, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.98, y_acc=0.37, l_acc=0.94, d0_v=1.92, y_explo=0.11 |
| 01   | -1440.2814   | 15.41      | y_att=0.22, y_ali=3.84, y_f=0.88, d0_att=2.48, l_att=6.07, l_ali=3.66, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.36, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.98, y_acc=0.37, l_acc=0.94, d0_v=1.92, y_explo=0.11 |
| 02   | -1601.1306   | 15.41      | y_att=0.30, y_ali=0.45, y_f=0.63, d0_att=3.05, l_att=6.42, l_ali=1.41, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.72, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.40, y_acc=0.48, l_acc=0.50, d0_v=2.59, y_explo=8.18 |
| 03   | -1601.1306   | 15.42      | y_att=0.30, y_ali=0.45, y_f=0.63, d0_att=3.05, l_att=6.42, l_ali=1.41, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.72, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.40, y_acc=0.48, l_acc=0.50, d0_v=2.59, y_explo=8.18 |
| 04   | -1711.9458   | 15.42      | y_att=1.32, y_ali=0.51, y_f=1.19, d0_att=5.05, l_att=8.03, l_ali=3.47, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.23, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.00, y_acc=0.62, l_acc=1.66, d0_v=1.63, y_explo=7.46 |
| 05   | -1711.9458   | 15.42      | y_att=1.32, y_ali=0.51, y_f=1.19, d0_att=5.05, l_att=8.03, l_ali=3.47, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.23, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=1.00, y_acc=0.62, l_acc=1.66, d0_v=1.63, y_explo=7.46 |
| 06   | -1797.6481   | 15.42      | y_att=0.23, y_ali=0.07, y_f=1.38, d0_att=6.14, l_att=6.13, l_ali=3.73, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.71, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.15, y_acc=0.08, l_acc=1.43, d0_v=2.55, y_explo=10.28 |
| 07   | -1797.6481   | 15.42      | y_att=0.23, y_ali=0.07, y_f=1.38, d0_att=6.14, l_att=6.13, l_ali=3.73, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.71, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.15, y_acc=0.08, l_acc=1.43, d0_v=2.55, y_explo=10.28 |
| 08   | -1825.4880   | 15.43      | y_att=1.84, y_ali=0.44, y_f=0.64, d0_att=0.84, l_att=1.85, l_ali=5.28, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.81, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.04, l_acc=0.86, d0_v=1.86, y_explo=11.06 |
| 09   | -1825.4880   | 15.43      | y_att=1.84, y_ali=0.44, y_f=0.64, d0_att=0.84, l_att=1.85, l_ali=5.28, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.81, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.04, l_acc=0.86, d0_v=1.86, y_explo=11.06 |
| 10   | -1825.4880   | 15.43      | y_att=1.84, y_ali=0.44, y_f=0.64, d0_att=0.84, l_att=1.85, l_ali=5.28, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.81, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.04, l_acc=0.86, d0_v=1.86, y_explo=11.06 |
| 11   | -1825.4880   | 15.42      | y_att=1.84, y_ali=0.44, y_f=0.64, d0_att=0.84, l_att=1.85, l_ali=5.28, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.81, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.04, l_acc=0.86, d0_v=1.86, y_explo=11.06 |
| 12   | -1825.4880   | 15.43      | y_att=1.84, y_ali=0.44, y_f=0.64, d0_att=0.84, l_att=1.85, l_ali=5.28, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.81, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.04, l_acc=0.86, d0_v=1.86, y_explo=11.06 |
| 13   | -1825.4880   | 15.43      | y_att=1.84, y_ali=0.44, y_f=0.64, d0_att=0.84, l_att=1.85, l_ali=5.28, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.81, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.04, l_acc=0.86, d0_v=1.86, y_explo=11.06 |
| 14   | -1826.1477   | 15.42      | y_att=0.14, y_ali=2.18, y_f=0.55, d0_att=1.40, l_att=9.37, l_ali=2.60, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.16, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.02, l_acc=0.20, d0_v=2.28, y_explo=8.99 |
| 15   | -1826.1477   | 15.42      | y_att=0.14, y_ali=2.18, y_f=0.55, d0_att=1.40, l_att=9.37, l_ali=2.60, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.16, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.02, l_acc=0.20, d0_v=2.28, y_explo=8.99 |
| 16   | -1826.1477   | 15.42      | y_att=0.14, y_ali=2.18, y_f=0.55, d0_att=1.40, l_att=9.37, l_ali=2.60, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.16, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.02, l_acc=0.20, d0_v=2.28, y_explo=8.99 |
| 17   | -1826.1477   | 15.42      | y_att=0.14, y_ali=2.18, y_f=0.55, d0_att=1.40, l_att=9.37, l_ali=2.60, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.16, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.02, l_acc=0.20, d0_v=2.28, y_explo=8.99 |
| 18   | -1826.1477   | 15.42      | y_att=0.14, y_ali=2.18, y_f=0.55, d0_att=1.40, l_att=9.37, l_ali=2.60, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.16, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.02, l_acc=0.20, d0_v=2.28, y_explo=8.99 |
| 19   | -1826.1477   | 15.42      | y_att=0.14, y_ali=2.18, y_f=0.55, d0_att=1.40, l_att=9.37, l_ali=2.60, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.16, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.02, l_acc=0.20, d0_v=2.28, y_explo=8.99 |

**End of experiment.**
