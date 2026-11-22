---
tag: 0BT9BYWVRY
kind: concept
name: Minor
aliases: [minor-of-a-matrix]
msc: ["15A15"]
topics: [DTBK11SR77]
audience: ug1
uses: [0C3CFHDN6R, 0N1MY1T0W9]
sources:
  - url: https://en.wikipedia.org/wiki/Minor_(linear_algebra)
    locator: General definition
  - url: https://en.wikipedia.org/wiki/Minor_(linear_algebra)
    locator: First minors
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: History
same_as:
  wikidata: Q1341061
  wikipedia: Minor (linear algebra)
---

## Summary

A minor is the determinant of a smaller square piece cut out of a matrix.
Minors are the pieces from which large determinants are built, and they also see the rank of a matrix of any shape.
Let $A$ be an $m \times n$ [[matrix|0N1MY1T0W9]] over a commutative ring, and let $1 \le k \le \min(m, n)$.
Choose $k$ rows $i_1 < \dots < i_k$ and $k$ columns $j_1 < \dots < j_k$, and keep the entries where they cross, in their original order.
The [[determinant|0C3CFHDN6R]] of this $k \times k$ submatrix is a *minor of order $k$* of $A$, and the [[formal definition|0SD528P0EK]] states it with indices.
For a square matrix, the *first minor* $M_{ij}$ is the minor that deletes row $i$ and column $j$.

## Motivation

How do you compute a $3 \times 3$ determinant by hand?
The standard way expands it along a row, and each entry of that row is paired with the $2 \times 2$ determinant left after its row and column are removed.
Those smaller determinants are the first minors.
With signs attached they become [[cofactors|0XPKR18APA]], and the cofactors build the [[Laplace expansion|0C08BQ3M05]], the [[adjugate|07W9H8QF38]] and the formula for the inverse.

