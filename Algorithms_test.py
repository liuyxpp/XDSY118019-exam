import numpy as np
from scipy import *
import matplotlib.pyplot as plt
from Algorithms import *
import math


def function1(x):
    return 2 * x - np.tan(x)


def function2(x):
    return np.exp(x + 1) - x - 2


def function3(x):
    return (x ** 2) * np.sin(x) - 1


def function4(x):
    return (x ** 2) - 2


funcs = [function1, function2, function3]


def dfunction1(x):
    return misc.derivative(function1, x, dx=1e-10)


def dfunction2(x):
    return misc.derivative(function2, x, dx=1e-10)


def dfunction3(x):
    return misc.derivative(function3, x, dx=1e-10)


def dfunction4(x):
    return 2 * x


dfuncs = [dfunction1, dfunction2, dfunction3]


def algorithms_comparation(func, dfunc, a, b, epsilon):
    #  for i in range(len(func)):
    print(f"Scipy.optimize.root gives answer: "
          f"{optimize.root(func, (a + b) / 2)}")
    print(f"My Bisection algorithm gives answer: "
          f"{bisection(func, a, b, epsilon, 0, False)}")
    print(f"optimize.bisect gives answer: "
          f"{optimize.bisect(func, a, b, xtol=epsilon)}")
    print(f"My Newton algorithm gives answer: "
          f"{newton(func, dfunc, (a + b) / 2, epsilon, 0, False)}")
    print(f"optimize.newton gives answer: "
          f"{optimize.newton(func, (a + b) / 2, tol=epsilon)}")


def question3_test():
    print('------ Question3 Test ------')
    while True:
        i = eval(input("input the number of function to be tested (1-3): "))
        if i >= 1 and i <= 3:
            break
        print("!!! wrong index number, please enter again !!!")
    print(f"--- function{i} test ---")
    a = eval(input("input lower bound (a) :"))
    b = eval(input("input upper bound (b) :"))
    algorithms_comparation(funcs[i - 1], dfuncs[i - 1], a, b, 1e-10)


def question4_test():
    print('------ Question4 Test ------')
    # Bisection算法每次迭代后的收敛序列
    bisection_error_list = bisection(function4, 1, 2, 1e-10, math.sqrt(2), True)
    bi_len = len(bisection_error_list)
    # Newton算法每次迭代后的收敛序列
    newton_error_list = newton(function4, dfunction4, 1.5, 1e-10, math.sqrt(2), True)
    new_len = len(newton_error_list)

    iterator_times_max = max(bi_len, new_len)  # 两个算法进行迭代的最大次数

    print(f"Bisection algorithm iterations: {bisection_error_list}")
    print(f"Newton algorithm iterations: {newton_error_list}")

    x = np.arange(1, iterator_times_max + 1, 1)
    y1 = np.array(bisection_error_list)
    y2 = np.array(newton_error_list)

    plt.figure(1)
    plt.plot(x[:bi_len], y1, label='Bisection', marker='o')  # Bisection算法的收敛曲线
    plt.plot(x[:new_len], y2, label='Newton', marker='o')  # Newton算法的收敛曲线
    plt.plot([0, iterator_times_max], [0, 0], linestyle='--')  # 恒为0的标准线
    plt.legend()
    plt.show()


if __name__ == '__main__':
    while True:
        choice = input("Input the question you want to solve (3 / 4):")
        if choice != '3' and choice != '4':
            input('Invalid input, enter again.')
        elif choice == '3':
            question3_test()
        else:
            question4_test()