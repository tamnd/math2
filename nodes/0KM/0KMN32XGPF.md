---
tag: 0KMN32XGPF
kind: statement
role: proposition
name: Determinant of a linear map is the determinant of its matrix
msc: [15A04, 15A15]
topics: [DTBK11SR77]
audience: ug2
uses: [03F5KP94K0, 0YYMY95FWS]
sources:
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: Determinant of an endomorphism
---

## Statement

Let $F$ be a field, let $V$ be a finite-dimensional vector space over $F$ with a basis $B$, and let $T \colon V \to V$ be a linear map.
Then the [[determinant of $T$|03F5KP94K0]] equals the determinant of the [[matrix of $T$|0YYMY95FWS]] in $B$:
$$\det T = \det [T]_B.$$
In particular, $\det [T]_B = \det [T]_{B'}$ for any two bases $B$ and $B'$ of $V$.

## Remarks

### Why each hypothesis is needed

- Finite dimension: an infinite-dimensional space has no finite matrix for $T$.
- One basis $B$ for the domain and the codomain: with $B$ on the domain and $B'$ on the codomain, the matrix of $\operatorname{id}_V$ is a change of basis matrix, and its determinant can be any nonzero scalar.
- Commutativity of $F$: the proof uses $\det(P^{-1}) \det(A) \det(P) = \det(A)$, which needs commuting factors.

### Consequences

- Similar matrices have the same determinant, because they are matrices of one map in two bases.
- $\det(S \circ T) = \det S \cdot \det T$, because $[S \circ T]_B = [S]_B [T]_B$ and the determinant of matrices is multiplicative.
- If $T$ has a basis of eigenvectors with eigenvalues $\lambda_1, \dots, \lambda_n$, then $\det T = \lambda_1 \cdots \lambda_n$.

### Converse

Equal determinants do not make two matrices similar.
For example, $I_2$ and $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ both have determinant $1$.
They are not similar, because $P^{-1} I_2 P = I_2$ for every invertible $P$.

### Generalizations

- The statement holds for an endomorphism of a free module of finite rank over a commutative ring, with the same proof.
- The trace and the characteristic polynomial of $[T]_B$ also do not depend on $B$.

## Explanations

### L1 human

We can compute the determinant of a linear map in any basis.
We write its matrix in that basis, and we take the determinant of the matrix.
Every basis gives the same answer.

### L2 human

Let $T \colon \mathbb{R}^2 \to \mathbb{R}^2$ be the reflection in the line $y = x$, so $T(x, y) = (y, x)$.

1. In the standard basis, $[T] = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$, with determinant $-1$.
2. In the basis $(1, 1), (1, -1)$: $T(1, 1) = (1, 1)$ and $T(1, -1) = -(1, -1)$.
3. So the matrix is $\operatorname{diag}(1, -1)$, again with determinant $-1$.

The typical use is to choose the basis that makes the matrix diagonal or triangular.
A trap: the statement needs the same basis on both sides of $T$.

### L3 human

A basis-free reason: $\Lambda^n V$ is a line, and $\Lambda^n T$ acts on it as multiplication by one scalar.
The determinant of $[T]_B$ is this scalar, computed with the generator $b_1 \wedge \dots \wedge b_n$ of $\Lambda^n V$.
