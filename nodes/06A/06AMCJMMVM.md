---
tag: 06AMCJMMVM
kind: statement
role: theorem
name: Laplace expansion along a column
msc: [15A15]
uses: [0C3CFHDN6R, 0W2QAVJQ1W]
sources:
  - url: https://en.wikipedia.org/wiki/Laplace_expansion
    locator: lead section
---

## Statement

Let $K$ be a commutative ring, let $n \ge 2$, and let $A = (a_{ij})$ be an $n \times n$ matrix over $K$.
Let $C_{ij}$ be the [[cofactors|0XPKR18APA]] of $A$.
Then, for each column $j$,
$$\det A = \sum_{i=1}^{n} a_{ij} C_{ij} = \sum_{i=1}^{n} (-1)^{i+j} a_{ij} M_{ij}.$$

## Remarks

It follows from the [[expansion along a row|0C08BQ3M05]], applied to $A^T$, because $\det A^T = \det A$.
For example, expansion along column $1$ of $\begin{pmatrix} 1 & 2 & 3 \\ 0 & 4 & 5 \\ 0 & 6 & 7 \end{pmatrix}$ gives $1 \cdot (28 - 30) = -2$.

## Explanations

### L1 human

The same expansion works down a column instead of across a row.
We choose the column with the most zeros, to save work.
Each zero entry removes one smaller determinant from the sum.
