# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 20:23:24 2023

@author: 17124
"""

import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return (np.sin(x)-1/x**2)
x = np.arange(0.5,4*np.pi, 0.01)
plt.plot(x, f(x))
plt.plot([0.5,4*np.pi], [0, 0])

from scipy.optimize import root_scalar
#from scipy.optimize import root

x1=root_scalar(f, bracket=[0.5, 2], method='bisect')
print(x1)
x2=root_scalar(f, bracket=[2,4], method='bisect')
print(x2)
x3=root_scalar(f, bracket=[4,8], method='bisect')
print(x3)
x4=root_scalar(f, bracket=[8,11], method='bisect')
print(x4)
#x5=root_scalar(f, bracket=[11,4*np.pi], method='bisect')
#print(x5)