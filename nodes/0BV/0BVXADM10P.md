---
tag: 0BVXADM10P
kind: definition
name: Matrix addition
msc: [15A99]
defines: 0Y7H3SAVA1
uses: [0N1MY1T0W9]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_addition
    locator: lead section
---

## Definition

Let $R$ be a ring and let $A = (a_{ij})$ and $B = (b_{ij})$ be $m \times n$ [[matrices|0VD9ZSWWJG]] over $R$.
The *sum* $A + B$ is the $m \times n$ matrix with entries
$$(A + B)_{ij} = a_{ij} + b_{ij}$$
for $1 \le i \le m$ and $1 \le j \le n$.

## Remarks

The sum is defined only for two matrices of the same size.
Matrix addition is associative and commutative, the [[zero matrix|0ZTKJJDGR7]] is its identity element, and $-A = (-a_{ij})$ is the additive inverse of $A$.
Thus $M_{m \times n}(R)$ is an abelian group under addition.
For example, $\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} + \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 1 & 3 \\ 4 & 4 \end{pmatrix}$.

## Explanations

### L1 human

To add two matrices of the same size, add the numbers in the same position.
The result has the same size as the two matrices.
Matrix addition has the same rules as the addition of numbers.
