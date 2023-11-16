import numpy as np
from scipy.stats import linregress
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = "SimHei"
plt.rcParams['axes.unicode_minus'] = False

data = np.loadtxt('uspop.txt')
x = data[:, 0]
y = data[:, 1]
result = linregress(x, y)
k, b, r, p, std_err = result


def func1(x, a, c):
    return a * np.exp(c * x)


def func2(x, a, c):
    return c * x + a


params1, _ = curve_fit(func1, x, y, p0=[np.exp(-21.5789), 0.020758])
a1, c1 = params1
params2, _ = curve_fit(func2, x, np.log(y))
a2, c2 = params2

x_ = np.arange(1780, 2000, 1)
y_1 = k * x_ + b
y_2 = func1(x_, a1, c1)
y_3 = np.exp(func2(x_, a2, c2))

plt.figure(figsize=(16, 3.5))
plt.subplot(1, 4, 1)
plt.plot(x, y, label="原始数据")
plt.plot(x_, y_1, label="直线拟合")
plt.plot(x_, y_2, label="y-exp(x)拟合")
plt.plot(x_, y_3, label="lny-x拟合")
plt.legend()

plt.subplot(1, 4, 2)
plt.plot(x, y, label="原始数据")
plt.plot(x_, y_1, label="直线拟合")
plt.legend()

plt.subplot(1, 4, 3)
plt.plot(x, y, label="原始数据")
plt.plot(x_, y_2, label="y-exp(x)拟合")
plt.legend()

plt.subplot(1, 4, 4)
plt.plot(x, y, label="原始数据")
plt.plot(x_, y_3, label="lny-x拟合")
plt.legend()
plt.show()
