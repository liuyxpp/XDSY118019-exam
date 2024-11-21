# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

# Henon map函数
def HM(a, b, x0, y0, n):
    def HMX(a, x0, y0):
        x = 1 - a * x0**2 + y0
        return x

    def HMY(b, x0):
        y = b * x0
        return y

    output = []
    for i in range(n):
        x = HMX(a, x0, y0)  # 计算当前的 x 值
        y = HMY(b, x0)       # 计算当前的 y 值
        output.append((x, y))
        x0, y0 = x, y        # 更新 x0 和 y0 为当前的 x 和 y

    return output

# 固定参数
b = 0.3
x0 = 0
y0 = 0
n = 50000  # 迭代次数

# 创建a值的范围，设置不同的a值
a_values = [i * 0.1 for i in range(15)]  # 生成a的不同值，0.0到1.4之间，步长为0.1

# 存储对应的x值
x_results = []

# 对每个a值计算Henon映射轨迹的最后一个x值（收敛到稳定状态的x值）
for a in a_values:
    trajectory = HM(a, b, x0, y0, n)
    x_results.append(trajectory[-1][0])  # 获取轨迹的最后一个x值

# 绘制a值与x的关系图
plt.figure(figsize=(8, 6))
plt.plot(a_values, x_results, color='blue', marker='o', linestyle='-', linewidth=2, markersize=5)
plt.title("Effect of 'a' on Henon Map (Fixed b = 0.3)")
plt.xlabel("a")
plt.ylabel("x")
plt.grid(True)
plt.savefig("C:\\Users\\12892\Desktop\\跨入科学研究之门\\henon_map_a_x.png", dpi=300, bbox_inches='tight')
