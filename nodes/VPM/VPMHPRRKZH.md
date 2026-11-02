---
tag: VPMHPRRKZH
kind: definition
name: Positive-definite function
msc: [42A82, 43A35]
defines: F73VWGF637
uses: [0880F9EQCP, 0EKZCX4K3P]
sources:
  - url: https://en.wikipedia.org/wiki/Positive-definite_function
---

## Definition

Let $n \ge 1$.
A function $f \colon \R^n \to \C$ is *positive-definite* if for every $N \ge 1$, all points $x_1, \dots, x_N \in \R^n$ and all $c_1, \dots, c_N \in \C$,
$$\sum_{i=1}^{N} \sum_{j=1}^{N} c_i \, \overline{c_j} \, f(x_i - x_j) \ge 0.$$

## Remarks

Equivalently, each matrix $\big( f(x_i - x_j) \big)_{i,j=1}^{N}$ is [[Hermitian|0EKZCX4K3P]] and [[positive semidefinite|0880F9EQCP]].
Taking $N = 1$ and $N = 2$ gives $f(0) \ge 0$, $f(-x) = \overline{f(x)}$ and $\abs{f(x)} \le f(0)$.
This is the case $G = \R^n$ of a [[positive-definite function on a group|3PRZ02APFA]], except that continuity is not part of the definition here.
Some authors call these functions positive semidefinite and reserve "positive-definite" for strict inequality when the points are distinct and $c \ne 0$.

Example: $f(x) = \cos x$ on $\R$.
Since $\cos(x_i - x_j) = \frac12 \big( e^{ix_i} e^{-ix_j} + e^{-ix_i} e^{ix_j} \big)$,
$$\sum_{i,j} c_i \overline{c_j} \cos(x_i - x_j) = \frac12 \Big| \sum_i c_i e^{ix_i} \Big|^2 + \frac12 \Big| \sum_i c_i e^{-ix_i} \Big|^2 \ge 0.$$

Non-example: $f = 1_{[-1,1]}$ on $\R$.
For the points $0, 1, 2$ the matrix $\big(f(x_i - x_j)\big)$ is
$$\begin{pmatrix} 1 & 1 & 0 \\ 1 & 1 & 1 \\ 0 & 1 & 1 \end{pmatrix},$$
whose determinant is $-1$.
A positive semidefinite matrix has nonnegative determinant, so $f$ is not positive-definite.
