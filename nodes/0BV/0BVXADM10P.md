---
tag: 0BVXADM10P
kind: definition
name: Matrix addition
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: school
defines: 0Y7H3SAVA1
uses: [0N1MY1T0W9]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_addition
    locator: Entrywise sum
  - book: isbn:9780321982384
    locator: Section 2.1
inventory: [NAYXFHVVCR]
---

## Definition

Let $R$ be a ring, and let $A = (a_{ij})$ and $B = (b_{ij})$ be [[matrices|0N1MY1T0W9]] of the same size $m \times n$ over $R$.
The *sum* $A + B$ is the $m \times n$ matrix with entries
$$(A + B)_{ij} = a_{ij} + b_{ij}, \qquad 1 \le i \le m, \ 1 \le j \le n.$$
The *negative* $-A$ has the entries $-a_{ij}$, and the *difference* is $A - B = A + (-B)$.
The sum of two matrices of different sizes is not defined.

## Remarks

- Addition is commutative and associative, because the addition of $R$ is.
- The [[zero matrix|0ZTKJJDGR7]] $0_{m \times n}$ is the identity element, and $-A$ is the inverse of $A$.
- So $M_{m \times n}(R)$ is an abelian group under addition.
- Other entrywise sums exist, such as the direct sum $A \oplus B$ of [[block diagonal matrices|001T5FJDC1]], but they are different operations.

## Explanations

### L1 human

To add two matrices of the same size, add the entries in the same position.
For example, $\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} + \begin{pmatrix} 0 & 5 \\ -3 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 7 \\ 0 & 5 \end{pmatrix}$.

### L2 human

Addition is defined position by position, so each law of the addition of $R$ gives the same law for matrices.
