% q2_klein.m
% 期末考试第二部分第 2 题：用 surf 渲染克莱因瓶（Klein bottle）
%
% 采用经典的 "figure-8 immersion"（8 字形浸入）参数化，
% 参数范围 u in [0, 2*pi), v in [0, 2*pi)：
%
%   x(u,v) = -(2/15) cos u ( 3 cos v - 30 sin u + 90 cos^4 u sin u
%                            - 60 cos^6 u sin u + 5 cos u cos v sin u )
%   y(u,v) = -(1/15) sin u ( 3 cos v - 3 cos^2 u cos v - 48 cos^4 u cos v
%                            + 48 cos^6 u cos v - 60 sin u + 5 cos u cos v sin u
%                            - 5 cos^3 u cos v sin u - 80 cos^5 u cos v sin u
%                            + 80 cos^7 u cos v sin u )
%   z(u,v) = (2/15) ( 3 + 5 cos u sin u ) sin v
%
% 运行环境：MATLAB R2020b 及以上（turbo colormap 与 exportgraphics 所需）。
% 若在 GNU Octave 中运行，见文件末尾的兼容说明。

clear; clc; close all;

% ---------- 参数网格 ----------
u = linspace(0, 2*pi, 240);
v = linspace(0, 2*pi, 120);
[U, V] = meshgrid(u, v);          % U, V 均为 120 x 240

% ---------- 预计算三角函数（避免重复计算） ----------
cu = cos(U);  su = sin(U);
cv = cos(V);  sv = sin(V);

% ---------- 参数方程 ----------
X = -(2/15) * cu .* ( 3*cv - 30*su + 90*cu.^4.*su - 60*cu.^6.*su ...
                      + 5*cu.*cv.*su );

Y = -(1/15) * su .* ( 3*cv - 3*cu.^2.*cv - 48*cu.^4.*cv + 48*cu.^6.*cv ...
                      - 60*su + 5*cu.*cv.*su - 5*cu.^3.*cv.*su ...
                      - 80*cu.^5.*cv.*su + 80*cu.^7.*cv.*su );

Z = (2/15) * ( 3 + 5*cu.*su ) .* sv;

% ---------- 绘图 ----------
figure('Color', 'w');             % 白色背景
surf(X, Y, Z);                    % 三维曲面
shading interp;                   % 光滑插值着色（同时隐藏网格边线）
colormap(turbo);                  % 颜色映射（R2020b+；旧版可用 jet/parula）
axis equal;                       % 等比例坐标，避免形变
axis off;                         % 隐藏坐标轴
view(3);                          % 三维视角
title('Klein bottle');
exportgraphics(gcf, 'q2_klein_bottle.png', 'Resolution', 200);

% ---------- GNU Octave 兼容写法 ----------
% Octave 没有 exportgraphics / turbo（旧版），可把末尾两行替换为：
%   colormap(jet);
%   print(gcf, '-dpng', '-r200', 'q2_klein_bottle.png');
% 其余代码（surf / shading interp / axis equal / view(3)）在 Octave 中完全兼容。

% ---------- 附：第二个视角（可选） ----------
% figure('Color', 'w');
% surf(X, Y, Z); shading interp; colormap(turbo);
% axis equal; axis off; view(60, 20); title('Klein bottle');
% exportgraphics(gcf, 'q2_klein_bottle_alt.png', 'Resolution', 200);
