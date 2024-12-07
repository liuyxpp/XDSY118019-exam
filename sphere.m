[x,y,z]=meshgrid(-1:0.1:1);
isosurface(x,y,z,x.^2+y.^2+z.^2-1,0)
colormap("jet")

axis equal
