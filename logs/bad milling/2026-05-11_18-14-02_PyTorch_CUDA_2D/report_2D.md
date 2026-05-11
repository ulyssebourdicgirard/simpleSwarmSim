# Experiment Report - PyTorch_CUDA (2D)
**Date:** 2026-05-11_18-14-02

## 1. Initial Configuration
| Parameter | Value |
| :--- | :--- |
| ALPHA_LPF            | 0.2        |
| ARENA_RADIUS         | 50.0       |
| COLLISION_DIST       | 0.4        |
| DT                   | 0.1        |
| ENABLE_3D            | False      |
| EXPLO_STRATEGY       | global_best |
| FOV_FACTOR           | 0.9        |
| FULL_MILLING_MODE    | True       |
| GEN_CPU              | 20         |
| GEN_GPU              | 20         |
| GRID_RES             | 5.0        |
| MAP_STRATEGY         | local_shared |
| MAX_SPEED            | 20.0       |
| MAX_YAW_RATE         | 3.14       |
| MIN_SPAWN_DIST       | 2.0        |
| NB_DRONES            | 5          |
| NEIGHBORS            | 2          |
| N_INIT_CONDITIONS    | 4          |
| POP_SIZE_CPU         | 150        |
| POP_SIZE_GPU         | 5000       |
| REFRESH_MAP_TICKS    | 100        |
| SCENARIO             | default    |
| SIM_STEPS            | 3000       |
| SPOIL_ADD            | 0.02       |
| SPOIL_MULT           | 1.002      |
| VISU_STEPS           | 6000       |
| W_COLL               | 500.0      |
| W_DISP               | 10.0       |
| W_EFFORT             | 0.3        |
| W_EXPLO              | 0.0        |
| W_MILL               | -600.0     |
| W_POL                | 250.0      |
| W_STATIONARY         | 400        |
| Z_MAX                | 10.0       |
| Z_MIN                | 1.0        |

