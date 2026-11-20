---
tag: 0AXZNE5XNH
kind: concept
name: Symmetric bilinear form
msc: ["15A63"]
topics: [DYAK7YMK7B]
audience: ug1
specializes: [0SQZMXB6GP]
uses: [0SQZMXB6GP, 0QK6K857HS, 0VR671PHE5]
sources:
  - url: https://en.wikipedia.org/wiki/Symmetric_bilinear_form
    locator: Formal definition
  - url: https://en.wikipedia.org/wiki/Symmetric_bilinear_form
    locator: lead section
  - book: isbn:9780387728285
    locator: Chapter 11
  - url: https://en.wikipedia.org/wiki/Sylvester%27s_law_of_inertia
    locator: lead section
same_as:
  wikidata: Q2100018
  wikipedia: Symmetric bilinear form
---

## Summary

Let $V$ be a vector space over a field $F$.
A symmetric bilinear form on $V$ is a [[bilinear form|0SQZMXB6GP]] $B$ with $B(u, v) = B(v, u)$ for all $u, v \in V$.
The [[formal definition|0744CN4MDA]] states the same.
In a basis, $B$ is symmetric exactly when its [[matrix|0QK6K857HS]] is a [[symmetric matrix|0VR671PHE5]].
Symmetric forms matter because they carry the geometry of lengths and right angles, and they are the bilinear side of [[quadratic forms|0RBQS1JJCR]].

## Motivation

In the plane, the angle between $u$ and $v$ is the angle between $v$ and $u$.
The [[dot product|0S52TNNTH9]] reflects this: $u \cdot v = v \cdot u$.
A form with this symmetry gives a relation "$u$ is orthogonal to $v$" that does not depend on the order of $u$ and $v$.
Symmetric forms also arise from functions of degree $2$: the expression $q(x + y) - q(x) - q(y)$ is symmetric in $x$ and $y$.

## Notation

- A space $V$ with a symmetric bilinear form $B$ is often written $(V, B)$, and called a quadratic space or an orthogonal space in some books.
- When $B$ has a diagonal matrix $\operatorname{diag}(a_1, \dots, a_n)$ in some basis, many books write $B = \langle a_1, \dots, a_n \rangle$.

## Remarks

### Examples

- The [[dot product|0S52TNNTH9]] on $F^n$ is symmetric, because $x_k y_k = y_k x_k$ in $F$.
- The [[trace form $\tr(XY)$ on $M_2(F)$|CWKB533GHM]] is symmetric, because $\tr(XY) = \tr(YX)$.
- The [[form $x_1 y_1 - x_2 y_2$ on $\R^2$|X6C1Z0W252]] is symmetric. It is not positive, and it has nonzero vectors with $B(v, v) = 0$.
- For each symmetric matrix $A$, the form $x^T A y$ is symmetric, because $y^T A x$ is a $1 \times 1$ matrix and so equals its transpose $x^T A^T y = x^T A y$.
- Every real [[inner product|0NB0AWGJBW]] is a symmetric form with $B(v, v) > 0$ for $v \neq 0$.

### Non-examples

- The [[form with matrix $\begin{pmatrix} 1 & 2 \\ 0 & 3 \end{pmatrix}$|N9CJZW5596]] is not symmetric: $B(e_1, e_2) = 2$ but $B(e_2, e_1) = 0$.
- The [[determinant form $x_1 y_2 - x_2 y_1$|8K74K4BF5H]] is not symmetric when $\operatorname{char} F \neq 2$: it gives $1$ on $(e_1, e_2)$ and $-1$ on $(e_2, e_1)$.
- The [[standard inner product on $\C^n$|TFZ8DYVJ1J]] is not a symmetric bilinear form: it is conjugate-linear in the second slot, and $\ip{y}{x} = \overline{\ip{x}{y}}$.

### Basic properties

- $B$ is symmetric exactly when its matrix $A$ satisfies $A^T = A$. One direction: $A_{ji} = B(e_j, e_i) = B(e_i, e_j) = A_{ij}$. The other direction: the formula $x^T A y$ of the [[correspondence theorem|ZVMJAF7D53]].
- $B$ is symmetric exactly when the two maps $u \mapsto B(u, \cdot)$ and $v \mapsto B(\cdot, v)$ into $V^*$ are equal.
- The symmetric forms on a space of dimension $n$ form a subspace of dimension $n(n + 1)/2$, since a symmetric matrix is fixed by its entries on and above the diagonal.
- If $\operatorname{char} F \neq 2$, every bilinear form is the sum of a symmetric form $\frac12(B(u, v) + B(v, u))$ and a [[skew-symmetric form|0DGDS5XY84]] $\frac12(B(u, v) - B(v, u))$.
- For a symmetric form, orthogonality is a symmetric relation, so the form is [[reflexive|M0G958M917]].
- If $\operatorname{char} F \neq 2$, a symmetric form is fixed by its values $B(v, v)$, by the [[polar form|0HYFWKKY3C]]. Sub-area 20 studies this link with quadratic forms.

### History

Sylvester published his law of inertia for real symmetric forms in 1852, according to the Wikipedia article on the law.

### Common errors

- A symmetric form need not be positive. The form $x_1 y_1 - x_2 y_2$ is symmetric, and $B(e_2, e_2) = -1$.
- In characteristic $2$, symmetric and skew-symmetric forms are the same, since $-1 = 1$. Then a symmetric form need not come from its values $B(v, v)$: the [[determinant form|8K74K4BF5H]] over $\mathbb{F}_2$ is symmetric with $B(v, v) = 0$ for all $v$.
- The matrix of a symmetric form is symmetric in every basis, but it is diagonal only in special bases.

## Explanations

### L1 human

A symmetric form gives the same number when we swap the two vectors.
The dot product is the main example: $(1, 2) \cdot (3, 4) = 11 = (3, 4) \cdot (1, 2)$.
The square of numbers that describes a symmetric form is the same as its mirror image across the diagonal.
Symmetric forms can give negative numbers, unlike the dot product of a vector with itself.

### L2 human

We check that $B(x, y) = 2x_1 y_1 + 3x_1 y_2 + 3x_2 y_1 - x_2 y_2$ on $\Q^2$ is symmetric.

1. The matrix is $A = \begin{pmatrix} 2 & 3 \\ 3 & -1 \end{pmatrix}$, read off from the coefficients of $x_i y_j$.
2. $A^T = A$, so $B$ is symmetric.
3. A check: $B((1, 0), (0, 1)) = 3$ and $B((0, 1), (1, 0)) = 3$.
4. The value $B(v, v)$ for $v = (x_1, x_2)$ is $2x_1^2 + 6x_1 x_2 - x_2^2$, a polynomial of degree $2$.

The typical use is to study the geometry of the form: its orthogonal vectors, its orthogonal bases and its signature.
A trap: the coefficient $6$ of $x_1 x_2$ in $B(v, v)$ splits into two matrix entries of $3$, not one entry of $6$.

### L3 human

Symmetric bilinear forms are the elements of $(\operatorname{Sym}^2 V)^*$, and outside characteristic $2$ they correspond to [[quadratic forms|0RBQS1JJCR]].
Their classification up to [[congruence|WJWNYSQKK8]] depends on the arithmetic of the field, and it leads to the [[Witt group|KFVY0RPGF2]] and the [[Hasse-Minkowski theorem|R8HCWA981S]] in number theory.
The isometries of a nondegenerate symmetric form make the [[orthogonal group|0TKYAEJ8N7]], and a pseudo-Riemannian metric on a manifold is a smooth family of nondegenerate symmetric forms on the tangent spaces.
