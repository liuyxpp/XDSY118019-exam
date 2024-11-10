#实现hemon_map函数
#谭芃容睿24301020064

##定义hemon_map函数
def h(a,b):
    def f(x,y):
        return 1-a*x**2+y,b*x
    return f

##输出轨迹
def orbit(f,u0,N):
    x,y = u0
    orbit=[u0]
    for i in range(1,N+1):
        x,y = f(x,y)
        orbit.append((x,y))
    return orbit

##计算经典轨迹并绘图
import matplotlib.pyplot as plt

def classical_orbit():
    classical_orbit=orbit(h(1.4,0.3),(0,0),10000)
#输出轨迹并直接打印
    x=[orbits0[0] for orbits0 in classical_orbit]
    y=[orbits1[1] for orbits1 in classical_orbit]
    plt.scatter(x,y)
    plt.show()
#画出散点图

    return print(classical_orbit)

##绘制orbit digram，假设a的范围为1~2，步长为0.01
a_list=[a*0.01 for a in range(100,201)]
for a in a_list:
    b=0.3
    orbit1=orbit(h(a,b),(0,0),1000)
    x=[orbits[0] for orbits in orbit1]
    y=[orbits[1] for orbits in orbit1]
    plt.scatter([a]*len(x),x)
  
#plt.show

##找到使原函数收敛的a值
#for a in a_list:
    for i in range(1,len(orbit1)):
        if x[i]==x[0] and y[i]==y[0]:
            print(a)
            plt.scatter(x,y)
            plt.show()
            break
    
    

