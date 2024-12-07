# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 18:35:20 2023

@author: 17124
"""

import numpy as np

from scipy import stats

from scipy.optimize import curve_fit

import matplotlib.pyplot as plt

data=np.loadtxt('C:/Users/17124/Desktop/python/exam2/uspop.txt')
#print(data)
x=data[:,0]
y=data[:,1]

#print(x,y)
res=stats.linregress(x,y)

plt.plot(x, y, 'o', label='original data')
plt.plot(x, res.intercept + res.slope*x, 'r', label='fitting result')
plt.legend()
plt.show()

def func(x, a, c):
    return a * np.exp(c * x)

popt, pcov = curve_fit(func, x, y)
print(popt)
plt.plot(x, func(x, *popt), 'r-')
plt.xlabel('x')
plt.ylabel('y')
plt.plot(x, y, 'b-', label='original data')

plt.legend()
plt.show()

res1=stats.linregress(x,np.log(y))

plt.plot(x, y, 'o', label='original data')
plt.plot(x, np.exp(res1.intercept + res1.slope*x), 'r', label='fitting result')
plt.legend()
plt.show()
