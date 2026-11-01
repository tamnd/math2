---
tag: TRRREQX56B
kind: definition
name: Hankel matrix
msc: [15B05]
defines: PQ1D8FQB3E
uses: [0B1261B5ED, 0VD9ZSWWJG]
sources:
  - url: https://en.wikipedia.org/wiki/Hankel_matrix
---

## Definition

Let $R$ be a [[ring|0B1261B5ED]] and let $A = (a_{ij})$ be an $m \times n$ [[matrix|0VD9ZSWWJG]] over $R$.
The matrix $A$ is a *Hankel matrix* when $a_{i, j+1} = a_{i+1, j}$ for all $1 \le i < m$ and $1 \le j < n$.
Equivalently, there are elements $h_k \in R$, for $2 \le k \le m + n$, with $a_{ij} = h_{i+j}$ for all $i, j$.

## Remarks

Example: $\begin{pmatrix} 1 & 1 & 2 \\ 1 & 2 & 3 \\ 2 & 3 & 5 \end{pmatrix}$ is Hankel, with $h_2, \dots, h_6 = 1, 1, 2, 3, 5$; each anti-diagonal is constant.
Non-example: $\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ is not Hankel, because $a_{12} = 2 \ne 3 = a_{21}$.
A square Hankel matrix is symmetric, since $a_{ij} = h_{i+j} = a_{ji}$.
The [[Hilbert matrix|2DTWB6F5TA]], with $h_k = 1/(k-1)$, is a Hankel matrix.
If $J$ is the $m \times m$ matrix with ones on the anti-diagonal and zeros elsewhere, then $A$ is Hankel exactly when $JA$ is a [[Toeplitz matrix|GKY2WSHE26]].
