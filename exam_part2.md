---
title: "期末考试第二部分 参考答案"
subtitle: "跨入科学研究之门（XDSY118019）"
author: "学号：26800190065　姓名：BruceGao"
date: "2026-11-19"
---



## 第1题（30分）　Python 编程题：Minkowski 距离

本题对应 `finalexam-part2.pdf` 第 1 题。涉及的文件：

- `minkowski.py`（原地修改：补充参数校验与 Examples）
- `part2_solution/q1_distances.py`（新建：第 (iii) 问的计算脚本）
- `part2_solution/q1_results.md`（本文件）

运行环境：Python 3.12+，依赖 `numpy`、`scipy`。

---

#### 1(i) 输入参数校验

**校验设计**

- `u`、`v`：直接复用文件中已有的 `_validate_vector(u)` / `_validate_vector(v)`。该函数内部执行 `np.asarray(u, dtype=None, order='c')`，若结果不是 1-D 数组则抛出 `ValueError("Input vector should be 1-D.")`。
- `w`：当 `w is not None` 时复用 `_validate_weights(w)`。它先调用 `_validate_vector(w, dtype=np.float64)`（同样 `order='c'`），再检查权重是否全部非负，否则抛出 `ValueError("Input weights should be all non-negative")`。
- `p`：自行实现 `_validate_p(p)`，校验规则如下：
  1. 拒绝 `bool` / `np.bool_`，因为 `bool` 是 `int` 的子类，若不先排除，`True` 会被当作 `p=1` 而悄悄通过；
  2. 拒绝 `np.ndarray`（包括 0 维数组），因为数组不是标量；
  3. 只接受实数标量类型 `int / float / np.integer / np.floating`，因此复数、字符串、`None`、`list` 等都会被拒绝；
  4. 转成 `float` 后拒绝 `NaN`；
  5. 要求 `p > 0` 或 `p == np.inf`，否则抛出 `ValueError`，错误信息同时给出中文和英文说明。
- 形状一致性：在完成上述校验之后，再检查 `u.shape == v.shape`，以及（若给出 `w`）`w.shape == u.shape`，不一致即抛出 `ValueError`。

校验顺序严格按照题目要求：`u -> v -> w -> p -> 形状一致性`，校验完成后才进入原有的距离计算逻辑。

**新增的 p 校验函数（`_validate_p`，这里只展示核心代码，完整版本见文末附录）**

```python
def _validate_p(p):
    """Validate the order ``p`` of the Minkowski distance."""
    # bool 是 int 的子类，必须先排除，否则 True 会被当成 p=1。
    if isinstance(p, (bool, np.bool_)):
        raise ValueError(
            "p 必须是实数标量，不能是布尔值 "
            "(p must be a real scalar, not a bool).")
    # 数组（包括 0 维数组）不是标量，予以拒绝。
    if isinstance(p, np.ndarray):
        raise ValueError(
            "p 必须是实数标量，不能是数组 "
            "(p must be a real scalar, not an array).")
    # 只接受 Python / NumPy 的实数标量类型；复数、字符串、None 等在此被拒绝。
    if not isinstance(p, (int, float, np.integer, np.floating)):
        raise ValueError(
            "p 必须是实数标量，收到类型 "
            f"{type(p).__name__!r} (p must be a real scalar).")
    p_value = float(p)
    # NaN 与任何数比较均为 False，必须单独拒绝。
    if math.isnan(p_value):
        raise ValueError("p 不能是 NaN (p must not be NaN).")
    # 合法的 p：正实数，或正无穷。
    if not (p_value > 0.0 or p_value == np.inf):
        raise ValueError(
            f"p 必须满足 p > 0 或 p == np.inf，收到 p = {p!r} "
            "(p must satisfy p > 0 or p == np.inf).")
    return p_value
```

**`minkowski()` 函数体的校验部分**

```python
    # ----- i. 参数校验 -----
    u = _validate_vector(u)
    v = _validate_vector(v)
    if w is not None:
        w = _validate_weights(w)
    p = _validate_p(p)
    if u.shape != v.shape:
        raise ValueError(
            f"u 与 v 的形状必须一致，当前分别为 {u.shape} 和 {v.shape}。")
    if w is not None and w.shape != u.shape:
        raise ValueError(
            f"w 与 u 的长度必须一致，当前分别为 {w.shape} 和 {u.shape}。")

    # ----- 原有的距离计算逻辑（未改动） -----
    u_v = u - v
    if w is not None:
        if p == 1:
            root_w = w
        elif p == 2:
            # better precision and speed
            root_w = np.sqrt(w)
        elif p == np.inf:
            root_w = (w != 0)
        else:
            root_w = np.power(w, 1/p)
        u_v = root_w * u_v
    dist = norm(u_v, ord=p)
    # 统一转换为 Python float，使 doctest 与打印结果不随 numpy 版本变化
    return float(dist)
```

原有的 `p == 1 / p == 2 / p == np.inf / 其他` 的 `root_w` 分支和 `norm(u_v, ord=p)` 算法完全保留，只在计算前增加了校验、在计算后统一返回 Python `float`（仍是双精度）。

**非法输入实测（均抛出 `ValueError`）**

