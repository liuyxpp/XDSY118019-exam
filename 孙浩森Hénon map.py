import numpy as np
import matplotlib.pyplot as plt#引入需要用到的模块

def henon_map(a, b, u0, N): #计算 Hénon map 的轨迹
    '''
    参数:
        a (float): Hénon map 的参数 a
        b (float): Hénon map 的参数 b
        u0 (tuple): 初始值 (u0, v0)
        N (int): 轨迹长度
    返回:轨迹点的坐标
    '''
    u = np.zeros((N+1, 2))    #创建一个（N+1）*2的数组，用于存储轨迹点的坐标
    u[0] = np.array(u0)     #将初始值赋值给u[0]
    for i in range(N):      #将所给的方程表达出来，计算出u[i+1]的值
        u[i+1, 0] = 1 - a * u[i, 0]**2 + u[i, 1]
        u[i+1, 1] = b * u[i, 0]
    return u                #返回轨迹点的坐标

def plot_henon_trajectory(a, b, u0, N):    #定义一个函数，用于绘制Hénon map的轨迹图
    """
    参数:
        a (float): Hénon map 的参数 a
        b (float): Hénon map 的参数 b
        u0 (tuple): 初始值 (u0, v0)
        N (int): 轨迹长度
    """
    u = henon_map(a, b, u0, N)
    plt.plot(u[:,0], u[:,1], 'b.', markersize=1)#绘制轨迹图
    plt.title(f'Hénon map trajectory (a={a}, b={b}, u0={u0}, N={N})')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

def plot_orbit_diagram(b, a_min, a_max, N):    #定义一个函数，用于绘制Hénon map中a和x的关系图
    """
    参数:
        b (float): Hénon map 的参数 b
        a_min (float): 参数 a 的最小值
        a_max (float): 参数 a 的最大值
        N (int): 轨迹长度
    """
    a_values = np.linspace(a_min, a_max, 1000)#在给定的范围内生成1000个a的值
    for a in a_values:
        x_values = (henon_map(a, b, (0, 0), N))[N//2:,0]#计算Hénon map的轨迹，并取其中后半部分的x值
        plt.scatter([a]*len(x_values), x_values,c='k',s=0.00001)#绘制散点图
    plt.title(f'Hénon map orbit diagram (b={b}, a_min={a_min}, a_max={a_max}, N={N})')
    plt.xlabel('a')
    plt.ylabel('x')
    plt.show()                                   #显示图像

if __name__ == '__main__':

    # 计算经典 Hénon map 的轨迹并绘图
    plot_henon_trajectory(1.4, 0.3, (0, 0), 1000)

    # 绘制 Hénon map 的 orbit diagram
    plot_orbit_diagram(0.3, -0.1, 1.6, 1000)
    plot_orbit_diagram(0.3, 1, 1.1, 1000)
    plot_orbit_diagram(0.3, 1.5, 1.6, 1000)
    #找到范围中使轨迹收敛的a值1.525-1.530附近，1.091附近，1.081附近1.079附近1.0615附近，1.0678附近等等
    #以1.527为例画图
    plot_henon_trajectory(1.527, 0.3, (0, 0), 1000)
