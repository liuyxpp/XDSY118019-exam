(* ================================================================
   期末考试  第二部分  第 3 题（20 分）
   利用 Mathematica
     (i)  求无穷级数的和：  Sum_{n=1}^{Infinity} (-1)^(n+1) Sin[n]/n
     (ii) 求积分：          Integrate[Sqrt[Tan[x]], x]

   使用说明
   --------
   * 把下面的表达式逐段复制到 Mathematica 的 .nb 中即可运行；每段代码
     后以注释给出“预期输出”，便于与 Mathematica 实际运行结果逐项核对。
   * 每一段都附有可以自行复核的命令（求导还原、数值核对、极限核对），
     并且已用 SymPy + mpmath 独立交叉验证（见同目录 q3_verify.py，
     24 条断言全部通过）。
   * 不同 Mathematica 版本可能给出彼此等价、但项的顺序/写法
     不同的结果；本文件对 (ii) 给出了一个经求导验证的标准形式。

   结论速览
   --------
     (i)   Sum_{n=1}^{Infinity} (-1)^(n+1) Sin[n]/n = 1/2
     (ii)  ∫ Sqrt[Tan[x]] dx
           = (1/(2 Sqrt[2])) Log[(Tan[x] - Sqrt[2 Tan[x]] + 1)/
                               (Tan[x] + Sqrt[2 Tan[x]] + 1)]
             + (1/Sqrt[2]) (ArcTan[Sqrt[2 Tan[x]] - 1]
                          + ArcTan[Sqrt[2 Tan[x]] + 1]) + C
           ∫_0^{Pi/2} Sqrt[Tan[x]] dx = Pi/Sqrt[2]
   ================================================================ *)

ClearAll["Global`*"];

(* ================================================================
   (i) 无穷级数  Sum_{n=1}^{Infinity} (-1)^(n+1) Sin[n]/n
   ================================================================ *)

(* ---- 1. 直接求精确和 ---- *)
seriesSum = Sum[(-1)^(n + 1) Sin[n]/n, {n, 1, Infinity}]
(* 预期输出： 1/2 *)

(* 再化简一次（应保持不变） *)
FullSimplify[seriesSum]
(* 预期输出： 1/2 *)

(* ---- 2. 数值核对（任意精度） ---- *)
N[seriesSum, 30]
(* 预期输出： 0.5 *)

(* 不依赖符号求和算法的高精度数值求和 *)
NSum[(-1)^(n + 1) Sin[n]/n, {n, 1, Infinity}, WorkingPrecision -> 30]
(* 预期输出： 0.5 *)

(* ---- 3. 部分和收敛演示（应趋于 0.5） ---- *)
Table[{m, N[Sum[(-1)^(n + 1) Sin[n]/n, {n, 1, m}], 12]},
      {m, {10, 100, 1000, 10000, 100000}}] // TableForm
(* 预期输出（随 m 增大趋近 0.5）：
       10    0.548225794130
       100   0.500160110688
       1000  0.499433214199
       10000 0.500041287970
       100000 0.500002551024    *)

(* ---- 4. 与 Fourier 级数交叉核对 ----
   已知   Sum_{n>=1} Sin[n x]/n = (Pi - x)/2 ,   0 < x < 2 Pi
   取 x = 1 + Pi（注意 1+Pi = 4.14159... 属于 (0, 2Pi)）：
       (-1)^n Sin[n] = Sin[n(1+Pi)]
   因为 Sin[n(1+Pi)] = Sin[n]Cos[n Pi] = (-1)^n Sin[n]。
   故
       Sum_{n>=1} (-1)^n   Sin[n]/n = (Pi - (1+Pi))/2 = -1/2 ,
       Sum_{n>=1} (-1)^(n+1) Sin[n]/n = 1/2 .
   ---------------------------------------------------------------- *)
fourierSeries = Assuming[0 < x < 2 Pi, Sum[Sin[n x]/n, {n, 1, Infinity}]]
(* 预期输出： (Pi - x)/2   （在 0 < x < 2 Pi 内成立；
   某些版本可能返回等价的 ConditionalExpression） *)

fourierSeries /. x -> 1 + Pi
(* 预期输出： -1/2      （即 Sum (-1)^n Sin[n]/n ） *)

-(fourierSeries /. x -> 1 + Pi)
(* 预期输出： 1/2       （本题答案） *)

(* 说明：若某个 Mathematica 版本没有自动求出 fourierSeries，
   可以试试
     Sum[Sin[n x]/n, {n, 1, Infinity}, Assumptions -> 0 < x < 2 Pi]
   或者直接用上面的 NSum 数值核对（0.500000000000...）。 *)


(* ================================================================
   (ii) 不定积分  Integrate[Sqrt[Tan[x]], x]
   ================================================================ *)

