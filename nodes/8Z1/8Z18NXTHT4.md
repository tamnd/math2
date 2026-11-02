---
tag: 8Z18NXTHT4
kind: definition
name: Cayley–Menger determinant
msc: [51K05, 51M25]
defines: KGC5CYDF53
uses: [0C3CFHDN6R, 0C95TG69SG]
sources:
  - url: https://en.wikipedia.org/wiki/Cayley%E2%80%93Menger_determinant
---

## Definition

Let $n \ge 1$ and $N \ge 1$, and let $p_0, \ldots, p_n$ be points of $\R^N$.
Write $d_{ij} = \norm{p_i - p_j}$ for their [[Euclidean distances|0C95TG69SG]].
The *Cayley–Menger determinant* of the points is the [[determinant|0C3CFHDN6R]] of the $(n + 2) \times (n + 2)$ matrix
$$\operatorname{CM}(p_0, \ldots, p_n) = \det \begin{pmatrix} 0 & 1 & 1 & \cdots & 1 \\ 1 & 0 & d_{01}^2 & \cdots & d_{0n}^2 \\ 1 & d_{10}^2 & 0 & \cdots & d_{1n}^2 \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 1 & d_{n0}^2 & d_{n1}^2 & \cdots & 0 \end{pmatrix}.$$

## Remarks

The $n$-dimensional volume $V_n$ of the simplex with vertices $p_0, \ldots, p_n$ satisfies
$$V_n^2 = \frac{(-1)^{n+1}}{2^n (n!)^2} \operatorname{CM}(p_0, \ldots, p_n).$$

Example: for $n = 1$ and two points at distance $d$, the matrix is $\begin{pmatrix} 0 & 1 & 1 \\ 1 & 0 & d^2 \\ 1 & d^2 & 0 \end{pmatrix}$.
Its determinant is $2d^2$, and the formula gives $V_1^2 = \frac{1}{2} \cdot 2d^2 = d^2$, the squared length.

Example: for $n = 2$ and an equilateral triangle of side $1$, the matrix is $J - I$ with $J$ the $4 \times 4$ all-ones matrix.
Its eigenvalues are $3, -1, -1, -1$, so the determinant is $-3$.
The formula gives $V_2^2 = \frac{-1}{16} \cdot (-3) = \frac{3}{16}$, the square of the area $\frac{\sqrt{3}}{4}$.

Degenerate case: if the points are affinely dependent, such as three points on a line, the determinant is $0$.
The border of ones is essential: the determinant of the matrix of squared distances alone does not give the volume.
