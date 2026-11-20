---
tag: 0PHDYNR24D
kind: concept
name: Null space
aliases: [null-space-of-a-matrix]
msc: ["15A03", "15A06"]
topics: [S6559D61BP]
audience: ug1
specializes: [00YC1D652K]
uses: [0VD9ZSWWJG, 00YC1D652K, 04KGXJG1A2, 0S23E6YE83]
sources:
  - url: https://en.wikipedia.org/wiki/Kernel_(linear_algebra)
    locator: lead section
  - book: isbn:9780321982384
    locator: Section 4.2
  - book: isbn:9781733146678
    locator: Chapter 3
---

## Summary

The null space of an $m \times n$ [[matrix|0VD9ZSWWJG]] $A$ over a field $F$ is the set of vectors $x \in F^n$ with $Ax = 0$.
It is the solution set of the [[homogeneous system|04KGXJG1A2]] with matrix $A$, and the [[kernel|0S23E6YE83]] of the map $x \mapsto Ax$.
It is a [[subspace|00YC1D652K]] of $F^n$ of dimension $n - \rank A$, with a basis read from the free variables.

## Motivation

Every solution of $Ax = b$ is one particular solution plus a vector of the null space.
So the null space measures how far a system is from having a unique solution.
Each vector of the null space is also a linear relation among the columns of $A$: $Ax = x_1 a_1 + \dots + x_n a_n = 0$.

## Notation

The null space is written $\operatorname{Null}(A)$, $\operatorname{Nul} A$, $N(A)$ or $\ker A$.
Lay writes $\operatorname{Nul} A$, and Strang writes $N(A)$.
The null space of $A^\top$ is the left null space of $A$, written $N(A^\top)$.
Its vectors $y$ satisfy $y^\top A = 0$.
In Mathlib, the null space is `LinearMap.ker (Matrix.mulVecLin A)`.

## Remarks

### Examples

- [[A $3 \times 4$ matrix|GG03BSSZ43]]: the free variables $x_2$ and $x_4$ give the basis $(-2, 1, 0, 0)$, $(-1, 0, -2, 1)$.
- [[The left null space of the same matrix|KJ7X8CZWNT]]: it is the line spanned by $(-1, -1, 1)$, which records that row 3 is the sum of rows 1 and 2.
- The null space of an invertible matrix is $\{0\}$.
- The null space of the $m \times n$ zero matrix is $F^n$.
- The null space of $\begin{pmatrix} 1 & 1 & 1 \end{pmatrix}$ is the plane $x + y + z = 0$ in $F^3$, with basis $(-1, 1, 0)$, $(-1, 0, 1)$.

### Non-examples

- [[The left null space|GS2PYPBGGJ]]: for $\begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix}$ it is the line through $(0, 1)$, not the null space, the line through $(1, -1)$.
- [[The solution set of an inhomogeneous equation|HSXSS57MS3]] does not contain $0$, so it is not a subspace and not a null space.

### Basic properties

- The free variables of the reduced form give a basis, and $\dim \operatorname{Null}(A) = n - \rank A$, by the [[theorem on the free variables|5NKND0CPKP]].
- Row equivalent matrices have the same null space, by the [[theorem on row equivalence|E4GKK727ZM]].
- $\operatorname{Null}(B) \subseteq \operatorname{Null}(AB)$, since $Bx = 0$ gives $ABx = 0$.
- $Ax = b$ has at most one solution if and only if $\operatorname{Null}(A) = \{0\}$, that is, $\rank A = n$.
- Over $\R$, $\operatorname{Null}(A)$ is the orthogonal complement of the row space of $A$, by the [[theorem on the four fundamental subspaces|73DVECPAT6]].

### History

The null space of a matrix is the classical solution set of a homogeneous linear system.
The name "kernel" is used for linear maps, and "null space" is more common in books on matrices.

### Common errors

- Placing $\operatorname{Null}(A)$ in $F^m$. Its vectors have $n$ entries, one for each column.
- Confusing the null space with the left null space $\operatorname{Null}(A^\top)$.
- Reading the basis vectors from a non-reduced echelon form without solving for the pivot variables.
- Forgetting the $1$ in the free position of each basis vector.

## Explanations

### L1 human

The null space of a matrix is the set of solutions of $Ax = 0$.
Row reduction finds a basis of it: each free variable gives one basis vector.
It is the kernel of the matrix, viewed as a linear map.

### L2 human

Write the pivot variables in terms of the free variables, then set one free variable to $1$ and the others to $0$.
The number of basis vectors is the number of free variables, $n - \rank A$.
Each vector of the null space is a relation among the columns of $A$, and it is orthogonal to every row of $A$.

### L3 human

For a linear map $T$ with matrix $A$ in bases $B$ and $C$, the coordinate map $\phi_B$ sends $\ker T$ onto $\operatorname{Null}(A)$.
The left null space $\operatorname{Null}(A^\top)$ is the annihilator of the column space, under the identification of $F^m$ with its dual by the standard basis.
So the four subspaces $\operatorname{Col}(A)$, $\operatorname{Null}(A)$, $\operatorname{Row}(A)$ and $\operatorname{Null}(A^\top)$ come in two pairs of a subspace and its annihilator.
