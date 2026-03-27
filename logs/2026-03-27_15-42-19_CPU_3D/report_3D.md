# Experiment Report - CPU (3D)
**Date:** 2026-03-27_15-42-19

## 1. Initial Configuration
| Parameter | Value |
| :--- | :--- |
| ARENA_RADIUS         | 50.0       |
| COLLISION_DIST       | 0.4        |
| DT                   | 0.1        |
| ENABLE_3D            | True       |
| GEN_CPU              | 20         |
| GEN_GPU              | 2          |
| GRID_RES             | 5.0        |
| MAX_SPEED            | 2.0        |
| NB_DRONES            | 20         |
| NEIGHBORS            | 2          |
| POP_SIZE_CPU         | 150        |
| POP_SIZE_GPU         | 5000       |
| SCENARIO             | exploration |
| SIM_STEPS            | 500        |
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
| 00   | -4170.2337   | 5.13       | y_att=1.87, y_ali=0.81, y_f=1.34, d0_att=2.65, l_att=1.59, l_ali=4.53, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.88 |
| 01   | -4196.4995   | 4.41       | y_att=0.79, y_ali=2.12, y_f=1.07, d0_att=2.63, l_att=4.93, l_ali=4.34, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.72 |
| 02   | -4243.9585   | 5.97       | y_att=1.98, y_ali=0.81, y_f=1.34, d0_att=2.43, l_att=1.59, l_ali=4.53, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.88 |
| 03   | -4271.6218   | 4.35       | y_att=1.87, y_ali=0.81, y_f=1.34, d0_att=2.40, l_att=1.59, l_ali=4.53, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=2.88 |
| 04   | -4338.0717   | 5.02       | y_att=0.64, y_ali=1.51, y_f=1.07, d0_att=2.63, l_att=4.93, l_ali=4.34, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.72 |
| 05   | -4338.0717   | 4.76       | y_att=0.64, y_ali=1.51, y_f=1.07, d0_att=2.63, l_att=4.93, l_ali=4.34, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.72 |
| 06   | -4338.0717   | 4.54       | y_att=0.64, y_ali=1.51, y_f=1.07, d0_att=2.63, l_att=4.93, l_ali=4.34, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.72 |
| 07   | -4338.0717   | 4.53       | y_att=0.64, y_ali=1.51, y_f=1.07, d0_att=2.63, l_att=4.93, l_ali=4.34, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.72 |
| 08   | -4338.0717   | 4.48       | y_att=0.64, y_ali=1.51, y_f=1.07, d0_att=2.63, l_att=4.93, l_ali=4.34, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.72 |
| 09   | -4359.2001   | 4.82       | y_att=0.64, y_ali=1.51, y_f=1.07, d0_att=2.69, l_att=4.93, l_ali=4.34, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.72 |
| 10   | -4359.2001   | 4.75       | y_att=0.64, y_ali=1.51, y_f=1.07, d0_att=2.69, l_att=4.93, l_ali=4.34, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.72 |
| 11   | -4359.2001   | 4.78       | y_att=0.64, y_ali=1.51, y_f=1.07, d0_att=2.69, l_att=4.93, l_ali=4.34, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.72 |
| 12   | -4364.7995   | 4.54       | y_att=0.64, y_ali=1.51, y_f=1.07, d0_att=2.69, l_att=4.93, l_ali=4.34, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.72 |
| 13   | -4364.7995   | 4.24       | y_att=0.64, y_ali=1.51, y_f=1.07, d0_att=2.69, l_att=4.93, l_ali=4.34, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.72 |
| 14   | -4364.7995   | 4.27       | y_att=0.64, y_ali=1.51, y_f=1.07, d0_att=2.69, l_att=4.93, l_ali=4.34, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.72 |
| 15   | -4364.7995   | 4.35       | y_att=0.64, y_ali=1.51, y_f=1.07, d0_att=2.69, l_att=4.93, l_ali=4.34, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.72 |
| 16   | -4364.7995   | 4.30       | y_att=0.64, y_ali=1.51, y_f=1.07, d0_att=2.69, l_att=4.93, l_ali=4.34, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.72 |
| 17   | -4364.9233   | 4.27       | y_att=0.64, y_ali=1.51, y_f=1.07, d0_att=2.69, l_att=4.93, l_ali=4.34, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.72 |
| 18   | -4365.0427   | 5.60       | y_att=0.64, y_ali=1.49, y_f=1.07, d0_att=2.69, l_att=4.93, l_ali=4.34, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.72 |
| 19   | -4365.7881   | 4.53       | y_att=0.65, y_ali=1.51, y_f=1.07, d0_att=2.69, l_att=4.93, l_ali=4.34, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00, y_z_nav=1.00, y_vz_nav=1.00, target_altitude=7.72 |

**End of experiment.**
