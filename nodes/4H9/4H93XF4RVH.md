---
tag: 4H93XF4RVH
kind: definition
name: Matrix units
msc: ["15A99", "16S50"]
topics: [Y1ESNQ2V52]
audience: ug1
defines: A4HTT7JFD1
uses: [0N1MY1T0W9]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_unit
    locator: lead section
---

## Definition

A matrix unit is a matrix with a single entry $1$ and all other entries $0$.
Let $R$ be a ring with identity and let $m, n \ge 1$.
For $1 \le i \le m$ and $1 \le j \le n$, the *matrix unit* $E_{ij}$ is the $m \times n$ [[matrix|0N1MY1T0W9]] over $R$ with entries
$$(E_{ij})_{pq} = \delta_{ip} \delta_{jq} = \begin{cases} 1 & \text{if } p = i \text{ and } q = j, \\ 0 & \text{otherwise.} \end{cases}$$
Here $\delta$ is the Kronecker delta, with $\delta_{ab} = 1$ if $a = b$ and $\delta_{ab} = 0$ otherwise.

## Notation

Other notations are $e_{ij}$ and $E^{(ij)}$.
The size $m \times n$ is not part of the symbol; it comes from the context.
In Mathlib, `Matrix.stdBasisMatrix i j 1` is this matrix, and recent versions call it `Matrix.single i j 1`.

## Remarks

There are $mn$ matrix units of size $m \times n$, one for each place.
For $m = n = 2$ they are
$$E_{11} = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}, \quad E_{12} = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}, \quad E_{21} = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}, \quad E_{22} = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}.$$
The first index is the row and the second is the column, so $E_{21}$ has its $1$ in row $2$ and column $1$.

The definition needs the elements $0$ and $1$ of $R$, which is why $R$ must have an identity.
The word "unit" here means "a single $1$".
A matrix unit is not a unit of the ring $M_n(R)$ when $n \ge 2$, because it has a zero row and so is not invertible.
The concept page on [[matrix units|A4HTT7JFD1]] gives the product rule and its uses.

## Explanations

### L1 human

The matrix unit $E_{ij}$ has a $1$ in row $i$ and column $j$, and $0$ in every other place.
For example, the $2 \times 3$ matrix unit $E_{13}$ is $\begin{pmatrix} 0 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix}$.

### L2 human

The formula $\delta_{ip} \delta_{jq}$ is a product of two tests, one on the row index and one on the column index.
It equals $1$ only when both tests pass, that is, at the single place $(i, j)$.
Watch out: the identity matrix $I_2 = E_{11} + E_{22}$ has two entries $1$, so it is a sum of matrix units, not a matrix unit.
