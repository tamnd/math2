---
tag: 2JDRN4ZS49
kind: definition
name: Cauchy matrix
msc: [15B05, 15A15]
defines: 95MTQMX59H
uses: [04C5ZBG1WT, 0VD9ZSWWJG]
sources:
  - url: https://en.wikipedia.org/wiki/Cauchy_matrix
---

## Definition

Let $F$ be a [[field|04C5ZBG1WT]], and let $x_1, \dots, x_m$ and $y_1, \dots, y_n$ be elements of $F$ with $x_i \ne y_j$ for all $i, j$.
The *Cauchy matrix* of these elements is the $m \times n$ [[matrix|0VD9ZSWWJG]] $C$ with entries
$$C_{ij} = \frac{1}{x_i - y_j} \qquad (1 \le i \le m,\ 1 \le j \le n).$$

## Remarks

Example: with $x = (1, 2)$ and $y = (0, -1)$ the Cauchy matrix is $\begin{pmatrix} 1 & \tfrac12 \\ \tfrac12 & \tfrac13 \end{pmatrix}$; here $x_1 - y_2 = 2$ and $x_2 - y_2 = 3$.
Non-example: $\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$ is not a Cauchy matrix, because no entry $1/(x_i - y_j)$ can be $0$.
For $m = n$, the Cauchy determinant is
$$\det C = \frac{\prod_{1 \le i < j \le n} (x_j - x_i)(y_i - y_j)}{\prod_{i=1}^n \prod_{j=1}^n (x_i - y_j)}.$$
So a square Cauchy matrix is invertible exactly when the $x_i$ are distinct and the $y_j$ are distinct.
Every square submatrix of a Cauchy matrix is again a Cauchy matrix.
