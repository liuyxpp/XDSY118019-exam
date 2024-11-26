[a,b] = meshgrid(0:0.01:2*pi,0:0.01:2*pi);
x = (3 + cos(b)).*cos(a);
y = (3 + cos(b)).*sin(a);
z = sin(b);
surf(x,y,z);

