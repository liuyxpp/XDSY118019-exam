import numpy as np
import matplotlib.pyplot as plt

def henon_map(a, b, x0, y0, N):
    x = np.zeros(N)
    y = np.zeros(N)
    x[0] = x0
    y[0] = y0
    for n in range(N - 1):
        x[n + 1] = 1 - a * x[n] * x[n] + y[n]
        y[n + 1] = b * x[n]
    return x, y


# 1. 计算Henon map的函数
def calculate_henon(a, b, u0, N):
    x0, y0 = u0
    return henon_map(a, b, x0, y0, N)


# 2. 计算经典Henon map的轨迹
a1 = 1.4
b1 = 0.3
u0_1 = (0, 0)
N_values = range(10, 1000, 10)
for N in N_values:
    x, y = calculate_henon(a1, b1, u0_1, N)
    plt.plot(x, y, 'o', markersize=0.5)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Henon Map Trajectory (a=1.4, b=0.3)')
plt.show()


# 3. 计算Henon map的orbit diagram
b2 = 0.3
a_values = np.linspace(0, 2, 1000)
N_orbits = 500
last_100_x = np.zeros((len(a_values), 100))
for i, a in enumerate(a_values):
    x, y = calculate_henon(a, b2, u0_1, N_orbits + 100)
    last_100_x[i, :] = x[-100:]
for i in range(len(a_values)):
    plt.plot(np.full(100, a_values[i]), last_100_x[i, :], 'b.', markersize=0.5)
plt.xlabel('a')
plt.ylabel('x')
plt.title('Henon Map Orbit Diagram (b=0.3)')
plt.show()


# 4. 找到Henon map收敛到周期轨道的a值并绘图
a_values_periodic = []
for a in np.linspace(0, 2, 1000):
    x, y = calculate_henon(a, b2, u0_1, 1000)
    if np.all(np.diff(x[-100:]) == 0):
        a_values_periodic.append(a)
for a in a_values_periodic:
    x, y = calculate_henon(a, b2, u0_1, 1000)
    plt.plot(x, y, 'o', markersize=0.5)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Periodic Orbits of Henon Map (b=0.3)')
plt.show()
