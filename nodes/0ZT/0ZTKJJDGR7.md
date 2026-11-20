---
tag: 0ZTKJJDGR7
kind: object
name: Zero matrix
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: school
instance_of: [0VD9ZSWWJG]
uses: [0N1MY1T0W9]
sources:
  - url: https://en.wikipedia.org/wiki/Zero_matrix
    locator: lead section
same_as:
  wikidata: Q338028
  wikipedia: Zero matrix
---

## Description

Let $R$ be a ring and let $m, n \ge 0$ be integers.
The $m \times n$ *zero matrix* over $R$ is the [[matrix|0VD9ZSWWJG]] $0_{m \times n}$ whose entries are all $0$.
The [[formal definition|~d9ded4cd]] gives it in terms of entries.
It is the identity element for [[matrix addition|0Y7H3SAVA1]]: $A + 0 = 0 + A = A$ for each $m \times n$ matrix $A$.
For each matrix $B$ with $n$ rows, the product $0_{m \times n} B$ is a zero matrix.

## Remarks

- The $2 \times 2$ zero matrix is $\begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}$.
- The zero matrix is the matrix of the zero linear map in any pair of bases.
- The [[zero matrix of size 2 × 3|~a6b3ad05]] shows the additive rules.
- A product of two nonzero matrices can be a zero matrix, as the [[zero divisor example|~9b17504f]] shows.
- A nonzero matrix can have square zero, for example $\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}^2 = 0$; see the [[nonzero matrix with square zero|~47ca595b]].
- So $M_n(R)$ for $n \ge 2$ has [[zero divisors|0NNRDW10RZ]] and nonzero [[nilpotent elements|0ZB2JG1M9C]], even when $R$ is a field.

## Explanations

### L1 human

The zero matrix is the table with $0$ in every position.
It plays the role of the number $0$: adding it to a matrix changes nothing.
There is one zero matrix for each size.

### L2 human

For numbers, $ab = 0$ forces $a = 0$ or $b = 0$.
For matrices of order at least 2 this fails, so we cannot cancel a factor from a matrix equation $AB = AC$.
