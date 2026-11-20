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

Let $F$ be a field and let $A$ be an $n \times n$ matrix over $F$, with $n \ge 1$.
Assume that the characteristic polynomial of $A$ splits over $F$ as $p_A(t) = (t - \lambda_1) \cdots (t - \lambda_n)$.
Then
$$\det A = \lambda_1 \lambda_2 \cdots \lambda_n.$$

## Remarks

The $\lambda_i$ are the [[eigenvalues|0BQAA2BK3Q]] of $A$, each repeated according to its [[algebraic multiplicity|0FY42N02DV]].

### Why each hypothesis is needed

- The eigenvalues must be counted with multiplicity. The matrix $\begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix}$ has the single eigenvalue $2$ and the determinant $4 = 2 \cdot 2$.
- The polynomial must split. The real matrix $\begin{pmatrix} 0 & -2 \\ 1 & 0 \end{pmatrix}$ has no real eigenvalue and $\det A = 2$.
- In a splitting field $E$ of $p_A$, the statement holds with the roots in $E$. For the last matrix, the roots are $\pm i \sqrt{2}$, with product $2$.

### Consequences

- $A$ is invertible if and only if $0$ is not an eigenvalue, over a field where $p_A$ splits; this also holds without splitting, by the constant term of $p_A$.
- $\det(A^k) = \prod_i \lambda_i^k$, since $\det$ is multiplicative.
- Over $\C$, $\det(e^A) = e^{\tr A}$, by the proof that the [[determinant of the exponential is the exponential of the trace|W69VC0G18A]]. This is a result of matrix analysis.
- A real matrix with $\det A < 0$ has a negative real eigenvalue, because its nonreal eigenvalues come in conjugate pairs with positive products.

### Converse

The determinant does not determine the eigenvalues: $\operatorname{diag}(1, 4)$ and $\operatorname{diag}(2, 2)$ both have determinant $4$.

### Generalizations

The same formula holds for an endomorphism of a finite-dimensional space, with the [[determinant of the linear map|0X0HQYSZ0K]].
For operators of the form $I + K$ with $K$ trace class, the Fredholm determinant is the product of $1 + \mu_j$ over the eigenvalues $\mu_j$ of $K$.

## History

The relation is Viète's formula for the product of the roots of the characteristic polynomial, applied to its constant term.

## Explanations

### L1 human

The determinant of a matrix is the product of its eigenvalues, counted with multiplicity.
This agrees with the volume picture: in a basis of eigenvectors, the map stretches each direction by its eigenvalue.
The volume then changes by the product of these factors.

### L2 human

We check the theorem for $A = \begin{pmatrix} 4 & 1 & 1 \\ 1 & 4 & 1 \\ 1 & 1 & 4 \end{pmatrix}$.

1. Its eigenvalues are $3$, $3$ and $6$, from $p_A(t) = (t - 3)^2 (t - 6)$.
2. Their product is $3 \cdot 3 \cdot 6 = 54$.
3. By cofactor expansion, $\det A = 4 \cdot 15 - 1 \cdot 3 + 1 \cdot (-3) = 54$.

The typical use is to test invertibility, or to find a missing eigenvalue from the others and the determinant.
A trap: the product uses each eigenvalue as often as its algebraic multiplicity, not once.

### L3 human

The theorem is the case $k = n$ of the formula $E_k(A) = e_k(\lambda_1, \dots, \lambda_n)$ for the [[coefficients of the characteristic polynomial|0FRYPZ6D0X]].
For an endomorphism, $\det T$ is the scalar by which $T$ acts on the top exterior power $\Lambda^n V$, and the eigenvalues give this scalar in a triangular basis.
In Mathlib, `Matrix.det_eq_prod_roots_charpoly` states the theorem over an algebraically closed field.
