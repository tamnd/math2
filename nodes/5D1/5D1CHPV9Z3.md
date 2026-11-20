---
tag: 5D1CHPV9Z3
kind: statement
role: proposition
name: A family of n vectors is a basis if and only if its determinant is nonzero
msc: [15A15, 15A75]
topics: [DTBK11SR77]
audience: ug2
uses: [0V94H674MB, 0VTQTPQGAV]
sources:
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: Determinant of n vectors
---

## Statement

Let $F$ be a field, let $V$ be a vector space over $F$ of dimension $n \ge 1$, and let $B$ be a basis of $V$.
Then vectors $v_1, \dots, v_n \in V$ form a [[basis|0VTQTPQGAV]] of $V$ if and only if
$$\det_B(v_1, \dots, v_n) \ne 0,$$
where $\det_B$ is the [[determinant in the basis $B$|0V94H674MB]].

## Remarks

### Why each hypothesis is needed

- The number of vectors must be $n = \dim V$; otherwise $\det_B$ is not defined.
- $F$ must be a field. Over $\mathbb{Z}$, the family $(2)$ in $\mathbb{Z}^1$ has determinant $2 \ne 0$, but it is not a basis of $\mathbb{Z}$.
- Over a commutative ring, the correct condition is that $\det_B(v_1, \dots, v_n)$ is a unit.

### Consequences

- The vectors are linearly dependent if and only if $\det_B(v_1, \dots, v_n) = 0$.
- The answer can depend on the field: a family with integer coordinates can be a basis over $\mathbb{Q}$ and fail to be one over $\mathbb{F}_2$.
- To test whether $n$ vectors form a basis, one determinant suffices.

### Converse

The statement is an equivalence, so both directions hold.

## Explanations

### L1 human

Take $n$ vectors in an $n$-dimensional space.
Write their coordinates as the columns of a square matrix.
The vectors form a basis exactly when the determinant of this matrix is not zero.

### L2 human

In the space of polynomials of degree at most $2$ with basis $1, x, x^2$, take $1 + x$, $x + x^2$ and $1 + x^2$.

1. The coordinate matrix is $\begin{pmatrix} 1 & 0 & 1 \\ 1 & 1 & 0 \\ 0 & 1 & 1 \end{pmatrix}$.
2. Its determinant is $2$, so over $\mathbb{Q}$ the three polynomials form a basis.

The [[worked example|XNG0N654EM]] checks this by solving a system, and it treats $\mathbb{F}_2$, where the determinant is $0$.
The typical use is a quick test for a basis.
A trap: the test needs exactly $n$ vectors; for fewer vectors, use the rank instead.

### L3 human

The statement is the invertibility criterion for the coordinate matrix, moved to $V$ by the coordinate isomorphism.
Over a commutative ring $K$, the vectors form a basis of the free module if and only if the determinant is a unit of $K$.
