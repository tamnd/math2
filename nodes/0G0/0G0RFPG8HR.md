---
tag: 0G0RFPG8HR
kind: concept
name: Eigenspace
msc: ["15A18"]
topics: [6R1D6QPY3S]
audience: ug1
specializes: [0ACX5QT8TE]
uses: [0BQAA2BK3Q, 0N6960W0BV, 0S23E6YE83, 0J7H0YBFDJ]
sources:
  - url: https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors
    locator: Eigenspaces, geometric multiplicity, and the eigenbasis
  - url: https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors
    locator: History
  - book: isbn:9783031410253
    locator: Chapter 5
  - book: isbn:9780321982384
---

## Summary

The eigenspace of a linear map for a scalar $\lambda$ collects all the vectors that the map multiplies by $\lambda$, together with the zero vector.
It is a subspace, so it can be described by a basis, and it is the place where the map acts as plain multiplication by $\lambda$.
Let $T \colon V \to V$ be an [[endomorphism|0J7H0YBFDJ]] of a vector space $V$ over a field $F$, and let $\lambda \in F$.
The *eigenspace* of $T$ for $\lambda$ is
$$E_\lambda = \ker(T - \lambda \id_V) = \{ v \in V : T(v) = \lambda v \}.$$
Its nonzero vectors are the [[eigenvectors|0N6960W0BV]] of $T$ for $\lambda$, so $E_\lambda \ne 0$ exactly when $\lambda$ is an [[eigenvalue|0BQAA2BK3Q]] of $T$.
The [[formal definition|0AYEPBQMAW]] states this, and it allows every $\lambda$, also when $E_\lambda = 0$.

## Motivation

The eigenvectors for one eigenvalue do not form a subspace, because the zero vector is missing.
Adding it repairs this, and the result is the [[kernel|0S23E6YE83]] of the linear map $T - \lambda \id_V$.
So we can use all the tools for subspaces: bases, dimension and row reduction.

The dimension of $E_\lambda$ counts the independent directions that $T$ stretches by $\lambda$.
This number is the [[geometric multiplicity|099TWVJ909]] of $\lambda$.
The sub-area on [[diagonalization|Z6S6PWMJPH]] shows that a map has a basis of eigenvectors exactly when these dimensions add up to $\dim V$.

## Notation

Books write $E_\lambda$, $E_\lambda(T)$, $V_\lambda$ or $E(\lambda, T)$; Axler uses the last one.
For a matrix $A$, the eigenspace $E_\lambda(A)$ is the null space of $A - \lambda I$.
In Mathlib it is `Module.End.eigenspace T λ`.
Do not confuse $E_\lambda$ with the generalized eigenspace $\ker (T - \lambda \id_V)^n$, which can be larger.

## Remarks

### A first computation

Take $A = \begin{pmatrix} 4 & 1 & 1 \\ 1 & 4 & 1 \\ 1 & 1 & 4 \end{pmatrix}$ and $\lambda = 3$.
Every row of $A - 3I$ is $(1, 1, 1)$, so the system $(A - 3I)v = 0$ is the single equation
$$v_1 + v_2 + v_3 = 0.$$
Choose $v_2$ and $v_3$ freely; the basis $(1, -1, 0)$ and $(1, 0, -1)$ shows that $E_3$ is a plane, of dimension $2$.
Check: $A(1, -1, 0) = (3, -3, 0)$ and $A(1, 0, -1) = (3, 0, -3)$.
[[The 3 by 3 matrix with 4 on the diagonal and 1 elsewhere|7XFGVVTZ2X]] studies this matrix in full.

### A basis by row reduction

For the same matrix and $\lambda = 6$, row reduce $A - 6I$:
$$\begin{pmatrix} -2 & 1 & 1 \\ 1 & -2 & 1 \\ 1 & 1 & -2 \end{pmatrix} \longrightarrow \begin{pmatrix} 1 & -2 & 1 \\ 0 & -3 & 3 \\ 0 & 3 & -3 \end{pmatrix} \longrightarrow \begin{pmatrix} 1 & 0 & -1 \\ 0 & 1 & -1 \\ 0 & 0 & 0 \end{pmatrix}.$$
The first step swaps rows $1$ and $2$ and clears the first column, and the second step clears the second column and scales.
The reduced system says $v_1 = v_3$ and $v_2 = v_3$, so $E_6$ is the line spanned by $(1, 1, 1)$.
Check: $A(1, 1, 1) = (6, 6, 6)$.
In general, by [[rank-nullity|0W4FSW1TVB]], $\dim E_\lambda = n - \operatorname{rank}(A - \lambda I)$; here $3 - 2 = 1$.

### An invariant subspace

