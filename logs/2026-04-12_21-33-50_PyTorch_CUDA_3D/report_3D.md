# Experiment Report - PyTorch_CUDA (3D)
**Date:** 2026-04-12_21-33-50

## 1. Initial Configuration
| Parameter | Value |
| :--- | :--- |
| ALPHA_LPF            | 0.2        |
| ARENA_RADIUS         | 100.0      |
| COLLISION_DIST       | 0.4        |
| DT                   | 0.01       |
| ENABLE_3D            | True       |
| GEN_CPU              | 20         |
| GEN_GPU              | 20         |
| GRID_RES             | 5.0        |
| MAX_SPEED            | 20.0       |
| MAX_YAW_RATE         | 3.14       |
| NB_DRONES            | 20         |
| NEIGHBORS            | 3          |
| POP_SIZE_CPU         | 150        |
| POP_SIZE_GPU         | 5000       |
| SCENARIO             | exploration |
| SIM_STEPS            | 500        |
| SPOIL_ADD            | 0.05       |
| SPOIL_MULT           | 1.01       |
| VISU_STEPS           | 1000       |
| W_COLL               | 500.0      |
| W_DISP               | 0.0        |
| W_EFFORT             | 1          |
| W_EXPLO              | -50.0      |
| W_MILL               | 20.0       |
| W_POL                | -0.0       |
| Z_MAX                | 10.0       |
| Z_MIN                | 1.0        |

## 2. Optimization Evolution
| Gen  |  Best Cost   |  Time (s)  |                                                                All Parameters                                                                |
| :--: | :----------: | :--------: | :------------------------------------------------------------------------------------------------------------------------------------------ |
| 00   | -692.3864    | 3.38       | y_att=2.65, y_ali=1.61, y_f=1.68, d0_att=1.16, l_att=4.45, l_ali=4.76, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.38, y_acc=1.76, l_acc=3.75, d0_v=0.53 |
| 01   | -708.6057    | 4.37       | y_att=2.65, y_ali=1.61, y_f=1.68, d0_att=1.16, l_att=4.45, l_ali=4.76, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.38, y_acc=1.76, l_acc=3.75, d0_v=0.53 |
| 02   | -747.6952    | 3.29       | y_att=2.65, y_ali=1.87, y_f=1.68, d0_att=1.16, l_att=4.45, l_ali=4.76, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.93, y_acc=1.76, l_acc=3.75, d0_v=0.51 |
| 03   | -797.4830    | 3.30       | y_att=2.65, y_ali=1.87, y_f=1.68, d0_att=1.13, l_att=4.45, l_ali=3.94, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.93, y_acc=1.76, l_acc=3.75, d0_v=0.51 |
| 04   | -819.8652    | 3.25       | y_att=4.64, y_ali=2.21, y_f=1.86, d0_att=1.26, l_att=3.54, l_ali=1.13, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=8.45, y_acc=2.43, l_acc=5.29, d0_v=0.89 |
| 05   | -836.8961    | 4.33       | y_att=2.65, y_ali=2.07, y_f=1.68, d0_att=1.25, l_att=4.45, l_ali=6.03, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.93, y_acc=1.76, l_acc=3.75, d0_v=0.51 |
| 06   | -875.3926    | 3.18       | y_att=2.38, y_ali=2.36, y_f=2.03, d0_att=1.36, l_att=5.37, l_ali=2.40, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.83, y_acc=1.76, l_acc=4.24, d0_v=0.48 |
| 07   | -850.1161    | 3.11       | y_att=2.38, y_ali=2.36, y_f=2.03, d0_att=1.36, l_att=5.37, l_ali=2.40, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.83, y_acc=1.76, l_acc=4.24, d0_v=0.48 |
| 08   | -875.7484    | 3.44       | y_att=3.36, y_ali=2.20, y_f=1.96, d0_att=1.50, l_att=4.71, l_ali=4.76, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.59, y_acc=1.76, l_acc=4.75, d0_v=0.54 |
| 09   | -864.1686    | 4.34       | y_att=3.30, y_ali=1.73, y_f=1.71, d0_att=1.16, l_att=4.21, l_ali=5.33, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.25, y_acc=2.08, l_acc=4.04, d0_v=0.61 |
| 10   | -882.6981    | 3.34       | y_att=2.63, y_ali=1.61, y_f=1.96, d0_att=0.97, l_att=4.46, l_ali=8.15, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=5.85, y_acc=1.41, l_acc=4.84, d0_v=0.44 |
| 11   | -891.9349    | 3.36       | y_att=3.58, y_ali=1.36, y_f=2.16, d0_att=1.32, l_att=4.67, l_ali=12.22, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.76, y_acc=1.76, l_acc=4.40, d0_v=0.49 |
| 12   | -896.9286    | 3.09       | y_att=2.65, y_ali=2.00, y_f=2.16, d0_att=1.00, l_att=4.66, l_ali=9.53, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.63, y_acc=1.76, l_acc=4.31, d0_v=0.45 |
| 13   | -892.1307    | 3.98       | y_att=2.65, y_ali=2.00, y_f=2.16, d0_att=1.00, l_att=4.66, l_ali=9.53, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.63, y_acc=1.76, l_acc=4.31, d0_v=0.45 |
| 14   | -916.2942    | 2.82       | y_att=2.78, y_ali=1.72, y_f=2.23, d0_att=1.00, l_att=4.66, l_ali=11.81, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.63, y_acc=1.76, l_acc=4.57, d0_v=0.52 |
| 15   | -990.7496    | 2.89       | y_att=2.78, y_ali=1.72, y_f=2.23, d0_att=1.00, l_att=4.66, l_ali=11.81, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.63, y_acc=1.76, l_acc=4.83, d0_v=0.52 |
| 16   | -975.3099    | 2.93       | y_att=2.78, y_ali=1.72, y_f=2.23, d0_att=1.00, l_att=4.66, l_ali=11.81, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.63, y_acc=1.76, l_acc=4.83, d0_v=0.52 |
| 17   | -975.3099    | 4.34       | y_att=2.78, y_ali=1.72, y_f=2.23, d0_att=1.00, l_att=4.66, l_ali=11.81, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.63, y_acc=1.76, l_acc=4.83, d0_v=0.52 |
| 18   | -975.3099    | 3.15       | y_att=2.78, y_ali=1.72, y_f=2.23, d0_att=1.00, l_att=4.66, l_ali=11.81, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.63, y_acc=1.76, l_acc=4.83, d0_v=0.52 |
| 19   | -975.3099    | 3.07       | y_att=2.78, y_ali=1.72, y_f=2.23, d0_att=1.00, l_att=4.66, l_ali=11.81, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=3.63, y_acc=1.76, l_acc=4.83, d0_v=0.52 |

**End of experiment.**
