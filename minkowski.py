"""
Minkowski distance with optional coordinate weights.

Examples
--------
>>> minkowski([1, 2], [4, 6], p=2)
5.0
>>> minkowski([1, 2], [4, 6], p=1)
7.0
>>> minkowski([1, 2], [4, 6], p=3)
4.497941445275415
>>> minkowski([0, 0], [3, 4], p=2)
5.0
>>> minkowski([1, 1, 1], [2, 2, 2], p=2)
1.7320508075688772
"""

def _validate_vector(x, name):
    if not isinstance(x, (list, tuple)) or len(x) == 0:
        raise ValueError(f"{name} must be a non-empty list or tuple")
    if any(not isinstance(a, (int, float)) for a in x):
        raise TypeError(f"{name} must contain only numbers")

def _validate_weights(w, n):
    if w is None:
        return
    if not isinstance(w, (list, tuple)) or len(w) != n:
        raise ValueError("w must have the same length as the vectors")
    if any(not isinstance(a, (int, float)) or a < 0 for a in w):
        raise ValueError("weights must be non-negative numbers")

def minkowski(u, v, p=2, w=None):
    """Weighted Minkowski distance: (sum(w[i]*abs(u[i]-v[i])**p))**(1/p)."""
    _validate_vector(u, "u")
    _validate_vector(v, "v")
    if len(u) != len(v):
        raise ValueError("u and v must have the same length")
    if not isinstance(p, (int, float)) or p <= 0:
        raise ValueError("p must be a positive number")
    _validate_weights(w, len(u))
    weights = [1.0] * len(u) if w is None else w
    return sum(weights[i] * abs(u[i]-v[i])**p for i in range(len(u)))**(1/p)

if __name__ == "__main__":
    tests = [
        ([1,2,3], [3,2,1], 2, [0.1,0.7,0.2]),
        ([0,1,1,0,0,1], [1,0,0,1,1,0], 0.5, None),
        ([0.1,0.5,-0.3,-1.2], [-0.5,1.5,0.3,0.6], 3, None)
    ]
    for u,v,p,w in tests:
        print(minkowski(u,v,p,w))
