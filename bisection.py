import math
li_bisec = list()
def bisection(fun, a, b, e, mode):
    assert b > a
    assert fun(a) * fun(b) < 0
    while b - a > e:
        c = (a + b) / 2
        if mode == 1:
            li_bisec.append(c - math.sqrt(2))
        if fun(c) == 0:
            return c
        elif fun(a) * fun(c) < 0:
            b = c
        else:
            a = c
    if mode == 1:
        li_bisec.append((a + b) / 2 - math.sqrt(2))
    return (a + b) / 2