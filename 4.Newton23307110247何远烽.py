# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 21:37:06 2023

@author: 17124
"""

from scipy.misc import derivative
import math
def f(x):
    return (x**2-2)
def f_derive(x):
    return (derivative(f, x,dx=1e-10))

x0=1
e=1e-10

x1=x0-f(x0)/f_derive(x0)
d=math.fabs(x0-x1)
cnt=1
while d>=e:
    x0=x1
    x1=x0-f(x0)/f_derive(x0)
    d=math.fabs(x0-x1)
    cnt+=1
print("root=",x1,"\n迭代次数：",cnt)

