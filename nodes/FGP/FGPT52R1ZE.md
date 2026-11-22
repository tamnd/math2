---
tag: FGPT52R1ZE
kind: statement
role: proposition
name: The rank of the transpose times a real matrix
aliases: [rank-of-a-gram-matrix]
msc: ["15A03"]
topics: [S6559D61BP]
audience: ug2
about: [0ZC9YTXZRY]
uses: [0EWQEYRVA8, 0W809K6AW0, 076JGP6R3T]
sources:
  - url: https://en.wikipedia.org/wiki/Rank_(linear_algebra)
    locator: Properties
---

## Statement

For a real matrix, multiplying by its transpose keeps the rank.
Let $A$ be an $m \times n$ matrix over $\mathbb{R}$, with [[transpose|0W809K6AW0]] $A^{\mathsf{T}}$.
Then
$$\rank(A^{\mathsf{T}} A) = \rank(A A^{\mathsf{T}}) = \rank A,$$
where $\rank$ is the [[rank of a matrix|0ZC9YTXZRY]].

## Remarks

### A first check

Take the $3 \times 2$ matrix with rows $(1, 0)$, $(1, 1)$ and $(0, 1)$.
Its columns $(1, 1, 0)$ and $(0, 1, 1)$ are independent, so $\rank A = 2$.
Entry $(i, j)$ of $A^{\mathsf{T}} A$ is the dot product of columns $i$ and $j$ of $A$:
$$A^{\mathsf{T}} A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}, \qquad \det(A^{\mathsf{T}} A) = 4 - 1 = 3 \ne 0.$$
So $\rank(A^{\mathsf{T}} A) = 2$.
The other product is $3 \times 3$, with the dot products of the rows as entries:
$$A A^{\mathsf{T}} = \begin{pmatrix} 1 & 1 & 0 \\ 1 & 2 & 1 \\ 0 & 1 & 1 \end{pmatrix}.$$
Its determinant is $1(2 - 1) - 1(1 - 0) + 0 = 0$, and its first two rows are independent, so its rank is also $2$.

### Why the real numbers are needed

The [[proof|B4TGR752QE]] uses one fact: a real vector $y$ with $y^{\mathsf{T}} y = 0$ is zero.
Over $\mathbb{C}$ this fails.
The column $A = \begin{pmatrix} 1 \\ i \end{pmatrix}$ has rank $1$, but $A^{\mathsf{T}} A = 1 + i^2 = 0$, as the [[counterexample|AX5JTDETRA]] works out.
Over $\mathbb{F}_2$ it fails too: $A = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$ has rank $1$, and $A^{\mathsf{T}} A = 1 + 1 = 0$.
The fact holds over every ordered field, such as $\mathbb{Q}$, so the theorem holds there as well.

### What it gives you

The $n \times n$ matrix $A^{\mathsf{T}} A$ is invertible exactly when the columns of $A$ are independent, that is, when $\rank A = n$.
So the normal equations $A^{\mathsf{T}} A x = A^{\mathsf{T}} b$ of least squares have exactly one solution when the columns of $A$ are independent.
The column space of $A^{\mathsf{T}} A$ lies in the column space of $A^{\mathsf{T}}$, and the two have the same dimension, so
$$\operatorname{Col}(A^{\mathsf{T}} A) = \operatorname{Col}(A^{\mathsf{T}}) = \operatorname{Row}(A).$$
In particular, $A^{\mathsf{T}} b$ always lies in the column space of $A^{\mathsf{T}} A$, so the normal equations always have a solution, even when $A$ has dependent columns.

### What it does not say

The two products have the same rank, but they are different matrices, usually of different sizes.
In the first check, $A^{\mathsf{T}} A$ is $2 \times 2$ and invertible, while $A A^{\mathsf{T}}$ is $3 \times 3$ and singular.
Their null spaces have dimensions $n - r = 0$ and $m - r = 1$.

### Generalizations

Over $\mathbb{C}$, the correct form uses the conjugate transpose $A^*$: $\rank(A^* A) = \rank(A A^*) = \rank A$.
For a linear map $T$ between finite-dimensional inner product spaces, $\rank(T^* T) = \rank T$, with the adjoint $T^*$.

## History

The matrix $A^{\mathsf{T}} A$ is the Gram matrix of the columns of $A$, named after Jørgen Pedersen Gram.

## Explanations

### L1 human

Entry $(i, j)$ of $A^{\mathsf{T}} A$ is the dot product of column $i$ with column $j$ of $A$.
So $A^{\mathsf{T}} A$ is a table of the lengths and angles of the columns.
That table knows which columns are independent, so for real numbers it has the same rank as $A$.

### L2 human

Here is a typical use: the least squares solution of $Ax = b$ for the matrix of the first check and $b = (1, 2, 3)$.
The system itself has no solution, so we solve $A^{\mathsf{T}} A x = A^{\mathsf{T}} b$ instead, with $A^{\mathsf{T}} b = (1 + 2, 2 + 3) = (3, 5)$:
$$\begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix} x = \begin{pmatrix} 3 \\ 5 \end{pmatrix}, \qquad x = \frac{1}{3} \begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix} \begin{pmatrix} 3 \\ 5 \end{pmatrix} = \begin{pmatrix} 1/3 \\ 7/3 \end{pmatrix}.$$
The theorem guarantees that $A^{\mathsf{T}} A$ is invertible, since $\rank A = 2$.
Check: $Ax = (1/3, 8/3, 7/3)$, the residual is $b - Ax = (2/3, -2/3, 2/3)$, and $A^{\mathsf{T}}(b - Ax) = (2/3 - 2/3, -2/3 + 2/3) = (0, 0)$.
Watch out: over $\mathbb{C}$ you must use $A^*$, or the matrix of the normal equations can be singular.

### L3 human

The identity behind the theorem is $x^{\mathsf{T}} A^{\mathsf{T}} A x = \lVert Ax \rVert^2$, which makes $A^{\mathsf{T}} A$ positive semidefinite with the same null space as $A$.
The statement fails over fields with isotropic vectors, that is, nonzero $y$ with $y^{\mathsf{T}} y = 0$, and such vectors exist over $\mathbb{C}$ and, in a suitable dimension, over every finite field.
The singular value decomposition gives the finer statement that the nonzero eigenvalues of $A^{\mathsf{T}} A$ are the squares of the nonzero singular values of $A$, counted with multiplicity.
