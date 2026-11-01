---
tag: 5T4DY28JSK
kind: definition
name: Vandermonde matrix
msc: [15B99, 15A15, 41A05]
defines: Q3JWBZ7EFY
uses: [0VD9ZSWWJG, 0310REJJY8]
sources:
  - url: https://en.wikipedia.org/wiki/Vandermonde_matrix
---

## Definition

Let $R$ be a [[commutative ring|0310REJJY8]], let $m, n \ge 1$, and let $x_1, \dots, x_m \in R$.
The *Vandermonde matrix* of $x_1, \dots, x_m$ with $n$ columns is the $m \times n$ [[matrix|0VD9ZSWWJG]] $V$ with entries
$$V_{ij} = x_i^{\,j-1} \qquad (1 \le i \le m,\ 1 \le j \le n),$$
where $x_i^0 = 1$.

## Remarks

Example: for $x_1 = 1$, $x_2 = 2$, $x_3 = 3$ and $n = 3$, the matrix is $\begin{pmatrix} 1 & 1 & 1 \\ 1 & 2 & 4 \\ 1 & 3 & 9 \end{pmatrix}$; row $i$ is $(1, x_i, x_i^2)$.
Non-example: $\begin{pmatrix} 2 & 4 \\ 3 & 9 \end{pmatrix}$ is not a Vandermonde matrix, because a Vandermonde matrix has first column $1, \dots, 1$.
It is obtained from the Vandermonde matrix $\begin{pmatrix} 1 & 2 \\ 1 & 3 \end{pmatrix}$ of $2, 3$ by multiplying row $i$ by $x_i$.
In the square case $m = n$, the [[Vandermonde determinant|0P84B554AS]] is $\det V = \prod_{1 \le i < j \le n} (x_j - x_i)$.
For a polynomial $p(t) = c_0 + c_1 t + \cdots + c_{n-1} t^{n-1}$, the vector $V c$ lists the values $p(x_1), \dots, p(x_m)$.
Some authors use the transpose of $V$ instead.
