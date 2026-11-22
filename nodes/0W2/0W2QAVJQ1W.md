---
tag: 0W2QAVJQ1W
kind: definition
name: Cofactor
msc: ["15A15"]
topics: [DTBK11SR77]
audience: ug1
defines: 0XPKR18APA
uses: [0SD528P0EK]
sources:
  - url: https://en.wikipedia.org/wiki/Minor_(linear_algebra)
    locator: First minors
---

## Definition

A cofactor of a square matrix is a first minor multiplied by a sign that depends on its position.
Let $K$ be a commutative ring, and let $A$ be an $n \times n$ matrix over $K$ with $n \ge 2$.
The *cofactor* of $A$ in position $(i, j)$ is
$$C_{ij} = (-1)^{i+j} M_{ij},$$
where $M_{ij}$ is the first [[minor|0SD528P0EK]] of $A$ that deletes row $i$ and column $j$.
The *cofactor matrix* of $A$ is the $n \times n$ matrix $(C_{ij})$.
For $n = 1$ we set $C_{11} = 1$, the determinant of the empty matrix.

## Notation

We write $C_{ij}$ or $\operatorname{cof}_{ij}(A)$, and $\operatorname{cof} A$ for the cofactor matrix.
Some books write $A_{ij}$ for the cofactor, which clashes with the use of $A_{ij}$ for an entry or a submatrix in other books.

## Remarks

The ring is commutative so that the minors are defined.
The condition $n \ge 2$ makes sure that deleting a row and a column leaves a nonempty matrix, and the convention for $n = 1$ makes the identity $A \operatorname{adj} A = (\det A) I$ true also in that case, since then $a \cdot 1 = \det(a)$.
The sign $(-1)^{i+j}$ is $+$ when $i + j$ is even and $-$ when it is odd, so the signs form a checkerboard with $+$ in the top left corner.

A small example: for the matrix with rows $(1, 2)$ and $(3, 4)$, the cofactors are $C_{11} = 4$, $C_{12} = -3$, $C_{21} = -2$ and $C_{22} = 1$.
Check: expanding along row $1$ gives $1 \cdot 4 + 2 \cdot (-3) = -2$, which is $1 \cdot 4 - 2 \cdot 3$.
A case that fails: the plain minor $M_{12} = 3$ is not the cofactor $C_{12} = -3$, because $1 + 2$ is odd.

The cofactors give the [[Laplace expansion|0C08BQ3M05]] of the determinant, and the transpose of the cofactor matrix is the [[adjugate matrix|07W9H8QF38]].
The [[concept page|0XPKR18APA]] works out larger examples.

## Explanations

### L1 human

A cofactor is a minor with a sign.
The sign is $+$ or $-$ according to a checkerboard pattern that starts with $+$ in the top left corner.
For the matrix with rows $(a, b)$ and $(c, d)$, the cofactors are $C_{11} = d$, $C_{12} = -c$, $C_{21} = -b$ and $C_{22} = a$.

### L2 human

To compute $C_{31}$ of the matrix with rows $(1, 2, 3)$, $(4, 5, 6)$ and $(7, 8, 10)$, delete row $3$ and column $1$:
$$M_{31} = \det \begin{pmatrix} 2 & 3 \\ 5 & 6 \end{pmatrix} = 12 - 15 = -3.$$
Since $3 + 1 = 4$ is even, the sign is $+$, and $C_{31} = -3$.
Watch out: the sign depends on the position $(i, j)$, not on the value of the minor.
