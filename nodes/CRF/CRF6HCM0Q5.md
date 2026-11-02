---
tag: CRF6HCM0Q5
kind: definition
name: Kernel approximation in reproducing kernel Hilbert spaces
msc: ["46E22", 41A05, 41A63]
defines: R7RNMX78KZ
uses: [4CK2GSRAGD, 0VD9ZSWWJG]
sources:
  - url: https://en.wikipedia.org/wiki/Reproducing_kernel_Hilbert_space
---

## Definition

Let $X$ be a set and let $K \colon X \times X \to \R$ be a symmetric positive definite kernel.
Let $H_K$ be its [[reproducing kernel Hilbert space|4CK2GSRAGD]], so that $f(x) = \ip{f}{K(\cdot, x)}_{H_K}$ for all $f \in H_K$ and $x \in X$.
Let $x_1, \dots, x_n \in X$ be distinct points and let $y_1, \dots, y_n \in \R$.
The *kernel matrix* is the $n \times n$ [[matrix|0VD9ZSWWJG]] $\mathbf{K} = (K(x_i, x_j))_{i,j}$.
If $\mathbf{K}$ is invertible, the *kernel interpolant* of the data is
$$s = \sum_{j=1}^{n} c_j K(\cdot, x_j), \qquad \mathbf{K} c = y ,$$
which satisfies $s(x_i) = y_i$ for $i = 1, \dots, n$.
For $\lambda > 0$, the *regularized kernel approximant* is $s_\lambda = \sum_{j} c_j K(\cdot, x_j)$ with $(\mathbf{K} + \lambda I) c = y$.
*Kernel approximation* in $H_K$ is the approximation of a function $f$ by $s$ or $s_\lambda$ built from the data $y_i = f(x_i)$.

## Remarks

The interpolant $s$ is the unique element of minimal norm in $H_K$ among those $g$ with $g(x_i) = y_i$ for all $i$.
If $f \in H_K$ and $y_i = f(x_i)$, then $s$ is the orthogonal projection of $f$ onto the span of $K(\cdot, x_1), \dots, K(\cdot, x_n)$.
The regularized approximant $s_\lambda$ minimizes $\sum_{i} (g(x_i) - y_i)^2 + \lambda \norm{g}_{H_K}^2$ over $g \in H_K$.
For $f \in H_K$, $\abs{f(x) - s(x)} \le P(x) \norm{f}_{H_K}$, where the power function is $P(x)^2 = K(x, x) - k(x)^{T} \mathbf{K}^{-1} k(x)$ with $k(x) = (K(x, x_j))_j$.
Example: $K(x, y) = e^{-(x - y)^2}$ on $X = \R$, points $x_1 = 0$, $x_2 = 1$, data $y = (1, 1)$.
Here $\mathbf{K} = \begin{pmatrix} 1 & e^{-1} \\ e^{-1} & 1 \end{pmatrix}$ is invertible, and $c_1 = c_2 = 1/(1 + e^{-1})$ solves $\mathbf{K} c = y$.
Non-example: the kernel $K(x, y) = xy$ on $\R$ is only positive semidefinite; for the points $1$ and $2$, $\mathbf{K} = \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$ is singular, and the data $y = (1, 0)$ cannot be interpolated by any $c\,x$.