## 2. Optimization Evolution
| Gen  |  Best Cost   |  Time (s)  |                                                                All Parameters                                                                |
| :--: | :----------: | :--------: | :------------------------------------------------------------------------------------------------------------------------------------------ |
| 00   | 1072845.8750 | 12.34      | y_att=0.61, y_ali=3.03, y_f=1.97, d0_att=2.99, l_att=1.02, l_ali=4.63, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.87, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.39, y_acc=0.17, l_acc=2.34, d0_v=2.77, y_explo=4.94 |
| 01   | 155303.4219  | 11.06      | y_att=0.16, y_ali=3.23, y_f=0.82, d0_att=6.48, l_att=1.94, l_ali=4.53, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.80, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.02, l_acc=1.27, d0_v=1.27, y_explo=2.31 |
| 02   | -120664.5938 | 11.68      | y_att=0.23, y_ali=3.01, y_f=1.90, d0_att=1.02, l_att=0.51, l_ali=5.93, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.96, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.42, y_acc=0.39, l_acc=0.62, d0_v=2.07, y_explo=0.76 |
| 03   | -416374.1875 | 11.25      | y_att=0.94, y_ali=0.17, y_f=1.70, d0_att=2.91, l_att=0.35, l_ali=6.52, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=0.56, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.40, y_acc=0.00, l_acc=0.78, d0_v=1.61, y_explo=1.98 |
| 04   | -446110.4062 | 11.45      | y_att=0.31, y_ali=1.22, y_f=1.46, d0_att=1.71, l_att=0.33, l_ali=4.59, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.98, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.57, y_acc=0.01, l_acc=0.84, d0_v=1.56, y_explo=4.92 |
| 05   | -446110.4062 | 10.87      | y_att=0.31, y_ali=1.22, y_f=1.46, d0_att=1.71, l_att=0.33, l_ali=4.59, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.98, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.57, y_acc=0.01, l_acc=0.84, d0_v=1.56, y_explo=4.92 |
| 06   | -471161.1562 | 11.38      | y_att=0.22, y_ali=2.81, y_f=4.17, d0_att=5.21, l_att=0.36, l_ali=9.15, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.46, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.05, y_acc=0.06, l_acc=1.89, d0_v=2.76, y_explo=0.16 |
| 07   | -486135.2500 | 11.24      | y_att=1.39, y_ali=3.08, y_f=1.95, d0_att=2.21, l_att=0.29, l_ali=11.52, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.53, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.63, y_acc=0.01, l_acc=1.04, d0_v=2.22, y_explo=5.04 |
| 08   | -943728.7500 | 11.12      | y_att=0.10, y_ali=0.93, y_f=2.99, d0_att=5.48, l_att=0.96, l_ali=26.84, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.92, y_acc=0.19, l_acc=0.33, d0_v=1.17, y_explo=3.32 |
| 09   | -1033217.6250 | 11.36      | y_att=0.10, y_ali=0.93, y_f=2.99, d0_att=5.48, l_att=0.96, l_ali=26.84, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.77, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.92, y_acc=0.19, l_acc=0.33, d0_v=1.17, y_explo=3.32 |
| 10   | -1033217.6250 | 11.10      | y_att=0.10, y_ali=0.93, y_f=2.99, d0_att=5.48, l_att=0.96, l_ali=26.84, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.77, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.92, y_acc=0.19, l_acc=0.33, d0_v=1.17, y_explo=3.32 |
| 11   | -1033217.6250 | 13.09      | y_att=0.10, y_ali=0.93, y_f=2.99, d0_att=5.48, l_att=0.96, l_ali=26.84, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.77, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.92, y_acc=0.19, l_acc=0.33, d0_v=1.17, y_explo=3.32 |
| 12   | -1073064.5000 | 12.78      | y_att=0.37, y_ali=0.93, y_f=2.99, d0_att=11.10, l_att=0.45, l_ali=26.84, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.66, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.53, y_acc=0.15, l_acc=0.77, d0_v=1.21, y_explo=3.32 |
| 13   | -1073064.5000 | 13.16      | y_att=0.37, y_ali=0.93, y_f=2.99, d0_att=11.10, l_att=0.45, l_ali=26.84, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.66, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=4.53, y_acc=0.15, l_acc=0.77, d0_v=1.21, y_explo=3.32 |
| 14   | -1075622.3750 | 11.48      | y_att=0.14, y_ali=0.55, y_f=2.99, d0_att=1.99, l_att=0.45, l_ali=30.84, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.12, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.04, y_acc=0.15, l_acc=0.77, d0_v=1.26, y_explo=3.16 |
| 15   | -1075622.3750 | 12.53      | y_att=0.14, y_ali=0.55, y_f=2.99, d0_att=1.99, l_att=0.45, l_ali=30.84, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.12, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.04, y_acc=0.15, l_acc=0.77, d0_v=1.26, y_explo=3.16 |
| 16   | -1075622.3750 | 13.05      | y_att=0.14, y_ali=0.55, y_f=2.99, d0_att=1.99, l_att=0.45, l_ali=30.84, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.12, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.04, y_acc=0.15, l_acc=0.77, d0_v=1.26, y_explo=3.16 |
| 17   | -1075622.3750 | 13.21      | y_att=0.14, y_ali=0.55, y_f=2.99, d0_att=1.99, l_att=0.45, l_ali=30.84, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.12, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.04, y_acc=0.15, l_acc=0.77, d0_v=1.26, y_explo=3.16 |
| 18   | -1075622.3750 | 13.17      | y_att=0.14, y_ali=0.55, y_f=2.99, d0_att=1.99, l_att=0.45, l_ali=30.84, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.12, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.04, y_acc=0.15, l_acc=0.77, d0_v=1.26, y_explo=3.16 |
| 19   | -1075622.3750 | 13.18      | y_att=0.14, y_ali=0.55, y_f=2.99, d0_att=1.99, l_att=0.45, l_ali=30.84, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.12, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=6.04, y_acc=0.15, l_acc=0.77, d0_v=1.26, y_explo=3.16 |

**End of experiment.**
