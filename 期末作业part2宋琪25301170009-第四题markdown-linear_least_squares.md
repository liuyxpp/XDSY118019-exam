# Linear Least Squares

Linear least squares (LLS) is the least squares approximation of linear functions to data. It is a set of formulations for solving statistical problems involved in [linear regression](https://en.wikipedia.org/wiki/Linear_regression), including variants for ordinary (unweighted), weighted, and generalized (correlated) residuals. Numerical methods for linear least squares include inverting the matrix of the normal equations and orthogonal decomposition methods.


## Basic Formulation

Consider the linear equation
$$
\mathbf{A}\mathbf{x} = \mathbf{b}
$$
where $\mathbf{A} \in \mathbb{R}^{m \times n}$ and $\mathbf{b} \in \mathbb{R}^m$ are given and $x \in \mathbb{R}^n$ is variable to be computed. When $m > n$, it is generally the case that Eq. (1) has no solution. For example, there is no value of $x$ that satisfies
$$
\begin{bmatrix} 1 & 0 \\ 0 & 1 \\ 1 & 1 \end{bmatrix} x = \begin{bmatrix} 1 \\ 1 \\ 0 \end{bmatrix}
$$
because the first two rows require that $x = (1, 1)$, but then the third row is not satisfied. Thus, for $m > n$, the goal of solving Eq. (1) exactly is typically replaced by finding the value of $x$ that minimizes some error. There are many ways that the error can be defined, but one of the most common is to define it as $\|\mathbf{A}\mathbf{x} - \mathbf{b}\|^2$. This produces a minimization problem, called a least squares problem
$$
\text{minimize}_{x \in \mathbb{R}^n} \|\mathbf{A}\mathbf{x} - \mathbf{b}\|^2
$$

The solution to the least squares problem is computed by solving the *normal equation*
$$
\mathbf{A}^T\mathbf{A}\mathbf{x} = \mathbf{A}^T\mathbf{b}
$$
where $\mathbf{A}^T$ denotes the transpose of the matrix $\mathbf{A}$.