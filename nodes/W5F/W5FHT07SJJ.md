---
tag: W5FHT07SJJ
kind: definition
name: Symplectic vector space
msc: [15A63, 53D05]
defines: PQ7JJY0VPH
uses: [0ZHWKQMVX5, 0SQZMXB6GP, 0DGDS5XY84, 01NHFZF2SK]
sources:
  - url: https://en.wikipedia.org/wiki/Symplectic_vector_space
---

## Definition

Let $F$ be a field and let $V$ be a [[finite-dimensional vector space|0ZHWKQMVX5]] over $F$.
A *symplectic form* on $V$ is a [[bilinear form|0SQZMXB6GP]] $\omega \colon V \times V \to F$ such that:

1. $\omega$ is [[alternating|0DGDS5XY84]]: $\omega(v, v) = 0$ for all $v \in V$.
2. $\omega$ is [[nondegenerate|01NHFZF2SK]]: if $\omega(v, w) = 0$ for all $w \in V$, then $v = 0$.

A *symplectic vector space* is a pair $(V, \omega)$ of such a space $V$ and a symplectic form $\omega$ on $V$.

## Remarks

Example: on $F^{2n}$ with coordinates $(x_1, \dots, x_n, y_1, \dots, y_n)$, the standard form is $\omega(u, u') = \sum_{i=1}^n (x_i y'_i - x'_i y_i)$.
It is alternating, since each term vanishes when $u = u'$.
It is nondegenerate: if $u$ has $x_i \ne 0$, then $\omega(u, f_i) = x_i \ne 0$, and if $u$ has $y_i \ne 0$, then $\omega(u, e_i) = -y_i \ne 0$.
Here $e_i$ and $f_i$ are the standard basis vectors for the coordinates $x_i$ and $y_i$.
Non-example: the form $\omega(u, u') = x_1 y'_1 - x'_1 y_1$ on $F^3$ with coordinates $(x_1, y_1, z)$ is alternating but degenerate, because $(0, 0, 1)$ pairs to zero with every vector.
Every symplectic vector space has even dimension $2n$ and a basis $e_1, \dots, e_n, f_1, \dots, f_n$ with $\omega(e_i, f_j) = \delta_{ij}$ and $\omega(e_i, e_j) = \omega(f_i, f_j) = 0$.
In such a basis, the matrix of $\omega$ is $J = \begin{pmatrix} 0 & I_n \\ -I_n & 0 \end{pmatrix}$.
In characteristic other than $2$, alternating is the same as skew-symmetric: $\omega(v, w) = -\omega(w, v)$.
