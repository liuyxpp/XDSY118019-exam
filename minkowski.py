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
