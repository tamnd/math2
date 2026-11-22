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

The null space of a matrix is the set of inputs that the matrix sends to zero.
It measures how far a linear system is from having a unique solution, and each of its vectors is a linear relation among the columns.
For an $m \times n$ [[matrix|0VD9ZSWWJG]] $A$ over a field $F$, the *null space* is
$$\operatorname{Null}(A) = \{x \in F^n : Ax = 0\},$$
the solution set of the [[homogeneous system|04KGXJG1A2]] with matrix $A$, and the [[kernel|0S23E6YE83]] of the map $x \mapsto Ax$.
The [[formal definition|0PQ2GGY1QV]] states it.
It is a [[subspace|00YC1D652K]] of $F^n$ of dimension $n - \operatorname{rank} A$, and the free variables of the reduced form give a basis.
The null space of $A^{\mathsf{T}}$ is called the *left null space* of $A$.

## Motivation

Suppose $x_0$ solves $Ax = b$.
Then another vector $x$ solves the same system exactly when $A(x - x_0) = 0$, that is, when $x - x_0$ lies in the null space.
So every solution is one particular solution plus a vector of the null space, and the system has at most one solution exactly when $\operatorname{Null}(A) = \{0\}$.

The null space also records the dependencies among the columns.
Since $Ax = x_1 a_1 + \dots + x_n a_n$, a vector $x$ lies in the null space exactly when $x_1 a_1 + \dots + x_n a_n = 0$.
In the same way the left null space records the dependencies among the rows.
Both are among the [[four fundamental subspaces|73DVECPAT6]], and their dimensions $n - r$ and $m - r$ complete the [[rank-nullity theorem for matrices|TR48YQGCCA]].

## Notation

Books write $\operatorname{Null}(A)$, $\operatorname{Nul} A$, $N(A)$ or $\ker A$.
Lay writes $\operatorname{Nul} A$, and Strang writes $N(A)$ and $N(A^{\mathsf{T}})$ for the left null space.
The vectors $y$ of the left null space satisfy $A^{\mathsf{T}} y = 0$, which is the same as $y^{\mathsf{T}} A = 0$, and the name "left" comes from this second form.
In Mathlib the null space is `LinearMap.ker (Matrix.mulVecLin A)`.

## Remarks

### A first computation

Take $A = \begin{pmatrix} 1 & 1 & 1 \end{pmatrix}$, one equation in three unknowns.
The equation is $x + y + z = 0$, so the pivot variable is $x = -y - z$ and the free variables are $y$ and $z$.
Setting one free variable to $1$ and the other to $0$ gives two vectors:
$$(-1, 1, 0) \text{ for } y = 1, z = 0, \qquad (-1, 0, 1) \text{ for } y = 0, z = 1.$$
These are a basis of the null space, the plane $x + y + z = 0$ in $F^3$, and $3 - 1 = 2$ is its dimension.

### The free variable method

The same method works for every matrix, and the [[free variable theorem|5NKND0CPKP]] proves it.
Row reduce $A$ to its reduced form $R$, which has the same null space, then solve for the pivot variables in terms of the free ones.
Each free variable, set to $1$ while the others are $0$, gives one basis vector.

For the [[3 by 4 matrix with rows (1, 2, 0, 1), (2, 4, 1, 4) and (3, 6, 1, 5)|GG03BSSZ43]], the free variables are $x_2$ and $x_4$, and the basis is
$$(-2, 1, 0, 0), \qquad (-1, 0, -2, 1).$$
The first vector says $a_2 = 2a_1$, and the second says $a_4 = a_1 + 2a_3$.
The [[left null space of that matrix|KJ7X8CZWNT]] is the line through $(-1, -1, 1)$, which records that row 3 is the sum of rows 1 and 2.

Two extreme cases complete the picture.
An invertible matrix has null space $\{0\}$, and the $m \times n$ zero matrix has null space $F^n$.

### What it is not

