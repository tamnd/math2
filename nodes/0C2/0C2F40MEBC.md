---
tag: 0C2F40MEBC
kind: statement
role: theorem
name: Determinant is the product of the eigenvalues
msc: ["15A15", "15A18"]
topics: [6R1D6QPY3S]
audience: ug2
about: [00KDZRW4C0, 0BQAA2BK3Q]
uses: [0ZND7NQ970, 0S7A0EMPF4, 0C3CFHDN6R, 039HF58KQ5]
formal:
  - system: lean4
    library: mathlib
    decl: Matrix.det_eq_prod_roots_charpoly
    match: exact
sources:
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: Eigenvalues and characteristic polynomial
  - book: isbn:9780134860244
---

## Statement

The determinant of a square matrix is the product of its eigenvalues, each taken as often as it is a root of the characteristic polynomial.
Let $F$ be a field, let $n \ge 1$ and let $A$ be an $n \times n$ matrix over $F$.
Assume that the [[characteristic polynomial|039HF58KQ5]] of $A$ splits over $F$:
$$p_A(t) = (t - \lambda_1)(t - \lambda_2) \cdots (t - \lambda_n), \qquad \lambda_1, \dots, \lambda_n \in F.$$
Then
$$\det A = \lambda_1 \lambda_2 \cdots \lambda_n.$$
The $\lambda_i$ are the [[eigenvalues|0BQAA2BK3Q]] of $A$, and each appears as often as its [[algebraic multiplicity|0FY42N02DV]].

## Remarks

### A first check

Take the [[symmetric matrix with rows (2, 1) and (1, 2)|Z6K3QPP7DY]], with the eigenvalues $1$ and $3$.
Its determinant is
$$\det \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix} = 2 \cdot 2 - 1 \cdot 1 = 3 = 1 \cdot 3.$$
The [[determinant|00KDZRW4C0]] measures how much the matrix scales area, and the eigenvalues say how much it stretches its two special directions.
The direction $(1, 1)$ is stretched by $3$ and the direction $(1, -1)$ is kept, so the area of the square on these two directions grows by $3 \cdot 1$.

### Why each hypothesis is needed

The eigenvalues must be counted with multiplicity.
The matrix $\begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix}$ has the single eigenvalue $2$, but its determinant is $4$.
The product of the distinct eigenvalues gives $2$, which is wrong; the product $2 \cdot 2$ with multiplicity is right.

The characteristic polynomial must split, or the product is not defined in $F$.
The real matrix $\begin{pmatrix} 0 & -2 \\ 1 & 0 \end{pmatrix}$ has $p_A(t) = t^2 + 2$, so it has no real eigenvalue, while $\det A = 0 \cdot 0 - (-2) \cdot 1 = 2$.
Over $\mathbb{C}$ the roots are $i\sqrt{2}$ and $-i\sqrt{2}$, and their product is $-i^2 \cdot 2 = 2$.
In general we pass to a splitting field $E$ of $p_A$, where $\det A$ and $p_A$ are the same, and there the theorem holds.

### What it gives you

The first use is a test for invertibility.
A matrix is invertible exactly when $\det A \ne 0$, so it is invertible exactly when $0$ is not an eigenvalue.
This holds even when $p_A$ does not split, because $p_A(0) = (-1)^n \det A$, so $0$ is a root of $p_A$ exactly when $\det A = 0$.

The theorem also finds a missing eigenvalue.
The [[3 by 3 matrix with 4 on the diagonal and 1 elsewhere|7XFGVVTZ2X]] has the eigenvalue $3$ twice and determinant
$$4(16 - 1) - 1(4 - 1) + 1(1 - 4) = 60 - 3 - 3 = 54,$$
so the third eigenvalue is $54 / 9 = 6$, which agrees with the trace $12 = 3 + 3 + 6$.

A third use is a sign argument.
A real matrix with $\det A < 0$ has a negative real eigenvalue.
The reason is that the nonreal eigenvalues come in conjugate pairs, and each pair has the positive product $\lambda \bar\lambda = \lvert \lambda \rvert^2$, so the real eigenvalues must supply the negative sign.

Since the determinant is multiplicative, $\det(A^k) = \lambda_1^k \cdots \lambda_n^k$.
Over $\mathbb{C}$, the same idea for the exponential gives $\det(e^A) = e^{\operatorname{tr} A}$, as in the [[proof for the matrix exponential|W69VC0G18A]].

### The converse

The determinant does not determine the eigenvalues.
The matrices $\operatorname{diag}(1, 4)$ and $\operatorname{diag}(2, 2)$ both have determinant $4$, but their eigenvalues differ.
Together with the trace it does determine them for $n = 2$, since the trace and the determinant are the two coefficients of $p_A$ after the leading one.

### Generalizations

The same formula holds for an endomorphism of a finite-dimensional space, with the [[determinant of the linear map|0X0HQYSZ0K]].
For an operator $I + K$ on a Hilbert space with $K$ trace class, the Fredholm determinant is the product of the numbers $1 + \mu_j$ over the eigenvalues $\mu_j$ of $K$.

## History

The relation is Viète's formula for the product of the roots, applied to the constant term of the characteristic polynomial.
The [[proof by comparing constant terms|Z182BABP6P]] makes this precise.

## Explanations

### L1 human

A matrix scales areas and volumes by its determinant.
In the special directions of the matrix, it only stretches, and each stretch factor is an eigenvalue.
If one direction is stretched by $2$ and another by $3$, then a square on those directions becomes a figure with $6$ times the area.
So the determinant is the product of the stretch factors.
A repeated factor must be counted each time it occurs.

### L2 human

Here is a typical use: find the eigenvalues of
$$A = \begin{pmatrix} 1 & 2 \\ 3 & 0 \end{pmatrix}$$
from the trace and the determinant alone.
The trace is $1$ and the determinant is $1 \cdot 0 - 2 \cdot 3 = -6$.
So the two eigenvalues have sum $1$ and product $-6$, and they are the roots of $t^2 - t - 6 = (t - 3)(t + 2)$.
The eigenvalues are $3$ and $-2$.
Check with eigenvectors: $A (1, 1)^{\mathsf{T}} = (3, 3)^{\mathsf{T}} = 3 (1, 1)^{\mathsf{T}}$ and $A (2, -3)^{\mathsf{T}} = (-4, 6)^{\mathsf{T}} = -2 (2, -3)^{\mathsf{T}}$.
Watch out: for $n \ge 3$ the trace and the determinant leave the middle coefficients of $p_A$ free, so they no longer fix the eigenvalues.

### L3 human

The theorem is the case $k = n$ of the formula that makes the coefficients of the characteristic polynomial the elementary symmetric functions of the eigenvalues, as in the theorem on the [[coefficients of the characteristic polynomial|0FRYPZ6D0X]].
For an endomorphism $T$, $\det T$ is the scalar by which $T$ acts on the top exterior power $\Lambda^n V$, and a triangular basis shows that this scalar is the product of the diagonal entries.
In Mathlib, `Matrix.det_eq_prod_roots_charpoly` states the theorem over an algebraically closed field.
