#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
q2_klein.py
===========
期末考试第二部分第 2 题的 Python 等价实现：渲染克莱因瓶（Klein bottle）。

与 q2_klein.m 采用完全相同的 "figure-8 immersion" 参数化，用 numpy +
matplotlib 实现并可一键重新渲染出图（便于复现与对比）：

    x(u,v) = -(2/15) cos u ( 3 cos v - 30 sin u + 90 cos^4 u sin u
                             - 60 cos^6 u sin u + 5 cos u cos v sin u )
    y(u,v) = -(1/15) sin u ( 3 cos v - 3 cos^2 u cos v - 48 cos^4 u cos v
                             + 48 cos^6 u cos v - 60 sin u + 5 cos u cos v sin u
                             - 5 cos^3 u cos v sin u - 80 cos^5 u cos v sin u
                             + 80 cos^7 u cos v sin u )
    z(u,v) = (2/15) ( 3 + 5 cos u sin u ) sin v

u, v in [0, 2*pi)

输出：
    figures/q2_klein_bottle.png      主视图
    figures/q2_klein_bottle_alt.png  第二视角（elev=30, azim=120）

运行：
    python3 q2_klein.py
"""

from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")  # 无界面后端，服务器/终端也可出图
import matplotlib.pyplot as plt
from matplotlib.colors import LightSource

HERE = Path(__file__).resolve().parent
FIG_DIR = HERE / "figures"
FIG_DIR.mkdir(parents=True, exist_ok=True)

# ----------------------------------------------------------------------------
# 1. 参数网格（与 q2_klein.m 完全一致）
# ----------------------------------------------------------------------------
u = np.linspace(0.0, 2.0 * np.pi, 240)
v = np.linspace(0.0, 2.0 * np.pi, 120)
U, V = np.meshgrid(u, v)          # 形状 (120, 240)

cu, su = np.cos(U), np.sin(U)
cv, sv = np.cos(V), np.sin(V)


def klein_bottle(U, V):
    """figure-8 浸入的克莱因瓶参数化，返回 X, Y, Z。"""
    cu, su = np.cos(U), np.sin(U)
    cv, sv = np.cos(V), np.sin(V)

    X = -(2.0 / 15.0) * cu * (
        3.0 * cv
        - 30.0 * su
        + 90.0 * cu**4 * su
        - 60.0 * cu**6 * su
        + 5.0 * cu * cv * su
    )

    Y = -(1.0 / 15.0) * su * (
        3.0 * cv
        - 3.0 * cu**2 * cv
        - 48.0 * cu**4 * cv
        + 48.0 * cu**6 * cv
        - 60.0 * su
        + 5.0 * cu * cv * su
        - 5.0 * cu**3 * cv * su
        - 80.0 * cu**5 * cv * su
        + 80.0 * cu**7 * cv * su
    )

    Z = (2.0 / 15.0) * (3.0 + 5.0 * cu * su) * sv
    return X, Y, Z


X, Y, Z = klein_bottle(U, V)


# ----------------------------------------------------------------------------
# 2. 渲染函数
# ----------------------------------------------------------------------------
# 数据三个方向的跨度，用于 set_box_aspect 等比例显示
EXT = np.array([np.ptp(X), np.ptp(Y), np.ptp(Z)])


def render(elev=20, azim=60, fname="q2_klein_bottle.png",
           figsize=(9.5, 8.5), zoom=1.30):
    """用 plot_surface + LightSource 着色渲染一个视角并保存 PNG。"""
    fig = plt.figure(figsize=figsize, facecolor="white")
    ax = fig.add_subplot(111, projection="3d")
    ax.set_facecolor("white")

    # 自定义光源：从左上偏前方照射，曲面明暗更有立体感
    ls = LightSource(azdeg=315.0, altdeg=45.0)

    ax.plot_surface(
        X,
        Y,
        Z,
        cmap="turbo",          # 与 Matlab 版 colormap(turbo) 对应
        rstride=1,             # 不降采样，保留 240 x 120 全部网格
        cstride=1,
        linewidth=0,
        antialiased=True,
        shade=True,            # 依据多边形法线 + 光源做明暗
        lightsource=ls,
    )

    # 等比例坐标轴：按数据实际跨度设置盒体比例，并适度放大填满画幅
    ax.set_box_aspect(tuple(EXT / EXT.max()), zoom=zoom)
    ax.set_xlim(X.min(), X.max())
    ax.set_ylim(Y.min(), Y.max())
    ax.set_zlim(Z.min(), Z.max())

    ax.view_init(elev=elev, azim=azim)
    ax.set_axis_off()             # 简洁：隐藏坐标轴
    ax.set_title("Klein bottle", fontsize=18, pad=10)
    fig.tight_layout()

    out = FIG_DIR / fname
    fig.savefig(out, dpi=200, facecolor="white", bbox_inches="tight",
                pad_inches=0.02, metadata={"Software": None})
    plt.close(fig)
    print(f"[saved] {out}  ({out.stat().st_size / 1024:.0f} KiB)")
    return out


if __name__ == "__main__":
    # 主视图：能同时看到瓶身、瓶口与穿过瓶身的瓶颈
    render(elev=20, azim=60, fname="q2_klein_bottle.png")
    # 第二视角：侧上方视角，瓶颈与瓶身的自交关系更清楚
    render(elev=30, azim=120, fname="q2_klein_bottle_alt.png")