| 非法输入 | 抛出信息 |
| --- | --- |
| `minkowski([1,2,3], [4,5])` | `u 与 v 的形状必须一致，当前分别为 (3,) 和 (2,)。` |
| `minkowski([1,2,3], [4,5,6], p=0)` | `p 必须满足 p > 0 或 p == np.inf，收到 p = 0 (p must satisfy p > 0 or p == np.inf).` |
| `minkowski([1,2,3], [4,5,6], p=True)` | `p 必须是实数标量，不能是布尔值 (p must be a real scalar, not a bool).` |
| `minkowski([1,2,3], [4,5,6], p=1+2j)` | `p 必须是实数标量，收到类型 'complex' (p must be a real scalar).` |
| `minkowski([1,2,3], [4,5,6], p=float('nan'))` | `p 不能是 NaN (p must not be NaN).` |
| `minkowski([1,2,3], [4,5,6], p=float('-inf'))` | `p 必须满足 p > 0 或 p == np.inf，收到 p = -inf ...` |
| `minkowski([1,2,3], [4,5,6], w=[0.1,0.2])` | `w 与 u 的长度必须一致，当前分别为 (2,) 和 (3,)。` |
| `minkowski([1,2,3], [4,5,6], w=[1,-1,1])` | `Input weights should be all non-negative` |
| `minkowski([[1,2],[3,4]], [1,2])` | `Input vector should be 1-D.` |

---

#### 1(ii) docstring 的 Examples 小节

Examples 小节共给出 **6 个真实可运行**的 doctest 用例，覆盖 p=1、p=2、p=3、p=0.5（准度量）、p=np.inf 以及带权 w 的用法：

| # | 用例 | 覆盖点 | doctest 输出 |
| --- | --- | --- | --- |
| 1 | `minkowski([1, 0, 0], [0, 1, 0], 1)` | p=1（曼哈顿距离） | `2.0` |
| 2 | `minkowski([1, 2, 3], [4, 5, 6])` | 默认 p=2（欧氏距离） | `5.196152422706632` |
| 3 | `minkowski([1, 2, 3], [4, 5, 6], 3)` | p=3 | `4.3267487109222245` |
| 4 | `minkowski([0, 0], [1, 1], 0.5)` | 0<p<1（准度量） | `4.0` |
| 5 | `minkowski([1, 2, 3], [4, 6, 8], np.inf)` | p=inf（切比雪夫距离） | `5.0` |
| 6 | `minkowski([1, 2, 3], [3, 2, 1], 2, w=[0.1, 0.7, 0.2])` | 带权 w | `1.0954451150103321` |

**完整 Examples 段落（已写入 `minkowski.py` 的 docstring）**

```text
    Examples
    --------
    >>> minkowski([1, 0, 0], [0, 1, 0], 1)              # p=1 (曼哈顿距离)
    2.0
    >>> minkowski([1, 2, 3], [4, 5, 6])                 # 默认 p=2 (欧氏距离)
    5.196152422706632
    >>> minkowski([1, 2, 3], [4, 5, 6], 3)              # p=3
    4.3267487109222245
    >>> minkowski([0, 0], [1, 1], 0.5)                  # 0<p<1，准度量
    4.0
    >>> minkowski([1, 2, 3], [4, 6, 8], np.inf)         # p=inf (切比雪夫距离)
    5.0
    >>> minkowski([1, 2, 3], [3, 2, 1], 2, w=[0.1, 0.7, 0.2])  # 带权 w
    1.0954451150103321

    非法输入会抛出 ``ValueError``（以下仅为说明，不是 doctest）::

        minkowski([1, 2, 3], [4, 5])                    # u 与 v 长度不一致
        minkowski([1, 2, 3], [4, 5, 6], p=0)            # p 必须 > 0
        minkowski([1, 2, 3], [4, 5, 6], p=True)         # p 不能是 bool
        minkowski([1, 2, 3], [4, 5, 6], w=[0.1, 0.2])   # w 与 u 长度不一致
```

说明：

- 原 docstring 中使用的 `distance.minkowski(...)` 已全部改为当前模块可直接调用的 `minkowski(...)`。
- 浮点期望值是先用实际解释器运行、再逐字符核对得到的（不是手写猜测），例如 `sqrt(6) = 5.196152422706632`（`minkowski([1,2,3],[4,5,6])` 的差向量为 `(3,3,3)`，`sqrt(27) = 5.196152422706632`）。
- 非法输入的说明放在 `::` 字面块中（不带 `>>>`），不会作为 doctest 执行，因此不会让 doctest 抛错。
- `minkowski` 返回 Python `float`，故 doctest 输出为稳定的 `2.0` 等写法，不随 numpy 版本显示 `np.float64(2.0)`。

**doctest 通过证据**

```console
$ cd XDSY118019-exam
$ python3 -m doctest minkowski.py && echo "doctest OK (exit 0)"
doctest OK (exit 0)
```

详细模式（`-v`）输出末尾：

```console
Trying:
    minkowski([1, 2, 3], [3, 2, 1], 2, w=[0.1, 0.7, 0.2])  # 带权 w
Expecting:
    1.0954451150103321
ok
1 item passed all tests:
   6 tests in minkowski.minkowski
6 tests in 5 items.
6 passed.
Test passed.
```

即 6 个 doctest 用例全部通过，进程退出码为 0。

---

#### 1(iii) 三组向量对的 Minkowski 距离

**计算脚本**：`part2_solution/q1_distances.py`

脚本要点：

1. 通过 `sys.path.insert(0, str(Path(__file__).resolve().parents[1]))` 从上一级目录导入 `minkowski`，因此可以在任意目录下直接运行；
2. 对每组分别用 `repr(float(d))`、`f'{d:.12f}'` 和 `f'{d:.15f}'` 打印高精度结果；
3. 用 numpy 公式独立重算（`math.fsum` 做精确求和）作为手算核验，并以 `1e-12` 的容差断言两种结果一致，不一致则退出码非 0。

运行命令：

```console
$ cd XDSY118019-exam
$ python3 part2_solution/q1_distances.py
```

运行输出：

