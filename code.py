import numpy as np
import matplotlib.pyplot as plt

def henon_map(a, b, u0, N):
    x, y = u0
    trajectory = [(x, y)]
    for _ in range(N):
        x, y = 1 - a * x**2 + y, b * x
        trajectory.append((x, y))
    return trajectory

def plot_trajectory(trajectory):
    x_values, y_values = zip(*trajectory)
    plt.figure(figsize=(8, 8))
    plt.scatter(x_values, y_values, s=1)
    plt.title('Hénon Map Trajectory')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()

def plot_orbit_diagram(b, a_values, N, u0):
    plt.figure(figsize=(10, 6))
    for i, a in enumerate(a_values):
        trajectory = henon_map(a, b, u0, N)
        x_values, _ = zip(*trajectory)
        plt.scatter([a] * len(x_values), x_values, s=1, alpha=0.5)
    plt.title('Orbit Diagram of Hénon Map')
    plt.xlabel('a')
    plt.ylabel('x')
    plt.grid(True)
    plt.show()

# 用户输入初始值
u0 = input("请输入初始值 (x0, y0)，用逗号分隔: ")
x0, y0 = map(float, u0.split(','))
a = float(input("请输入参数a:"))
b = float(input("请输入参数b:"))
N = int(input("请输入轨迹长度N:"))

# 计算Hénon map的轨迹
trajectory = henon_map(a, b, (x0, y0), N)

# 输出轨迹点
print("Hénon map的轨迹为:")
for point in trajectory:
    print(point)

# 重新设置参数
a = 1.4
b = 0.3
u0 = (0, 0)

# 探索N的取值并绘制轨迹图
print("现在可以探索N的取值,得到经典Hénon map的轨迹图(三次机会)\n")
for i in range(3):
    N = int(input("请输入轨迹长度N:"))
    trajectory = henon_map(a, b, (x0, y0), N)
    plot_trajectory(trajectory)

# 参数设置
a_values = np.linspace(0, 1.4, 200)  # a的取值范围

# 绘制轨道图orbit diagram
plot_orbit_diagram(b, a_values, N, (x0, y0))

# 通过观察图像，发现a = 1.02时x收敛于某几个点，这表明可能Hénon map中会出现周期性轨道，以此为例，绘制轨迹图
trajectory = henon_map(a = 1.02, b = 0.3, u0 = (0, 0), N=1000)
plot_trajectory(trajectory)