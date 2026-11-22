---
tag: 06AMCJMMVM
kind: statement
role: theorem
name: Laplace expansion along a column
msc: ["15A15"]
topics: [DTBK11SR77]
audience: ug1
uses: [0C3CFHDN6R, 0W2QAVJQ1W]
sources:
  - url: https://en.wikipedia.org/wiki/Laplace_expansion
    locator: lead section
---

## Statement

A determinant can be expanded down any column, in the same way as along any row.
Let $K$ be a commutative ring, let $n \ge 2$, and let $A = (a_{ij})$ be an $n \times n$ matrix over $K$ with first minors $M_{ij}$ and [[cofactors|0XPKR18APA]] $C_{ij} = (-1)^{i+j} M_{ij}$.
Then, for each column index $j$,
$$\det A = \sum_{i=1}^{n} a_{ij} C_{ij} = \sum_{i=1}^{n} (-1)^{i+j} a_{ij} M_{ij}.$$

## Remarks

### Where it comes from

The column version is the [[expansion along a row|0C08BQ3M05]] applied to the transpose $A^{\mathsf{T}}$.
Row $j$ of $A^{\mathsf{T}}$ is column $j$ of $A$, the minors match up, and $\det A^{\mathsf{T}} = \det A$, so the two sums agree.
The [[proof by transposition|3JJPXYGSB4]] writes this out.

### A small case

Take
$$A = \begin{pmatrix} 1 & 2 & 3 \\ 0 & 4 & 5 \\ 0 & 6 & 7 \end{pmatrix}.$$
Column $1$ has the single nonzero entry $a_{11} = 1$, with sign $+$, so
$$\det A = 1 \cdot \det \begin{pmatrix} 4 & 5 \\ 6 & 7 \end{pmatrix} = 28 - 30 = -2.$$
Check: along row $1$ we get $1 (28 - 30) - 2 (0 - 0) + 3 (0 - 0) = -2$, the same value.
No row of $A$ has two zeros, so here a column is the better choice.

### What it gives you

Together with the row version, the column version means that you may pick whichever of the $2n$ lines has the most zeros.
It also shows that $\det A$ is linear in each column, with the cofactors of that column as coefficients.
Pairing the entries of column $k$ with the cofactors of a different column $j$ gives $0$, and this is the identity $\operatorname{adj}(A) A = (\det A) I_n$ of the [[adjugate identity|0528HKWZ1Z]].

## Explanations

### L1 human

The same expansion works down a column instead of across a row.
Go down the column, multiply each entry by the signed determinant of what is left when you cross out its row and column, and add.
The signs follow the same checkerboard, with plus in the top left corner.
Choose the column with the most zeros, since each zero removes one smaller determinant from the work.

### L2 human

Here is a typical use: compute
$$\det \begin{pmatrix} 2 & 7 & 1 \\ 0 & 3 & 4 \\ 0 & 0 & 5 \end{pmatrix}.$$
Column $1$ has the single entry $2$, so the determinant is $2 \det \begin{pmatrix} 3 & 4 \\ 0 & 5 \end{pmatrix} = 2 \cdot 15 = 30$.
The minor is again upper triangular, so expanding it down its first column gives $3 \cdot 5$.
This is the proof, by induction on the size, that the determinant of a [[triangular matrix|0K1KKMFHYH]] is the product of its diagonal entries.
