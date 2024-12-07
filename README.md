# Hénon Map 轨迹与轨道图代码功能

## 问题描述

本代码的功能是计算并绘制 Hénon map 的轨迹和轨道图。具体功能包括：

1. **计算 Hénon map 的函数**：输入任意函数系数 `a`、`b`，初始值 `u0` 以及轨迹长度 `N`，输出 Hénon map 的轨迹 `[u0, u1, u2, ..., uN]`。
2. **绘制经典 Hénon map 的轨迹图**：参数取值为 `a=1.4`，`b=0.3`，`u0=(0, 0)`，探索 `N` 的取值，求解得到的轨迹，并绘制轨迹图（`x` 为横坐标，`y` 为纵坐标）。
3. **计算 Hénon map 的orbit digram**：固定 `b=0.3`，改变 `a` 后获得一系列 Hénon map 的轨迹，然后以 `a` 为横轴，`x` 为纵轴绘制orbit digram。
4. **分析orbit digram**：找到 Hénon map 可以收敛到一条周期性轨道的 `a` 值，计算该 `a` 值对应的 Hénon map 的轨迹并绘图。

## 解答思路

1. **计算 Hénon map 的函数**：编写一个函数henon_map，输入参数a, b, u0和N，使用 Hénon map 的迭代公式计算每个循环的 `x` 和 `y` 值，输出Hénon Map的轨迹。
2. **绘制经典 Hénon map 的轨迹图**：使用plot_henon_trajectory函数，提取每个点的 `x` 和 `y` 值，分别作为横纵坐标绘制轨迹。设置N的取值为100, 1000, 10000，分别计算 Hénon map 的轨迹，并用matplotlib绘制轨迹图。
3. **计算 Hénon map 的orbit digram**：编写henon_orbit_diagram函数，固定b值，设置 `a` 的取值范围为 `[1.0, 1.4]`，均匀选取1000个`a`，绘制一系列Hénon Map的轨迹，然后绘制Orbit Diagram。
4. **分析orbit digram**：通过观察轨道图，如果x取值分布是离散的，说明轨道大概率收敛。找到收敛到周期性轨道的 `a` 值为1.04，计算该 `a` 值对应的 Hénon map 的轨迹并绘图验证其周期性。

## 如何使用代码

1. **环境要求**：确保你的Python环境中安装了以下库：numpy；matplotlib。如果未安装，可以使用以下命令安装：`pip install numpy matplotlib`.
2. **使用步骤**：下载本 `answercode.ipynb` 文件，用你的Python编辑器打开，根据需要修改a_classic, b_classic, u0_classic, N_classic, a_values等参数。然后运行代码。代码运行结束后，会显示N取不同值的经典Hénon Map轨迹图和Orbit Diagram、以及a值为1.04对应的轨迹图。
3. **注意事项**：确保参数a, b, u0和N的值是合理的，以避免计算错误或图形绘制失败。可根据需要调整a_values的范围和步长，以更好地探索Hénon Map的行为。
