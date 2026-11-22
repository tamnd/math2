---
tag: 03AJKXH1AV
kind: concept
name: Column space
aliases: [range-of-a-matrix]
msc: ["15A03"]
topics: [S6559D61BP]
audience: ug1
specializes: [00YC1D652K]
uses: [0VD9ZSWWJG, 0DTY8B9HMS, 00YC1D652K, 0WSFKKT6FF]
sources:
  - url: https://en.wikipedia.org/wiki/Row_and_column_spaces
    locator: lead section
  - book: isbn:9780321982384
    locator: Section 4.2
  - book: isbn:9781733146678
    locator: Chapter 3
inventory: [6C8HH5VHGP]
---

## Summary

The column space of a matrix is the set of all vectors that the matrix can produce.
It answers the first question about a linear system $Ax = b$: for which right sides $b$ is there a solution at all?
For an $m \times n$ [[matrix|0VD9ZSWWJG]] $A$ over a field $F$ with columns $a_1, \dots, a_n$, the *column space* is the [[span|0DTY8B9HMS]] of the columns, a [[subspace|00YC1D652K]] of $F^m$:
$$\operatorname{Col}(A) = \operatorname{span}(a_1, \dots, a_n) = \{Ax : x \in F^n\}.$$
The second form says that the column space is the [[image|0WSFKKT6FF]] of the map $x \mapsto Ax$.
The [[formal definition|0F0RPPJ2TT]] states it, and its dimension is the [[rank|0ZC9YTXZRY]] of $A$.

## Motivation

A system $Ax = b$ asks for numbers $x_1, \dots, x_n$ with $x_1 a_1 + \dots + x_n a_n = b$.
So the system asks whether $b$ is a combination of the columns, and it has a solution exactly when $b$ lies in $\operatorname{Col}(A)$.
Once we know the column space, for example as a plane given by one equation, we can test any right side at once, without solving the system.

The column space is also the image of a linear map, written in coordinates.
If $T \colon V \to W$ has the matrix $A$ in some bases, then the coordinate vectors of the vectors in $\operatorname{im} T$ are exactly the vectors of $\operatorname{Col}(A)$.
So every question about the image of $T$ becomes a row reduction.
The column space is one of the [[four fundamental subspaces|73DVECPAT6]] of a matrix, and it returns in the [[Fredholm alternative|4HH8C9V8JQ]] and in least squares.

## Notation

Books write $\operatorname{Col}(A)$, $\operatorname{Col} A$, $C(A)$, $\mathcal{R}(A)$, $\operatorname{range}(A)$ or $\operatorname{im} A$.
Strang writes $C(A)$, and Lay writes $\operatorname{Col} A$.
In Mathlib the column space is `LinearMap.range (Matrix.mulVecLin A)`.
Watch the space: the columns have $m$ entries, so $\operatorname{Col}(A)$ lies in $F^m$, while the vectors $x$ lie in $F^n$.

## Remarks

### A first computation

Take $A = \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$ over $\mathbb{R}$.
The second column is twice the first, so every combination of the columns is a multiple of the first column:
$$x_1 \begin{pmatrix} 1 \\ 2 \end{pmatrix} + x_2 \begin{pmatrix} 2 \\ 4 \end{pmatrix} = (x_1 + 2x_2) \begin{pmatrix} 1 \\ 2 \end{pmatrix}.$$
So $\operatorname{Col}(A)$ is the line through $(1, 2)$, and $Ax = b$ has a solution only when $b_2 = 2b_1$.
For example, $b = (3, 6)$ works with $x = (3, 0)$, and $b = (1, 0)$ fails.

### A basis from the pivot columns

How do we find a basis in general?
Row reduce $A$, note which columns hold a pivot, and take those columns from $A$ itself.
The [[pivot basis theorem|11CSKXQNG3]] proves that they form a basis, so their number is the rank.

For the [[3 by 4 matrix with rows (1, 2, 0, 1), (2, 4, 1, 4) and (3, 6, 1, 5)|AGHYPF25CY]], the pivots fall in columns 1 and 3.
So $(1, 2, 3)$ and $(0, 1, 1)$ are a basis, and the column space is the plane $w = u + v$ in $\mathbb{R}^3$.
In the [[3 by 2 example|WK9NW65N8Z]], the two columns $(1, 2, 0)$ and $(-1, 0, 1)$ are independent, and the column space is the plane $2u - v + 2w = 0$.
That one equation decides at once that $Ax = (1, 4, 1)$ is solvable and $Ax = (1, 0, 0)$ is not.

