import numpy as np
import matplotlib.pyplot as plt

def henon_map(a,b,u_0,N):
    u = [u_0]
    x = u_0[0]
    y = u_0[1]
    n =0
    while n <= N:
        x_new = 1-a*x**2+y
        y_new = b*x
        u_n = [x_new,y_new]
        u.append(u_n)
        x, y = x_new, y_new
        n = n+1
    return u

# #1
# a = float(input("请输入参数 a: "))
# b = float(input("请输入参数 b: "))
# x0 = float(input("请输入初始值 x0: "))
# y0 = float(input("请输入初始值 y0: "))
# N = int(input("请输入迭代次数 N: "))

# u_0 = [x0, y0]
# result = henon_map(a, b, u_0, N)
# print("Henon 映射结果:",result)

#2
N = int(input("请输入迭代次数 N: "))
result = henon_map(1.25, 0.3, [0,0], N)
print("Henon 映射结果:",result)
x = [sublist[0] for sublist in result]
y = [sublist[1] for sublist in result]
plt.plot(x, y,".-")
plt.show()


# #3
# a_n = np.linspace(1.0, 1.4, 401)
# x_values = []
# a_values = []
# for a in a_n:
#     result = henon_map(a, 0.3, [0,0], 10000)
#     x_values.append(result[-1][0])
#     a_values.append(a)

# plt.figure(figsize=(10, 6))
# plt.plot(a_values, x_values, 'k') 
# plt.xlabel('a')
# plt.ylabel('x')
# plt.title('Hénon Map Orbit Diagram')
# plt.show()
    