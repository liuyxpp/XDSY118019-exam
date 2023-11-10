# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 20:08:55 2023

@author: 17124
"""

import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return (np.exp(x+1)-2-x)
x = np.arange(-1.5, 1.5, 0.01)
plt.plot(x, f(x))
plt.plot([-2, 2], [0, 0])

from scipy.optimize import root_scalar
#from scipy.optimize import root

x0=root_scalar(f, bracket=[-2, 2], method='brentq')
print(x0)
