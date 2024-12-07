import numpy as np
from scipy.optimize import bisect, newton
import matplotlib.pyplot as plt
#task1&task2 定义两种算法函数
def bisection_algorithm(f, a, b, epsilon):
    while (b - a) / 2 > epsilon:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2

def newton_algorithm(f, df, x0, epsilon):
    x = x0
    while abs(f(x)) > epsilon:
        x = x - f(x) / df(x)
    return x

#task3 需要使用到的函数
def f1(x):
    return 2*x - np.tan(x)

def df1(x):
    return 2 - 1/np.cos(x)**2

def f2(x):
    return np.exp(x + 1) - x - 2

def df2(x):
    return np.exp(x + 1) - 1

def f3(x):
    return x - 2 - np.sin(x)

def df3(x):
    return 1 - np.cos(x)
import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

# Define the functions
def f1(x):
    return 2*x - np.tan(x)

def f2(x):
    return np.exp(x + 1) - x - 2

def f3(x):
    return x - 2 - np.sin(x)

# 绘制大致图形
x_values = np.linspace(-0.2, 1.4, 1000)
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.plot(x_values, f1(x_values))
plt.title('2x = tan(x)')
plt.xlabel('x')
plt.ylabel('f(x)')

plt.subplot(1, 3, 2)
plt.plot(x_values, f2(x_values))
plt.title('e^(x+1) = 2 + x')
plt.xlabel('x')
plt.ylabel('f(x)')

plt.subplot(1, 3, 3)
plt.plot(x_values, f3(x_values))
plt.title('x - 2 = sin(x)')
plt.xlabel('x')
plt.ylabel('f(x)')

plt.tight_layout()
plt.show()

# Use fsolve from Scipy to find roots
roots_f1 = fsolve(f1, [-0.2, 0, 1.4])
roots_f2 = fsolve(f2, [-2, 0, 2])
roots_f3 = fsolve(f3, [0.5, 2, 4*np.pi])

# Print the roots obtained using fsolve
print(f"Roots using fsolve for Equation 1: {roots_f1}")
print(f"Roots using fsolve for Equation 2: {roots_f2}")
print(f"Roots using fsolve for Equation 3: {roots_f3}")

# Compare with Bisection and Newton methods
result_bisection_f1 = bisection_algorithm(f1, -0.2, 1.4, 1e-10)
result_newton_f1 = newton_algorithm(f1, df1, 0.5, 1e-10)

result_bisection_f2 = bisection_algorithm(f2, -2, 2, 1e-10)
result_newton_f2 = newton_algorithm(f2, df2, 0, 1e-10)

result_bisection_f3 = bisection_algorithm(f3, 0.5, 4*np.pi, 1e-10)
result_newton_f3 = newton_algorithm(f3, df3, 3, 1e-10)
# 2x = tan(x), x ∈ [−0.2, 1.4]
result_bisection = bisection_algorithm(f1, -0.2, 1.4, 1e-10)
result_newton = newton_algorithm(f1, df1, 0.5, 1e-10)
print(f"Equation 1: Bisection result: {result_bisection}, Newton result: {result_newton}")

# ex+1 = 2 + x, x ∈ [−2, 2]
result_bisection = bisection_algorithm(f2, -2, 2, 1e-10)
result_newton = newton_algorithm(f2, df2, 0, 1e-10)
print(f"Equation 2: Bisection result: {result_bisection}, Newton result: {result_newton}")

# x−2 = sin(x), x ∈ [0.5, 4π]
result_bisection = bisection_algorithm(f3, 0.5, 4*np.pi, 1e-10)
result_newton = newton_algorithm(f3, df3, 3, 1e-10)
print(f"Equation 3: Bisection result: {result_bisection}, Newton result: {result_newton}")

# task4 误差分析：x^2 - 2 = 0, in the interval (1, 2)
true_root = np.sqrt(2)

def bisection_error_analysis(max_iterations):
    errors = []
    for i in range(1, max_iterations + 1):
        result = bisection_algorithm(lambda x: x**2 - 2, 1, 2, 1e-10)
        error = abs(result - true_root)
        errors.append(error)
    return errors

def newton_error_analysis(max_iterations):
    errors = []
    for i in range(1, max_iterations + 1):
        result = newton_algorithm(lambda x: x**2 - 2, lambda x: 2*x, 2, 1e-10)
        error = abs(result - true_root)
        errors.append(error)
    return errors

max_iterations = 10
bisection_errors = bisection_error_analysis(max_iterations)
newton_errors = newton_error_analysis(max_iterations)

plt.plot(range(1, max_iterations + 1), bisection_errors, label='Bisection')
plt.plot(range(1, max_iterations + 1), newton_errors, label='Newton')
plt.xlabel('Iteration')
plt.ylabel('Error')
plt.title('Convergence Error Analysis')
plt.legend()
