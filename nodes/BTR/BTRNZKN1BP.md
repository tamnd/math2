---
tag: BTRNZKN1BP
kind: definition
name: Totally positive matrix
msc: [15B48]
defines: 5GN0RYRVBA
uses: [0VD9ZSWWJG, 0BT9BYWVRY]
sources:
  - url: https://en.wikipedia.org/wiki/Totally_positive_matrix
---

## Definition

Let $A$ be an $m \times n$ [[matrix|0VD9ZSWWJG]] with real entries.
The matrix $A$ is *totally positive* when every [[minor|0BT9BYWVRY]] of $A$ is positive.
That is, for all $1 \le k \le \min(m, n)$, all rows $i_1 < \cdots < i_k$ and all columns $j_1 < \cdots < j_k$, the $k \times k$ submatrix on these rows and columns has positive determinant.

## Remarks

Example: $\begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix}$ is totally positive: its $1 \times 1$ minors $1, 1, 1, 2$ are positive, and its only $2 \times 2$ minor is $2 - 1 = 1 > 0$.
Non-example: $\begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix}$ is not totally positive: all entries are positive, but the determinant is $1 - 4 = -3$.
The matrix is *totally nonnegative* when every minor is nonnegative.
Some authors use "totally positive" for this weaker condition and "strictly totally positive" for the condition above.
The [[Vandermonde matrix|Q3JWBZ7EFY]] of real numbers $0 < x_1 < \cdots < x_n$ is totally positive.
