---
tag: 3G7WAP9DJJ
kind: definition
name: Toeplitz matrix
msc: [15B05]
defines: GKY2WSHE26
uses: [0B1261B5ED, 0VD9ZSWWJG]
sources:
  - url: https://en.wikipedia.org/wiki/Toeplitz_matrix
---

## Definition

Let $R$ be a [[ring|0B1261B5ED]] and let $A = (a_{ij})$ be an $m \times n$ [[matrix|0VD9ZSWWJG]] over $R$.
The matrix $A$ is a *Toeplitz matrix* when $a_{ij} = a_{i+1, j+1}$ for all $1 \le i < m$ and $1 \le j < n$.
Equivalently, there are elements $t_k \in R$, for $1 - n \le k \le m - 1$, with $a_{ij} = t_{i-j}$ for all $i, j$.

## Remarks

Example: $\begin{pmatrix} 1 & 2 & 3 \\ 4 & 1 & 2 \\ 5 & 4 & 1 \end{pmatrix}$ is Toeplitz, with $t_0 = 1$, $t_{-1} = 2$, $t_{-2} = 3$, $t_1 = 4$, $t_2 = 5$.
Non-example: $\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ is not Toeplitz, because $a_{11} = 1 \ne 4 = a_{22}$.
For $m = n$, the circulant matrices are the Toeplitz matrices with $t_k = t_{k-n}$ for $1 \le k \le n-1$.
If $J$ is the $m \times m$ matrix with ones on the anti-diagonal and zeros elsewhere, then $A$ is Toeplitz exactly when $JA$ is a [[Hankel matrix|PQ1D8FQB3E]].
