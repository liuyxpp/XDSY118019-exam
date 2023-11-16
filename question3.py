import function
import numpy as np
from scipy.misc import derivative
from scipy.optimize import fsolve


def func1(x):
    return np.tan(x) - 2 * x


def func2(x):
    return np.exp(x + 1) - x - 2


def func3(x):
    return np.sin(x) - x ** (-2)


def dfunc1(x):
    return derivative(func1, x, dx=1e-10)


def dfunc2(x):
    return derivative(func2, x, dx=1e-10)


def dfunc3(x):
    return derivative(func3, x, dx=1e-10)


# 定义了一个求解函数，输入函数以及相关参数后，同时打印出三种方法的求解结果进行对比
# 参数i是方程的编号
def solve(i, func, dfunc, a, b, epsilon=1e-10):
    x0 = (a + b) / 2
    root1, = fsolve(func, x0)
    root2 = function.bisection(func, a, b, epsilon)
    root3 = function.newton(func, dfunc, x0, epsilon)
    if root1 is None or root2 is None or root3 is None:
        print(f"方程{i}在区间({a},{b})内无解")
    else:
        print(f"方程{i}在区间({a:<2},{b:<2})求解结果为:\t"
              f"使用scipy的fsolve函数:{root1:<18}\t"
              f"使用bisection算法:{root2:<20}\t"
              f"使用newton算法:{root3:<18}")


solve(1, func1, dfunc1, -0.2, 1)
solve(1, func1, dfunc1, 1, 1.4)
solve(2, func2, dfunc2, -1, -1)
solve(3, func3, dfunc3, 0.5, 2)
solve(3, func3, dfunc3, 2, 4)
solve(3, func3, dfunc3, 4, 8)
solve(3, func3, dfunc3, 8, 11)
solve(3, func3, dfunc3, 11, 4 * np.pi)
