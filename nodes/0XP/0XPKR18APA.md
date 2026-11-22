---
tag: 0XPKR18APA
kind: concept
name: Cofactor
msc: ["15A15"]
topics: [DTBK11SR77]
audience: ug1
uses: [0BT9BYWVRY]
sources:
  - url: https://en.wikipedia.org/wiki/Minor_(linear_algebra)
    locator: First minors
  - url: https://en.wikipedia.org/wiki/Minor_(linear_algebra)
    locator: Cofactor expansion of the determinant
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: History
---

## Summary

A cofactor is a minor with the right sign attached, and it measures how much the determinant changes when one entry changes.
With the cofactors of one row you can write any determinant as a short sum, and with all of them you can write the inverse matrix.
Let $A$ be an $n \times n$ matrix over a commutative ring, with $n \ge 2$.
The *cofactor* in position $(i, j)$ is
$$C_{ij} = (-1)^{i+j} M_{ij},$$
where $M_{ij}$ is the first [[minor|0BT9BYWVRY]] that deletes row $i$ and column $j$, and the [[formal definition|0W2QAVJQ1W]] states it in full.
The signs $(-1)^{i+j}$ form a checkerboard with $+$ in the top left corner.

## Motivation

Why attach a sign to a minor at all?
Look at the [[Leibniz formula|016PE4VZ8Q]] and collect the terms that contain the entry $a_{ij}$.
Their sum is $a_{ij}$ times a polynomial in the entries outside row $i$ and column $j$, and that polynomial is the minor $M_{ij}$ up to the sign $(-1)^{i+j}$.
The sign records the swaps needed to move row $i$ and column $j$ to the front.
So $\det A = \sum_j a_{ij} C_{ij}$ for each row $i$, which is the [[Laplace expansion|0C08BQ3M05]].