```text
==============================================================================
第 1 题 (iii)：三组向量对的 Minkowski 距离
==============================================================================

第 1 组:
  u = (1, 2, 3), v = (3, 2, 1), p = 2, w = (0.1, 0.7, 0.2)
  手算公式: sqrt(0.1*2^2 + 0.7*0^2 + 0.2*2^2) = sqrt(0.4 + 0.8)
  minkowski(...)          = 1.0954451150103321
  repr(float(d))          = 1.0954451150103321
  f'{d:.12f}'            = 1.095445115010
  f'{d:.15f}'            = 1.095445115010332
  独立公式手算值          = 1.0954451150103324
  绝对误差 abs_diff       = 2.220e-16   (容差 1e-12)
  核验结论                = 通过 (PASS)

第 2 组:
  u = (0, 1, 1, 0, 0, 1), v = (1, 0, 0, 1, 1, 0), p = 0.5, w = None
  手算公式: (6 * 1^0.5)^(1/0.5) = (6)^2
  minkowski(...)          = 36.0
  repr(float(d))          = 36.0
  f'{d:.12f}'            = 36.000000000000
  f'{d:.15f}'            = 36.000000000000000
  独立公式手算值          = 36.0
  绝对误差 abs_diff       = 0.000e+00   (容差 1e-12)
  核验结论                = 通过 (PASS)

第 3 组:
  u = (0.1, 0.5, -0.3, -1.2), v = (-0.5, 1.5, 0.3, 0.6), p = 3, w = None
  手算公式: (0.6^3 + 1.0^3 + 0.6^3 + 1.8^3)^(1/3) = 7.264^(1/3)
  minkowski(...)          = 1.9366833186578014
  repr(float(d))          = 1.9366833186578014
  f'{d:.12f}'            = 1.936683318658
  f'{d:.15f}'            = 1.936683318657801
  独立公式手算值          = 1.9366833186578014
  绝对误差 abs_diff       = 0.000e+00   (容差 1e-12)
  核验结论                = 通过 (PASS)

------------------------------------------------------------------------------
汇总结果（repr 高精度 / 12 位小数）：
  第 1 组: 1.0954451150103321   (1.095445115010)
  第 2 组: 36.0   (36.000000000000)
  第 3 组: 1.9366833186578014   (1.936683318658)

最终核验: 全部通过 (ALL PASS)
```

**结果汇总**

- 第 1 组：$u_1=(1,2,3)$，$v_1=(3,2,1)$，$p=2$，$w=(0.1,0.7,0.2)$
- 第 2 组：$u_2=(0,1,1,0,0,1)$，$v_2=(1,0,0,1,1,0)$，$p=0.5$
- 第 3 组：$u_3=(0.1,0.5,-0.3,-1.2)$，$v_3=(-0.5,1.5,0.3,0.6)$，$p=3$

| 组 | p | w | 距离（repr 完整双精度） | 12 位小数 |
| --- | --- | --- | --- | --- |
| 1 | 2 | $(0.1, 0.7, 0.2)$ | **1.0954451150103321** | 1.095445115010 |
| 2 | 0.5 | 无 | **36.0** | 36.000000000000 |
| 3 | 3 | 无 | **1.9366833186578014** | 1.936683318658 |

**手算过程（与脚本核验一致）**

1. **第 1 组**：$u_1 - v_1 = (-2, 0, 2)$，权重 $w = (0.1, 0.7, 0.2)$。按定义

   $$
   \begin{aligned}
   d &= \sqrt{w_1|u_1-v_1|^2 + w_2|u_2-v_2|^2 + w_3|u_3-v_3|^2}\\
     &= \sqrt{0.1 \times 4 + 0.7 \times 0 + 0.2 \times 4}\\
     &= \sqrt{0.4 + 0.8} = \sqrt{1.2} = 1.0954451150103321.
   \end{aligned}
   $$

   函数输出与 `math.sqrt(1.2)` 的 double 结果完全一致。（脚本中 numpy 手算因先算 `0.4+0.8=1.2000000000000002` 得到 `1.0954451150103324`，与函数值仅差 $2.2 \times 10^{-16}$，远小于 $10^{-12}$ 的容差。）

2. **第 2 组**：$u_2 - v_2 = (-1, 1, 1, -1, -1, 1)$，每个分量绝对值都是 1。按 p=0.5 的准度量定义

   $$
   \begin{aligned}
   d &= \left(\sum_i |u_i-v_i|^{0.5}\right)^{1/0.5}\\
     &= \left(6 \times 1^{0.5}\right)^{2} = 6^2 = 36.0.
   \end{aligned}
   $$

3. **第 3 组**：$u_3 - v_3 = (0.6, -1.0, -0.6, -1.8)$，$p=3$。

   $$
   \begin{aligned}
   d &= \left(0.6^3 + 1.0^3 + 0.6^3 + 1.8^3\right)^{1/3}\\
     &= \left(0.216 + 1 + 0.216 + 5.832\right)^{1/3}\\
     &= 7.264^{1/3} \approx 1.9366833186578017.
   \end{aligned}
   $$

   函数在双精度下输出 `1.9366833186578014`，与高精度真值 `1.9366833186578017` 相差约 $2.7 \times 10^{-16}$（相对误差约 $1.4 \times 10^{-16}$），属于正常的浮点舍入误差。


---

#### 附：`minkowski.py` 完整代码（可直接复制）

