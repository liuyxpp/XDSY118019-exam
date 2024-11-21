% 定义参数  
R = 3; % 大半径  
r = 1; % 小半径  

% 生成角度网格  
theta = linspace(0, 2*pi, 30); % θ 的范围  
phi = linspace(0, 2*pi, 30); % φ 的范围  
[Theta, Phi] = meshgrid(theta, phi); % 生成网格  

% 计算 x, y, z 坐标  
X = (R + r * cos(Theta)) .* cos(Phi);  
Y = (R + r * cos(Theta)) .* sin(Phi);  
Z = r * sin(Theta);  

% 绘制三维图像  
figure; % 创建新图形窗口  
surf(X, Y, Z); % 使用 surf 函数绘制  
shading interp; % 插值着色，使得表面更光滑  
axis equal; % 使轴比例相等  
xlabel('X轴'); % X轴标签  
ylabel('Y轴'); % Y轴标签  
zlabel('Z轴'); % Z轴标签  
title('环面 (Torus) 的三维图像'); % 图标题  
grid on; % 网格开启 