Two extreme cases complete the picture.
An invertible $n \times n$ matrix has column space $F^n$, since $Ax = b$ has the solution $x = A^{-1} b$ for every $b$.
The zero matrix has column space $\{0\}$.

### What it is not

The span of the pivot columns of the reduced form is not the column space in general.
For $A = \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$, the reduced form has the pivot column $(1, 0)$, and the [[span of (1, 0)|K21W7FA8MQ]] is a different line from $\operatorname{Col}(A)$.
The span of the rows is not the column space either, and for a non-square matrix it does not even lie in the same space.
For a $2 \times 3$ matrix the rows lie in $F^3$, while the column space lies in $F^2$.
Even for a square matrix the two can differ, as [[the matrix with rows (1, 1) and (0, 0)|BGWTDZRS5T]] shows.

### The rules you can use

A product never has a larger column space than its left factor: $\operatorname{Col}(AB) \subseteq \operatorname{Col}(A)$, because $ABx = A(Bx)$.
This gives $\operatorname{rank}(AB) \le \operatorname{rank} A$ in the [[rank inequality|02FDWY55AS]].
When $E$ is invertible, $\operatorname{Col}(AE) = \operatorname{Col}(A)$, because every $y$ equals $E(E^{-1} y)$.
So column operations keep the column space, and row operations in general do not.
The dimension of $\operatorname{Col}(A)$ equals the dimension of the row space, by the theorem that [[row rank equals column rank|0TZAG60ZYT]].
Over $\mathbb{R}$, $\operatorname{Col}(A)$ is the orthogonal complement of the null space of $A^{\mathsf{T}}$, by the [[theorem on the complement|J4SZVFBHS5]].

### Watch out

The most common error is to take the pivot columns of the reduced row echelon form as the basis.
Row operations change the column space and keep only its dimension and the relations among the columns.
In the $2 \times 2$ example above, the reduced form is $\begin{pmatrix} 1 & 2 \\ 0 & 0 \end{pmatrix}$, and its column $(1, 0)$ is not a multiple of $(1, 2)$.
The correct move is to use the reduced form only to find the positions of the pivots, and then to take the columns at those positions from $A$.

### Try it

First, find the column space of $\begin{pmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \end{pmatrix}$.
The first two columns are $e_1$ and $e_2$, which already span $\mathbb{R}^2$, so the column space is all of $\mathbb{R}^2$.

Second, is $(2, 1, 3)$ in the column space of the $3 \times 4$ matrix above?
The column space is the plane $w = u + v$, and $3 = 2 + 1$, so yes.

## Explanations

### L1 human

A matrix takes a list of numbers $x$ and returns a new list $Ax$.
The column space is the collection of every list that can come out.
Each output is a mix of the columns: $x_1$ of the first column, plus $x_2$ of the second, and so on.
For $\begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$, every output is a multiple of $(1, 2)$, such as $(3, 6)$ or $(-1, -2)$.
So the output $(1, 0)$ can never appear, and the system with right side $(1, 0)$ has no solution.

### L2 human

Here is a typical problem: for which $b$ does $Ax = b$ have a solution, when the columns of $A$ are $(1, 2, 0)$ and $(-1, 0, 1)$?
The product is $A(x, y) = (x - y, 2x, y)$.
A vector $(u, v, w)$ is of this form when $y = w$, $x = v/2$ and $u = x - y$, so the condition is
$$2u - v + 2w = 0.$$
Check: both columns satisfy it, since $2 - 2 + 0 = 0$ and $-2 - 0 + 2 = 0$.
For $b = (1, 4, 1)$ we get $2 - 4 + 2 = 0$, and indeed $A(2, 1) = (1, 4, 1)$.
The problem shows the typical use: the column space, described by equations, is a test for consistency.
Watch out: the equations of the column space live in $F^m$, the space of right sides, not in the space of unknowns.

### L3 human

For a linear map $T \colon V \to W$ with matrix $A$ in bases $B$ and $C$, the coordinate isomorphism of $W$ carries $\operatorname{im} T$ onto $\operatorname{Col}(A)$.
So the column space is the image in coordinates, and its dimension does not depend on the bases.
The quotient $F^m / \operatorname{Col}(A)$ is the [[cokernel|H8W38933NC]] of $A$, and its dimension $m - \operatorname{rank} A$ counts the independent conditions that $b$ must satisfy.
Over $\mathbb{R}$ these conditions are given by the left null space, which is the content of the [[Fredholm alternative|4HH8C9V8JQ]].
The [[sub-area on duality|9K7FFF26QR]] gives the same fact without an inner product, as $\ker f^* = (\operatorname{im} f)^0$.