```python
import math
import numpy as np
from scipy.linalg import norm


def _validate_vector(u, dtype=None):
    u = np.asarray(u, dtype=dtype, order='c')
    if u.ndim == 1:
        return u
    raise ValueError("Input vector should be 1-D.")


def _validate_weights(w, dtype=np.float64):
    w = _validate_vector(w, dtype=dtype)
    if np.any(w < 0):
        raise ValueError("Input weights should be all non-negative")
    return w


def _validate_p(p):
    """Validate the order ``p`` of the Minkowski distance.

    ``p`` must be a real scalar (not a bool, complex number, array or NaN)
    satisfying ``p > 0`` or ``p == np.inf``.  0 < p < 1 is allowed because
    the Minkowski distance then defines a quasi-metric.

    Parameters
    ----------
    p : scalar
        Order of the norm.

    Returns
    -------
    p : float
        The validated order as a Python float.

    Raises
    ------
    ValueError
        If ``p`` is not a real scalar, is NaN, or does not satisfy
        ``p > 0`` / ``p == np.inf``.
    """
    # bool 是 int 的子类，必须先排除，否则 True 会被当成 p=1。
    if isinstance(p, (bool, np.bool_)):
        raise ValueError(
            "p 必须是实数标量，不能是布尔值 "
            "(p must be a real scalar, not a bool).")
    # 数组（包括 0 维数组）不是标量，予以拒绝。
    if isinstance(p, np.ndarray):
        raise ValueError(
            "p 必须是实数标量，不能是数组 "
            "(p must be a real scalar, not an array).")
    # 只接受 Python / NumPy 的实数标量类型；复数、字符串、None 等在此被拒绝。
    if not isinstance(p, (int, float, np.integer, np.floating)):
        raise ValueError(
            "p 必须是实数标量，收到类型 "
            f"{type(p).__name__!r} (p must be a real scalar).")
    p_value = float(p)
    # NaN 与任何数比较均为 False，必须单独拒绝。
    if math.isnan(p_value):
        raise ValueError("p 不能是 NaN (p must not be NaN).")
    # 合法的 p：正实数，或正无穷。
    if not (p_value > 0.0 or p_value == np.inf):
        raise ValueError(
            f"p 必须满足 p > 0 或 p == np.inf，收到 p = {p!r} "
            "(p must satisfy p > 0 or p == np.inf).")
    return p_value


def minkowski(u, v, p=2, w=None):
    """
    Compute the Minkowski distance between two 1-D arrays.

    The Minkowski distance between 1-D arrays `u` and `v`,
    is defined as

    .. math::

       {\\|u-v\\|}_p = (\\sum{|u_i - v_i|^p})^{1/p}.


       \\left(\\sum{w_i(|(u_i - v_i)|^p)}\\right)^{1/p}.

    Parameters
    ----------
    u : (N,) array_like
        Input array.
    v : (N,) array_like
        Input array.
    p : scalar
        The order of the norm of the difference :math:`{\\|u-v\\|}_p`. Note
        that for :math:`0 < p < 1`, the triangle inequality only holds with
        an additional multiplicative factor, i.e. it is only a quasi-metric.
        ``p`` must be a real scalar satisfying ``p > 0`` or ``p == np.inf``.
    w : (N,) array_like, optional
        The weights for each value in `u` and `v`. Default is None,
        which gives each value a weight of 1.0

    Returns
    -------
    minkowski : double
        The Minkowski distance between vectors `u` and `v`.

    Raises
    ------
    ValueError
        If `u` or `v` is not 1-D; if their shapes differ; if `w` contains
        negative values or its length differs from that of `u`; or if `p`
        is not a real scalar satisfying ``p > 0`` or ``p == np.inf``.

    Examples
    --------
    >>> minkowski([1, 0, 0], [0, 1, 0], 1)              # p=1 (曼哈顿距离)
    2.0
    >>> minkowski([1, 2, 3], [4, 5, 6])                 # 默认 p=2 (欧氏距离)
    5.196152422706632
    >>> minkowski([1, 2, 3], [4, 5, 6], 3)              # p=3
    4.3267487109222245
    >>> minkowski([0, 0], [1, 1], 0.5)                  # 0<p<1，准度量
    4.0
    >>> minkowski([1, 2, 3], [4, 6, 8], np.inf)         # p=inf (切比雪夫距离)
    5.0
    >>> minkowski([1, 2, 3], [3, 2, 1], 2, w=[0.1, 0.7, 0.2])  # 带权 w
    1.0954451150103321

    非法输入会抛出 ``ValueError``（以下仅为说明，不是 doctest）::

        minkowski([1, 2, 3], [4, 5])                    # u 与 v 长度不一致
        minkowski([1, 2, 3], [4, 5, 6], p=0)            # p 必须 > 0
        minkowski([1, 2, 3], [4, 5, 6], p=True)         # p 不能是 bool
        minkowski([1, 2, 3], [4, 5, 6], w=[0.1, 0.2])   # w 与 u 长度不一致
    """
    # ----- i. 参数校验 -----
    u = _validate_vector(u)
    v = _validate_vector(v)
    if w is not None:
        w = _validate_weights(w)
    p = _validate_p(p)
    if u.shape != v.shape:
        raise ValueError(
            f"u 与 v 的形状必须一致，当前分别为 {u.shape} 和 {v.shape}。")
    if w is not None and w.shape != u.shape:
        raise ValueError(
            f"w 与 u 的长度必须一致，当前分别为 {w.shape} 和 {u.shape}。")

    # ----- 原有的距离计算逻辑 -----
    u_v = u - v
    if w is not None:
        if p == 1:
            root_w = w
        elif p == 2:
            # better precision and speed
            root_w = np.sqrt(w)
        elif p == np.inf:
            root_w = (w != 0)
        else:
            root_w = np.power(w, 1/p)
        u_v = root_w * u_v
    dist = norm(u_v, ord=p)
    # 统一转换为 Python float，使 doctest 与打印结果不随 numpy 版本变化
    return float(dist)


if __name__ == '__main__':
    pass
```


\newpage

## 第2题（20分）　Matlab 作图：克莱因瓶

#### 公式核对结论

