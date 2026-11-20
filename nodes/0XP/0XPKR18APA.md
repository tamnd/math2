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

The *cofactor* in position $(i, j)$ of a square matrix $A$ is $C_{ij} = (-1)^{i+j} M_{ij}$, where $M_{ij}$ is the first [[minor|0BT9BYWVRY]] that deletes row $i$ and column $j$.
The signs $(-1)^{i+j}$ form a checkerboard with $+$ in the top left corner.
Cofactors matter because $\det A = \sum_j a_{ij} C_{ij}$ for each row $i$, and because their matrix, transposed, is the adjugate, which gives the inverse.

## Motivation

In the Leibniz sum, collect the terms that contain the entry $a_{ij}$.
Their sum is $a_{ij}$ times a polynomial in the other entries, and this polynomial is $C_{ij}$.
So $C_{ij}$ is the partial derivative $\partial \det A / \partial a_{ij}$, and the sign $(-1)^{i+j}$ comes from moving row $i$ and column $j$ to the front.

## Notation

We write $C_{ij}$, $A_{ij}$ or $\operatorname{cof}_{ij}(A)$.
The *cofactor matrix* is $C = (C_{ij})$; its transpose is the [[adjugate|07W9H8QF38]] $\operatorname{adj} A$.
The checkerboard of signs for $n = 4$ is
$$\begin{pmatrix} + & - & + & - \\ - & + & - & + \\ + & - & + & - \\ - & + & - & + \end{pmatrix}.$$

## Remarks

### Examples

- For $\begin{pmatrix} a & b \\ c & d \end{pmatrix}$, the cofactors are $C_{11} = d$, $C_{12} = -c$, $C_{21} = -b$ and $C_{22} = a$.
- The cofactor matrix of a $3 \times 3$ matrix, and an expansion along row $2$; see the [[worked example|~9bb9fd5d]].
- The cofactors of a $4 \times 4$ triangular matrix, and the expansion along every row; see the [[second example|~301f6810]].

### Non-examples

- The first minor $M_{ij}$ without its sign is not the cofactor when $i + j$ is odd; the expansion with unsigned minors gives a wrong value. See the [[non-example|~265ba4d6]].

### Basic properties

- [[Laplace expansion|0C08BQ3M05]]: $\det A = \sum_{j} a_{ij} C_{ij}$ for each row $i$, and $\det A = \sum_{i} a_{ij} C_{ij}$ for each column $j$.
- Expansion with the cofactors of another row gives $0$: $\sum_j a_{kj} C_{ij} = 0$ for $k \neq i$. This is the [[adjugate identity|0528HKWZ1Z]].
- $C_{ij}$ does not depend on row $i$ or on column $j$ of $A$.
- $C_{ij} = \partial \det A / \partial a_{ij}$, which gives [[Jacobi's formula|357FEAZ0Q4]].

### History

Laplace gave the general expansion of a determinant in terms of its complementary minors in 1772.
Vandermonde had already given a special case.

### Common errors

- Forgetting the sign $(-1)^{i+j}$.
- Using the cofactor matrix instead of its transpose for the inverse; see the [[adjugate non-example|~53fcebc0]].

## Explanations

### L1 human

A cofactor is a minor with a sign.
The sign follows a checkerboard: plus in the top left corner, then alternating along each row and each column.
With the cofactors of one row, the determinant is the sum of each entry times its cofactor.

### L2 human

To find $C_{ij}$, delete row $i$ and column $j$, take the determinant of what is left, and multiply by $(-1)^{i+j}$.
The typical uses are the expansion of a determinant along a row with many zeros, and the formula for the inverse.
A trap: the cofactor of $a_{ij}$ uses the other entries only, so changing $a_{ij}$ itself does not change $C_{ij}$.

### L3 human

The cofactors are the coordinates of $\det$ as a linear function of one row: $\det(\dots, x, \dots) = \sum_j x_j C_{ij}$ with $x$ in row $i$.
In exterior algebra terms, the first minors are the entries of the matrix of $\Lambda^{n-1} A$, and the signs come from the identification of $\Lambda^{n-1} K^n$ with the dual of $K^n$.
