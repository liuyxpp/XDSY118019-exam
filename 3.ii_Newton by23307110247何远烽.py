# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 20:12:32 2023

@author: 17124
"""

from scipy.misc import derivative
import math
def f(x):
    return (math.exp(x+1)-2-x)
def f_derive(x):
    return (derivative(f, x,dx=1e-6))


x0=2


e=1e-10
#print(f_derive(x0))

x1=x0-f(x0)/f_derive(x0)
d=math.fabs(x0-x1)
while d>=e:
    x0=x1
    x1=x0-f(x0)/f_derive(x0)
    d=math.fabs(x0-x1)
print("root=",x1)