# Experiment Report - PyTorch_MULTI_2xGPU (3D)
**Date:** 2026-04-29_09-01-44

## 1. Initial Configuration
| Parameter | Value |
| :--- | :--- |
| ALPHA_LPF            | 0.2        |
| ARENA_RADIUS         | 100.0      |
| COLLISION_DIST       | 0.4        |
| DT                   | 0.1        |
| ENABLE_3D            | True       |
| EXPLO_STRATEGY       | global_closest |
| FOV_FACTOR           | 0.9        |
| FULL_MILLING_MODE    | False      |
| GEN_CPU              | 20         |
| GEN_GPU              | 20         |
| GRID_RES             | 5.0        |
| MAP_STRATEGY         | local_shared |
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
| 00   | -4350.3301   | 23.81      | y_att=1.09, y_ali=1.90, y_f=1.38, d0_att=3.74, l_att=1.06, l_ali=2.03, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.33, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.37, y_acc=1.09, l_acc=1.34, d0_v=2.04, y_explo=0.19 |
| 01   | -4622.1226   | 23.44      | y_att=3.25, y_ali=1.94, y_f=0.75, d0_att=3.92, l_att=3.53, l_ali=2.18, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.44, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.80, y_acc=0.16, l_acc=2.45, d0_v=2.92, y_explo=0.77 |
| 02   | -4622.1226   | 23.45      | y_att=3.25, y_ali=1.94, y_f=0.75, d0_att=3.92, l_att=3.53, l_ali=2.18, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.44, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.80, y_acc=0.16, l_acc=2.45, d0_v=2.92, y_explo=0.77 |
| 03   | -4628.2764   | 23.45      | y_att=1.32, y_ali=1.17, y_f=1.19, d0_att=1.52, l_att=3.44, l_ali=3.89, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.84, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.97, y_acc=0.17, l_acc=0.76, d0_v=0.49, y_explo=0.10 |
| 04   | -4736.0142   | 23.45      | y_att=1.32, y_ali=1.17, y_f=1.19, d0_att=1.52, l_att=3.44, l_ali=3.89, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.52, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.97, y_acc=0.17, l_acc=0.76, d0_v=0.49, y_explo=0.10 |
| 05   | -4736.0142   | 23.45      | y_att=1.32, y_ali=1.17, y_f=1.19, d0_att=1.52, l_att=3.44, l_ali=3.89, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.52, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.97, y_acc=0.17, l_acc=0.76, d0_v=0.49, y_explo=0.10 |
| 06   | -4786.4648   | 23.45      | y_att=1.91, y_ali=4.42, y_f=0.81, d0_att=3.56, l_att=2.76, l_ali=2.32, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.19, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.84, y_acc=0.08, l_acc=1.43, d0_v=2.45, y_explo=0.11 |
| 07   | -4794.3062   | 23.45      | y_att=4.35, y_ali=2.07, y_f=1.13, d0_att=1.44, l_att=1.47, l_ali=3.06, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.67, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.17, l_acc=1.30, d0_v=1.95, y_explo=0.11 |
| 08   | -4857.6191   | 23.45      | y_att=0.36, y_ali=5.64, y_f=0.75, d0_att=1.28, l_att=5.31, l_ali=2.69, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.05, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.26, l_acc=1.79, d0_v=1.75, y_explo=0.13 |
| 09   | -4857.6191   | 23.45      | y_att=0.36, y_ali=5.64, y_f=0.75, d0_att=1.28, l_att=5.31, l_ali=2.69, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.05, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.26, l_acc=1.79, d0_v=1.75, y_explo=0.13 |
| 10   | -4857.6191   | 23.44      | y_att=0.36, y_ali=5.64, y_f=0.75, d0_att=1.28, l_att=5.31, l_ali=2.69, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.05, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.26, l_acc=1.79, d0_v=1.75, y_explo=0.13 |
| 11   | -4880.2554   | 23.44      | y_att=3.29, y_ali=0.08, y_f=1.34, d0_att=2.26, l_att=2.07, l_ali=2.92, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.90, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.13, l_acc=3.70, d0_v=3.27, y_explo=0.10 |
| 12   | -4880.2554   | 23.44      | y_att=3.29, y_ali=0.08, y_f=1.34, d0_att=2.26, l_att=2.07, l_ali=2.92, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=2.90, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.13, l_acc=3.70, d0_v=3.27, y_explo=0.10 |
| 13   | -4966.2310   | 23.44      | y_att=0.58, y_ali=6.07, y_f=0.65, d0_att=0.51, l_att=1.67, l_ali=0.40, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.70, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.68, l_acc=0.57, d0_v=3.79, y_explo=0.12 |
| 14   | -4966.2310   | 23.44      | y_att=0.58, y_ali=6.07, y_f=0.65, d0_att=0.51, l_att=1.67, l_ali=0.40, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.70, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.68, l_acc=0.57, d0_v=3.79, y_explo=0.12 |
| 15   | -4966.2310   | 23.44      | y_att=0.58, y_ali=6.07, y_f=0.65, d0_att=0.51, l_att=1.67, l_ali=0.40, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.70, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.68, l_acc=0.57, d0_v=3.79, y_explo=0.12 |
| 16   | -4966.2310   | 23.44      | y_att=0.58, y_ali=6.07, y_f=0.65, d0_att=0.51, l_att=1.67, l_ali=0.40, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.70, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.68, l_acc=0.57, d0_v=3.79, y_explo=0.12 |
| 17   | -4966.2310   | 23.44      | y_att=0.58, y_ali=6.07, y_f=0.65, d0_att=0.51, l_att=1.67, l_ali=0.40, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.70, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.68, l_acc=0.57, d0_v=3.79, y_explo=0.12 |
| 18   | -4966.2310   | 23.44      | y_att=0.58, y_ali=6.07, y_f=0.65, d0_att=0.51, l_att=1.67, l_ali=0.40, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.70, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.68, l_acc=0.57, d0_v=3.79, y_explo=0.12 |
| 19   | -4966.2310   | 23.44      | y_att=0.58, y_ali=6.07, y_f=0.65, d0_att=0.51, l_att=1.67, l_ali=0.40, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.70, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=10.00, y_acc=0.68, l_acc=0.57, d0_v=3.79, y_explo=0.12 |

**End of experiment.**
