clear all
close all
num = 50;
u = linspace(0, 2*pi, num);
v = linspace(0, 2*pi, num);
[u, v] = meshgrid(u, v);
X = cos(v)*[6-(5/4+sin(3*u))*sin(u-3*v)];
Y = sin(v)*[6-(5/4+sin(3*u))*sin(u-3*v)];
Z = -cos(u-3*v)*(5/4+sin(3*u));
surf(X, Y, Z)
colormap(gca, 'jet')
axis equal