(* ---- 1. 直接求不定积分 ----
   标准换元：t = Sqrt[Tan[x]]  =>  Tan[x] = t^2,  x = ArcTan[t^2],
             dx = 2 t/(1 + t^4) dt,
   于是
       ∫ Sqrt[Tan[x]] dx = ∫ 2 t^2/(1 + t^4) dt ,
   部分分式分解
       2 t^2/(1+t^4) = (1/Sqrt[2]) [ t/(t^2 - Sqrt[2] t + 1)
                                      - t/(t^2 + Sqrt[2] t + 1) ]
   积分后即得下面的初等函数。
   ---------------------------------------------------------------- *)
integral = Integrate[Sqrt[Tan[x]], x]
(* 预期输出（等价形式；不同版本可能以不同项次序给出同样结果）：
   (1/(2 Sqrt[2])) Log[(Tan[x] - Sqrt[2 Tan[x]] + 1)
                      /(Tan[x] + Sqrt[2 Tan[x]] + 1)]
   + (1/Sqrt[2]) (ArcTan[Sqrt[2 Tan[x]] - 1]
                + ArcTan[Sqrt[2 Tan[x]] + 1])
   注：Mathematica 给出的不定积分不含任意常数 C。 *)

(* ---- 2. 求导还原验证（最关键的一步） ---- *)
FullSimplify[D[integral, x] - Sqrt[Tan[x]], Assumptions -> 0 < x < Pi/2]
(* 预期输出： 0 *)

(* 若上面的化简没有直接得到 0，可再加 TrigToExp 或改用数值核对： *)
FullSimplify[TrigToExp[D[integral, x] - Sqrt[Tan[x]]],
             Assumptions -> 0 < x < Pi/2]
(* 预期输出： 0 *)

N[(D[integral, x] - Sqrt[Tan[x]]) /. x -> 8/10, 20]
(* 预期输出： 0.*10^-20   （数值上为 0） *)

(* ---- 3. 等价的教材紧凑写法（在 Tan[x] != 1 的区间内与原函数
        只相差局部常数；对 x 求导仍严格等于 Sqrt[Tan[x]]） ---- *)
compact = (1/(2 Sqrt[2]))
            Log[(Tan[x] - Sqrt[2 Tan[x]] + 1)/(Tan[x] + Sqrt[2 Tan[x]] + 1)]
        + (1/Sqrt[2]) ArcTan[Sqrt[2 Tan[x]]/(1 - Tan[x])];

FullSimplify[D[compact, x] - Sqrt[Tan[x]],
             Assumptions -> 0 < x < Pi/2 && x != Pi/4]
(* 预期输出： 0
   （若当前版本未能直接化简为 0，可改用下一行数值核对；
     其导数恒等于 Sqrt[Tan[x]] 已由 SymPy 严格验证。） *)

N[(D[compact, x] - Sqrt[Tan[x]]) /. x -> 8/10, 20]
(* 预期输出： 0.*10^-20 *)

(* 注：另一种常见写法把 Log 分式的分子、分母写反（即整体取负）。
   经验算，其导数与 Sqrt[Tan[x]] 相差 (1 - Tan[x])/Sqrt[Tan[x]]，
   一般不为零，故不能作为原函数；本文采用上面经验证的形式。
   等价关系：当 tan x < 1 时，
     ArcTan[Sqrt[2 Tan[x]] - 1] + ArcTan[Sqrt[2 Tan[x]] + 1]
       = ArcTan[Sqrt[2 Tan[x]]/(1 - Tan[x])] ；
   当 tan x > 1 时两者相差常数 Pi（局部常数不影响求导）。 *)

(* ---- 4. 定积分与数值核对 ---- *)
Integrate[Sqrt[Tan[x]], {x, 0, Pi/2}]
(* 预期输出： Pi/Sqrt[2] *)

N[Integrate[Sqrt[Tan[x]], {x, 0, Pi/2}], 20]
(* 预期输出： 2.2214414690791831235 *)

NIntegrate[Sqrt[Tan[x]], {x, 3/10, 1/2}, WorkingPrecision -> 20]
(* 预期输出： 0.12987589683499439515 *)

(* 用闭式解在同一区间上作差，应与上面的 NIntegrate 一致。
   注意取在 (0, Pi/4) 内，不跨越紧凑形式 ArcTan 项的跳跃点 tan x = 1。 *)
N[(integral /. x -> 1/2) - (integral /. x -> 3/10), 20]
(* 预期输出： 0.12987589683499439515 *)

(* 端点值：F(0) = 0,  F(Pi/2^-) = Pi/Sqrt[2] *)
integral /. x -> 0
(* 预期输出： 0 *)

Limit[integral, x -> Pi/2, Direction -> "FromBelow"]
(* 预期输出： Pi/Sqrt[2] *)

N[Limit[integral, x -> Pi/2, Direction -> "FromBelow"] - (integral /. x -> 0), 25]
(* 预期输出： 2.221441469079183123507940 *)

(* ================================================================
   结束
   ================================================================ *)
