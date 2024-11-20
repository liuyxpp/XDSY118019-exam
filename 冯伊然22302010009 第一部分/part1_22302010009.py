# 冯伊然 22302010009
import matplotlib.pyplot as plt


# Henon map函数
def henon_map(a, b):
    def f(x, y):
        return 1 - a * x * x + y, b * x
    return f


# 输入函数f、初始值u0和轨迹长度N，返回point_list = [u0, u1, ..., uN]
def trajectory(f, u0, N):
    point_list = [u0]
    x, y = u0
    for i in range(N):
        x, y = f(x, y)
        point_list.append((x, y))
    return point_list


# 将轨迹point_list = [u0, u1, ..., uN]绘制成散点图
def plot_trajectory(point_list):
    x = [point[0] for point in point_list]
    y = [point[1] for point in point_list]
    plt.scatter(x, y, c="blue", s=0.1)
    plt.show()


# 主函数
if __name__ == '__main__':
    a = 1.4
    b = 0.3
    u0 = (0, 0)
    N = 10000
    a_list = [1.04, 1.24, 1.302, 1.422]

    # 1. 输出轨迹[u0, ..., uN]
    print(trajectory(henon_map(a, b), u0, N))

    # 2. 绘制a=1.4, b=0.3, u0=(0, 0)时的轨迹图
    plot_trajectory(trajectory(henon_map(a, b), u0, N))

    # 3. 改变a时绘制orbit diagram
    for a in a_list:
        point_list = trajectory(henon_map(a, b), u0, N)
        point_list = point_list[N//2:]                  # 丢弃前一半的点
        point_list = [point[0] for point in point_list] # 只取x坐标
        plt.scatter([a] * len(point_list), point_list, c="blue", s=0.1)
    plt.show()

    # 4. 画出使henon map收敛为周期数列的a对应的轨迹图
    for a in a_list:
        plot_trajectory(trajectory(henon_map(a, b), u0, N))


# 结果: -0.12~1.05, 1.23~1.25, 1.300~1.304, 1.4219~1.4221的a导致周期轨道