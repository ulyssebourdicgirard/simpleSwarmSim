# Experiment Report - PyTorch_CUDA (3D)
**Date:** 2026-03-15_16-23-28

## 1. Initial Configuration
| Parameter | Value |
| :--- | :--- |
| ARENA_RADIUS         | 500.0      |
| COLLISION_DIST       | 0.4        |
| DT                   | 0.1        |
| ENABLE_3D            | True       |
| GEN_CPU              | 20         |
| GEN_GPU              | 20         |
| GPU_AVAILABLE        | True       |
| GRID_RES             | 5.0        |
| MAX_SPEED            | 2.0        |
| NB_DRONES            | 20         |
| NEIGHBORS            | None       |
| POP_SIZE_CPU         | 150        |
| POP_SIZE_GPU         | 5000       |
| SCENARIO             | exploration |
| SIM_STEPS            | 500        |
| VISU_STEPS           | 1000       |
| W_COLL               | 500.0      |
| W_DISP               | 0.0        |
| W_EFFORT             | 1          |
| W_EXPLO              | -50.0      |
| W_MILL               | -20.0      |
| W_POL                | -0.0       |
| Z_MAX                | 10.0       |
| Z_MIN                | 1.0        |

## 2. Optimization Evolution
| Gen  |  Best Cost   |  Time (s)  |                                                                All Parameters                                                                |
| :--: | :----------: | :--------: | :------------------------------------------------------------------------------------------------------------------------------------------ |
| 00   | -387.0803    | 8.52       | y_att=0.80, y_ali=1.88, y_f=1.52, d0_att=3.43, l_att=1.17, l_ali=2.57, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 01   | -561.2283    | 8.30       | y_att=0.70, y_ali=1.60, y_f=1.33, d0_att=2.34, l_att=0.75, l_ali=1.60, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 02   | -722.1206    | 8.27       | y_att=3.28, y_ali=0.45, y_f=1.12, d0_att=4.09, l_att=0.31, l_ali=2.63, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 03   | -834.8199    | 8.29       | y_att=1.61, y_ali=2.64, y_f=1.06, d0_att=2.93, l_att=0.38, l_ali=5.05, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 04   | -821.5428    | 8.38       | y_att=2.35, y_ali=0.59, y_f=0.76, d0_att=4.61, l_att=0.29, l_ali=1.12, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 05   | -869.4556    | 8.39       | y_att=0.78, y_ali=0.58, y_f=0.87, d0_att=0.81, l_att=0.22, l_ali=1.34, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 06   | -928.3958    | 8.39       | y_att=0.44, y_ali=3.81, y_f=1.77, d0_att=3.99, l_att=0.44, l_ali=5.36, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 07   | -909.8884    | 8.58       | y_att=0.87, y_ali=2.74, y_f=1.90, d0_att=1.21, l_att=0.23, l_ali=4.35, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 08   | -943.8209    | 8.41       | y_att=0.42, y_ali=1.40, y_f=1.28, d0_att=7.13, l_att=0.34, l_ali=1.17, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 09   | -912.2501    | 8.41       | y_att=1.30, y_ali=0.77, y_f=0.59, d0_att=5.77, l_att=0.16, l_ali=0.90, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 10   | -915.4613    | 8.40       | y_att=0.54, y_ali=3.43, y_f=1.45, d0_att=4.77, l_att=0.55, l_ali=4.78, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 11   | -934.8293    | 8.38       | y_att=0.50, y_ali=3.29, y_f=0.97, d0_att=5.82, l_att=0.43, l_ali=4.62, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 12   | -949.7491    | 8.63       | y_att=0.26, y_ali=0.11, y_f=2.03, d0_att=13.28, l_att=0.17, l_ali=5.20, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 13   | -942.6661    | 8.62       | y_att=0.28, y_ali=2.20, y_f=1.73, d0_att=1.31, l_att=0.19, l_ali=3.68, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 14   | -897.8381    | 8.31       | y_att=0.67, y_ali=3.77, y_f=2.91, d0_att=4.23, l_att=0.56, l_ali=2.80, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 15   | -939.4930    | 8.30       | y_att=0.77, y_ali=1.97, y_f=0.77, d0_att=4.21, l_att=0.25, l_ali=2.12, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 16   | -934.7270    | 8.51       | y_att=0.34, y_ali=3.41, y_f=1.42, d0_att=2.83, l_att=0.35, l_ali=2.56, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 17   | -949.8986    | 8.83       | y_att=0.32, y_ali=0.54, y_f=1.62, d0_att=4.09, l_att=0.10, l_ali=0.19, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 18   | -925.0789    | 8.88       | y_att=0.48, y_ali=2.42, y_f=0.58, d0_att=2.10, l_att=0.34, l_ali=1.74, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 19   | -941.3853    | 8.53       | y_att=0.40, y_ali=4.84, y_f=0.63, d0_att=2.97, l_att=0.28, l_ali=1.54, a_att=0.00, b1_att=0.00, b2_att=0.00, d0_ali=1.00, a_ali=0.00, b1_ali=0.00, b2_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |

**End of experiment.**
