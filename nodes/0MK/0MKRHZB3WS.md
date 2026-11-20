---
tag: 0MKRHZB3WS
kind: concept
name: Change of basis matrix
aliases: [transition-matrix, change-of-basis-matrix]
msc: ["15A03", "15A04"]
topics: [S6559D61BP]
audience: ug1
specializes: [0EB9N0S33C]
uses: [0KCQ9Y3QKA, 04CYQHN6MC, 0VD9ZSWWJG]
sources:
  - url: https://en.wikipedia.org/wiki/Change_of_basis
    locator: Change-of-basis formula
  - book: isbn:9780134860244
    locator: Section 2.5
  - book: isbn:9780321982384
    locator: Section 4.7
---

## Summary

Let $B$ and $B'$ be two [[bases|0KCQ9Y3QKA]] of an $n$-dimensional vector space $V$.
The change of basis matrix from $B$ to $B'$ is the $n \times n$ [[matrix|0VD9ZSWWJG]] $P$ whose column $j$ is the [[coordinate vector|04CYQHN6MC]] of the new basis vector $b'_j$ in the old basis $B$.
It converts new coordinates into old coordinates: $[v]_B = P[v]_{B'}$.
It is invertible, and its inverse is the change of basis matrix from $B'$ to $B$.

## Motivation

A vector has different coordinates in different bases.
A good basis can make a linear map diagonal, or a quadratic form a sum of squares.
The change of basis matrix is the tool that translates between the two coordinate systems.

## Notation

The [[definition|0KWXYZPJKN]] writes $P$ for the matrix from $B$ to $B'$, with $b'_j = \sum_i p_{ij} b_i$.
It is the matrix of the identity map with the domain basis $B'$ and the codomain basis $B$: $P = [\id_V]_{B, B'}$.
Friedberg, Insel and Spence call it the change of coordinate matrix that changes $B'$-coordinates into $B$-coordinates.
Lay writes $P_{C \leftarrow B}$ for the matrix that changes $B$-coordinates into $C$-coordinates; its columns are $[b_j]_C$.
In Mathlib, `Basis.toMatrix e v` has as column $j$ the coordinates of $v_j$ in the basis $e$.

**Warning.** Books disagree on the direction.
Some call $P$ the matrix "from $B$ to $B'$", and others call it the matrix "from $B'$ to $B$", or use $P^{-1}$.
Always check which coordinates the matrix takes as input.

## Remarks

### Examples

- [[A basis of the plane|~3f7d5cf4]]: for $B'$ $= ((1, 1), (1, -1))$, $P = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$, and $(5, 1)$ has new coordinates $(3, 2)$.
- [[Taylor coordinates of polynomials|~cc3f9754]]: the basis $1, x - 1, (x - 1)^2$ of polynomials of degree at most $2$.
- For $B' = B$, the change of basis matrix is the identity $I_n$.
- For $B' = (b_2, b_1)$ in a plane, $P = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$, a permutation matrix.
- For $B' = (2b_1, b_2)$, $P = \operatorname{diag}(2, 1)$, and $[v]_{B'} = (x/2, y)$ when $[v]_B = (x, y)$.

### Non-examples

- [[A singular matrix|~8fd4d703]]: the columns $(1, 2)$ and $(2, 4)$ do not form a basis, so $\begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$ is not a change of basis matrix.
- A non-square matrix is never a change of basis matrix, since two bases of $V$ have the same number of vectors.

### Basic properties

- $[v]_B = P[v]_{B'}$ and $[v]_{B'} = P^{-1}[v]_B$, by the [[change of basis formula|0MQXVZEBMT]].
- $P$ is invertible. Conversely, every invertible $n \times n$ matrix is the change of basis matrix from $B$ to some basis $B'$.
- If $Q$ is the matrix from $B'$ to $B''$, then $PQ$ is the matrix from $B$ to $B''$.
- For $V = F^n$ and $B$ the standard basis, the columns of $P$ are the vectors of $B'$ themselves.

### History

Coordinate changes appear in the work of Cayley and Sylvester on invariants of quadratic forms in the nineteenth century.

### Common errors

- Using $P$ where $P^{-1}$ is needed. New coordinates come from old ones by $P^{-1}$, not by $P$.
- Writing the new basis vectors as rows instead of columns.
- Mixing two conventions from two books in one computation.

## Explanations

### L1 human

The change of basis matrix lists the new basis vectors, written in the old coordinates, as its columns.
It translates coordinates in the new basis into coordinates in the old basis.
Its inverse translates in the other direction.

### L2 human

To find new coordinates of a vector, solve $P y = [v]_B$ for $y = [v]_{B'}$.
When $B$ is the standard basis of $F^n$, the matrix $P$ has the new basis vectors as columns.
The matrix of a linear map changes by $P^{-1} A P$, by the change of basis formula.

### L3 human

The change of basis matrix is the matrix of $\id_V$ in the bases $B'$ and $B$.
So the set of bases of $V$ is a principal homogeneous space for the group $GL_n(F)$, acting by $B \mapsto BP$.
