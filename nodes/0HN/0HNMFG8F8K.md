---
tag: 0HNMFG8F8K
kind: statement
role: theorem
name: Eigenvectors with distinct eigenvalues are linearly independent
msc: ["15A18"]
topics: [6R1D6QPY3S]
audience: ug1
about: [0N6960W0BV, 0G0RFPG8HR]
uses: [0B5H4208Z9, 0EVHJFTG9Z, 0AYEPBQMAW]
formal:
  - system: lean4
    library: mathlib
    decl: Module.End.eigenvectors_linearIndependent
    match: exact
sources:
  - url: https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors
    locator: Eigenspaces, geometric multiplicity, and the eigenbasis
  - book: isbn:9783031410253
    locator: Chapter 5
---

## Statement

Eigenvectors that belong to different eigenvalues can never be combined to give one another, so they always form an independent list.
Let $F$ be a field, let $V$ be a vector space over $F$, and let $T \colon V \to V$ be a linear map.

1. Let $v_1, \dots, v_k$ be [[eigenvectors|0N6960W0BV]] of $T$ for eigenvalues $\lambda_1, \dots, \lambda_k$ that are pairwise distinct.
   Then $v_1, \dots, v_k$ are [[linearly independent|0CRMGPAH83]].
2. For pairwise distinct scalars $\lambda_1, \dots, \lambda_k$, the sum $E_{\lambda_1} + \dots + E_{\lambda_k}$ of the [[eigenspaces|0G0RFPG8HR]] is a direct sum.
3. If $\dim V = n$ is finite, then $T$ has at most $n$ distinct eigenvalues, and $\sum_\lambda \dim E_\lambda \le n$.

## Remarks

### A first check

Take $A = \begin{pmatrix} 1 & 2 \\ 0 & 3 \end{pmatrix}$.
It is upper triangular, so its eigenvalues are the diagonal entries $1$ and $3$.
The vectors $v_1 = (1, 0)$ and $v_2 = (1, 1)$ are eigenvectors, as the products show:
$$A v_1 = (1, 0) = 1 \cdot v_1, \qquad A v_2 = (1 + 2, 3) = 3 \cdot v_2.$$
The matrix with columns $v_1, v_2$ has determinant $1 \cdot 1 - 1 \cdot 0 = 1 \ne 0$, so the two vectors are independent, as part 1 says.
In the plane this means that the two eigenvectors lie on two different lines.

### Why each hypothesis is needed

The eigenvalues must be distinct.
For the identity map of $\mathbb{R}^2$, the vectors $e_1$, $e_2$ and $e_1 + e_2$ are all eigenvectors for the eigenvalue $1$, and they are dependent, since the third is the sum of the first two.
Inside one eigenspace, eigenvectors behave like arbitrary nonzero vectors of a subspace, and nothing forces independence.

The vectors must be nonzero, which is part of the definition of an eigenvector.
The zero vector satisfies $T(0) = \lambda \cdot 0$ for every $\lambda$, and a list that contains $0$ is always dependent.

The field matters in one place of the [[proof by induction|E04G0RHT95]]: we divide by $\lambda_i - \lambda_k$, which needs a nonzero scalar to be invertible.

### What it gives you

Part 3 bounds the number of eigenvalues by the dimension, without any determinant.
It also gives the standard test for a good basis.
A map $T$ on an $n$-dimensional space is [[diagonalizable|07SQCNV233]] exactly when the dimensions of its eigenspaces add up to $n$, because part 2 then makes $V$ the direct sum of the eigenspaces.
In particular, an $n \times n$ matrix with $n$ distinct eigenvalues is diagonalizable, as the theorem that [[n distinct eigenvalues imply diagonalizable|0Y95Z7MT02]] states.

The theorem also works in infinite dimension.
The functions $e^{\lambda x}$ for distinct real $\lambda$ are eigenvectors of the [[derivative|1SKH5XJ5RB]], with $\frac{d}{dx} e^{\lambda x} = \lambda e^{\lambda x}$.
So any finite list of them is linearly independent, which is hard to see directly from the functions.

### The converse

The converse is false.
Independent eigenvectors can share an eigenvalue: $e_1$ and $e_2$ are independent eigenvectors of the identity of $\mathbb{R}^2$, both for the eigenvalue $1$.

### Generalizations

Generalized eigenvectors for distinct eigenvalues are also independent, and the sum of the generalized eigenspaces is direct; the [[decomposition into generalized eigenspaces|0Z3GDY89T5]] builds on this.
More generally, if $p_1, \dots, p_k \in F[x]$ are pairwise coprime, then the sum of the kernels of the maps $p_i(T)$ is direct.
Eigenspaces are the case $p_i = x - \lambda_i$.

## History

The result belongs to the standard theory of diagonalization.
Most first courses prove it by induction, and Axler's textbook proves it in chapter 5 with a shortest dependent list, a form of the same argument.

## Explanations

### L1 human

An eigenvector of a matrix is an arrow that the matrix only stretches, and the stretch factor is its eigenvalue.
Two arrows with different stretch factors cannot lie on the same line, because on one line the matrix stretches every arrow by the same factor.
The theorem says more: with any number of different stretch factors, no arrow in the list is a combination of the others.
For example, in space, three eigenvectors with factors $1$, $2$ and $3$ never lie in one plane.

### L2 human

Here is a typical use: show that $A = \begin{pmatrix} 2 & 0 & 0 \\ 1 & 3 & 0 \\ 0 & 1 & 5 \end{pmatrix}$ has a basis of eigenvectors without finding them.
The matrix is lower triangular, so its eigenvalues are $2$, $3$ and $5$.
Each eigenvalue has an eigenvector, and the three eigenvalues are distinct.
By part 1 the three eigenvectors are independent, and three independent vectors in $\mathbb{R}^3$ form a basis.
Watch out: when an eigenvalue repeats, the theorem says nothing, and you must count the dimension of each eigenspace, as the [[3 by 3 matrix with a defective eigenvalue|18XQY67HMS]] shows.

### L3 human

In module language, $V$ is a module over $F[x]$ with $x$ acting as $T$, and $E_\lambda$ is the part of $V$ killed by $x - \lambda$.
The kernel of $p_i(T)$ meets the sum of the other kernels only in $0$, because that sum is killed by the product of the other $p_j$, and a Bézout relation with this coprime product kills every common vector.
This is the first step of the primary decomposition, which the sub-areas on diagonalization and on canonical forms develop.
