# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 20:53:06 2023

@author: 17124
"""

from scipy.misc import derivative
import math
def f(x):
    return (math.sin(x)-1/x**2)
def f_derive(x):
    return (derivative(f, x,dx=1e-10))

for i in range(5):
    x0=i*3+1
    e=1e-10

    x1=x0-f(x0)/f_derive(x0)
    d=math.fabs(x0-x1)
    while d>=e:
        x0=x1
        x1=x0-f(x0)/f_derive(x0)
        d=math.fabs(x0-x1)
    print("root",i+1,"=",x1)