Minors also answer a question that the determinant alone cannot: what can we say about a matrix that is not square?
A $2 \times 3$ matrix has no determinant, but each pair of its columns gives a $2 \times 2$ minor, and these minors decide whether the rows are independent.
Later the same idea gives [[Sylvester's criterion|0WKEF78PMV]] for positive definite matrices and, in commutative algebra, the [[determinantal ideals|SXD7X0WQH1]].

## Notation

For row indices $I = \{ i_1 < \dots < i_k \}$ and column indices $J = \{ j_1 < \dots < j_k \}$, books write the minor as $\det A_{I,J}$, $[A]_{I,J}$ or $A^{I}_{J}$, and some write $\det A[I, J]$.
The letter $M_{ij}$ for the first minor is common, but a few books use $M_{ij}$ for the deleted submatrix itself and not for its determinant, so read the convention first.
A *principal minor* has $I = J$, so it uses the same rows as columns.
The *leading principal minor* of order $k$ has $I = J = \{ 1, \dots, k \}$, the top left $k \times k$ corner.

## Remarks

### A first computation

Take the matrix
$$A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 10 \end{pmatrix}.$$
To find $M_{11}$, delete row $1$ and column $1$ and take the determinant of what remains:
$$M_{11} = \det \begin{pmatrix} 5 & 6 \\ 8 & 10 \end{pmatrix} = 50 - 48 = 2.$$
In the same way $M_{12} = 40 - 42 = -2$ and $M_{13} = 32 - 35 = -3$.
Expanding along the first row with the signs $+, -, +$ gives
$$\det A = 1 \cdot 2 - 2 \cdot (-2) + 3 \cdot (-3) = -3.$$
The leading principal minors are $1$, then $1 \cdot 5 - 2 \cdot 4 = -3$, then $\det A = -3$.
The [[worked example|B2YDT3YNCW]] checks all of this by row reduction.

### Minors of a rectangular matrix

The matrix with rows $(1, 2, 3)$ and $(4, 5, 6)$ has three minors of order $2$, one for each pair of columns.
They are $5 - 8 = -3$, $6 - 12 = -6$ and $12 - 15 = -3$.
One of them is nonzero, so the two rows are independent and the rank is $2$.
In general an $m \times n$ matrix has $\binom{m}{k} \binom{n}{k}$ minors of order $k$, and the [[example of a 2 by 3 matrix|8827Y0CH3H]] also checks its minors with the Cauchy-Binet formula.

### The rules you can use

The minors of order $1$ are the entries, and the only minor of order $n$ of an $n \times n$ matrix is $\det A$ itself.
Over a field, the [[rank|0ZC9YTXZRY]] of $A$ is the largest $k$ for which some minor of order $k$ is nonzero, by the theorem on [[rank by minors|HVHQ50TJB1]].
The minors of a product $AB$ are sums of products of minors of $A$ and of $B$, by the [[Cauchy-Binet formula|08WE2W7DYS]].
A real symmetric matrix is positive definite exactly when all its leading principal minors are positive, by [[Sylvester's criterion|0WKEF78PMV]].
For example, the symmetric matrix with rows $(2, 1)$ and $(1, 2)$ has leading principal minors $2$ and $3$, so it is positive definite.

### What it is not

A minor keeps the chosen rows and columns in their original order.
If you take rows $1, 2$ and columns $2, 1$ of $A$ above, you get the array with rows $(2, 1)$ and $(5, 4)$, with determinant $3$.
That is the negative of the true minor $-3$, and [[no minor of order 2 of A equals 3|Q3M8S1K799]].
A non-square piece of a matrix gives no minor at all, since it has no determinant.

### Watch out

A minor is not a cofactor.
The cofactor is $C_{ij} = (-1)^{i+j} M_{ij}$, and the two differ in sign whenever $i + j$ is odd.
If you expand the determinant of $A$ above with minors and no signs, you get $2 + 2 \cdot (-2) + 3 \cdot (-3) = -11$ instead of $-3$, as the [[expansion with unsigned minors|4HC79H7TJR]] shows.
The correct move is to write the checkerboard of signs before you expand.
A second trap is the order of indices: $M_{ij}$ deletes row $i$ and column $j$, and the adjugate places the cofactor $C_{ij}$ in position $(j, i)$.

### History

The expansion of a determinant by complementary minors, which uses minors of every order and not only first minors, is named after Laplace, and the [[general Laplace expansion|541X51GQTV]] states it.

### Try it

First, compute the first minor $M_{22}$ of the matrix $A$ above.
Delete row $2$ and column $2$ to get the rows $(1, 3)$ and $(7, 10)$, so $M_{22} = 10 - 21 = -11$.

Second, how many minors of order $2$ does a $3 \times 4$ matrix have?
There are $\binom{3}{2} = 3$ choices of rows and $\binom{4}{2} = 6$ choices of columns, so $18$ minors.

## Explanations

### L1 human

A minor is the determinant of a smaller square piece of a table of numbers.
For a $3 \times 3$ table, cover one row and one column, and look at the four numbers left.
For the rows $(1, 2, 3)$, $(4, 5, 6)$ and $(7, 8, 10)$, covering the first row and the first column leaves $5, 6, 8, 10$.
Their $2 \times 2$ determinant is $5 \cdot 10 - 6 \cdot 8 = 2$, and that is one minor.
Each of the nine entries has a minor of this kind, and the big determinant is built from them.

### L2 human

Here is a typical use: what is the rank of the matrix with rows $(1, 2, 3)$, $(2, 4, 6)$ and $(1, 0, 1)$?
The full determinant is a first test.
The second row is twice the first, so the rows are dependent and $\det = 0$, which means the rank is less than $3$.
Now look for a nonzero minor of order $2$.
Rows $1$ and $3$ with columns $1$ and $2$ give
$$\det \begin{pmatrix} 1 & 2 \\ 1 & 0 \end{pmatrix} = 0 - 2 = -2 \neq 0,$$
so the rank is exactly $2$.
One nonzero minor of order $k$ is enough to show that the rank is at least $k$.
To show that the rank is less than $k$, you need every minor of order $k$ to vanish, and there are many of them, so for large matrices row reduction is faster.

### L3 human

The minors of order $k$ of $A$ are the entries of the matrix of the $k$-th exterior power $\Lambda^k A$, in the bases of wedge products of basis vectors of the [[exterior algebra|0MDMZ965VE]].
In this language the Cauchy-Binet formula is the rule $\Lambda^k(AB) = \Lambda^k A \, \Lambda^k B$.
The ideal $I_k(A)$ generated by the minors of order $k$ does not change when $A$ is multiplied on either side by invertible matrices.
Up to a shift of index, these [[determinantal ideals|SXD7X0WQH1]] are the Fitting ideals of the module presented by $A$, an invariant studied in commutative algebra.
Principal minors return in the [[characteristic polynomial|0VSSPAFM2C]], whose coefficients are sums of principal minors up to sign.