This short sum is the practical way to compute a determinant with many zeros in one row or column.
The cofactors also assemble into a matrix whose transpose, the [[adjugate|07W9H8QF38]], satisfies $A \operatorname{adj} A = (\det A) I$, and that identity gives the inverse and [[Cramer's rule|0977KZ6PQB]].

## Notation

Books write $C_{ij}$, $A_{ij}$, $\Delta_{ij}$ or $\operatorname{cof}_{ij}(A)$.
Watch out for $A_{ij}$: some books use it for the entry, others for the cofactor, and others for the submatrix that deletes row $i$ and column $j$.
The *cofactor matrix* is $\operatorname{cof} A = (C_{ij})$, and its transpose is $\operatorname{adj} A$.
For $n = 4$ the checkerboard of signs is
$$\begin{pmatrix} + & - & + & - \\ - & + & - & + \\ + & - & + & - \\ - & + & - & + \end{pmatrix}.$$

## Remarks

### The smallest case

For a $2 \times 2$ matrix, deleting a row and a column leaves a single entry.
So for the matrix with rows $(a, b)$ and $(c, d)$ the cofactors are
$$C_{11} = d, \qquad C_{12} = -c, \qquad C_{21} = -b, \qquad C_{22} = a.$$
Expanding along row $1$ gives $a \cdot d + b \cdot (-c) = ad - bc$, the familiar [[2 by 2 determinant|0ZN2J42SK7]].
The adjugate swaps $a$ and $d$ and negates $b$ and $c$, which is the usual formula for the inverse of a $2 \times 2$ matrix.

### A full cofactor matrix

Take the matrix with rows $(1, 2, 3)$, $(4, 5, 6)$ and $(7, 8, 10)$, whose determinant is $-3$.
Its nine cofactors, computed in the [[worked example|CS8M5BY36A]], form
$$\operatorname{cof} A = \begin{pmatrix} 2 & 2 & -3 \\ 4 & -11 & 6 \\ -3 & 6 & -3 \end{pmatrix}.$$
Pair row $2$ of $A$ with row $2$ of this matrix:
$$4 \cdot 4 + 5 \cdot (-11) + 6 \cdot 6 = 16 - 55 + 36 = -3.$$
Pair row $1$ of $A$ with row $2$ of the cofactors instead:
$$1 \cdot 4 + 2 \cdot (-11) + 3 \cdot 6 = 0.$$
The first sum is the determinant, and the second is $0$; together they are the [[adjugate identity|0528HKWZ1Z]].

### Triangular matrices

For an upper triangular $4 \times 4$ matrix, every cofactor above the diagonal is $0$, so the cofactor matrix is lower triangular.
The [[triangular example|206N17YCRR]] computes all sixteen cofactors and expands along three different lines, each time getting the product of the diagonal.

### The rules you can use

The cofactors of row $i$ give $\det A = \sum_j a_{ij} C_{ij}$, and the cofactors of column $j$ give $\det A = \sum_i a_{ij} C_{ij}$.
With the cofactors of a different row, $\sum_j a_{kj} C_{ij} = 0$ for $k \neq i$, because that sum is the determinant of a matrix with two equal rows.
The cofactor $C_{ij}$ does not involve row $i$ or column $j$ of $A$, so changing $a_{ij}$ leaves $C_{ij}$ unchanged.
As a function of the entries, $C_{ij} = \partial \det A / \partial a_{ij}$, and this leads to [[Jacobi's formula|357FEAZ0Q4]] for the derivative of a determinant.

### Watch out

Two errors are common.
The first is to forget the sign: expanding the $3 \times 3$ matrix above with plain minors gives $-11$ instead of $-3$, as the [[unsigned expansion|4HC79H7TJR]] shows.
The second is to use the cofactor matrix where the adjugate is needed.
For the same matrix, $A \operatorname{cof} A$ has the entry $-2$ in position $(1, 2)$, so it is not a multiple of $I$, and the [[missing transpose|2BJC4DHCMK]] example works this out.
The correct move is to transpose: $\operatorname{adj} A = (\operatorname{cof} A)^{\mathsf{T}}$.

### History

Expansion by cofactors along one row is the simplest case of the expansion by complementary minors that is named after Laplace.

### Try it

First, find $C_{23}$ for the matrix with rows $(1, 0, 2)$, $(3, 1, 4)$ and $(0, 5, 6)$.
Delete row $2$ and column $3$ to get the rows $(1, 0)$ and $(0, 5)$, so $M_{23} = 5$ and $C_{23} = (-1)^{5} \cdot 5 = -5$.

Second, what is the sign in position $(3, 4)$ of the checkerboard?
It is $(-1)^{3 + 4} = -1$, a minus sign.

## Explanations

### L1 human

A cofactor is a minor with a sign.
The sign follows a checkerboard: plus in the top left corner, and then it alternates along each row and down each column.
To get the determinant, take one row, multiply each entry by its cofactor, and add.
For the table with rows $(3, 1)$ and $(2, 4)$, the cofactors of the first row are $4$ and $-2$, so the determinant is $3 \cdot 4 + 1 \cdot (-2) = 10$.

### L2 human

Here is a typical use: compute the determinant of
$$A = \begin{pmatrix} 2 & 0 & 1 \\ 3 & 0 & 5 \\ 1 & 4 & 2 \end{pmatrix}.$$
Column $2$ has only one nonzero entry, $a_{32} = 4$, so we expand along it.
The cofactor is
$$C_{32} = (-1)^{3+2} \det \begin{pmatrix} 2 & 1 \\ 3 & 5 \end{pmatrix} = -(10 - 3) = -7.$$
So $\det A = 4 \cdot (-7) = -28$.
Check by Sarrus: $(0 + 0 + 12) - (0 + 40 + 0) = -28$.
The lesson is to choose the row or column with the most zeros, and to take the sign from the checkerboard before you multiply.

### L3 human

The cofactors are the coefficients of $\det$ as a linear function of one row: if row $i$ is replaced by a vector $x$, the determinant becomes $\sum_j x_j C_{ij}$.
So the cofactors of row $i$ are the coordinates of a linear form that vanishes on the other $n - 1$ rows, and in $\mathbb{R}^3$ this form is the dot product with the cross product of those two rows.
In the language of exterior algebra, the minors of order $n - 1$ are the entries of $\Lambda^{n-1} A$, and the checkerboard signs come from identifying $\Lambda^{n-1} K^n$ with the dual of $K^n$.
Cofactors return in the theory of the [[adjugate|07W9H8QF38]], in the gradient of the determinant, and in the cofactor matrix that appears in the formula for the normal of a deformed surface in mechanics.
