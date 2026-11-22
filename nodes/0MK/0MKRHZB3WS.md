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

One vector has different coordinates in different bases, and the change of basis matrix is the dictionary that translates one list of coordinates into the other.
It is a square matrix that you build once from the two bases and then apply to every vector.
Let $B = (b_1, \dots, b_n)$ and $B' = (b'_1, \dots, b'_n)$ be two [[bases|0KCQ9Y3QKA]] of an $n$-dimensional vector space $V$ over a field $F$.
The change of basis matrix from $B$ to $B'$ is the $n \times n$ [[matrix|0VD9ZSWWJG]] $P$ whose column $j$ is the [[coordinate vector|04CYQHN6MC]] of the new vector $b'_j$ in the old basis $B$:
$$b'_j = \sum_{i=1}^{n} p_{ij}\, b_i \qquad (1 \le j \le n).$$
It turns new coordinates into old ones, $[v]_B = P[v]_{B'}$ for every $v \in V$.
It is [[invertible|0EB9N0S33C]], and its inverse is the change of basis matrix from $B'$ to $B$.
The [[formal definition|0KWXYZPJKN]] states this with all the conditions.

## Motivation

A good basis can make a problem easy.
A linear map can become diagonal, a quadratic form can become a sum of squares, and a polynomial can be written around a chosen point.
To use a good basis you must move between it and the basis in which the problem was given, and you must do this for vectors, for maps and for forms.
The change of basis matrix does the move for vectors, and the [[change of basis formula|0MQXVZEBMT]] uses it to move matrices of linear maps.
Later the same matrix decides when two matrices are [[similar|0E89HQATM8]], that is, when they describe one map in two bases.

## Notation

We write $P$, or $P_{B \to B'}$ when the two bases must be named.
The matrix is also the matrix of the identity map, with $B'$ in the domain and $B$ in the target: $P = [\mathrm{id}_V]_{B, B'}$.
Friedberg, Insel and Spence call it the change of coordinate matrix that changes $B'$-coordinates into $B$-coordinates.
Lay writes $P_{C \leftarrow B}$ for the matrix with columns $[b_j]_C$, which changes $B$-coordinates into $C$-coordinates, so the arrow points the way the coordinates move.
In Mathlib, `Basis.toMatrix e v` has as column $j$ the coordinates of $v_j$ in the basis $e$, so it is our $P$ for $B = e$ and $B' = v$.

## Remarks

### A first computation

Take $V = \mathbb{R}^2$ with the standard basis $B = (e_1, e_2)$ and the new basis $b'_1 = (1, 1)$, $b'_2 = (1, -1)$.
In the standard basis a vector is its own coordinate vector, so the columns of $P$ are the new vectors themselves:
$$P = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}.$$
Which coordinates does $v = (5, 1)$ have in $B'$?
We need $[v]_{B'} = P^{-1}[v]_B$, and $P^{-1} = \tfrac12 P$ here, so
$$[v]_{B'} = \tfrac12 \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} \begin{pmatrix} 5 \\ 1 \end{pmatrix} = \begin{pmatrix} 3 \\ 2 \end{pmatrix}.$$
Check: $3(1, 1) + 2(1, -1) = (5, 1)$.
The [[example of the plane|MRQWBXDZCG]] does every step of this computation.

### More examples

When $B' = B$, nothing changes and $P = I_n$.
When $B' = (b_2, b_1)$ swaps the two vectors of a basis of a plane, the new vectors have old coordinates $(0, 1)$ and $(1, 0)$, so $P = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$, a permutation matrix.
When $B' = (2b_1, b_2)$, we get $P = \operatorname{diag}(2, 1)$, and a vector with old coordinates $(x, y)$ has new coordinates $(x/2, y)$.
The longer vector needs a smaller coefficient, which is the first hint that coordinates move by $P^{-1}$.

For polynomials of degree at most $2$, the bases $(1, x, x^2)$ and $(1, x - 1, (x - 1)^2)$ give an upper triangular $P$.
The new coordinates of a polynomial are then its [[Taylor coefficients at 1|F4TC36FYWW]].

### What it is not

The matrix $\begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$ is [[not a change of basis matrix|EX8DT1BY8G]], because its columns $(1, 2)$ and $(2, 4)$ are dependent and so are not a basis.
A matrix that is not square is never a change of basis matrix either, since two bases of one space have the same number of vectors.
Both cases fail the same condition: the columns of $P$ must form a basis, which for a square matrix means that $P$ is invertible.

### The rules you can use

Each rule comes from $[v]_B = P[v]_{B'}$.
The matrix $P$ is invertible, and $[v]_{B'} = P^{-1}[v]_B$, because the matrix of the reverse change undoes $P$.
Conversely, every invertible $n \times n$ matrix is the change of basis matrix from $B$ to some basis, namely to the basis whose $j$-th vector has $B$-coordinates equal to column $j$.
Changes compose: if $Q$ is the matrix from $B'$ to $B''$, then $[v]_B = P[v]_{B'} = PQ[v]_{B''}$, so $PQ$ is the matrix from $B$ to $B''$.
If both bases of $F^n$ are given as the columns of matrices $S$ and $S'$, then $S[v]_B = S'[v]_{B'}$, so $P = S^{-1}S'$.

### Watch out

Books disagree on the direction of the change of basis matrix.
Some call our $P$ the matrix from $B$ to $B'$, others call it the matrix from $B'$ to $B$, and some use the name for $P^{-1}$.
The safe test is to ask which coordinates the matrix takes as input.
The most common error is to apply $P$ to old coordinates: in the first computation, $P(5, 1) = (6, 4)$, and $6(1, 1) + 4(1, -1) = (10, 2)$ is not $v$.
The correct move is $P^{-1}(5, 1) = (3, 2)$.

### History

The idea is older than matrices.
In the invariant theory of the nineteenth century, Cayley and Sylvester studied how the coefficients of a form change under a linear substitution of the variables, and such a substitution is a change of basis.

### Try it

First, let $B'$ consist of $(2, 1)$ and $(1, 1)$ in $\mathbb{R}^2$, and find the coordinates of $(3, 2)$ in $B'$.
Here $P = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}$ has $\det P = 1$ and $P^{-1} = \begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix}$, so the coordinates are $(3 - 2, -3 + 4) = (1, 1)$, and indeed $(2, 1) + (1, 1) = (3, 2)$.

Second, for $B' = (2b_1, b_2)$, what is the change of basis matrix from $B'$ back to $B$?
It is the inverse $\operatorname{diag}(\tfrac12, 1)$, since $b_1 = \tfrac12 (2b_1)$ and $b_2 = b_2$.

## Explanations

### L1 human

Think of two grids drawn on the same page, one square and one tilted.
A point has one pair of grid readings in the square grid and another pair in the tilted grid.
The change of basis matrix is the conversion table between the two readings.
Its columns say where the steps of the tilted grid go, measured in the square grid.
For the new directions $(1, 1)$ and $(1, -1)$, the point $(5, 1)$ is reached by $3$ steps along the first and $2$ steps along the second.

### L2 human

Here is a typical task: find the coordinates of $v = (4, 9)$ in the basis $b'_1 = (1, 2)$, $b'_2 = (1, 3)$ of $\mathbb{R}^2$.
The change of basis matrix from the standard basis has the new vectors as columns:
$$P = \begin{pmatrix} 1 & 1 \\ 2 & 3 \end{pmatrix}, \qquad \det P = 3 - 2 = 1, \qquad P^{-1} = \begin{pmatrix} 3 & -1 \\ -2 & 1 \end{pmatrix}.$$
The new coordinates are the old ones multiplied by $P^{-1}$:
$$[v]_{B'} = \begin{pmatrix} 3 & -1 \\ -2 & 1 \end{pmatrix} \begin{pmatrix} 4 \\ 9 \end{pmatrix} = \begin{pmatrix} 12 - 9 \\ -8 + 9 \end{pmatrix} = \begin{pmatrix} 3 \\ 1 \end{pmatrix}.$$
Check: $3(1, 2) + 1(1, 3) = (4, 9)$.
In practice you often skip the inverse and solve $Py = [v]_B$ by row reduction, which gives the same $y$.
So $P$ itself is easy to write down, and the work of a change of basis lies in inverting it.

### L3 human

The change of basis matrix is the matrix of $\mathrm{id}_V$ in the bases $B'$ and $B$, so the rules above are cases of the theorem on the [[matrix of a composition|05Q1B7MH0M]].
If we write a basis as a row $B = (b_1, \dots, b_n)$, the definition reads $B' = BP$, and the group $GL_n(F)$ acts on the set of bases from the right.
This action is free and transitive, so after one basis is fixed, the bases of $V$ correspond to the invertible matrices.
In differential geometry the same picture gives the frame bundle, and coordinates that change by the inverse matrix are called contravariant.
The [[dual basis|0ZD2CF6ZS0]] changes by the inverse transpose, as the sub-area on duality shows.
