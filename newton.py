import math
li_newton = list()
def newton(fun, dfun, x0, e, mode):
    delta = fun(x0) / dfun(x0)
    if math.fabs(delta) < e:
        if mode == 1:
            li_newton.append(math.fabs(x0 - delta - math.sqrt(2)))
        return x0 - delta
    if mode == 1:
        li_newton.append(math.fabs(x0 - delta - math.sqrt(2)))
    return newton(fun, dfun, x0 - delta, e, mode)
