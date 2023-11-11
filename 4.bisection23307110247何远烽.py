# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 20:59:10 2023

@author: 17124
"""

import math
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return (x**2-2)

epsilon=np.array([])
x1=1
x2=2
d=math.fabs(x1-x2)
epsilon=np.append(epsilon, d)
e=1e-10
cnt=0
while d>=e:
    x0=(x1+x2)/2
    if f(x1)*f(x0)<0:
        x2=x0
    else:
        x1=x0
    cnt+=1
    d=math.fabs(x1-x2)
    epsilon=np.append(epsilon, d)
print("root1=",(x1+x2)/2)
#print(epsilon)
n=np.array(range(0,cnt+1,1))
#print(n)
plt.plot(n,epsilon)