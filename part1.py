import numpy as np
import matplotlib.pyplot as plt
def getin_int(tempstr):
    return int(tempstr)

def getin_float(tempstr):
    return float(tempstr)
#分为浮点数和整形数读入输入的对应值

def generate_henonmap_xy(a,b,x,y,N):
    henon_setx = [x]
    henon_sety = [y]
    for i in range(0 ,N + 1):
        x ,y = 1 - a*x**2 + y ,b*x
        henon_setx.append(x)
        henon_sety.append(y)
    return henon_setx,henon_sety
#产生HenonMap
#为便于后续画图，此处输出的为上述形式

def generate_henonmap(henon_setx ,henon_sety):
    return list(zip(henon_setx ,henon_sety))
#这里生成正式的Henonmap

def output_orbit(henonmap, N):
    temp_list = henonmap
    for i in range(0 ,N + 1):
        print(temp_list[i])
#输出轨迹

def ploting_orbit_diagram(start,end,step,b,N):
    a = start
    while a <= end:
        A = [a]
        henon_setx = [x]
        for i in range(0,N+1):
            x ,y = 1 - a*x**2 + y ,b*x
            henon_setx.append(x)
            A.append(a)
        plt.plot(A,henon_setx,'*')
        a += step
#画出orbitdiagram
henon_x,henon_y = generate_henonmap_xy(1.2,0.3,0,0,10000)
output_orbit(generate_henonmap(henon_x,henon_y), 10000)




