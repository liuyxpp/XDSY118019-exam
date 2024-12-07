# 期末考试

## 第1题
```python
import numpy as np
import scipy.stats as stats
import scipy.optimize as optimize
import matplotlib.pyplot as plt

data = np.loadtxt('C:\Users\林朝夕\Desktop\uspop.txt', delimiter=',', dtype=float, skiprows=1)
x = data[:, 0]  # 存储第一列数据到变量x
y = data[:, 1]  # 存储第二列数据到变量y

# 线性拟合
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
linear_fit = slope * x + intercept

# 曲线拟合
def curve_func(x, a, c):
    return a * np.exp(c * x)

params, params_covariance = optimize.curve_fit(curve_func, x, y)
curve_fit = curve_func(x, params[0], params[1])

# 公式变换的线性拟合
x_transformed = x
y_transformed = np.log(y)
slope_transformed, intercept_transformed, r_value_transformed, p_value_transformed, std_err_transformed = stats.linregress(x_transformed, y_transformed)
linear_fit_transformed = slope_transformed * x_transformed + intercept_transformed

# 绘制图形
plt.plot(x, y, 'bo', label='Original Data')
plt.plot(x, linear_fit, 'r-', label='Linear Fit')
plt.plot(x, curve_fit, 'g-', label='Curve Fit')
plt.plot(x, np.exp(linear_fit_transformed), 'm--', label='Linear Fit (Transformed)')
plt.xlabel('Year')
plt.ylabel('Population')
plt.legend()
plt.show()
```


---

备注：老师我不知道为什么编辑器还是一直显示未定义loadtxt，上面代码应该没错但是运行不了。最后就暴力输入数据了。


---


```python
data = np.array([
[1990,248709873],
[1980,226545805],
[1970,203211926],
[1960,179323175],
[1950,150697361],
[1940,131669275],
[1930,122775046],
[1920,105710620],
[1910,91972266],
[1900,75994575],
[1890,62947714],
[1880,50155783],
[1870,38558371],
[1860,31443321],
[1850,23191876],
[1840,17063353],
[1830,12860702],
[1820,9638453],
[1810,7239881],
[1800,5308483],
[1790,3929214]])
x = data[:, 0]  # 存储第一列数据到变量x
y = data[:, 1]  # 存储第二列数据到变量y
```
![美国人口变化]("C:\Users\林朝夕\Desktop\population.png")
![美国人口变化]("C:\Users\林朝夕\Desktop\美国人口变化.png")

## 第2题
### (1)用Matlab中isosurface函数渲染绿色半径为1的球
```
% 创建一个网格
[x, y, z] = meshgrid(-1:0.1:1, -1:0.1:1, -1:0.1:1);

% 计算球体的等值函数
R = sqrt(x.^2 + y.^2 + z.^2);
isosurface = R <= 1;

% 绘制等值面并设置颜色
figure;
p = patch(isosurface, 'FaceColor', 'green', 'EdgeColor', 'none');
daspect([1 1 1]);  % 设置坐标轴比例一致
xlabel('X');
ylabel('Y');
zlabel('Z');
```
![绿色球体1]("C:\Users\林朝夕\Documents\MATLAB\sphere.fig")
![绿色球体2]("C:\Users\林朝夕\Desktop\图片1.png")

### （2）渲染红色的椭球面
```
% 定义椭球的参数
a = 2;  % 长轴
b = 1;  % 短轴
theta = linspace(0, 2*pi, 100);  % 角度范围

% 计算椭球的坐标
x = a * cos(theta);
y = b * sin(theta);
z = zeros(size(theta));

% 绘制椭球面
figure;
surf(x, y, z, 'FaceColor', 'red', 'EdgeColor', 'none');
axis equal;  % 设置坐标轴比例一致
xlabel('X');
ylabel('Y');
zlabel('Z');
```
![红色椭球1]("C:\Users\林朝夕\Documents\MATLAB\ellipsoid.fig")
![红色椭球2]("C:\Users\林朝夕\Desktop\图片2.png")

## 第3题

在mathematica中输入如下代码


**Integrate[Sin[x]-Sin[3x]+Sin[5x]/Cos[x]+Cos[3x]+Cos[5x],x]**


得到结果
$$
-\cos(x) + \frac{1}{3} \cos(3x) - \log(\cos(x)) + 2 \sin^2(x) - 4 \sin^4(x) + \frac{1}{3} \sin(3x) + \frac{1}{5} \sin(5x)
$$


## 第4题
# **Lorenz Attractor**

The Lorenz attractor is an <span style="color: blue;">attractor</span> that arises in a simplified system of equations describing the two-dimensional flow of fluid. ln the early 1960s, Lorenz accidentally discovered the chaotic behavior of this system when he found that, for a simplified system, periodic solutions of the form.

$$
\psi = \psi_0 \sin\left(\frac{\pi ax}{H}\right) \sin\left(\frac{\pi z}{H}\right)
$$

$$
\theta = \theta_0 \cos\left(\frac{\pi ax}{H}\right) \sin\left(\frac{\pi z}{H}\right)
$$

grew for Rayleigh numbers larger than the critical value, $Ra > Rac$. Furthermore, vastly different results were obtained for very small changes in the initial values, representing one of the earliest discoveries of the so-called <span style="color: blue;">butterfly effect.</span>

Lorenz obtained the simplified equations

$$
\dot{X} = \sigma\left(Y-X\right)
$$

$$
\dot{Y} = X\left(\rho-Z\right)
$$

$$
\dot{Z} = XY - \beta Z
$$

now known as the Lorenz equation.