PDF 中的三个公式以分数形式排版、且正文抽取会错乱，因此把 PDF 第 2 页渲染成 200 dpi 图片后逐项核对。核对结果：**题给参数化与下述经典 "figure-8 immersion"（8 字形浸入）完全一致，未发现系数或上标差异**（系数 $2/15$、$1/15$、$30$、$90$、$60$、$5$、$3$、$48$、$80$ 以及 $\cos$ 的 2、3、4、5、6、7 次方均与 PDF 相同）。

$$
\begin{aligned}
x(u,v) &= -\frac{2}{15}\cos u\Big(3\cos v - 30\sin u + 90\cos^4 u\,\sin u \\
       &\qquad\qquad - 60\cos^6 u\,\sin u + 5\cos u\,\cos v\,\sin u\Big),\\[4pt]
y(u,v) &= -\frac{1}{15}\sin u\Big(3\cos v - 3\cos^2 u\,\cos v - 48\cos^4 u\,\cos v
          + 48\cos^6 u\,\cos v \\
       &\qquad\qquad - 60\sin u + 5\cos u\,\cos v\,\sin u - 5\cos^3 u\,\cos v\,\sin u \\
       &\qquad\qquad - 80\cos^5 u\,\cos v\,\sin u + 80\cos^7 u\,\cos v\,\sin u\Big),\\[4pt]
z(u,v) &= \frac{2}{15}\Big(3 + 5\cos u\,\sin u\Big)\sin v,
\end{aligned}
$$

其中 $u\in[0,2\pi)$，$v\in[0,2\pi)$。

#### Matlab 实现（`q2_klein.m`）

完整源码如下（可直接在 MATLAB R2020b 及以上版本运行；已注明 GNU Octave 的替换写法）：

```matlab
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
```

说明：MATLAB 中 `shading interp` 会同时隐藏网格边线，得到光滑曲面；`turbo` 配色需 R2020b 以上版本。`exportgraphics` 把图输出到**当前工作目录**；若希望输出到本目录的 `figures/` 子目录，把该行路径改为 `fullfile('figures','q2_klein_bottle.png')` 即可。

#### Python 复现与渲染（`q2_klein.py`）

另附与 Matlab 版**完全相同**网格与公式的 Python 实现（numpy 向量化，便于复现与对比），代码要点：

- 网格：`u = linspace(0, 2π, 240)`、`v = linspace(0, 2π, 120)`，`meshgrid` 后得到 `(120, 240)` 的 `X, Y, Z`；
- 绘图：`matplotlib.use("Agg")` 无界面后端；`ax.plot_surface(..., cmap="turbo", rstride=1, cstride=1, linewidth=0, antialiased=True, shade=True, lightsource=ls)`，其中 `ls = LightSource(azdeg=315, altdeg=45)`，不降采样、按多边形法线做真实光照；
- 版式：`ax.set_box_aspect(...)` 按 X/Y/Z 实际跨度等比（`zoom=1.30` 填满画幅）、`ax.set_axis_off()`、白色背景、标题 `Klein bottle`；
- 输出：`dpi=200`，两个视角分别为 `(elev=20°, azim=60°)` 与 `(elev=30°, azim=120°)`，均保存到 `figures/`。

渲染结果（主视图）：

![Klein bottle 主视图](part2_solution/figures/q2_klein_bottle.png){width=72%}

第二视角（瓶颈穿过瓶身的自交关系更清楚）：

![Klein bottle 第二视角](part2_solution/figures/q2_klein_bottle_alt.png){width=72%}

#### 图像与参数化说明

该参数化是克莱因瓶的 **figure-8 immersion**：固定 $u$ 时截面是 $v$ 方向的一条 8 字形闭曲线，$u$ 从 $0$ 绕到 $2\pi$ 后 8 字的内外两瓣互换（截面整体翻转），因此它无法在三维空间中无自交地嵌入，只能以"瓶颈穿过瓶身"的自交方式闭合——图中可见瓶颈沿把手绕回后穿入瓶身所形成的自交线。曲面按 $z$ 值映射为 `turbo` 配色，并用 `LightSource` 模拟光照，使瓶身、瓶口与自交处都有清晰的明暗层次。渲染结果与 PDF 公式逐项一致，形状为正确的克莱因瓶。

#### 环境说明

`q2_klein.m` 可直接在 MATLAB 中运行得到上图；同一参数化的 Python 版运行命令为 `python3 q2_klein.py`（需 `numpy`、`matplotlib`），输出图片尺寸 1582 × 1648 px（dpi = 200，白底）。


\newpage

## 第3题（20分）　Mathematica：级数求和与积分

**题目**：利用 Mathematica

i. 求无穷级数的和：$\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^{n+1}\sin n}{n}$；
ii. 求积分：$\displaystyle\int\sqrt{\tan x}\,\mathrm{d}x$。

**环境与验证说明**

- 源代码文件 [`q3_series_integral.wl`](part2_solution/q3_series_integral.wl) 中的 Wolfram Language 代码可直接复制到 `.nb` 中逐段运行，每段后以注释给出**预期输出**，并附求导/数值/极限复核命令。
- 除 Mathematica 求值外，另用 **SymPy + mpmath** 对全部结论做独立交叉验证，脚本为 [`q3_verify.py`](part2_solution/q3_verify.py)：**24 条断言全部通过**（退出码 0）。
- 运行方式：

  ```bash
  python3 part2_solution/q3_verify.py
  ```

- 需要说明的是，SymPy 对本题的两个表达式**不能直接给出闭式**（`sympy.summation` 与 `sympy.integrate` 均返回未求值的 `Sum` / `Integral`）。因此验证脚本先打印这一事实，再用严格等价的路线求精确值：
  - 级数：参数化对数级数 $\sum_{n\ge1}(-1)^{n+1}z^n/n=\ln(1+z)$，取 $z=e^{\mathrm i}$；
  - 积分：标准换元 $t=\sqrt{\tan x}$，化为有理函数积分。

