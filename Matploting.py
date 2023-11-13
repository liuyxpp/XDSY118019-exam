import numpy as np
import matplotlib.pyplot as plt

# 定义目标函数
def f(x):
    return x**(-2) - np.sin(x)

# 生成 x 值
x_values = np.linspace(-0.2, 1.4, 1000)

# 计算对应的 y 值
y_values = f(x_values)

# 绘制图像
plt.figure(figsize=(8, 6))
plt.plot(x_values, y_values)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(-0.2, color='red', linestyle='--', label='Lower Bound')
plt.axvline(1.4, color='blue', linestyle='--', label='Upper Bound')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
