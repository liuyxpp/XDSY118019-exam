### PART 2

#### Q1.

详见`part2_q1.ipynb`



#### Q2.

Input:
`Integrate[(Sin[x] - Sin[3*x] + Sin[5*x])/(Cos[x] + Cos[3*x] + Cos[5*x]),x]`
Output:
`-Log(Cos[x])`

![image-20231116184346300](C:\Users\HP\AppData\Roaming\Typora\typora-user-images\image-20231116184346300.png)



#### Q3.

```matlab
[x,y,z]=meshgrid(-1:0.1:1); isosurface(x,y,z,x.^2+y.^2+z.^2-1,0); axis equal; colormap summer
```

![image-20231116190040769](C:\Users\HP\AppData\Roaming\Typora\typora-user-images\image-20231116190040769.png)

```matlab
[x,y,z] = meshgrid(-1:0.1:1,-1:0.1:1,-1:0.1:1); a = 2; b = 1; V = (x.^2/a^2 + y.^2/b^2 + z.^2/b^2); isosurface(x,y,z,V,1); axis equal; colormap([1 0 0])
```

![image-20231116190124143](C:\Users\HP\AppData\Roaming\Typora\typora-user-images\image-20231116190124143.png)



#### Q4.

# Lorenz Attractor

The Lorenz attractor is an [attractor](https://mathworld.wolfram.com/Attractor.html) that arises in a simplified system of equations describing the two-dimensional flow of fluid. In the early 1960s, Lorenz accidentally discovered the chaotic behavior of this system when he found that, for a simplified system, periodic solutions of the form

$$\psi = \psi_0 \sin\left(\frac{\pi ax}{H}\right)\sin\left(\frac{\pi z}{H}\right)$$

$$\theta = \theta_0 \cos\left(\frac{\pi ax}{H}\right)\sin\left(\frac{\pi z}{H}\right)$$

grew for Rayleigh numbers larger than the critical value, $Ra>Ra_c$. Furthermore, vastly different results were obtained for very small changes in the initial values, representing one of the earliest discoveries of the so-called [butterfly effect](https://mathworld.wolfram.com/ButterflyEffect.html).

Lorenz obtained the simplified equations

$$\dot{X} = \sigma(Y-X)$$

$$\dot{Y} = X(\rho-Z)-Y$$

$$\dot{Z} = XY-\beta Z$$

now known as the Lorenz equations.

