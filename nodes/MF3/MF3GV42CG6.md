---
tag: MF3GV42CG6
kind: definition
name: Nonnegative matrix
msc: [15B48]
defines: JPQCCFCY8X
uses: [0VD9ZSWWJG]
sources:
  - url: https://en.wikipedia.org/wiki/Nonnegative_matrix
---

## Definition

Let $m, n \ge 1$ and let $A = (a_{ij})$ be a real $m \times n$ [[matrix|0VD9ZSWWJG]].
The matrix $A$ is *nonnegative* if $a_{ij} \ge 0$ for all $i$ and $j$.
The matrix $A$ is *positive* if $a_{ij} > 0$ for all $i$ and $j$.

## Remarks

One writes $A \ge 0$ for a nonnegative matrix and $A > 0$ for a positive matrix.
More generally, $A \ge B$ means that $A - B \ge 0$ entry by entry.
Example: $\begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix}$ is positive, hence nonnegative.
It is not [[positive semidefinite|01MMVW8CKC]], because it has the eigenvalue $-1$.
Non-example: $\begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix}$ is not nonnegative, because its entry in row $1$ and column $2$ is $-1$.
Products and sums of nonnegative matrices are nonnegative.
