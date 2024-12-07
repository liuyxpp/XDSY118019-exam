# final
# 1
```python
import numpy as np

  

data = np.loadtxt("uspop.txt")

x = data[:, 0] # 年份

y = data[:, 1] # 人口数
from scipy.stats import linregress

import matplotlib.pyplot as plt

  

slope, intercept, r_value, p_value, std_err = linregress(x, y)

plt.plot(x, y, 'o', label='original data')

plt.plot(x, intercept + slope*x, 'r', label='fitted line')

plt.legend()

plt.show()

```
![[Pasted image 20231116200910.png]]

```python
from scipy.optimize import curve_fit

  

def func(x, a, c):

    return a * np.exp(c * x)

x_scaled = x / 1000

y_scaled = y / 1e6

popt, pcov = curve_fit(func, x_scaled, y_scaled)

a_scaled, c_scaled = popt

a = a_scaled * 1e6  

c = c_scaled / 1000

  

y_fit = func(x, a, c)

  

plt.plot(x, y_fit,label='fitted line')

plt.scatter(x, y, label='Original Data')

plt.legend()

plt.show()
```
![[Pasted image 20231116201039.png]]
```python
y_log = np.log(y)

slope, intercept, r_value, p_value, std_err = linregress(x, y_log)

a = np.exp(intercept)

c = slope

  

plt.plot(x, y, 'o', label='original data')

plt.plot(x, a * np.exp(c * x), 'r', label='transform linear fitted line')

plt.plot(x, y_fit,label='fitted line')

plt.legend()

plt.show()
```
![[Pasted image 20231116201128.png]]
# 2

```matlab
%球面
% 创建一个网格
[x, y, z] = meshgrid(-1:0.1:1, -1:0.1:1, -1:0.1:1);

% 计算球面的方程
radius = sqrt(x.^2 + y.^2 + z.^2);

% 创建球面
isosurface(x, y, z, radius, 1);

% 设置球面颜色为绿色
colormap([0 1 0]);

% 添加标题和标签
title('Sphere Surface');
xlabel('X');
ylabel('Y');
zlabel('Z');

% 显示图形
axis equal;
grid on;
%椭球
% 创建一个网格
[x, y, z] = meshgrid(-1:0.1:1, -1:0.1:1, -1:0.1:1);

% 计算球面的方程
radius = sqrt(x.^2 + y.^2 + z.^2);

% 创建球面
isosurface(x, y, z, radius, 1);

% 设置球面颜色为绿色
colormap([0 1 0]);

% 添加标题和标签
title('Sphere Surface');
xlabel('X');
ylabel('Y');
zlabel('Z');

% 显示图形
axis equal;
grid on;
% 椭球面
 % 创建一个网格
[x, y, z] = meshgrid(-2:0.1:2, -1:0.1:1, -1:0.1:1);

% 定义椭球的参数
a = 2; % 长轴
b = 1; % 短轴

% 计算椭球面的方程
equation = (x.^2)/(a^2) + (y.^2)/(b^2) + (z.^2)/(b^2) - 1;

% 创建椭球面
isosurface(x, y, z, equation, 0);

% 设置椭球面颜色为红色
colormap([1 0 0]);

% 添加标题和标签
title('Ellipsoid Surface');
xlabel('X');
ylabel('Y');
zlabel('Z');

% 显示图形
axis equal;
grid on;
```
![[球 1.jpg]]![[椭球面.jpg]]
# 3
```Mathematica
Integrate[(Sin[x] - Sin[3x] + Sin[5x]) / (Cos[x] + Cos[3x] + Cos[5x]), x]
```

![[Pasted image 20231116185318.png]]
# 4
# Lorenz Attractor
<font size=3>The Lorenz <a href="https://mathworld.wolfram.com/Attractor.html" style="color: #007bff;">attractor</a> is an attractor that arises in a simplified system of equations describing the two-dimensional flow of fluid. In the early 1960s, Lorenz accidentally discovered the chaotic behavior of this system when he found that, for a simplified system, periodic solutions of the form

$$\psi=\psi_0sin(\frac{\pi ax}{H})sin(\frac{\pi z}{H})$$
$$\theta=\theta_0cos(\frac{\pi ax}{H})sin(\frac{\pi z}{H})$$
<font size=3>grew for Rayleigh numbers larger than the critical value,$R$$a$>$R$$a_c$.Furthermore, vastly different results were obtained for very small changes in the initial values, representing one of the earliest discoveries of the so-called  <a href="https://mathworld.wolfram.com/ButterflyEffect.html" style="color: #007bff;">butterfly effect</a>.
<font size=3>Lorenz obtained the simplified equations

$$\
\begin{align*}
\dot{X} &= \sigma(Y - X) \\
\dot{Y} &= X(\rho - Z) - Y \\
\dot{Z} &= XY - \beta Z
\end{align*}
$$
<font size=3>
now known as the Lorenz equations.



