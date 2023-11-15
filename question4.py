import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = "SimHei"

# 定义存放误差的列表
global bisection_list
global newton_list
bisection_list = []
newton_list = []
root = np.sqrt(2)


def func4(x):
    return x ** 2 - 2


def dfunc4(x):
    return 2 * x


def bisection(func, a, b, epsilon):
    if func(a) * func(b) > 0 or a > b:
        print("bisection function:input error")
        return None
    while (b - a) > epsilon:
        c = (a + b) / 2
        bisection_list.append(np.fabs(c - root))
        if func(c) == 0:
            return c
        elif func(a) * func(c) > 0:
            a = c
        else:
            b = c

    return (a + b) / 2


def newton(func, dfunc, x0, epsilon):
    if func(x0) == 0:
        return x0
    if dfunc(x0) == 0:
        print("newton function:Zero derivative. No solution found.")
        return None
    x1 = x0 - func(x0) / dfunc(x0)
    newton_list.append(np.fabs(x1 - x0))
    while np.fabs(x1 - x0) >= epsilon:
        x0 = x1
        if dfunc(x0) == 0:
            print("newton function:Zero derivative. No solution found.")
            return None
        x1 = x0 - func(x0) / dfunc(x0)
        newton_list.append(np.fabs(x1 - x0))
    return x1


bisection(func4, 1, 2, 1e-10)
list1 = np.arange(len(bisection_list))
newton(func4, dfunc4, 1, 1e-10)
list2 = np.arange(len(newton_list))

plt.figure(figsize=(14, 4))
plt.subplot(1, 3, 1)
plt.plot(list1, bisection_list)
plt.title("bisection算法收敛图")
plt.xlabel("迭代次数")
plt.ylabel("误差")

plt.subplot(1, 3, 2)
plt.plot(list2, newton_list)
plt.title("newton算法收敛图(以1为初始值)")
plt.xlabel("迭代次数")
plt.ylabel("误差")

newton_list = []
newton(func4, dfunc4, 2, 1e-10)
list3 = np.arange(len(newton_list))
plt.subplot(1, 3, 3)
plt.plot(list3, newton_list)
plt.title("newton算法收敛图(以2为初始值)")
plt.xlabel("迭代次数")
plt.ylabel("误差")

plt.show()
