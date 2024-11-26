# -*- coding: utf-8 -*-

# 定义 Henon 映射函数
def HM(a, b, x0, y0, n):
    # 定义 Hénon 映射的 x 更新公式
    def HMX(a, x0, y0):
        x = 1 - a * x0**2 + y0  # 经典的 Hénon 映射公式
        return x

    # 定义 Hénon 映射的 y 更新公式
    def HMY(b, x0):
        y = b * x0  # 经典的 Hénon 映射公式
        return y

    # 存储轨迹的输出列表
    output = []

    # 迭代计算 n 次
    for i in range(n):
        x = HMX(a, x0, y0)  # 计算当前的 x 值
        y = HMY(b, x0)       # 计算当前的 y 值
        output.append((x, y))  # 将 (x, y) 添加到输出列表中
        x0, y0 = x, y          # 更新 x0 和 y0 为当前的 x 和 y，以便进行下一次迭代

    return output  # 返回轨迹数据

# a = float(input('please input a:'))
# b = float(input('please input b:'))
# x0 = float(input('please input x0:'))
# y0 = float(input('please input y0:'))
# n = int(input('please input n:'))
#这里被注释掉的代码可以自由输入初始的a,b,x0,y0,n，需要时可以取消注释（同时注释掉下面的5行代码）

# 初始化 Henon 映射的参数
a = 1.4       
b = 0.3        # 参数 b
x0 = 0      # 初始值 x0
y0 = 0      # 初始值 y0
n = 50000        # 迭代次数

# 打印 Henon 映射的轨迹（仅输出数据）
print(HM(a, b, x0, y0, n))

# 导入 matplotlib 用于绘制轨迹图
import matplotlib.pyplot as plt

# 获取 Henon 映射的轨迹
trajectory = HM(a, b, x0, y0, n)

# 提取轨迹中的 x 和 y 值
x_values = [point[0] for point in trajectory]  # 提取 x 值
y_values = [point[1] for point in trajectory]  # 提取 y 值

# 绘制轨迹图
plt.figure(figsize=(8, 6))  # 设置图像的大小
plt.plot(x_values, y_values, color='blue', linewidth=0.5)  # 绘制轨迹线，颜色为蓝色，线宽为0.5
plt.title("Henon Map Trajectory")  # 设置图像标题
plt.xlabel("x")  # 设置 x 轴标签
plt.ylabel("y")  # 设置 y 轴标签
plt.grid(True)   # 显示网格线
plt.show()       # 显示图像