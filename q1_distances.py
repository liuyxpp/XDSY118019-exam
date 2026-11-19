"""第 1 题 (iii)：计算三组向量对之间的 Minkowski 距离。

本脚本做三件事：
1. 从上一级目录导入 minkowski()，计算题目给出的三组距离；
2. 用 ``repr(float(d))``、``f\"{d:.12f}\"``、``f\"{d:.15f}\"`` 三种形式打印高精度结果；
3. 用 numpy 公式独立重算（手算核验），并以 1e-12 的相对/绝对容差断言两者一致。

运行方式：
    python3 part2_solution/q1_distances.py
"""

import math
import sys
from pathlib import Path

import numpy as np

# 让脚本无论从哪个目录运行，都能导入上一级的 minkowski.py
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from minkowski import minkowski  # noqa: E402  (import 需在 sys.path 设置之后)


def manual_minkowski(u, v, p, w=None):
    """按数学定义独立手算 Minkowski 距离（不调用 minkowski 函数）。

    .. math::
        d(u, v) = \\left( \\sum_i w_i |u_i - v_i|^p \\right)^{1/p}

    权重缺省时 ``w_i = 1``。本函数只用于交叉核验，不处理 p=inf 的情形。
    """
    u = np.asarray(u, dtype=float)
    v = np.asarray(v, dtype=float)
    terms = np.abs(u - v) ** p
    if w is not None:
        terms = np.asarray(w, dtype=float) * terms
    # math.fsum 做精确求和，减少浮点累加误差
    return float(math.fsum(terms.tolist()) ** (1.0 / p))


CASES = [
    {
        "name": "第 1 组",
        "u": (1, 2, 3),
        "v": (3, 2, 1),
        "p": 2,
        "w": (0.1, 0.7, 0.2),
        "formula": "sqrt(0.1*2^2 + 0.7*0^2 + 0.2*2^2) = sqrt(0.4 + 0.8)",
    },
    {
        "name": "第 2 组",
        "u": (0, 1, 1, 0, 0, 1),
        "v": (1, 0, 0, 1, 1, 0),
        "p": 0.5,
        "w": None,
        "formula": "(6 * 1^0.5)^(1/0.5) = (6)^2",
    },
    {
        "name": "第 3 组",
        "u": (0.1, 0.5, -0.3, -1.2),
        "v": (-0.5, 1.5, 0.3, 0.6),
        "p": 3,
        "w": None,
        "formula": "(0.6^3 + 1.0^3 + 0.6^3 + 1.8^3)^(1/3) = 7.264^(1/3)",
    },
]

TOL = 1e-12


def main():
    print("=" * 78)
    print("第 1 题 (iii)：三组向量对的 Minkowski 距离")
    print("=" * 78)

    all_ok = True
    for i, case in enumerate(CASES, start=1):
        u, v, p, w = case["u"], case["v"], case["p"], case["w"]
        d = minkowski(u, v, p, w=w)
        d_float = float(d)
        d_manual = manual_minkowski(u, v, p, w=w)
        diff = abs(d_float - d_manual)
        ok = diff <= TOL * max(1.0, abs(d_float))
        all_ok = all_ok and ok

        print(f"\n{case['name']}:")
        print(f"  u = {u}, v = {v}, p = {p!r}, w = {w}")
        print(f"  手算公式: {case['formula']}")
        print(f"  minkowski(...)          = {d!r}")
        print(f"  repr(float(d))          = {d_float!r}")
        print(f"  f'{{d:.12f}}'            = {d_float:.12f}")
        print(f"  f'{{d:.15f}}'            = {d_float:.15f}")
        print(f"  独立公式手算值          = {d_manual!r}")
        print(f"  绝对误差 abs_diff       = {diff:.3e}   (容差 {TOL:.0e})")
        print(f"  核验结论                = {'通过 (PASS)' if ok else '失败 (FAIL)'}")

    print("\n" + "-" * 78)
    print("汇总结果（repr 高精度 / 12 位小数）：")
    for case in CASES:
        d = float(minkowski(case["u"], case["v"], case["p"], w=case["w"]))
        print(f"  {case['name']}: {d!r}   ({d:.12f})")

    print("\n最终核验:", "全部通过 (ALL PASS)" if all_ok else "存在失败 (FAIL)")
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
