import math


def bisection(function, a, b, epsilon, root, if_need_error_list):
    assert (b > a) and (function(a) * function(b) < 0)  # 算法基本条件

    bisection_error_list = []  # 返回每次迭代后与真实根的误差列表
    while b - a > epsilon:
        c = (a + b) / 2

        if if_need_error_list == True:
            bisection_error_list.append(c - root)

        if function(c) == 0:  # 找到根了，直接返回
            return c

        if function(a) * function(c) < 0:  # 按Bisection算法迭代
            b = c
        else:
            a = c

    if if_need_error_list == True:
        bisection_error_list.append((a + b) / 2 - root)  # 加入误差列表
        return bisection_error_list

    return (a + b) / 2




newton_error_list = []  # 因为递归，需要提前声明


def newton(fun, dfun, x0, epsilon, root, if_need_error_list):
    iterator = fun(x0) / dfun(x0)  # newton算法中的迭代误差
    global newton_error_list

    if math.fabs(iterator) < epsilon:
        if if_need_error_list == True:  # 迭代最后一步，返回误差列表
            newton_error_list.append(math.fabs(x0 - iterator - root))
            return newton_error_list
        return x0 - iterator  # 不需要列表就返回根

    if if_need_error_list == True:
        newton_error_list.append(math.fabs(x0 - iterator - root))

    return newton(fun, dfun, x0 - iterator, epsilon, root, if_need_error_list)