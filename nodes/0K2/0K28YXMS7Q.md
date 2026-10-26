---
tag: 0K28YXMS7Q
kind: definition
name: Scalar multiplication of matrices
msc: [15A99]
defines: 09V6DDACXR
uses: [0N1MY1T0W9]
sources:
  - url: https://en.wikipedia.org/wiki/Scalar_multiplication
    locator: lead section
---

## Definition

Let $R$ be a ring, let $c \in R$, and let $A = (a_{ij})$ be an $m \times n$ [[matrix|0VD9ZSWWJG]] over $R$.
The *scalar multiple* $cA$ is the $m \times n$ matrix with entries
$$(cA)_{ij} = c\, a_{ij}$$
for $1 \le i \le m$ and $1 \le j \le n$.

## Remarks

Over a field $F$, matrix addition and scalar multiplication make $M_{m \times n}(F)$ a [[vector space|000AYPA9AJ]] of dimension $mn$.
The rules $c(A + B) = cA + cB$, $(c + d)A = cA + dA$, $(cd)A = c(dA)$ and $1A = A$ hold.
For example, $2 \begin{pmatrix} 1 & -1 \\ 0 & 3 \end{pmatrix} = \begin{pmatrix} 2 & -2 \\ 0 & 6 \end{pmatrix}$.

## Explanations

### L1 human

Multiplying a matrix by a number means multiplying every entry by that number.
The size of the matrix does not change.
Doubling a matrix doubles every number in the table.
