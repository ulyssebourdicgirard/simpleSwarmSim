# Experiment Report - GPU (3D)
**Date:** 2026-03-13_13-11-00

## 1. Initial Configuration
| Parameter | Value |
| :--- | :--- |
| ARENA_RADIUS         | 50.0       |
| COLLISION_DIST       | 0.4        |
| DT                   | 0.1        |
| ENABLE_3D            | True       |
| GEN_CPU              | 20         |
| GEN_GPU              | 2          |
| GPU_AVAILABLE        | False      |
| MAX_SPEED            | 2.0        |
| NB_DRONES            | 20         |
| NEIGHBORS            | None       |
| POP_SIZE_CPU         | 150        |
| POP_SIZE_GPU         | 5000       |
| SIM_STEPS            | 500        |
| VISU_STEPS           | 1000       |
| W_COLL               | 500.0      |
| W_DISP               | 0.0        |
| W_EFFORT             | 1          |
| W_MILL               | -20.0      |
| W_POL                | -0.0       |
| Z_MAX                | 10.0       |
| Z_MIN                | 1.0        |

## 2. Optimization Evolution
| Gen  |  Best Cost   |  Time (s)  |                                                                All Parameters                                                                |
| :--: | :----------: | :--------: | :------------------------------------------------------------------------------------------------------------------------------------------ |
| 00   | 163.1902     | 11.35      | y_att=0.78, y_ali=0.13, y_f=1.51, d0_att=3.87, l_att=2.99, l_ali=4.60, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |
| 01   | -168.4001    | 11.18      | y_att=1.74, y_ali=1.06, y_f=1.60, d0_att=3.95, l_att=1.78, l_ali=1.97, alpha_att=1.00, alpha_ali=0.00, y_z=1.00, l_z=3.00, a_z=1.00, d0_z=0.50, sigma_z=1.00, y_z_w=2.00, dz_w=1.00 |

**End of experiment.**
