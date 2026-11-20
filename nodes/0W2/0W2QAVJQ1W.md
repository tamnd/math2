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

Let $K$ be a commutative ring and let $A$ be an $n \times n$ matrix over $K$, with $n \ge 2$.
The *cofactor* of $A$ in position $(i, j)$ is
$$C_{ij} = (-1)^{i+j} M_{ij},$$
where $M_{ij}$ is the first [[minor|0SD528P0EK]] of $A$ that deletes row $i$ and column $j$.
The *cofactor matrix* of $A$ is the $n \times n$ matrix $(C_{ij})$.
For $n = 1$ one sets $C_{11} = 1$, the determinant of the empty matrix.

## Remarks

The signs $(-1)^{i+j}$ form a checkerboard pattern, with $+$ in the top left corner.
The cofactors give the [[Laplace expansion|0C08BQ3M05]] of the determinant.
The transpose of the cofactor matrix is the [[adjugate matrix|07W9H8QF38]].

## Explanations

### L1 human

A cofactor is a minor with a sign.
The sign is $+$ or $-$, according to a checkerboard pattern.
For the matrix $\begin{pmatrix} a & b \\ c & d \end{pmatrix}$, the cofactors are $C_{11} = d$, $C_{12} = -c$, $C_{21} = -b$ and $C_{22} = a$.
