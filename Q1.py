
def bisection(f, a, b, epsilon):
    if f(a) * f(b) > 0:
        raise ValueError("Function values at interval endpoints must have opposite signs.")
    
    while (b - a) / 2 > epsilon:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    
    return (a + b) / 2

# 获取用户输入的方程表达式
equation_str = input("Enter the equation (in terms of 'x'): ")

# 定义目标函数
def f(x):
    return eval(equation_str, {'x': x})

# 初始区间 [a, b]
a = float(input("Enter the lower bound of the interval (a): "))
b = float(input("Enter the upper bound of the interval (b): "))

# 目标误差
epsilon = 1e-6

# 调用Bisection算法函数
root1 = bisection(f, a, b, epsilon)

# 输出第一个根的近似值
print("Approximate root: ", root1)