The map sends its eigenspace into itself: if $v \in E_\lambda$, then $T(v) = \lambda v$ lies in $E_\lambda$ again.
So $E_\lambda$ is an [[invariant subspace|0ACX5QT8TE]], and $T$ restricted to it is $\lambda \id_{E_\lambda}$.
For each eigenvalue it is a nonzero invariant subspace, and it is the largest subspace on which $T$ acts as the scalar $\lambda$.
Maps that commute with $T$ also keep it: if $ST = TS$ and $v \in E_\lambda$, then $T(Sv) = S(Tv) = \lambda Sv$, so $Sv \in E_\lambda$.

### Other examples

The derivative on smooth functions has the line spanned by $e^{\lambda x}$ as its eigenspace for $\lambda$, as [[the eigenvalues of the derivative|1SKH5XJ5RB]] show.
A reflection of the plane has a line of fixed vectors and a line of reversed vectors as its two eigenspaces, as in [[projections, reflections and shears of the plane|HJ117SV1AN]].
At the extremes, the eigenspace of $\id_V$ for $1$ is all of $V$, and so is the eigenspace of the zero map for $0$.

### The rules you can use

For distinct scalars $\lambda_1, \dots, \lambda_k$, the sum $E_{\lambda_1} + \dots + E_{\lambda_k}$ is direct, by the theorem that [[eigenvectors with distinct eigenvalues are linearly independent|0HNMFG8F8K]].
So in a space of dimension $n$ the dimensions of all the eigenspaces add up to at most $n$.
The map is [[diagonalizable|07SQCNV233]] exactly when these dimensions add up to $n$, that is, when $V$ is the direct sum of the eigenspaces.
For the matrix above, $2 + 1 = 3$, so it is diagonalizable.

### Watch out

The union of two eigenspaces is not a subspace.
For $\operatorname{diag}(1, 2)$, the vectors $(1, 0) \in E_1$ and $(0, 1) \in E_2$ add up to $(1, 1)$, which lies in neither, as [[the union of two eigenspaces is not a subspace|7WYEAWSYNZ]] shows.
The right object is the sum $E_1 + E_2$.
A second trap is to take the generalized eigenspace for the eigenspace.
For the shear $H = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ we have $(H - I)^2 = 0$, so the generalized eigenspace is the whole plane, while $E_1 = \ker(H - I)$ is only the horizontal axis.

### History

Lagrange saw that the principal axes of a rotating rigid body are the eigenvectors of its inertia matrix.
Cauchy used this work to classify the quadric surfaces, and he extended it to any number of dimensions.

### Try it

First, find the eigenspace of $\operatorname{diag}(2, 2, 5)$ for $2$.
The equation $(A - 2I)v = (0, 0, 3v_3) = 0$ gives $v_3 = 0$, so $E_2$ is the plane spanned by $e_1$ and $e_2$.

Second, find $E_0$ for $\begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$.
Both rows give $v_1 + 2v_2 = 0$, so $E_0$ is the line spanned by $(2, -1)$.

## Explanations

### L1 human

Fix one stretch factor, say $3$, and collect all the arrows that the map stretches by exactly $3$.
Add the zero arrow to the collection.
The result is always a flat space through the origin: a line, a plane, or something bigger.
This flat space is the eigenspace for $3$, and on it the map just multiplies by $3$.

### L2 human

Here is a typical use: build a basis of eigenvectors for $A = \begin{pmatrix} 4 & 1 & 1 \\ 1 & 4 & 1 \\ 1 & 1 & 4 \end{pmatrix}$.
The eigenspaces found above give the three vectors $(1, -1, 0)$, $(1, 0, -1)$ and $(1, 1, 1)$.
Put them into the columns of $S$, and expand along the first row:
$$\det S = \det \begin{pmatrix} 1 & 1 & 1 \\ -1 & 0 & 1 \\ 0 & -1 & 1 \end{pmatrix} = 1 \cdot 1 - 1 \cdot (-1) + 1 \cdot 1 = 3 \ne 0.$$
So the three vectors form a basis, and $S^{-1} A S = \operatorname{diag}(3, 3, 6)$.
The method always works this way: a basis of each eigenspace, joined together, gives an independent set.
Watch out: the basis of $E_\lambda$ comes from the null space of $A - \lambda I$, not from its column space.

### L3 human

The eigenspace $E_\lambda$ is the largest subspace on which $T$ acts as the scalar $\lambda$.
For a family of commuting endomorphisms, each eigenspace of one member is invariant under all the others, and this leads to simultaneous diagonalization.
In the language of modules over $F[x]$, with $x$ acting as $T$, the eigenspace $E_\lambda$ is the set of elements killed by $x - \lambda$.
For self-adjoint operators on inner product spaces, eigenspaces for distinct eigenvalues are orthogonal, which is the start of the [[spectral theorems|3YM9EK6VMB]].
