---
tag: 0ZC9YTXZRY
kind: concept
name: Rank of a matrix
aliases: [rank-of-a-matrix]
msc: ["15A03"]
topics: [S6559D61BP]
audience: ug1
uses: [0VD9ZSWWJG, 03AJKXH1AV, 03GSZ8RTZJ]
sources:
  - url: https://en.wikipedia.org/wiki/Rank_(linear_algebra)
    locator: lead section
  - book: isbn:9780134860244
    locator: Section 3.2
  - book: isbn:9780321982384
    locator: Section 4.6
same_as:
  wikidata: Q656784
  wikipedia: Rank (linear algebra)
inventory: [5AH385RGHD]
---

## Summary

The rank of an $m \times n$ [[matrix|0VD9ZSWWJG]] $A$ over a field $F$ is the [[dimension|03GSZ8RTZJ]] of its [[column space|03AJKXH1AV]].
It equals the number of pivots of a row echelon form, the dimension of the row space, and the largest order of a nonzero minor.
It is the rank of the linear map $x \mapsto Ax$ from $F^n$ to $F^m$.

## Motivation

The rank counts the independent columns of a matrix, and so the independent equations of a linear system.
It decides whether $Ax = b$ is solvable, and how many free parameters the solutions have.
It is the only invariant of a matrix under multiplication by invertible matrices on both sides.

## Notation

The rank is written $\rank A$, $\operatorname{rk} A$ or $r(A)$.
The [[definition|0EWQEYRVA8]] uses the column space.
In Mathlib, `Matrix.rank A` is the dimension of the range of `Matrix.mulVecLin A`, which is the column space.

## Remarks

### Examples

- [[A $3 \times 4$ matrix of rank 2|~b964ba7f]]: the rank is computed by pivots, by columns, by rows and by minors.
- [[The $3 \times 3$ matrix with entries 1 to 9|~94c0778f]]: it has rank $2$ over $\R$ and rank $1$ over $\mathbb{F}_3$.
- The identity matrix $I_n$ has rank $n$, and the zero matrix has rank $0$.
- For nonzero $u \in F^m$ and $v \in F^n$, the matrix $uv^\top$ has rank $1$, by the [[rank factorization theorem|~5d7700d1]].
- The diagonal matrix $\operatorname{diag}(1, 0, 3)$ has rank $2$, the number of nonzero diagonal entries.

### Non-examples

- [[Counting the nonzero rows of $A$ itself|~f5639817]] does not give the rank: $\begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$ has two nonzero rows and rank $1$.
- [[Counting columns|R7N2K2EVJP]] does not give the rank of a linear map either.

### Basic properties

- $\rank A \le \min(m, n)$.
- $\rank A^\top = \rank A$, by [[row rank equals column rank|0TZAG60ZYT]].
- $\rank A$ is the number of pivots of the reduced row echelon form, by the [[theorem on the column space|11CSKXQNG3]].
- $\rank A + \dim \operatorname{Null}(A) = n$, by the [[rank-nullity theorem for matrices|TR48YQGCCA]].
- $\rank(AB) \le \min(\rank A, \rank B)$, by the [[rank of a product|02FDWY55AS]].
- Multiplying by an invertible matrix on either side does not change the rank.
- The rank is the largest $k$ such that some $k \times k$ [[minor|0BT9BYWVRY]] of $A$ is nonzero. This determinantal rank belongs to the area on determinants.
- An $n \times n$ matrix is invertible if and only if its rank is $n$.

### History

Frobenius used the notion of rank in his work on linear equations and bilinear forms in the nineteenth century.

### Common errors

- Computing the rank of a matrix that is not reduced, by counting its nonzero rows.
- Forgetting that the rank depends on the field: the rank over $\mathbb{F}_p$ can be smaller than the rank over $\Q$.
- Assuming that $\rank(A + B) = \rank A + \rank B$. Only the inequality $\le$ holds, by [[subadditivity|~6224e0e0]].
- Assuming that $\rank(AB) = \rank(BA)$. For $A = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ and $B = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$, $AB = 0$ but $BA = A$ has rank $1$.

## Explanations

### L1 human

The rank of a matrix counts how many of its columns are really independent.
For $\begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$, the second column is twice the first, so the rank is $1$.
Row reduction finds the rank: it is the number of pivots.

### L2 human

The rank is the dimension of the image of $x \mapsto Ax$.
Row operations do not change it, so it can be read from an echelon form.
The same number counts the independent rows, which is a theorem and not a definition.
With $n$ columns, the solutions of $Ax = 0$ form a space of dimension $n - \rank A$.

### L3 human

Two $m \times n$ matrices are [[equivalent|0CMHSGTWXB]] if and only if they have the same rank.
So the rank classifies matrices up to multiplication by invertible matrices on both sides.
For a linear map $T \colon V \to W$ with matrix $A$ in any bases, $\rank T = \rank A$.