---

#### 3(i) 无穷级数

**题目**：求 $\displaystyle S=\sum_{n=1}^{\infty}\frac{(-1)^{n+1}\sin n}{n}$。

**Mathematica 代码**

```mathematica
(* 精确求和 *)
Sum[(-1)^(n + 1) Sin[n]/n, {n, 1, Infinity}]
(* 预期输出: 1/2 *)

(* 数值核对（任意精度） *)
N[Sum[(-1)^(n + 1) Sin[n]/n, {n, 1, Infinity}], 30]
(* 预期输出: 0.5 *)

(* 不依赖符号求和算法的高精度数值求和 *)
NSum[(-1)^(n + 1) Sin[n]/n, {n, 1, Infinity}, WorkingPrecision -> 30]
(* 预期输出: 0.5 *)

(* 部分和收敛演示 *)
Table[{m, N[Sum[(-1)^(n + 1) Sin[n]/n, {n, 1, m}], 12]},
      {m, {10, 100, 1000, 10000, 100000}}] // TableForm
(* 预期输出（随 m 增大趋近 0.5）:
     10    0.548225794130
     100   0.500160110688
     1000  0.499433214199
     10000 0.500041287970
     100000 0.500002551024 *)
```

**Mathematica 预期输出（精确形式 + 数值）**

| 命令 | 预期输出 |
|---|---|
| `Sum[(-1)^(n+1) Sin[n]/n, {n,1,Infinity}]` | \(\dfrac12\) |
| `N[%, 30]` | `0.5` |
| `NSum[..., WorkingPrecision -> 30]` | `0.5`（即 `0.500000000000000000000000000000`） |

**SymPy / mpmath 独立验证结论**

1. `sympy.summation` 直接对一般项求和返回未求值的 `Sum`（SymPy 的已知局限）。
2. 参数化和（SymPy 能精确求出）：
   $$\sum_{n=1}^{\infty}\frac{(-1)^{n+1}z^n}{n}=\ln(1+z),\qquad |z|\le 1,\; z\ne -1,$$
   在 $z=\tfrac12$ 处核对：左边 $=\ln\tfrac32$，与 `sympy.log(Rational(3,2))` 完全相同。
3. 取 $z=e^{\mathrm i}$，得 $S=\ln(1+e^{\mathrm i})$。由
   $$1+e^{\mathrm i}=e^{\mathrm i/2}\left(e^{-\mathrm i/2}+e^{\mathrm i/2}\right)=2\cos\tfrac12\,e^{\mathrm i/2},$$
   SymPy 精确验证 $(1+e^{\mathrm i})e^{-\mathrm i/2}=2\cos\tfrac12$，且 $2\cos\tfrac12>0$，故主值对数
   $$\ln(1+e^{\mathrm i})=\ln\!\left(2\cos\tfrac12\right)+\frac{\mathrm i}{2},\qquad \operatorname{Im}\ln(1+e^{\mathrm i})=\frac12 .$$
   SymPy 直接给出的虚部为 $\arctan\!\frac{\sin 1}{1+\cos 1}$，经 `nsimplify` 识别为 $1/2$。
4. 高精度数值：`mpmath.nsum(..., dps=50)` 给出 `0.5`，与 $1/2$ 的偏差在 50 位精度下为 `0.0`（断言阈值 $10^{-40}$ 通过）。
5. 部分和 $S_N$（高精度）：

   | \(N\) | \(S_N\) | \(\lvert S_N-\tfrac12\rvert\) |
   |---|---|---|
   | 10 | 0.548225794129905734 | \(4.82\times10^{-2}\) |
   | 100 | 0.500160110687578641 | \(1.60\times10^{-4}\) |
   | 1000 | 0.49943321419909545 | \(5.67\times10^{-4}\) |
   | 10000 | 0.500041287969635706 | \(4.13\times10^{-5}\) |
   | 100000 | 0.500002551023657189 | \(2.55\times10^{-6}\) |

   注意 $|S_N-\tfrac12|$ 不单调：项的符号由 $(-1)^{n+1}\sin n$ 决定，$n$ 增大时 $\sin n$ 的符号会变化，序列并非严格交错；但整体仍按 $O(1/N)$ 趋于 0.

**推导（Fourier 级数）**

由标准的 Fourier 级数（$0<x<2\pi$）
$$\sum_{n=1}^{\infty}\frac{\sin nx}{n}=\frac{\pi-x}{2}.$$
注意到
$$(-1)^n\sin n=\sin(n)\cos(n\pi)=\sin\bigl(n(1+\pi)\bigr),$$
即把 $x$ 取为 $x=1+\pi$（注意 $1+\pi=4.14159\ldots\in(0,2\pi)$）。于是
$$\sum_{n=1}^{\infty}\frac{(-1)^n\sin n}{n}=\frac{\pi-(1+\pi)}{2}=-\frac12,$$
从而
$$S=\sum_{n=1}^{\infty}\frac{(-1)^{n+1}\sin n}{n}=-\left(-\frac12\right)=\boxed{\frac12}.$$

（另一种更直接的推导：$\sum_{n\ge1}(-1)^{n+1}z^n/n=\ln(1+z)$，取 $z=e^{\mathrm i}$，则 $S=\operatorname{Im}\ln(1+e^{\mathrm i})=\operatorname{Im}\bigl[\ln(2\cos\tfrac12)+\tfrac{\mathrm i}{2}\bigr]=\tfrac12$。）

---

#### 3(ii) 不定积分

**题目**：求 $\displaystyle\int\sqrt{\tan x}\,\mathrm{d}x$。

**Mathematica 代码**