The left null space is not the null space.
For $\begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix}$, the null space is the line through $(1, -1)$, while the [[left null space is the line through (0, 1)|GS2PYPBGGJ]].
The solution set of a system with a nonzero right side is not a null space either.
It does not contain $0$, so it is not a subspace, as the [[equation x + y = 1|HSXSS57MS3]] shows.

### The rules you can use

Row equivalent matrices have the same null space, by the [[theorem on row equivalence|E4GKK727ZM]], which is why we may solve with $R$ in place of $A$.
For a product, $\operatorname{Null}(B) \subseteq \operatorname{Null}(AB)$, because $Bx = 0$ gives $ABx = A0 = 0$.
The dimension is the [[nullity|0APCFW7639]] $n - \operatorname{rank} A$, so $Ax = 0$ has a nonzero solution whenever $n > m$.
Over $\mathbb{R}$, each vector of the null space is orthogonal to each row, since entry $i$ of $Ax$ is the dot product of row $i$ with $x$.
So $\operatorname{Null}(A)$ is the orthogonal complement of the row space.

### Watch out

The vectors of $\operatorname{Null}(A)$ have $n$ entries, one for each column, so the null space lies in $F^n$, not in $F^m$.
A second trap is to forget the $1$ in the free position.
For $x + y + z = 0$, writing $(-1, 0, 0)$ for the free variable $y$ gives a vector with $-1 + 0 + 0 \ne 0$, while $(-1, 1, 0)$ works.
A third trap is to read coefficients from an echelon form that is not reduced without solving for the pivot variables first.

### Try it

First, find a basis of the null space of $\begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$.
The reduced form is $\begin{pmatrix} 1 & 2 \\ 0 & 0 \end{pmatrix}$, so $x_1 = -2x_2$, and $(-2, 1)$ is a basis.

Second, what is the dimension of the null space of a $3 \times 5$ matrix of rank $3$?
It is $5 - 3 = 2$.

## Explanations

### L1 human

A matrix turns an input list into an output list.
The null space is the collection of inputs that give an output of all zeros.
For the single equation $x + y + z = 0$, the inputs $(1, -1, 0)$ and $(2, 3, -5)$ both give zero.
You can choose two of the numbers freely, and the third is then fixed, so the null space is a flat plane.
If the null space contains only the zero input, every output comes from at most one input.

### L2 human

Here is a typical problem: describe all solutions of $Ax = b$ for $A$ with rows $(1, 2, 0, 1)$, $(2, 4, 1, 4)$, $(3, 6, 1, 5)$ and $b = (1, 4, 5)$.
One solution is $x_0 = (0, 0, 0, 1)$, because column 4 of $A$ is $(1, 4, 5)$.
The null space has the basis $s_1 = (-2, 1, 0, 0)$ and $s_2 = (-1, 0, -2, 1)$, so the general solution is
$$x = (0, 0, 0, 1) + t_1 (-2, 1, 0, 0) + t_2 (-1, 0, -2, 1).$$
Check at $t_1 = t_2 = 1$: $x = (-3, 1, -2, 2)$, and row 1 gives $-3 + 2 + 0 + 2 = 1$.
The problem shows the typical use: the null space describes the freedom in the solutions.
Watch out: the particular solution $x_0$ is not unique, but the null space that we add to it is.

### L3 human

For a linear map $T$ with matrix $A$ in bases $B$ and $C$, the coordinate isomorphism of $V$ carries $\ker T$ onto $\operatorname{Null}(A)$.
The left null space $\operatorname{Null}(A^{\mathsf{T}})$ is the annihilator of the column space, once $F^m$ is identified with its dual through the standard basis.
So the four fundamental subspaces come in two pairs of a subspace and its annihilator: $\operatorname{Row}(A)$ with $\operatorname{Null}(A)$ in $F^n$, and $\operatorname{Col}(A)$ with $\operatorname{Null}(A^{\mathsf{T}})$ in $F^m$.
The [[sub-area on duality|9K7FFF26QR]] develops this view without coordinates.
