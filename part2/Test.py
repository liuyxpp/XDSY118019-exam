import numpy as np
from scipy import *
import matplotlib.pyplot as plt

# 第一题
x, y = np.loadtxt('uspop.txt', delimiter=' ', usecols=(0, 1), unpack=True)

# 第二题
def linregeress(x, y):
    res = stats.linregress(x, y)
    def fun(x):  # 拟合后的线性函数
        return res.intercept + res.slope * x

    plt.plot(x, y, 'o', label='original data')  # 原数据标点
    plt.plot(x, fun(x), 'r', label='fitted line')  # 拟合直线
    plt.legend()
    plt.show()

linregeress(x, y)

# 第三题
def func(x, a, c):
    return a * np.exp(c * x)


def curve_fit(xdata, ydata):
    plt.plot(xdata, ydata, 'o', label='data')
    popt = optimize.curve_fit(func, xdata, ydata, bounds=(-10, 10))  # 拟合方程，参数包括func，xdata，ydata，
    # plot出拟合曲线，其中的y使用拟合方程和xdata求出
    plt.plot(xdata, func(xdata, popt[0][0], popt[0][1]), label='fitted curve')
    plt.legend()
    plt.show()


curve_fit(x, y)

# 第四题
linregeress(x, np.log(y))

# if __name__ == '__main__':
