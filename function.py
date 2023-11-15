import math


# 定义bisection算法函数
def bisection(func, a, b, epsilon):
    if func(a) * func(b) > 0 or a > b:
        print("bisection function:input error")
        return None
    while (b - a) > epsilon:
        c = (a + b) / 2
        if func(c) == 0:
            return c
        elif func(a) * func(c) > 0:
            a = c
        else:
            b = c

    return (a + b) / 2


# 定义newton算法函数
def newton(func, dfunc, x0, epsilon):
    if func(x0) == 0:
        return x0
    if dfunc(x0) == 0:
        print("newton function:Zero derivative. No solution found.")
        return None
    x1 = x0 - func(x0) / dfunc(x0)
    while math.fabs(x1 - x0) >= epsilon:
        x0 = x1
        if dfunc(x0) == 0:
            print("newton function:Zero derivative. No solution found.")
            return None
        x1 = x0 - func(x0) / dfunc(x0)
    return x1