```mathematica
(* 不定积分 *)
integral = Integrate[Sqrt[Tan[x]], x]
(* 预期输出（等价形式；不同版本可能以不同项次序给出同样结果）:
   (1/(2 Sqrt[2])) Log[(Tan[x] - Sqrt[2 Tan[x]] + 1)
                      /(Tan[x] + Sqrt[2 Tan[x]] + 1)]
   + (1/Sqrt[2]) (ArcTan[Sqrt[2 Tan[x]] - 1]
                + ArcTan[Sqrt[2 Tan[x]] + 1])
   注: Mathematica 的 Integrate 结果不含任意常数 C *)

(* 最关键的一步: 求导还原被积函数 *)
FullSimplify[D[integral, x] - Sqrt[Tan[x]], Assumptions -> 0 < x < Pi/2]
(* 预期输出: 0 *)

(* 定积分 *)
Integrate[Sqrt[Tan[x]], {x, 0, Pi/2}]
(* 预期输出: Pi/Sqrt[2] *)

N[Integrate[Sqrt[Tan[x]], {x, 0, Pi/2}], 20]
(* 预期输出: 2.2214414690791831235 *)

NIntegrate[Sqrt[Tan[x]], {x, 3/10, 1/2}, WorkingPrecision -> 20]
(* 预期输出: 0.12987589683499439515 *)

(* 用闭式解在同一区间作差, 应与上面 NIntegrate 一致
   (区间在 (0, Pi/4) 内, 不跨越紧凑形式 ArcTan 项的跳跃点 tan x = 1) *)
N[(integral /. x -> 1/2) - (integral /. x -> 3/10), 20]
(* 预期输出: 0.12987589683499439515 *)
```

**最简闭式解**（以 SymPy 结果为准，并写成教材常用的紧凑形式）

$$\boxed{
\int\sqrt{\tan x}\,\mathrm{d}x
=\frac{1}{2\sqrt2}\ln\left|\frac{\tan x-\sqrt{2\tan x}+1}{\tan x+\sqrt{2\tan x}+1}\right|
+\frac{1}{\sqrt2}\arctan\frac{\sqrt{2\tan x}}{1-\tan x}+C
}$$

其中紧凑形式的 $\arctan$ 项在 $\tan x=1$ 处有跳跃；若要求在整个区间上连续的原函数，应写成等价形式

$$
F(x)=\frac{1}{2\sqrt2}\ln\left|\frac{\tan x-\sqrt{2\tan x}+1}{\tan x+\sqrt{2\tan x}+1}\right|
+\frac{1}{\sqrt2}\Bigl[\arctan\bigl(\sqrt{2\tan x}-1\bigr)+\arctan\bigl(\sqrt{2\tan x}+1\bigr)\Bigr]+C,
$$

它不依赖分段常数（两种写法在 $\tan x\ne1$ 的区间内只相差局部常数，求导结果相同）。Mathematica 的 `Integrate` 通常返回后者或其等价写法。

**推导（换元 $t=\sqrt{\tan x}$）**

令 $t=\sqrt{\tan x}$，则 $\tan x=t^2$、$x=\arctan(t^2)$、$\mathrm{d}x=\dfrac{2t}{1+t^4}\,\mathrm{d}t$，故
$$\int\sqrt{\tan x}\,\mathrm{d}x=\int t\cdot\frac{2t}{1+t^4}\,\mathrm{d}t=\int\frac{2t^2}{1+t^4}\,\mathrm{d}t .$$
分解
$$\frac{2t^2}{1+t^4}=\frac{2t^2}{(t^2+\sqrt2\,t+1)(t^2-\sqrt2\,t+1)}
=\frac{1}{\sqrt2}\left(\frac{t}{t^2-\sqrt2\,t+1}-\frac{t}{t^2+\sqrt2\,t+1}\right),$$
而
$$
\int\frac{t}{t^2-\sqrt2 t+1}\mathrm{d}t=\frac12\ln(t^2-\sqrt2t+1)+\arctan(\sqrt2t-1),
$$
$$
\int\frac{t}{t^2+\sqrt2 t+1}\mathrm{d}t=\frac12\ln(t^2+\sqrt2t+1)-\arctan(\sqrt2t+1).
$$
回代 $t=\sqrt{\tan x}$ 即得上式。特别地，$F(0)=0$，且
$$\lim_{x\to\pi/2^-}F(x)=\frac{\pi}{\sqrt2},$$
于是
$$\int_0^{\pi/2}\sqrt{\tan x}\,\mathrm{d}x=\frac{\pi}{\sqrt2}=2.2214414690791831235079404950303468493\ldots$$

**SymPy 验证结论**

1. `sympy.integrate(sqrt(tan(x)), x)` 在 SymPy 中返回未求值的 `Integral`（直接积分、`risch=True`、定积分均如此）。
2. 换元被严格验证：
   - $\mathrm{d}x/\mathrm{d}t=2t/(1+t^4)$（`dx/dt - 2t/(1+t^4)` 化简为 0）；
   - $\sqrt{\tan x(t)}=t$（即 $\tan(\arctan t^2)=t^2$，$t>0$）；
   - $\sqrt{\tan x}\,\mathrm{d}x=2t^2/(1+t^4)\,\mathrm{d}t$（化简为 0）。
3. 有理函数积分 $F_u(u)=\int 2u^2/(1+u^4)\,\mathrm{d}u$ 由 SymPy 精确给出；`diff(Fu,u) - 2u^2/(1+u^4)` 化简为 **0**。
4. 回代 $u=\sqrt{\tan x}$ 得到 $F(x)$，SymPy 直接验证
   $$\frac{\mathrm{d}F}{\mathrm{d}x}-\sqrt{\tan x}=0\quad(\text{精确化简}).$$
