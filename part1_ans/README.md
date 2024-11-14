# Hénon Map 的实现与分析

## 问题描述

Hénon map 是一种著名的离散时间动态系统，广泛应用于混沌理论研究中。它通过简单的迭代公式展示了系统在某些参数条件下的周期性和混沌行为。本程序的任务是实现 Hénon map 的计算和分析，具体包含以下几个部分：

1. 编写一个函数来计算 Hénon map 的轨迹，输入参数包括函数系数 `a` 和 `b`、初始值 `u0` 以及轨迹长度 `N`，输出为轨迹 `[u0, u1, u2, ..., uN]`。
2. 使用上述函数计算经典 Hénon map 的轨迹（参数为 `a=1.4`，`b=0.3`，`u0=(0, 0)`），并绘制轨迹图，探索 `N` 值不同时轨迹图变化的情况。
3. 绘制 Hénon map 的 **orbit diagram**，即在固定 `b=0.3` 的情况下，改变 `a` 值，生成一系列 Hénon map 轨迹，以 `a` 为横坐标，`x` 为纵坐标绘制 orbit diagram。
4. 分析 orbit diagram，找到一个使 Hénon map 收敛到周期性轨道的 `a` 值，并绘制对应的轨迹图。

## 解答思路

为了解决上述问题，解答思路如下：

1. **计算 Hénon map 轨迹**：
    - 定义 `henon_map` 函数，接收 `a`、`b`、`u0` 和 `N` 作为参数，使用 Hénon map 的迭代公式计算每个时间步的 `x` 和 `y` 值，并将这些点存储在一个列表中作为返回值。
2. **绘制轨迹图**：
    - 通过 `plot_trajectory` 函数绘制轨迹图。函数接受一个轨迹列表作为输入，并提取每个点的 `x` 和 `y` 值，分别作为横纵坐标绘制轨迹。该函数帮助我们直观地观察系统在给定参数下的演化路径。
3. **绘制 Orbit Diagram**：
    - 通过 `plot_orbit_diagram` 函数生成 orbit diagram。在固定 `b=0.3` 的情况下，对一系列 `a` 值进行迭代。对于每个 `a` 值，计算对应的 Hénon map 轨迹，将最后的 `N_plot` 个点的 `x` 值记录下来，并用 `a` 值作为横坐标，`x` 值作为纵坐标绘制图像。通过观察不同 `a` 值下的轨迹分布，可以识别出系统的周期性和混沌行为。
4. **分析周期性轨道**：
    - 通过观察 orbit diagram 中的轨迹点分布，若对应的x值表现出**离散性**，则该 `a` 值下轨迹具有周期性。对于该 `a` 值，我们可以再次使用 `plot_trajectory` 函数绘制对应的轨迹，验证系统的周期性特征。

## 使用说明

### 运行步骤

1. **计算 Hénon map 轨迹**：调用 `henon_map(a, b, u0, N)` 计算给定参数的 Hénon map 轨迹。例如：
    
    ```python
    trajectory = henon_map(1.4, 0.3, (0, 0), 10000)
    ```
    
2. **绘制轨迹图**：调用 `plot_trajectory(trajectory, title)` 绘制系统的演化轨迹，例如：
    
    ```python
    plot_trajectory(trajectory, title="Hénon Map Trajectory for a=1.4, b=0.3")
    ```
    
3. **绘制 Orbit Diagram**：调用 `plot_orbit_diagram(b, a_min, a_max, a_steps, u0, N_plot)` 绘制 orbit diagram。例如：
    
    ```python
    plot_orbit_diagram(0.3, 1.0, 1.4, 400, (0, 0), 500)
    ```
    
4. **分析并验证周期性轨道**：通过 orbit diagram 找到周期性参数 `a`，并用 `henon_map` 和 `plot_trajectory` 函数生成轨迹验证。