Solution to Part II
==================
Q1：
---
初始代码的分析：无法读入连续的文件名，比如下面的测试点给出的那样
- 1.分析代码功能,将文件中的名称和数字分开，数字后有'n'代表数字为负数
- 2.测试点:phi0.1 xN14.2 kappa0.5n
a1 b14n n0 c0.2 phi0.1_xN14.2 phi0.1_xN14.2_kappa0.5n a1_b14n n0_c0.2
- 3 并没有完成任务但是附上代码

Q2：
---
>画图的代码:
```
[a,b] = meshgrid(0:0.01:2*pi,0:0.01:2*pi);
x = (3 + cos(b)).*cos(a);
y = (3 + cos(b)).*sin(a);
z = sin(b);
surf(x,y,z);
```
>最终的图像：在附件中(此处难以导入)

Q3:
---
- 1.代码:
```
Sum[1/(n^3+n^2),{n,1,Infinity}]
```
最终的结果:$\frac{\pi^2}{6}-1$
- 2.代码:
```
Integrate[(x^0.5)*Log[x]/(x + 1)^2, {x, 0, Infinity}]
```
最终的结果:$\pi$

Q4:
---
 <font face="Sylfaen" font size = 4>$\mathbf{Q:}$ Find the solution of the following equation with respect to $\theta$:$${Acos\theta+Bcos\theta+C}$$ $\mathbf{A:}$ 
let$x_1 = cos\theta$ and $x_2 = sin\theta$ then the solution is given by the intersection of the circle and the line:$$x_1^2+x_2^2 = 1$$ $$Ax_1+Bx_2+C=0$$We reformulate the equations in a parametric form:$$|\mathbf{x}|^2 = 1$$ $$\mathbf{x}(t)=\mathbf{a}+t\mathbf{b}$$ where $\mathbf{x} = (x_1,x_2)$,$\mathbf{a}=(0,-C/B)$,$\mathbf{b}=(-C/A,C/B)$,and $t$ is a parameter. The intersection points satisfythe following equation:$$|\mathbf{a}+t\mathbf{b}|^2= 1$$ 
which can be solved for 𝑡 to find the intersection points:$$t_{1,2}=\frac{-\mathbf{a}*\mathbf{b}\pm\sqrt{(\mathbf{a}*\mathbf{b})^2-|\mathbf{b}|^2(|\mathbf{a}|^2-1)}}{|\mathbf{b}|^2}$$

</font>