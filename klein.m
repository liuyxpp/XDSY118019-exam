% klein.m — Klein bottle rendered with surf
[u,v] = meshgrid(linspace(0,2*pi,160), linspace(0,2*pi,100));
X = -(2/15).*cos(u).*(3.*cos(v)-30.*sin(u)+90.*cos(u).^4.*sin(u) ...
    -60.*cos(u).^6.*sin(u)+5.*cos(u).*cos(v).*sin(u));
Y = -(1/15).*sin(u).*(3.*cos(v)-3.*cos(u).^2.*cos(v) ...
    -48.*cos(u).^4.*cos(v)+48.*cos(u).^6.*cos(v)-60.*sin(u) ...
    +5.*cos(u).*cos(v).*sin(u)-5.*cos(u).^3.*cos(v).*sin(u) ...
    -80.*cos(u).^5.*cos(v).*sin(u)+80.*cos(u).^7.*cos(v).*sin(u));
Z = (2/15).*(3+5.*cos(u).*sin(u)).*sin(v);
surf(X,Y,Z);
shading interp; axis equal;
xlabel('x'); ylabel('y'); zlabel('z');
title('Klein bottle');
saveas(gcf,'klein_bottle.png');
