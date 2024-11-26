import numpy as np
import matplotlib.pyplot as plt

def henon_map(a, b, u0, N):
    """
    计算Hénon map的轨迹。

    参数:
    a (float): 函数系数a。
    b (float): 函数系数b。
    u0 (tuple): 初始值 (x0, y0)。
    N (int): 轨迹长度。

    返回:
    list: Hénon map的轨迹 [(x0, y0), (x1, y1), ..., (xN, yN)]。
    """
    trajectory = [u0]  # 初始化轨迹列表，以初始值开始
    x, y = u0  # 解包初始值

    # 迭代N-1次以生成整个轨迹
    for _ in range(N - 1):
        # 使用Hénon map的递推关系计算下一个点,使用numpy的浮点数类型来提高数值计算的稳定性
        x_next = 1 - a * np.float64(x)**2 + y
        y_next = b * x
        trajectory.append((x_next, y_next))  # 将新点添加到轨迹中
        x, y = x_next, y_next  # 更新x和y为新点的坐标

        # 如果数值过大，则停止计算
        if np.abs(x) > 1e10 or np.abs(y) > 1e10:
            break

    return trajectory


# 调用函数并打印结果
def plot_trajectory(trajectory):
    """
    绘制Hénon map的轨迹图。

    参数:
    trajectory (list): Hénon map的轨迹列表。
    """
    x_coords, y_coords = zip(*trajectory)
    plt.figure(figsize=(8, 6))
    plt.scatter(x_coords, y_coords, s=1, alpha=0.5)
    plt.title('Hénon Map Trajectory')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()

# 经典Hénon map参数
a_classic = 1.4
b_classic = 0.3
u0_classic = (0, 0)

# 探索不同的N值
N_values = [100, 1000, 10000]

for N in N_values:
    # 计算轨迹
    trajectory = henon_map(a_classic, b_classic, u0_classic, N)
    
    # 打印轨迹
    print(f"轨迹长度N={N}的Hénon map轨迹: {trajectory}")
    
    # 绘制轨迹图
    plot_trajectory(trajectory)
    
# 利⽤编写的函数计算Hénon map的orbit digram
def plot_orbit_diagram(a_values, b, u0, N):
    """
    计算并绘制Hénon map的orbit diagram。

    参数:
    a_values (list): a值的列表。
    b (float): 函数系数b。
    u0 (tuple): 初始值 (x0, y0)。
    N (int): 轨迹长度。
    """
    plt.figure(figsize=(10, 6))
    for a in a_values:
        trajectory = henon_map(a, b, u0, N)
        x_coords, _ = zip(*trajectory)
        plt.scatter([a] * len(x_coords), x_coords, s=1, alpha=0.3, label=f'a={a}')
    plt.title('Orbit Diagram of Hénon Map')
    plt.xlabel('a')
    plt.ylabel('x')
    plt.legend()
    plt.grid(True)
    plt.show()

# 固定b值和初始值
b_fixed = 0.3
u0_fixed = (0, 0)

# 改变a值
a_values = np.linspace(0, 1.4, 100)  # 从0到1.4，100个a值
N = 100  # 轨迹长度

# 绘制orbit diagram
plot_orbit_diagram(a_values, b_fixed, u0_fixed, N)

# 找到可以收敛到周期性轨道的a值
def find_periodic_a(a_values, b, u0, N):
    """
    找到Hénon map可以收敛到周期性轨道的a值。

    参数:
    a_values (list): a值的列表。
    b (float): 函数系数b。
    u0 (tuple): 初始值 (x0, y0)。
    N (int): 轨迹长度。

    返回:
    float: 可以收敛到周期性轨道的a值。
    """
    for a in a_values:
        trajectory = henon_map(a, b, u0, N)
        points_set = set(trajectory)
        if len(points_set) < N:  # 如果不同的点的数量少于N，可能是周期性的
            return a
    return None

periodic_a = find_periodic_a(a_values, b_fixed, u0_fixed, N)
if periodic_a is not None:
    print(f"找到可以收敛到周期性轨道的a值: {periodic_a}")
    # 计算该a值对应的Hénon map的轨迹
    trajectory = henon_map(periodic_a, b_fixed, u0_fixed, N)
    # 以列表形式输出轨迹
    print("对应的Hénon map轨迹为:")
    print(trajectory)
    # 绘制轨迹图
    plot_trajectory(trajectory)
else:
    print("未找到可以收敛到周期性轨道的a值。")
