# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 20:46:16 2023

@author: 17124
"""

from scipy.misc import derivative
import math
def f(x):
    return (2*x-math.tan(x))
def f_derive(x):
    return (derivative(f, x,dx=1e-10))

x0=-0.2
e=1e-10

x1=x0-f(x0)/f_derive(x0)
d=math.fabs(x0-x1)
cnt=1
while d>=e:
    x0=x1
    x1=x0-f(x0)/f_derive(x0)
    d=math.fabs(x0-x1)
    cnt+=1
print("root1=",x1,"\n迭代次数：",cnt)

x0=1

x1=x0-f(x0)/f_derive(x0)
d=math.fabs(x0-x1)
cnt=1
while d>=e:
    x0=x1
    x1=x0-f(x0)/f_derive(x0)
    d=math.fabs(x0-x1)
    cnt+=1
print("root2=",x1,"\n迭代次数：",cnt)