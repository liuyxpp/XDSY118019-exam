# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 20:30:40 2023

@author: 17124
"""

import math

def f(x):
    return (2*x-math.tan(x))

x1=-0.2
x2=1
d=math.fabs(x1-x2)
    
e=1e-10
while d>=e:
    x0=(x1+x2)/2
    if f(x1)*f(x0)<0:
        x2=x0
    else:
        x1=x0
    d=math.fabs(x1-x2)
print("root1=",(x1+x2)/2,"\nin fact,root1=0.")

x1=1
x2=1.4
d=math.fabs(x1-x2)
    
e=1e-10
while d>=e:
    x0=(x1+x2)/2
    if f(x1)*f(x0)<0:
        x2=x0
    else:
        x1=x0
    d=math.fabs(x1-x2)
print("root2=",(x1+x2)/2)