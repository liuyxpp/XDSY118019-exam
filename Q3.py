import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

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

def newton_method(f, df, x0, epsilon):
    x = x0
    while abs(f(x)) > epsilon:
        x = x - f(x) / df(x)
    return x

# Define the functions and their derivatives
def f1(x):
    return 2 * x - np.tan(x)

def df1(x):
    return 2 - (1 / (np.cos(x) ** 2))

def f2(x):
    return np.exp(x + 1) - 2 - x

def df2(x):
    return np.exp(x + 1) - 1

def f3(x):
    return 1/x**(2) - np.sin(x)

def df3(x):
    return -2*x**(-3) - np.cos(x)

# i. 2x = tan(x), x ∈ [-0.2, 1.4]
root1_1_bisection = bisection(f1, -0.2, 0.2, 1e-10)
root1_2_bisection = bisection(f1, 0.2, 1.4,1e-10)
root1_1_scipy = fsolve(f1,0)
root1_2_scipy = fsolve(f1,1.1)
root1_1_newton = newton_method(f1, df1, 0, 1e-10)
root1_2_newton = newton_method(f1, df1, 1, 1e-10)

# ii. exp(x+1) = 2 + x, x ∈ [-2, 2]
root2_bisection = bisection(f2, -1, -1, 1e-10)
root2_scipy = fsolve(f2,-1)
root2_newton = newton_method(f2, df2, 0, 1e-10)

# iii. x - 2 = sin(x), x ∈ [0.5, 4π]
root3_1_bisection = bisection(f3, 0.5, 2, 1e-10)
root3_2_bisection = bisection(f3, 2, 4, 1e-10)
root3_3_bisection = bisection(f3, 6, 8, 1e-10)
root3_4_bisection = bisection(f3, 8, 10, 1e-10)

root3_1_scipy = fsolve(f3, 0.5)
root3_2_scipy = fsolve(f3, 3)
root3_3_scipy = fsolve(f3, 6)
root3_4_scipy = fsolve(f3, 9)

root3_1_newton = newton_method(f3, df3, 0.5, 1e-10)
root3_2_newton = newton_method(f3, df3, 3, 1e-10)
root3_3_newton = newton_method(f3, df3, 6, 1e-10)
root3_4_newton = newton_method(f3, df3, 9, 1e-10)

# Output the results
print("i. 2x = tan(x):")
print("Bisection result:", root1_1_bisection, root1_2_bisection)
print("Scipy result:", root1_1_scipy, root1_2_scipy)
print("Newton result:", root1_1_newton, root1_2_newton)

print("\nii. exp(x+1) = 2 + x:")
print("Bisection result:", root2_bisection)
print("Scipy result:", root2_scipy)
print("Newton result:", root2_newton)

print("\niii. x - 2 = sin(x):")
print("Bisection result:", root3_1_bisection,root3_2_bisection,root3_3_bisection,root3_4_bisection)
print("Scipy result:", root3_1_scipy,root3_2_scipy,root3_3_scipy,root3_4_scipy)
print("Newton result:", root3_1_newton,root3_2_newton,root3_3_newton,root3_4_newton)
