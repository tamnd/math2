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

Every basis gives the same determinant for the matrix of a linear map, so the determinant of the map can be computed in any basis we like.
Let $F$ be a field, let $V$ be a finite-dimensional vector space over $F$ with a basis $B$, and let $T \colon V \to V$ be a linear map.
Then the [[determinant of $T$|03F5KP94K0]] equals the determinant of the [[matrix of $T$|0YYMY95FWS]] in $B$, with $B$ used on both sides:
$$\det T = \det [T]_B.$$
In particular, $\det [T]_B = \det [T]_{B'}$ for any two bases $B$ and $B'$ of $V$.

## Remarks

### A check with a reflection

Let $T(x, y) = (y, x)$ be the reflection of $\mathbb{R}^2$ in the line $y = x$.
In the standard basis its matrix and determinant are
$$\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \qquad 0 \cdot 0 - 1 \cdot 1 = -1.$$
In the basis $(1, 1), (1, -1)$ we have $T(1, 1) = (1, 1)$ and $T(1, -1) = (-1, 1) = -(1, -1)$.
So the matrix is $\operatorname{diag}(1, -1)$, and its determinant is $-1$ again.

### Why each hypothesis is needed

The space must be finite-dimensional, because otherwise $T$ has no finite matrix and the right side has no meaning.

The same basis $B$ must be used for the domain and the codomain.
With $B$ on the domain and $B'$ on the codomain, the matrix of $\operatorname{id}_V$ is a change of basis matrix, and its determinant can be any nonzero scalar.
For example, the basis $e_1, e_2$ on the domain of $\operatorname{id}_{\mathbb{R}^2}$ and $c e_1, e_2$ on the codomain give $\operatorname{diag}(1/c, 1)$, with determinant $1/c$.

The scalars must commute.
The proof rewrites $\det(P^{-1}) \det(A) \det(P)$ as $\det(A)$, which moves $\det A$ past $\det P^{-1}$.

### What it gives you

Similar matrices have the same determinant, because they are the matrices of one map in two bases.
The product rule for maps follows: $[S \circ T]_B = [S]_B [T]_B$, so $\det(S \circ T) = \det S \cdot \det T$ by [[multiplicativity|04CPJ6AF00]] for matrices.
If $V$ has a basis of eigenvectors of $T$ with eigenvalues $\lambda_1, \dots, \lambda_n$, then the matrix in that basis is diagonal and $\det T = \lambda_1 \cdots \lambda_n$.
The reflection above shows this with eigenvalues $1$ and $-1$.

### The converse

Equal determinants do not make two matrices similar.
For example, $I_2$ and $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ both have determinant $1$.
They are not similar, because $P^{-1} I_2 P = I_2$ for every invertible $P$, so $I_2$ is similar only to itself.

### Generalizations

The statement holds for an endomorphism of a free module of finite rank over a commutative ring, with the same proof.
The trace and the characteristic polynomial of $[T]_B$ are also the same for all bases, by the same similarity argument.

## Explanations

### L1 human

We can compute the determinant of a linear map in any basis.
We write its matrix in that basis and take the determinant of the matrix.
Every basis gives the same answer, so the answer belongs to the map.

### L2 human

The typical use is to choose a basis that makes the matrix diagonal or triangular, as the reflection above shows.
For the map $T(x, y) = (x + y, 2y)$, the standard basis gives $\begin{pmatrix} 1 & 1 \\ 0 & 2 \end{pmatrix}$ with determinant $2$.
The basis $(1, 0), (1, 1)$ gives $\operatorname{diag}(1, 2)$, since $T(1, 1) = (2, 2)$, and the determinant is $2$ again.
Watch out: the statement needs the same basis on both sides of $T$.

### L3 human

A reason without coordinates uses the top [[exterior power|0MDMZ965VE]] $\Lambda^n V$, which is a line.
The induced map $\Lambda^n T$ acts on that line as multiplication by one scalar.
The determinant of $[T]_B$ is this scalar, computed with the generator $b_1 \wedge \dots \wedge b_n$, and a scalar on a line does not depend on the generator we pick.
The [[proof|YTKK8764G7]] gives the matrix argument in full.
