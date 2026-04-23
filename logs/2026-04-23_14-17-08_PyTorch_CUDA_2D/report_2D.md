# Experiment Report - PyTorch_CUDA (2D)
**Date:** 2026-04-23_14-17-08

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
| 00   | -4832.1401   | 15.07      | y_att=3.31, y_ali=2.69, y_f=1.69, d0_att=1.34, l_att=2.79, l_ali=2.00, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.44, y_acc=1.64, l_acc=0.78, d0_v=0.69 |
| 01   | -4832.1401   | 14.58      | y_att=3.31, y_ali=2.69, y_f=1.69, d0_att=1.34, l_att=2.79, l_ali=2.00, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.44, y_acc=1.64, l_acc=0.78, d0_v=0.69 |
| 02   | -7821.2490   | 14.69      | y_att=2.52, y_ali=3.41, y_f=2.26, d0_att=3.11, l_att=2.61, l_ali=1.60, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.83, y_acc=1.00, l_acc=0.14, d0_v=0.30 |
| 03   | -7821.2490   | 14.90      | y_att=2.52, y_ali=3.41, y_f=2.26, d0_att=3.11, l_att=2.61, l_ali=1.60, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.83, y_acc=1.00, l_acc=0.14, d0_v=0.30 |
| 04   | -7821.2490   | 15.07      | y_att=2.52, y_ali=3.41, y_f=2.26, d0_att=3.11, l_att=2.61, l_ali=1.60, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.83, y_acc=1.00, l_acc=0.14, d0_v=0.30 |
| 05   | -7821.2490   | 15.02      | y_att=2.52, y_ali=3.41, y_f=2.26, d0_att=3.11, l_att=2.61, l_ali=1.60, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.83, y_acc=1.00, l_acc=0.14, d0_v=0.30 |
| 06   | -7821.2490   | 15.33      | y_att=2.52, y_ali=3.41, y_f=2.26, d0_att=3.11, l_att=2.61, l_ali=1.60, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.83, y_acc=1.00, l_acc=0.14, d0_v=0.30 |
| 07   | -7821.2490   | 15.10      | y_att=2.52, y_ali=3.41, y_f=2.26, d0_att=3.11, l_att=2.61, l_ali=1.60, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.83, y_acc=1.00, l_acc=0.14, d0_v=0.30 |
| 08   | -7821.2490   | 15.10      | y_att=2.52, y_ali=3.41, y_f=2.26, d0_att=3.11, l_att=2.61, l_ali=1.60, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.83, y_acc=1.00, l_acc=0.14, d0_v=0.30 |
| 09   | -7821.2490   | 15.38      | y_att=2.52, y_ali=3.41, y_f=2.26, d0_att=3.11, l_att=2.61, l_ali=1.60, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.83, y_acc=1.00, l_acc=0.14, d0_v=0.30 |
| 10   | -7821.2490   | 15.18      | y_att=2.52, y_ali=3.41, y_f=2.26, d0_att=3.11, l_att=2.61, l_ali=1.60, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.83, y_acc=1.00, l_acc=0.14, d0_v=0.30 |
| 11   | -7821.2490   | 15.21      | y_att=2.52, y_ali=3.41, y_f=2.26, d0_att=3.11, l_att=2.61, l_ali=1.60, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.83, y_acc=1.00, l_acc=0.14, d0_v=0.30 |
| 12   | -7821.2490   | 15.21      | y_att=2.52, y_ali=3.41, y_f=2.26, d0_att=3.11, l_att=2.61, l_ali=1.60, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.83, y_acc=1.00, l_acc=0.14, d0_v=0.30 |
| 13   | -7821.2490   | 15.17      | y_att=2.52, y_ali=3.41, y_f=2.26, d0_att=3.11, l_att=2.61, l_ali=1.60, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.83, y_acc=1.00, l_acc=0.14, d0_v=0.30 |
| 14   | -7821.2490   | 15.38      | y_att=2.52, y_ali=3.41, y_f=2.26, d0_att=3.11, l_att=2.61, l_ali=1.60, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.83, y_acc=1.00, l_acc=0.14, d0_v=0.30 |
| 15   | -7821.2490   | 15.24      | y_att=2.52, y_ali=3.41, y_f=2.26, d0_att=3.11, l_att=2.61, l_ali=1.60, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.83, y_acc=1.00, l_acc=0.14, d0_v=0.30 |
| 16   | -7821.2490   | 15.33      | y_att=2.52, y_ali=3.41, y_f=2.26, d0_att=3.11, l_att=2.61, l_ali=1.60, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.83, y_acc=1.00, l_acc=0.14, d0_v=0.30 |
| 17   | -7821.2490   | 15.11      | y_att=2.52, y_ali=3.41, y_f=2.26, d0_att=3.11, l_att=2.61, l_ali=1.60, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.83, y_acc=1.00, l_acc=0.14, d0_v=0.30 |
| 18   | -7821.2490   | 14.55      | y_att=2.52, y_ali=3.41, y_f=2.26, d0_att=3.11, l_att=2.61, l_ali=1.60, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.83, y_acc=1.00, l_acc=0.14, d0_v=0.30 |
| 19   | -7821.2490   | 14.52      | y_att=2.52, y_ali=3.41, y_f=2.26, d0_att=3.11, l_att=2.61, l_ali=1.60, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.83, y_acc=1.00, l_acc=0.14, d0_v=0.30 |

**End of experiment.**
