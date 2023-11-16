import numpy as np
import matplotlib.pyplot as plt

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

# 绘制收敛速度的图表
iterations_bisection = range(len(errors_bisection))
iterations_newton = range(len(errors_newton))

plt.figure(figsize=(12, 6))
plt.plot(iterations_bisection, errors_bisection, label="Bisection")
plt.plot(iterations_newton, errors_newton, label="Newton")
plt.yscale('log')
plt.xlabel('Iterations')
plt.ylabel('Error')
plt.title('Convergence Speed Comparison')
plt.legend()
plt.show()

# 输出最终的根
print("Root found by Bisection:", root_bisection)
print("Root found by Newton:", root_newton)