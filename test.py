from bisection import *
from newton import *
from scipy import optimize
from scipy.misc import derivative
import matplotlib.pyplot as plt
import numpy as np
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)
# [-0.2, 1.4]
def fun1(x):
    return 2 * x - np.tan(x)
# [-2, 2]
def fun2(x):
    return np.exp(x + 1) - x - 2
# [0.5, 4pi]
def fun3(x):
    return (x ** 2) * np.sin(x) - 1
def fun4(x):
    return (x ** 2) - 2

def dfun1(x):
    return derivative(fun1, x, dx=1e-6)
def dfun2(x):
    return derivative(fun2, x, dx=1e-6)
def dfun3(x):
    return derivative(fun3, x, dx=1e-6)
def dfun4(x):
    return 2 * x

fun_li = [fun1, fun2, fun3, fun4]
dfun_li = [dfun1, dfun2, dfun3, dfun4]

# Compute root and compare to numpy/scipy's result
# mode for whether draw limitation speed, 0 no 1 yes
def compare(fun, dfun, a, b, mode):
    print("Scipy result: ", optimize.root(fun, (a + b) / 2))
    print("My_Bisection:", bisection(fun, a, b, 1e-10, mode))
    print("Standard_Bisection:", optimize.bisect(fun, a, b, xtol=1e-10))
    print("My_Newton:", newton(fun, dfun, (a + b) / 2, 1e-10, mode))
    print("Standard_Newton:", optimize.newton(fun, (a + b) / 2, tol=1e-10))

# draw a function from a to b
def draw(fun, a, b):
    x = np.arange(a, b + 0.1, (b - a) / 20)
    y = fun(x)
    plt.plot(x, y, '-')
    plt.plot([a, b], [0, 0])
    plt.show()

# Show limitation speed
def show_limitation(li_bisec, li_newton):
    x_range = max(len(li_bisec), len(li_newton))
    x = np.arange(1, x_range + 1, 1)
    y1 = np.array(li_bisec)
    y2 = np.array(li_newton)
    plt.plot(x[:len(li_bisec)], y1, '-')
    plt.plot(x[:len(li_newton)], y2, '-')
    plt.plot([1, x_range], [0, 0])
    plt.show()


if __name__ == '__main__':
    command = input("Which question do you want? (q3/q4) : ")
    if command[:2] == 'q3':
        draworcomp = input("Draw or compute? (draw/comp) : ")
        if draworcomp == 'draw':
            num = eval(input("Please enter function number: "))
            a = eval(input("Please enter lower bound: "))
            b = eval(input("Please enter upper bound: "))
            draw(fun_li[num - 1], a, b)
        elif draworcomp == 'comp':
            num = eval(input("Please enter function number: "))
            a = eval(input("Please enter lower bound: "))
            b = eval(input("Please enter upper bound: "))
            compare(fun_li[num - 1], dfun_li[num - 1], a, b, 0)      
        else:
            raise Exception("Invalid arguments!")      
    elif command[:2] == 'q4':
        compare(fun_li[3], dfun_li[3], 1, 2, 1)
        show_limitation(li_bisec, li_newton)   
    else:
        raise Exception("Invalid arguments!")