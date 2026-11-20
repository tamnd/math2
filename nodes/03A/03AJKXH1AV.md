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

The column space of an $m \times n$ [[matrix|0VD9ZSWWJG]] $A$ over a field $F$ is the [[span|0DTY8B9HMS]] of its columns, a [[subspace|00YC1D652K]] of $F^m$.
It is the set $\{Ax : x \in F^n\}$, the [[image|0WSFKKT6FF]] of the map $x \mapsto Ax$.
Its dimension is the [[rank|0ZC9YTXZRY]] of $A$, and the pivot columns of $A$ form a basis of it.

## Motivation

The system $Ax = b$ asks whether $b$ is a combination of the columns of $A$.
So the system has a solution exactly when $b$ lies in the column space.
The column space is also the concrete form of the image of a linear map: in coordinates, $\im T$ becomes the column space of the matrix of $T$.

## Notation

The column space is written $\operatorname{Col}(A)$, $\operatorname{Col} A$, $C(A)$, $\mathcal{R}(A)$ or $\operatorname{range}(A)$.
Strang writes $C(A)$, and Lay writes $\operatorname{Col} A$.
In Mathlib, the column space is `LinearMap.range (Matrix.mulVecLin A)`.

## Remarks

### Examples

- [[A $3 \times 4$ matrix|AGHYPF25CY]]: the pivot columns $(1, 2, 3)$ and $(0, 1, 1)$ are a basis, and the column space is the plane $w = u + v$.
- [[A $3 \times 2$ matrix and consistency|WK9NW65N8Z]]: the column space is the plane $2u - v + 2w = 0$, and this equation tests whether $Ax = b$ is solvable.
- The column space of an invertible $n \times n$ matrix is all of $F^n$.
- The column space of the zero matrix is $\{0\}$.
- The column space of $\begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$ is the line spanned by $(1, 2)$.

### Non-examples

- [[The span of the pivot columns of the reduced form|K21W7FA8MQ]]: for $\begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$ it is the line spanned by $(1, 0)$, not the column space.
- The span of the rows of a non-square matrix lies in a different space. For a $2 \times 3$ matrix, the rows lie in $F^3$ and the column space lies in $F^2$.

### Basic properties

- $\operatorname{Col}(A) = \{Ax : x \in F^n\}$, and the pivot columns of $A$ form a basis, by the [[theorem on the pivot basis|11CSKXQNG3]].
- $Ax = b$ is consistent if and only if $b \in \operatorname{Col}(A)$.
- $\operatorname{Col}(AB) \subseteq \operatorname{Col}(A)$, since $ABx = A(Bx)$. This gives $\rank AB \le \rank A$ in the [[rank inequality|02FDWY55AS]].
- $\operatorname{Col}(AE) = \operatorname{Col}(A)$ for each invertible $E$. So column operations keep the column space, but row operations do not.
- $\dim \operatorname{Col}(A) = \dim \operatorname{Col}(A^\top)$, by the theorem that [[row rank equals column rank|0TZAG60ZYT]].
- Over $\R$, $\operatorname{Col}(A)$ is the orthogonal complement of the null space of $A^\top$, by the [[theorem on the four fundamental subspaces|73DVECPAT6]].

### History

The names "column space" and "row space" are standard in books on matrices, such as those of Strang and Lay.
Books on linear maps say "image" or "range" for the same subspace.

### Common errors

- Taking the pivot columns of the reduced row echelon form as a basis. The basis must come from the columns of $A$.
- Thinking that row operations keep the column space. They keep only its dimension.
- Placing $\operatorname{Col}(A)$ in $F^n$. The columns have $m$ entries, so $\operatorname{Col}(A) \subseteq F^m$.

## Explanations

### L1 human

The column space is the set of all combinations of the columns of a matrix.
These are the vectors $b$ for which $Ax = b$ has a solution.
For the matrix $\begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$, it is the line through $(1, 2)$.

### L2 human

To find a basis, row reduce $A$ and note the pivot columns.
Then take those columns from $A$, not from the reduced form.
The number of pivot columns is the rank.
To decide whether $b$ is in the column space, row reduce the augmented matrix $[A \mid b]$ and check for a pivot in the last column.

### L3 human

For a linear map $T \colon V \to W$ with matrix $A$ in bases $B$ and $C$, the coordinate map $\phi_C$ sends $\im T$ onto $\operatorname{Col}(A)$.
So the column space is the image in coordinates.
The quotient $F^m / \operatorname{Col}(A)$ is the cokernel of $A$, and its dimension $m - \rank A$ counts the independent conditions on $b$ for $Ax = b$ to be solvable.
