#task 1:Bisection Function
import numpy as np
from numpy.polynomial import Polynomial

def f(x):
    # 输入系数，创建多项式函数（或者直接输入函数）
    coef = []  
    while input("Please input the coeffient of the polynomial:"):
        coef.append(input)
    polynomial = Polynomial(coef)
    return polynomial

def main():
    # 二分查找
    left = float(input("The left side:"))
    right = float(input("The right side:"))
    epsilon = float(input("The accuracy:"))
    while f(left)*f(right)>0:
        print("Wrong input.")#这个区间内没有零点或有多个零点
        left = float(input("The left side:"))
        right = float(input("The right side:"))
    mid = (left + right)/2
    while np.abs(f(mid)-0)>epsilon:
        if f(left)*f(mid)<0:
            left = left
            right = mid
        else:
            left = mid
            right = right
        mid = (left + right)/2
    print(mid)
    
    
#task 2:Newton Function
import numpy as np
from numpy.polynomial import Polynomial

def f(x):
    # 通过系数创建多项式函数，或直接输入
    coef = []  
    while input("Please input the coeffient of the polynomial:"):
        coef.append(input)
    polynomial = Polynomial(coef)
    return polynomial

def g(x):
    #对f(x)进行求导
    coef = []  
    while input("Please input the coeffient of the polynomial:"):
        coef.append(input)
    polynomial = Polynomial(coef)
    return polynomial.deriv()


def main():
    # 牛顿迭代
    x0 = float(input("The initial number:"))
    cnt = 0#初始迭代次数
    epsilon = float(input("The accuracy:"))
    while np.abs(f(x0)-0)>epsilon:
        x1 = x0 - f(x0)/g(x0)
        x0 = x1
        cnt = cnt + 1
    print(x0)


#task 3:using root function to solve equation
import numpy as np
from scipy.optimize import root #使用root函数
def func1(x):
    return 2*x - np.tan(x)
sol = root(func1,x0 = -0.2)

def func2(x):
    return np.exp(1+x)-2-x
sol = root(func2,x0 = -2)

import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
x = np.linspace(0.5,4*np.pi,100)
y = x**(-2) - np.sin(x)
plt.scatter(x,y)
f = interp1d(x,y,kind='linear')
x_dense = np.linspace(0.5,4*np.pi,100)
y_dense = f(x_dense)
plt.plot(x_dense,y_dense)
plt.show()#画出图像，得到各个根所在的区间

def func3(x):
    return x**(-2) - np.sin(x)
sol1 = root(func3,x0 = 1.0)
sol2 = root(func3,x0 = 3.0)
sol3 = root(func3,x0 = 6.0)
sol4 = root(func3,x0 = 9.7)
sol5 = root(func3,x0 = 12.1)

#task4:比较收敛速度

import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial

def f(x):
    return x**2 - 2

def main1():
    #创建两个列表，分别用来储存迭代次数和误差
    x_data1 = []
    y_data1 = []
    time1 = 0
    dis1 = 0
    left = 1.0
    right = 2.0
    final = np.sqrt(2)
    epsilon = np.e**(-10)
    while f(left)*f(right)>0:
        print("Wrong input.")
        left = float(input("The left side:"))
        right = float(input("The right side:"))
    mid = (left + right)/2
    while np.abs(f(mid)-0)>epsilon:
        if f(left)*f(mid)<0:
            left = left
            right = mid
        else:
            left = mid
            right = right
        mid1 = (left + right)/2
        time1 = time1 + 1
        dis1 = mid1 - final
        x_data1.append(time)
        y_data1.append(dis)
    print(mid)
    plt.scatter(x_data1,y_data1)
    plt.show()


import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial

def f(x):
    return x**2 - 2

def g(x):
    return 2*x 

def main2():
    #创建两个列表，分别用来储存迭代次数和误差
    x_data2 = []
    y_data2 = []
    dis2 = 0
    final = np.sqrt(2)
    x0 = 1.0
    cnt = 0
    epsilon = np.e**(-10)
    while np.abs(f(x0)-0)>epsilon:
        x1 = x0 - f(x0)/g(x0)
        x0 = x1
        cnt = cnt + 1
        dis2 = x0 - final
        x_data2.append(cnt)
        y_data2.append(dis2)
    print(x0)
    plt.scatter(x_data2,y_data2)
    plt.show()

