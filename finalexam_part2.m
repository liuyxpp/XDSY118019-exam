% finalexam-part2
R = 3; r = 0.7;

[u, v] = meshgrid(-0.7:0.1:0.7, 0:0.1:2*pi);

x = (R + u.*cos(v/2)) .* cos(v);
y = (R + u.*cos(v/2)) .* sin(v);
z = u .* sin(v/2);

surf(x, y, z);