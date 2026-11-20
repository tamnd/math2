---
tag: W5FHT07SJJ
kind: definition
name: Symplectic vector space
msc: ["15A63", "53D05"]
topics: [DYAK7YMK7B]
audience: grad
defines: PQ7JJY0VPH
uses: [0ZHWKQMVX5, 0SQZMXB6GP, 08ZQAKBKHF, 0KAN330PAH]
sources:
  - url: https://en.wikipedia.org/wiki/Symplectic_vector_space
    locator: Standard symplectic space
---

## Definition

Let $F$ be a field and let $V$ be a [[finite-dimensional vector space|0ZHWKQMVX5]] over $F$.
A *symplectic form* on $V$ is a [[bilinear form|0SQZMXB6GP]] $\omega \colon V \times V \to F$ such that:

1. $\omega$ is [[alternating|08ZQAKBKHF]]: $\omega(v, v) = 0$ for all $v \in V$;
2. $\omega$ is [[nondegenerate|0KAN330PAH]]: if $\omega(v, w) = 0$ for all $w \in V$, then $v = 0$.

A *symplectic vector space* is a pair $(V, \omega)$ of such a space $V$ and a symplectic form $\omega$ on $V$.
A subspace $L$ of $V$ is *Lagrangian* when $L^\perp = L$, where $L^\perp = \{v : \omega(w, v) = 0 \text{ for all } w \in L\}$.

## Notation

The standard symplectic space is $F^{2m}$ with $\omega(x, y) = x^T J y$, where $J = \begin{pmatrix} 0 & I_m \\ -I_m & 0 \end{pmatrix}$.

## Remarks

Example: on $F^{2m}$ with coordinates $(x_1, \dots, x_m, y_1, \dots, y_m)$, the standard form is $\omega(u, u') = \sum_{i=1}^m (x_i y'_i - x'_i y_i)$.
It is alternating, since each term vanishes when $u = u'$.
It is nondegenerate: if $u$ has $x_i \ne 0$, then $\omega(u, f_i) = x_i \ne 0$, and if $u$ has $y_i \ne 0$, then $\omega(u, e_i) = -y_i \ne 0$.
Here $e_i$ and $f_i$ are the standard basis vectors for the coordinates $x_i$ and $y_i$.
Non-example: the form $\omega(u, u') = x_1 y'_1 - x'_1 y_1$ on $F^3$ with coordinates $(x_1, y_1, z)$ is alternating but degenerate, because $(0, 0, 1)$ pairs to zero with every vector.
Every symplectic vector space has even dimension $2m$ and a basis $e_1, \dots, e_m, f_1, \dots, f_m$ with $\omega(e_i, f_j) = \delta_{ij}$ and $\omega(e_i, e_j) = \omega(f_i, f_j) = 0$, by the [[classification of alternating forms|~a52a9f11]].
When $\operatorname{char} F \neq 2$, alternating is the same as skew-symmetric: $\omega(v, w) = -\omega(w, v)$.
In characteristic $2$ it is not.

## Explanations

### L1 human

A symplectic form is an area form on a vector space.
It gives zero for a vector with itself, and it sees every nonzero vector.

### L2 human

On $F^2$, $\omega(x, y) = x_1 y_2 - x_2 y_1$ is a symplectic form, with matrix $\begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$ of determinant $1$.
Each line $L$ in $F^2$ is Lagrangian: $\omega(v, v) = 0$ gives $L \subseteq L^\perp$, and $\dim L^\perp = 1$.
A trap: over $\mathbb{F}_2$, the identity matrix gives a nondegenerate skew-symmetric form that is not symplectic.