5. 紧凑形式同样通过求导验证：`diff(F_compact, x) - sqrt(tan x)` 化简为 **0**。
6. **Log 分式方向的核对**：另一种常见的写法把 Log 的分子、分母写成
   $\frac{1}{2\sqrt2}\ln\frac{\tan x+\sqrt{2\tan x}+1}{\tan x-\sqrt{2\tan x}+1}+\cdots$，
   求导后与 $\sqrt{\tan x}$ 相差
   $$\frac{1-\tan x}{\sqrt{\tan x}}\not\equiv0,$$
   可见它并不是原函数（分子分母恰好写反，等价于把整个 Log 项变号）。本解答采用上面经求导验证过的 Log 顺序（分子为 $\tan x-\sqrt{2\tan x}+1$），与 SymPy 的精确结果一致。
7. 端点值：$F(0)=0$（精确）；$\lim_{x\to\pi/2^-}F(x)=\pi/\sqrt2$（SymPy 符号极限给出 $\sqrt2\pi/2$，与 $\pi/\sqrt2$ 化简差为 0）。
8. **高精度数值验证**（mpmath，50 位十进制；取十进制精确点 $x=0.3,0.8,1.2$）：

   | \(x\) | \(F(x)\)（闭式解） |
   |---|---|
   | 0.3 | `0.1102617961963526713183046` |
   | 0.8 | `0.5022044662696318549279859` |
   | 1.2 | `1.009227222501672673296922` |

   闭式解的增量 $F(b)-F(a)$ 与 `mpmath.quad`（高精度数值积分）比较：

   - 区间 $[0.3,0.5]$：数值积分 `0.1298758968349943951503433`，差值 $1.0\times10^{-51}$；
   - 区间 $[0.3,0.8]$：数值积分 `0.3919426700732791836096814`，差值 `0.0`（$<10^{-50}$）；
   - 区间 $[0.3,1.2]$：数值积分 `0.8989654263053200019786175`，差值 `0.0`（$<10^{-50}$）。

   以及换元后的无奇点定积分
   $$\int_0^{\infty}\frac{2t^2}{1+t^4}\,\mathrm{d}t
   =\int_0^{\pi/2}\sqrt{\tan x}\,\mathrm{d}x
   =\frac{\pi}{\sqrt2}
   =2.22144146907918312350794049503\ldots$$
   数值积分给出 `2.22144146907918312350794049503`，与 $\pi/\sqrt2$ 的差为 \(5.35\times10^{-51}\)（断言阈值 \(10^{-30}\) 通过）。

**断言汇总**：`q3_verify.py` 共 24 条断言，全部 PASS；其中级数精确值 $1/2$、积分闭式解的求导还原、定积分 $\pi/\sqrt2$ 都有独立的符号与数值双重证据。


\newpage

## 第4题（30分）　排版：Navier–Stokes 方程

## Navier–Stokes Equations

The Navier–Stokes momentum equation can be derived as a particular form of the Cauchy momentum equation, whose general convective form is:

$$
\displaystyle \frac{D\mathbf{u}}{Dt} = \frac{1}{\rho}\,\nabla \cdot \boldsymbol{\sigma} + \mathbf{a}.
$$

By setting the Cauchy stress tensor $\boldsymbol{\sigma}$ to be the sum of a viscosity term $\boldsymbol{\tau}$ (the deviatoric stress) and a pressure term $-p\mathbf{I}$ (volumetric stress), we arrive at:

$$
\displaystyle \rho\,\frac{D\mathbf{u}}{Dt} = -\nabla p + \nabla \cdot \boldsymbol{\tau} + \rho\,\mathbf{a}
$$

where

- $\dfrac{D}{Dt}$ is the material derivative, defined as $\dfrac{\partial}{\partial t} + \mathbf{u} \cdot \nabla$,
- $\rho$ is the (mass) density,
- $\mathbf{u}$ is the flow velocity,
- $\nabla \cdot$ is the divergence,
- $p$ is the pressure,
- $t$ is time,
- $\boldsymbol{\tau}$ is the Deviatoric stress|deviatoric stress tensor, which has order 2,
- $\mathbf{a}$ represents body forces acting on the continuum, for example gravity, Fictitious force|inertial accelerations, Coulomb\'s law|electrostatic accelerations, and so on.

In this form, it is apparent that in the assumption of an inviscid fluid – no deviatoric stress – Cauchy equations reduce to the [Euler equations](https://en.wikipedia.org/wiki/Euler_equations_(fluid_dynamics)).




## 附录：文件清单与运行方式

| 文件 | 内容 |
|---|---|
| `minkowski.py` | 第1题：加入 u/v/w/p 参数校验并补全 Examples 的 `minkowski` 函数 |
| `part2_solution/q1_distances.py` | 第1题：三组向量对的 Minkowski 距离计算与独立核验脚本 |
| `part2_solution/q2_klein.m` | 第2题：Matlab `surf` 绘制克莱因瓶脚本 |
| `part2_solution/q2_klein.py` | 第2题：与 q2_klein.m 对应的 Python 等价实现（同一参数的复现与渲染） |
| `part2_solution/q3_series_integral.wl` | 第3题：Mathematica 求级数和与积分的源代码 |
| `part2_solution/q3_verify.py` | 第3题：SymPy 独立验证脚本（符号 + 数值） |
| `part2_solution/q4_navier_stokes.md` | 第4题：Navier--Stokes 文本的 Markdown 源文件 |
| `part2_solution/figures/*.png` | 本文引用的所有图片 |

本地复现所需环境：Python 3.12+，依赖 `numpy`、`scipy`、`matplotlib`、`sympy`；
第2题 Matlab 脚本在 MATLAB 中运行（正文另附 GNU Octave 兼容写法）；
第3题 Mathematica 源码可直接粘贴到 Wolfram Notebook 运行。
