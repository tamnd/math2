---
tag: PWKN6ANA0G
kind: statement
role: theorem
name: Levy–Desplanques theorem
msc: [15A15, 15A42]
uses: [89P5GTKW87, 0EB9N0S33C, 00KDZRW4C0]
about: [89P5GTKW87, 0EB9N0S33C]
sources:
  - url: https://en.wikipedia.org/wiki/Diagonally_dominant_matrix
---

## Statement

Let $A = (a_{ij})$ be an $n \times n$ complex matrix that is strictly [[diagonally dominant|89P5GTKW87]] by rows:
$$\abs{a_{ii}} > \sum_{j \ne i} \abs{a_{ij}} \quad \text{for } i = 1, \dots, n.$$
Then $A$ is [[invertible|0EB9N0S33C]], that is, $\det A \ne 0$.

## Remarks

Suppose $Ax = 0$ with $x \ne 0$, and choose $i$ with $\abs{x_i}$ maximal, so $\abs{x_i} > 0$.
Row $i$ gives $a_{ii} x_i = -\sum_{j \ne i} a_{ij} x_j$, so $\abs{a_{ii}} \abs{x_i} \le \sum_{j \ne i} \abs{a_{ij}} \abs{x_i}$.
This contradicts strict dominance in row $i$.
Equivalently, $0$ lies in no disc of the [[Gershgorin circle theorem|0ETGP0XVCJ]].

Example: $\begin{pmatrix} 3 & 1 & 1 \\ 0 & 2 & 1 \\ 1 & -1 & 4 \end{pmatrix}$ is strictly diagonally dominant, so it is invertible without any computation.

Strictness is necessary: $\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$ satisfies $\abs{a_{ii}} \ge \sum_{j \ne i} \abs{a_{ij}}$ with equality, and it is singular.
The theorem also holds for strict dominance by columns, by applying it to $A^T$.

## Explanations

### L1 human

If each diagonal entry is larger in absolute value than all other entries of its row together, the matrix cannot send a nonzero vector to zero.
The diagonal wins against the rest of the row, so it can never be cancelled.

### L2 human

The theorem gives a cheap test for invertibility, used for the matrices that arise when differential equations are discretised.
For strictly diagonally dominant matrices, the Jacobi and Gauss–Seidel iterations for $Ax = b$ converge.
It is the special case "$0$ is not an eigenvalue" of the Gershgorin circle theorem.
