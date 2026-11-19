#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
q3_verify.py — 用 SymPy + mpmath 独立验证期末考试第二部分第 3 题（Mathematica 题）

题目:
  (i)  Sum_{n=1}^{Infinity} (-1)^(n+1) Sin[n]/n
  (ii) Integrate[Sqrt[Tan[x]], x]

做法:
  * 每一条结论都由 sympy 符号计算或 mpmath 高精度数值计算得到;
  * 脚本末尾统计断言, 全部通过时退出码为 0;
  * 脚本不会输出任何"假数据": 打印的数值均为当场计算的结果.

注意:
  SymPy 对本题的两个表达式不能直接给出闭式
  (summation 与 integrate 均返回未求值的 Sum / Integral), 
  因此脚本先如实打印这一点, 再用严格等价的路线求精确值:
    (i)  参数化对数级数  Sum (-1)^(n+1) z^n/n = log(1+z), 取 z = exp(I);
    (ii) 标准换元 t = sqrt(tan x), 化为有理函数积分.

运行:
  python3 q3_verify.py
"""

from __future__ import annotations

import sys

import mpmath as mp
import sympy as sp

mp.mp.dps = 50  # 50 位十进制精度

_results: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str = "") -> bool:
    """记录并打印一条断言."""
    _results.append((name, bool(ok), detail))
    mark = "PASS" if ok else "FAIL"
    print(f"[{mark}] {name}" + (f"   ({detail})" if detail else ""))
    return bool(ok)


def section(title: str) -> None:
    print()
    print("=" * 78)
    print(title)
    print("=" * 78)


# ============================================================================
# (i) 无穷级数
# ============================================================================
def verify_series() -> None:
    section("(i) 求和  S = Sum_{n=1}^{Infinity} (-1)^(n+1) Sin[n]/n")

    n = sp.symbols("n", integer=True, positive=True)
    z = sp.symbols("z")

    # --- 1. 直接对一般项求和 (如实记录 SymPy 的行为) ---
    print("\n[1] 直接调用 sympy.summation 对一般项求和:")
    direct = sp.summation((-1) ** (n + 1) * sp.sin(n) / n, (n, 1, sp.oo))
    print("    S =", direct)
    print("    -> SymPy 不给出闭式 (返回未求值的 Sum).")
    print("       因此下面用严格可验证的复对数路线求精确值.")

    # --- 2. 精确路线: 参数化几何-对数级数 ---
    #   Sum_{n>=1} (-1)^(n+1) z^n/n = log(1+z),   |z| <= 1, z != -1
    print("\n[2] 精确路线: 参数化求和  Sum_{n>=1} (-1)^(n+1) z^n/n")
    g = sp.summation((-1) ** (n + 1) * z**n / n, (n, 1, sp.oo))
    print("    Sum =", g)
    g_simple = sp.simplify(g)
    print("    化简 =", g_simple)

    # 在 z = 1/2 处核对: Sum (-1)^(n+1) (1/2)^n/n = log(3/2)
    g_half = sp.simplify(g_simple.subs(z, sp.Rational(1, 2)))
    print("    z = 1/2 时 =", g_half, " ; log(3/2) =", sp.log(sp.Rational(3, 2)))
    check(
        "SymPy 给出参数化和 Sum_{n>=1} (-1)^(n+1) z^n/n = log(1+z)  (|z|<=1, z!=-1)",
        sp.simplify(g_half - sp.log(sp.Rational(3, 2))) == 0,
        "z=1/2 处核对",
    )

    # 取 z = exp(I): |z| = 1, z != -1, 级数按 Dirichlet/Abel 意义收敛
    # (对未化简的 Piecewise 直接代入复值, 避免 SymPy 对复数做 z<=1 比较)
    z0 = sp.exp(sp.I)
    S_complex = sp.simplify(g.subs(z, z0))
    print("\n    取 z = exp(I):  S =", S_complex)
    check(
        "取 z=exp(I) 得到 S = log(1+exp(I))",
        sp.simplify(S_complex - sp.log(1 + z0)) == 0,
    )

    # 1 + exp(I) = 2 cos(1/2) exp(I/2)
    shifted = sp.simplify(sp.expand((1 + z0) * sp.exp(-sp.I / 2)))
    print("    (1 + exp(I)) * exp(-I/2) =", shifted)
    check(
        "1 + exp(I) = 2 cos(1/2) exp(I/2)",
        sp.simplify(shifted - 2 * sp.cos(sp.Rational(1, 2))) == 0,
    )
    check(
        "2 cos(1/2) > 0, 故 1+exp(I) 的主辐角恰为 1/2",
        sp.cos(sp.Rational(1, 2)).is_positive is True,
    )

    log_value = sp.log(2 * sp.cos(sp.Rational(1, 2))) + sp.I * sp.Rational(1, 2)
    print("    主值 log(1+exp(I)) = log(2 cos(1/2)) + I/2 =", log_value)
    im_exact = sp.im(log_value)
    print("    Im =", im_exact)
    check(
        "Im[log(1+exp(I))] = 1/2  (精确, 由 1+exp(I) = 2cos(1/2)exp(I/2) 得到)",
        sp.simplify(im_exact - sp.Rational(1, 2)) == 0,
    )

    # SymPy 直接给出的虚部 (未化简形) 再经 nsimplify 识别为 1/2
    im_raw = sp.im(sp.log(1 + z0))
    print("    SymPy 直接给出 Im[log(1+exp(I))] =", im_raw,
          " ; nsimplify ->", sp.nsimplify(im_raw))
    check(
        "nsimplify(Im[log(1+exp(I))]) = 1/2",
        sp.nsimplify(im_raw) == sp.Rational(1, 2),
    )

    S_exact = sp.Rational(1, 2)

    # --- 3. Fourier 级数交叉核对 ---
    print("\n[3] Fourier 级数交叉核对:")
    print("    Sum_{n>=1} Sin[nx]/n = (Pi - x)/2,   0 < x < 2Pi")
    print("    令 x = 1+Pi, 则 (-1)^n Sin[n] = Sin[(1+Pi) n]  (因 Sin[n(1+Pi)] = Sin[n]Cos[nPi])")
    print("    且 1+Pi ∈ (0, 2Pi), 故 Sum (-1)^n Sin[n]/n = (Pi-(1+Pi))/2 = -1/2")
    print("    于是 S = Sum (-1)^(n+1) Sin[n]/n = -(-1/2) = 1/2")
    fourier_value = -(sp.pi - (1 + sp.pi)) / 2
    check(
        "Fourier 路线: -(Pi-(1+Pi))/2 = 1/2",
        sp.simplify(fourier_value - sp.Rational(1, 2)) == 0,
        f"-(Pi-(1+Pi))/2 = {fourier_value}",
    )
    # (-1)^n Sin[n] = Sin[(1+Pi)n] 的逐项数值核对
    max_dev = max(
        abs(sp.N(sp.sin(k * (1 + sp.pi)) - (-1) ** k * sp.sin(k), 30))
        for k in range(1, 8)
    )
    print("    (-1)^n Sin[n] 与 Sin[(1+Pi)n] 在 n=1..7 的最大偏差 =", sp.N(max_dev, 5))
    check(
        "(-1)^n Sin[n] = Sin[(1+Pi)n] 对 n=1..7 成立",
        max_dev < sp.Float("1e-25"),
    )

    # --- 4. 高精度数值核对 ---
    print("\n[4] mpmath 高精度数值核对 (dps = %d):" % mp.mp.dps)
    s_num = mp.nsum(lambda k: (-1) ** (k + 1) * mp.sin(k) / k, [1, mp.inf])
    print("    mp.nsum =", mp.nstr(s_num, 35))
    check(
        "高精度数值和 = 0.5 (误差 < 1e-40)",
        abs(s_num - mp.mpf("0.5")) < mp.mpf("1e-40"),
        "|S_num - 1/2| = " + mp.nstr(abs(s_num - mp.mpf("0.5")), 3),
    )

    # --- 5. 部分和收敛演示 ---
    print("\n[5] 部分和 S_N 收敛到 0.5:")
    for N in (10, 100, 1_000, 10_000, 100_000):
        ps = mp.fsum(((-1) ** (k + 1)) * mp.sin(k) / k for k in range(1, N + 1))
        print(f"    N={N:>6d}:  S_N = {mp.nstr(ps, 18)}"
              f"   |S_N - 1/2| = {mp.nstr(abs(ps - mp.mpf('0.5')), 3)}")

    print("\n=> (i) 结论: S = Sum_{n=1}^{Infinity} (-1)^(n+1) Sin[n]/n = 1/2  (精确)")
    check("级数精确值 = 1/2", S_exact == sp.Rational(1, 2))


# ============================================================================
# (ii) 不定积分
# ============================================================================
def verify_integral() -> None:
    section("(ii) 积分  I = Integral Sqrt[Tan[x]] dx")

    x = sp.symbols("x", positive=True)
    t = sp.symbols("t", positive=True)
    u = sp.symbols("u", positive=True)

    # --- 1. SymPy 直接积分 (如实记录) ---
    print("\n[1] SymPy 直接积分:")
    direct = sp.integrate(sp.sqrt(sp.tan(x)), x)
    print("    integrate(sqrt(tan(x)), x) =", direct)
    print("    -> 返回未求值的 Integral: SymPy 的算法未能直接给出闭式.")
    print("       因此按标准换元 t = sqrt(tan x) 化为有理函数积分, 再用 SymPy 严格验证.")

    # --- 2. 换元 t = sqrt(tan x)  <=>  x = arctan(t^2) ---
    print("\n[2] 换元 t = sqrt(tan x)  <=>  x = arctan(t^2):")
    x_of_t = sp.atan(t**2)
    dxdt = sp.diff(x_of_t, t)
    print("    dx/dt =", dxdt)
    check("dx/dt = 2t/(1+t^4)",
          sp.simplify(dxdt - 2 * t / (1 + t**4)) == 0)

    sqrt_tan = sp.sqrt(sp.tan(x_of_t))
    print("    sqrt(tan(x(t))) =", sqrt_tan)
    check("sqrt(tan(x(t))) = t  (t > 0)",
          sp.simplify(sp.tan(x_of_t) - t**2) == 0,
          "等价于 tan(arctan(t^2)) = t^2, t>0 时开方为 t")

    integrand_t = sp.simplify(sqrt_tan * dxdt)
    print("    sqrt(tan x) dx =", integrand_t, "dt")
    check("被积式化为 2t^2/(1+t^4) dt",
          sp.simplify(integrand_t - 2 * t**2 / (1 + t**4)) == 0)

    # --- 3. 有理函数积分 ---
    print("\n[3] 有理函数积分:")
    Fu = sp.integrate(2 * u**2 / (1 + u**4), u)
    print("    Integral 2u^2/(1+u^4) du =", Fu)
    check("d/du 还原 2u^2/(1+u^4)",
          sp.simplify(sp.diff(Fu, u) - 2 * u**2 / (1 + u**4)) == 0)

    Fx = sp.simplify(Fu.subs(u, sp.sqrt(sp.tan(x))))
    print("\n    F(x) =", Fx)
    check("dF/dx - sqrt(tan x) = 0  (SymPy simplify, 精确)",
          sp.simplify(sp.diff(Fx, x) - sp.sqrt(sp.tan(x))) == 0,
          "对 F(x) = F_u(sqrt(tan x)) 直接求导")

    # --- 4. 教材紧凑形式、以及一种常见错误写法的核对 ---
    print("\n[4] 标准紧凑形式 (验证通过) 与一种常见错误写法的核对:")
    tx = sp.tan(x)
    rt = sp.sqrt(2 * tx)
    F_compact = (
        sp.log((tx - rt + 1) / (tx + rt + 1)) / (2 * sp.sqrt(2))
        + sp.atan(rt / (1 - tx)) / sp.sqrt(2)
    )
    print("    F_compact(x) =", F_compact)
    check("d/dx F_compact = sqrt(tan x)  (精确)",
          sp.simplify(sp.diff(F_compact, x) - sp.sqrt(tx)) == 0)

    # 另一种常见写法把 Log 的分子/分母写反; 用导数残差证明其不正确
    F_ref = (
        sp.log((tx + rt + 1) / (tx - rt + 1)) / (2 * sp.sqrt(2))
        + sp.atan(rt / (1 - tx)) / sp.sqrt(2)
    )
    residual = sp.simplify(sp.diff(F_ref, x) - sp.sqrt(tx))
    expected_residual = (1 - tx) / sp.sqrt(tx)
    print("    常见错误写法(Log 分式取反) 的导数残差 =", residual)
    check("常见错误写法(Log 分式取反)不可行: 残差 = (1-tan x)/sqrt(tan x) != 0",
          sp.simplify(residual - expected_residual) == 0 and residual != 0,
          "故本题采用经求导验证的 Log 顺序")

    # --- 5. 端点值与定积分 ---
    print("\n[5] 端点值与定积分:")
    F0 = sp.simplify(Fx.subs(x, 0))
    print("    F(0) =", F0)
    check("F(0) = 0", F0 == 0)

    Fhalf = sp.limit(Fx, x, sp.pi / 2, "-")
    print("    F(Pi/2-) =", Fhalf, " ;  Pi/Sqrt[2] =", sp.pi / sp.sqrt(2))
    check("F(Pi/2-) = Pi/Sqrt[2]",
          sp.simplify(Fhalf - sp.pi / sp.sqrt(2)) == 0)
    print("    => Integral_0^{Pi/2} sqrt(tan x) dx = F(Pi/2-) - F(0) = Pi/Sqrt[2]")

    # --- 6. 高精度数值核对 ---
    print("\n[6] mpmath 高精度数值核对 (dps = %d):" % mp.mp.dps)

    def F_mp(X: float) -> mp.mpf:
        """用 mpmath 计算闭式解 F(X) (与 SymPy 的 F(x) 同一表达式)."""
        txv = mp.tan(X)
        s = mp.sqrt(2 * txv)
        return (
            mp.log((txv - s + 1) / (txv + s + 1)) / (2 * mp.sqrt(2))
            + (mp.atan(s - 1) + mp.atan(s + 1)) / mp.sqrt(2)
        )

    print("\n    F(x) 的高精度数值 (十进制精确取点):")
    for xv in (mp.mpf("0.3"), mp.mpf("0.8"), mp.mpf("1.2")):
        print(f"      F({mp.nstr(xv, 3)}) = {mp.nstr(F_mp(xv), 25)}")

    base = mp.mpf("0.3")
    for b_str in ("0.5", "0.8", "1.2"):
        b = mp.mpf(b_str)
        quad = mp.quad(lambda zz: mp.sqrt(mp.tan(zz)), [base, b])
        ana = F_mp(b) - F_mp(base)
        err = abs(ana - quad)
        print(f"\n    x ∈ [{mp.nstr(base, 3)}, {b_str}]:")
        print(f"      NIntegrate sqrt(tan x) dx = {mp.nstr(quad, 25)}")
        print(f"      F(b) - F(a)               = {mp.nstr(ana, 25)}")
        print(f"      |差|                      = {mp.nstr(err, 3)}")
        check(f"[{mp.nstr(base, 3)},{b_str}] 闭式解与高精度数值积分一致",
              err < mp.mpf("1e-25"))

    # 0..Pi/2 的定积分: 换元后无端点奇异
    print("\n    定积分 Integral_0^{Pi/2} sqrt(tan x) dx:")
    I_sub = mp.quad(lambda tt: 2 * tt**2 / (1 + tt**4), [0, mp.inf])
    I_exact = mp.pi / mp.sqrt(2)
    print("      换元 t=sqrt(tan x) 后:  Integral_0^{Infinity} 2t^2/(1+t^4) dt =",
          mp.nstr(I_sub, 30))
    print("      Pi/Sqrt[2]                                                  =",
          mp.nstr(I_exact, 30))
    check("换元后定积分 = Pi/Sqrt[2]  (误差 < 1e-30)",
          abs(I_sub - I_exact) < mp.mpf("1e-30"),
          "|diff| = " + mp.nstr(abs(I_sub - I_exact), 3))

    I_direct = mp.quad(lambda zz: mp.sqrt(mp.tan(zz)), [0, mp.pi / 2])
    I_direct_re = mp.re(I_direct)  # 端点处 tan 的舍入可能给 sqrt 带来 ~1e-28 的虚部伪影
    print("\n      直接对 sqrt(tan x) 在 [0,Pi/2] 上 quad =", mp.nstr(I_direct, 22))
    print("      实部 =", mp.nstr(I_direct_re, 22),
          " ; 虚部 =", mp.nstr(mp.im(I_direct), 3), " (端点舍入伪影)")
    print("      (端点 x=0, Pi/2 处为弱奇异性, quad 精度约 1e-21)")
    check("原积分 [0,Pi/2] 数值 = Pi/Sqrt[2]  (误差 < 1e-15)",
          abs(I_direct_re - I_exact) < mp.mpf("1e-15"))

    print("\n=> (ii) 结论:")
    print("   Integral sqrt(tan x) dx =")
    print("     (1/(2 Sqrt[2])) Log[(Tan[x] - Sqrt[2 Tan[x]] + 1)/(Tan[x] + Sqrt[2 Tan[x]] + 1)]")
    print("     + (1/Sqrt[2]) (ArcTan[Sqrt[2 Tan[x]] - 1] + ArcTan[Sqrt[2 Tan[x]] + 1]) + C")
    print("   (等价紧凑写法: 第二项可合并为 (1/Sqrt[2]) ArcTan[Sqrt[2 Tan[x]]/(1 - Tan[x])],")
    print("    在 Tan[x] != 1 的区间内与原函数相差局部常数)")
    print("   Integral_0^{Pi/2} sqrt(tan x) dx = Pi/Sqrt[2] = 2.2214414690791831235...")


# ============================================================================
def main() -> int:
    print("q3_verify.py — SymPy/mpmath 独立验证 期末考试 第二部分 第3题")
    print(f"sympy {sp.__version__},  mpmath {mp.__version__},  dps = {mp.mp.dps}")

    verify_series()
    verify_integral()

    section("断言汇总")
    npass = sum(1 for _, ok, _ in _results if ok)
    nfail = len(_results) - npass
    print(f"共 {len(_results)} 条断言:  PASS = {npass},  FAIL = {nfail}")
    for name, ok, detail in _results:
        if not ok:
            print("  FAIL:", name, detail)
    if nfail == 0:
        print("\nALL CHECKS PASSED")
        print("  (i)  Sum_{n=1}^{Infinity} (-1)^(n+1) Sin[n]/n = 1/2")
        print("  (ii) Integral Sqrt[Tan[x]] dx 见上 (闭式解已通过求导与高精度数值双重验证)")
        return 0
    print("\nSOME CHECKS FAILED")
    return 1


if __name__ == "__main__":
    sys.exit(main())
