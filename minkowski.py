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
    w : (N,) array_like, optional
        The weights for each value in `u` and `v`. Default is None,
        which gives each value a weight of 1.0

    Returns
    -------
    minkowski : double
        The Minkowski distance between vectors `u` and `v`.

    Examples
    --------
    >>> distance.minkowski([1, 0, 0], [0, 1, 0], 1)
    2.0
    >>> 第1小题: 请在此处再补充5个使用案例。
    """
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
    return dist


if __name__ == '__main__':
    pass