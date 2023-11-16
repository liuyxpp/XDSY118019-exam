
import numpy as np
import matplotlib.pyplot as plt
from itertools import zip_longest

# 定义目标函数和其导数
def f(x):
    return x**2 - 2

def df(x):
    return 2 * x

# Bisection算法
def bisection(f, a, b, epsilon):
    errors = []
    approx_roots = []
    
    while (b - a) / 2 > epsilon:
        c = (a + b) / 2
        approx_roots.append(c)
        errors.append(abs(c - np.sqrt(2)))
        
        if f(c) == 0:
            return c, errors, approx_roots
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    
    return (a + b) / 2, errors, approx_roots

# Newton算法
def newton_method(f, df, x0, epsilon):
    x = x0
    errors = []
    approx_roots = []
    
    while abs(f(x)) > epsilon:
        x = x - f(x) / df(x)
        approx_roots.append(x)
        errors.append(abs(x - np.sqrt(2)))
    
    return x, errors, approx_roots

# 定义初始区间和初始估计值
a, b = 1, 2
x0 = 1.5

# 目标误差
epsilon = 1e-10

# 调用Bisection算法和Newton算法
root_bisection, errors_bisection, approx_roots_bisection = bisection(f, a, b, epsilon)
root_newton, errors_newton, approx_roots_newton = newton_method(f, df, x0, epsilon)

iterations_bisection = list(range(len(errors_bisection)))
iterations_newton = list(range(len(errors_newton)))
max_iterations = max(len(iterations_bisection), len(iterations_newton))
table_data = {
    'Iteration (Bisection)': iterations_bisection,
    'Error (Bisection)': errors_bisection,
    'Approx. Root (Bisection)': approx_roots_bisection,
    'Iteration (Newton)': iterations_newton,
    'Error (Newton)': errors_newton,
    'Approx. Root (Newton)': approx_roots_newton
}

# 补充短的行
for key in table_data:
    table_data[key] += [None] * (max_iterations - len(table_data[key]))
plt.figure(figsize=(12, 6))  # 设置初始窗口大小为 10x6
plt.table(cellText=[[table_data[key][i] for key in table_data] for i in range(max_iterations)],
          colLabels=list(table_data.keys()),
          cellLoc='center',
          loc='center')
table = plt.table(cellText=[[table_data[key][i] for key in table_data] for i in range(max_iterations)],
                  colLabels=list(table_data.keys()),
                  cellLoc='center',
                  loc='center')
table.auto_set_font_size(False)
table.set_fontsize(8)
plt.axis('off')  # 不显示坐标轴

plt.show()

# 输出最终的根
print("Root found by Bisection:", root_bisection)
print("Root found by Newton:", root_newton)