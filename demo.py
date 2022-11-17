# @Time:2022/11/10 18:28
# @Author: 梁浩渤
# @File:kaolazi.py
# @Software:PyCharm

n = int(input("请输入一个正整数n："))
a = n
t = ""
while True:
    if a % 2 == 0 and a != 2:
        a= a / 2
        t = t + str(int(a)) + ","
        continue
    if a % 2 != 0 and a != 1:
        a = 3 * a + 1
        t = t + str(int(a)) + ","
        continue
    if a == 2:
        a = a / 2
        t = t + str(int(a))
        break
    if a == 1:
        t = t + str(int(a))
        break

print(f"n={a}的考拉兹序列为：{t}")


import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline


plt.rcParams['axes.unicode_minus']=False


x = np.linspace(0, 10000000, 10000000)


nodeyState=np.array(list(eval(t)))
nodexState=np.array(list(range(1,len(t)+1)))


model0=make_interp_spline(times,nodeyState)
ys0=model0(x)


plt.plot(x,ys0,color='red',label='Node 0')


plt.legend()
plt.show()




