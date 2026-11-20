---
tag: 4KY5AWGMW5
kind: definition
name: Zero matrix
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: school
defines: 0ZTKJJDGR7
uses: [0N1MY1T0W9]
sources:
  - url: https://en.wikipedia.org/wiki/Zero_matrix
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Zero_matrix
    locator: Properties
---

## Definition

Let $R$ be a ring and let $m, n \ge 0$ be integers.
The $m \times n$ *zero matrix* over $R$ is the [[matrix|0N1MY1T0W9]] $0_{m \times n}$ with $(0_{m \times n})_{ij} = 0$ for all $i$ and $j$.
A matrix is *nonzero* when it is not the zero matrix of its size, that is, when at least one entry is not $0$.

## Notation

- Books write $0$, $O$, $0_{m \times n}$, $0_{m,n}$ or $0_n$ for the square case.
- The size is usually left out when the context fixes it, as in $A + 0 = A$.
- In Mathlib the zero matrix is `0 : Matrix m n α`, from the `Zero` instance on functions.

## Remarks

- There is one zero matrix for each size, and zero matrices of different sizes are different matrices.
- The zero matrix is the identity element for [[matrix addition|0Y7H3SAVA1]].
- For every matrix $B$ with $n$ rows, $0_{m \times n} B$ is a zero matrix, by the [[product rule|076JGP6R3T]]: each entry is a sum of terms $0 \cdot b_{kj}$.
- A product of two nonzero matrices can be zero, as the [[zero divisor example|WP764BBPKQ]] shows.

## Explanations

### L1 human

The zero matrix is the table with $0$ in every position.
It plays the role of the number $0$: adding it to a matrix of the same size changes nothing.

### L2 human

The zero matrix is the matrix of the zero linear map $x \mapsto 0$ in any pair of bases.
Unlike the number $0$, it is not the only matrix that squares to zero; see the [[nonzero matrix with square zero|DXX58EAKG3]].
