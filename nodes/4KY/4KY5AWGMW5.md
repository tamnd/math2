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

The zero matrix of a given size is the matrix of that size with every entry equal to $0$.
Let $R$ be a ring and let $m, n \ge 0$ be integers.
The $m \times n$ *zero matrix* over $R$ is the [[matrix|0N1MY1T0W9]] $0_{m \times n}$ with
$$(0_{m \times n})_{ij} = 0 \quad \text{for all } 1 \le i \le m \text{ and } 1 \le j \le n.$$
A matrix is *nonzero* when it is not the zero matrix of its size, that is, when at least one of its entries is not $0$.

## Notation

Books write $0$, $O$, $0_{m \times n}$ or $0_{m,n}$, and $0_n$ for the square zero matrix of order $n$.
The size is usually left out when the context fixes it, as in $A + 0 = A$.
In Mathlib the zero matrix is `0 : Matrix m n α`, which comes from the zero of the function type `m → n → α`, so it is the function with value $0$ at every pair of indices.

## Remarks

The definition fixes the size first, so there is one zero matrix for each pair $(m, n)$.
Zero matrices of different sizes are different matrices, because equal matrices must have the same size.
For example, $0_{2 \times 2} \ne 0_{2 \times 3}$, although all their entries are $0$.

The word "nonzero" needs care.
A nonzero matrix may have many zero entries: $\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ is nonzero, because its entry $(1, 2)$ is $1$.
It is a different thing from a matrix with no zero entries.

Two properties follow at once from the entries.
The zero matrix is the identity element for [[matrix addition|0Y7H3SAVA1]], since $a_{ij} + 0 = a_{ij}$.
For every $n \times p$ matrix $B$, the [[product|076JGP6R3T]] $0_{m \times n} B$ is $0_{m \times p}$, since each entry is a sum of terms $0 \cdot b_{kj}$.
The converse of the second property fails: a product of two nonzero matrices can be zero, as [[two nonzero matrices with product zero|WP764BBPKQ]] shows.
The [[zero matrix|0ZTKJJDGR7]] page collects these facts.

## Explanations

### L1 human

The zero matrix is the table with $0$ in every position.
It plays the role of the number $0$: adding it to a matrix of the same size changes nothing.
A $2 \times 2$ table of zeros and a $2 \times 3$ table of zeros count as two different zero matrices.

### L2 human

The zero matrix is the matrix of the zero linear map $x \mapsto 0$ from $R^n$ to $R^m$, in any pair of bases.
Unlike the number $0$, it is not the only matrix whose square is zero.
For $N = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ the product $N^2$ has entry $(1, 2)$ equal to $0 \cdot 1 + 1 \cdot 0 = 0$, and the other entries are $0$ as well, so $N^2 = 0$ with $N \ne 0$; see the [[nonzero matrix with square zero|DXX58EAKG3]].
The trap is to solve $A^2 = 0$ by "taking square roots" and concluding $A = 0$.
