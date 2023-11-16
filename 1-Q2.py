# # 修正后的Newton算法
# def newton_method(f, df, x0, epsilon):
#     x = x0
#     while abs(f(x)) > epsilon:
#         x = x - f(x) / df(x)
#     return x

# # 修正后的目标函数和其导数
# def f(x):
#     return 3*x-2

# def df(x):
#     return 3

# # 初始估计值
# x0 = 2

# # 目标误差
# epsilon = 1e-6

# # 调用修正后的Newton算法函数
# root = newton_method(f, df, x0, epsilon)

# # 输出根的近似值
# print("Approximate root: ", root)

# 修正后的Newton算法
def newton_method(f, df, x0, epsilon):
    x = x0
    while abs(f(x)) > epsilon:
        x = x - f(x) / df(x)
    return x

# 获取用户输入的目标函数和其导数表达式
equation_str = input("Enter the function (in terms of 'x'): ")
derivative_str = input("Enter the derivative of the function (in terms of 'x'): ")

# 定义目标函数和其导数
def f(x):
    return eval(equation_str, {'x': x})

def df(x):
    return eval(derivative_str, {'x': x})

# 初始估计值
x0 = float(input("Enter the initial guess (x0): "))

# 目标误差
epsilon = 1e-6

# 调用修正后的Newton算法函数
root = newton_method(f, df, x0, epsilon)

# 输出根的近似值
print("Approximate root: ", root)
