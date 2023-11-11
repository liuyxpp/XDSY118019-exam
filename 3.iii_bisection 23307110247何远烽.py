# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 20:37:03 2023

@author: 17124
"""
import math
def f(x):
    return (math.sin(x)-1/x**2)
for i in range(5):
    
    x1=i*math.pi-1
    x2=(i+1)*math.pi-1
    d=math.fabs(x1-x2)
    
    e=1e-10
    while d>=e:
        x0=(x1+x2)/2
        if f(x1)*f(x2)>0:
            print("无法用二分法求根。")
        if f(x1)*f(x0)<0:
            x2=x0
        else:
            x1=x0
        d=math.fabs(x1-x2)
    
    print("root",i+1,"=",(x1+x2)/2)