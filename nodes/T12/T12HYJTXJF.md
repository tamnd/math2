---
tag: T12HYJTXJF
kind: definition
name: Band matrix
msc: [15B99, 65F05]
defines: Z58FRZCF8P
uses: [0B1261B5ED, 0VD9ZSWWJG]
sources:
  - url: https://en.wikipedia.org/wiki/Band_matrix
---

## Definition

Let $R$ be a [[ring|0B1261B5ED]], let $A = (a_{ij})$ be an $m \times n$ [[matrix|0VD9ZSWWJG]] over $R$, and let $p, q \ge 0$ be integers.
The matrix $A$ is a *band matrix* with *lower bandwidth* $p$ and *upper bandwidth* $q$ when
$$a_{ij} = 0 \quad \text{whenever } i > j + p \text{ or } j > i + q.$$
The *bandwidth* of $A$ is often taken as the least $k$ such that the condition holds with $p = q = k$.

## Remarks

Example: $\begin{pmatrix} 1 & 2 & 0 & 0 \\ 3 & 4 & 5 & 0 \\ 6 & 7 & 8 & 9 \\ 0 & 1 & 2 & 3 \end{pmatrix}$ has lower bandwidth $2$ and upper bandwidth $1$: the entries with $i > j + 2$ or $j > i + 1$ are all $0$.
Non-example: $\begin{pmatrix} 1 & 0 & 1 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}$ has no upper bandwidth $q = 1$, because $a_{13} = 1$ and $3 > 1 + 1$.
With $p = q = 0$ one gets the diagonal matrices, and with $p = q = 1$ the [[tridiagonal matrices|DARX1KZRHZ]].
A square matrix with $p = 0$ is [[upper triangular|0N4XY7Z3NN]].
The term is mostly used when $p$ and $q$ are small compared with the size of the matrix.
