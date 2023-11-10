import numpy as np
from scipy.misc import derivative
import math
def f(x):
    return (math.sin(x))
def f_derive(x):
    return (derivative(f, x,dx=1e-6))

while True:
    x0=float(input("x0:"))
    if f_derive(x0)==0:
        continue
    else:
        break
e=float(input("目标误差："))
#e=1e-10
#print(f_derive(x0))

x1=x0-f(x0)/f_derive(x0)
d=math.fabs(x0-x1)
while d>=e:
    x0=x1
    x1=x0-f(x0)/f_derive(x0)
    d=math.fabs(x0-x1)
print("root=",x1)






