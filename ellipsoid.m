[x,y,z]=meshgrid(-2:0.1:2);
isosurface(x,y,z,x.^2/4+y.^2+z.^2-1,0,'red')
colormap([1 0 0])
axis equal