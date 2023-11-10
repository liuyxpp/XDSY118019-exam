# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 18:51:19 2023

@author: 17124
"""
import math

def f(x):
    
    return (-2+x-x**2+x**3)

while True:
    x1=float(input("x1:"))
    x2=float(input("x2:"))
    if f(x1)*f(x2)<=0:
        break
    else:
        print("Please input again.")
        continue
if f(x1)==0:
    root=x1
    e=0
if f(x2)==0:
    root=x2
    e=0
    
else:
    d=math.fabs(x1-x2)
    cnt=0
    e=float(input("目标误差："))
    while d>=e:
        x0=(x1+x2)/2
        if f(x1)*f(x0)<0:
            x2=x0
        else:
            x1=x0
        d=math.fabs(x1-x2)
        cnt+=1
    print("root=",(x1+x2)/2,"迭代次数：",cnt)