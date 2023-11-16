import scipy.optimize
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

def func(x, a, c):
    return a * np.exp(c * x)

def fun(x, k, b):
    return b + k * x


def line_fit(x,y):
    res = stats.linregress(x, y)
    plt.plot(x, y, 'o', label='original data')
    plt.plot(x, fun(x, res.slope, res.intercept), 'r', label='fitted line')
    print("ln(y) = ", res.slope, " * x + ", res.intercept)
    plt.legend()
    # plt.show()
def curve_fit(xdata, ydata):
    plt.plot(xdata, ydata, 'o', label='original data')
    popt= scipy.optimize.curve_fit(func, xdata, ydata, bounds=(-10,10))
    plt.plot(xdata, func(xdata, popt[0][0], popt[0][1]), label='fitted curve')
    print("y =", popt[0][0], " * e^(",popt[0][1], " * x)")
    # plt.show()

x, y = np.loadtxt('uspop.txt', delimiter=' ', usecols=(0, 1), unpack=True)

line_fit(x, y)
curve_fit(x, y)
plt.show()
line_fit(x, np.log(y))
plt.show()
