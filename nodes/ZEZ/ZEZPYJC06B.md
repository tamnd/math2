---
tag: ZEZPYJC06B
kind: definition
name: Irreducible matrix
msc: [15B48, 05C50]
defines: 7Q60BB01YG
uses: [0JXZKX526R, 08SP3DF8NB, 0KFYGSHHF5]
sources:
  - url: https://en.wikipedia.org/wiki/Perron%E2%80%93Frobenius_theorem
---

## Definition

Let $n \ge 2$, let $\mathbb{K}$ be a field, and let $A$ be an $n \times n$ [[matrix|0JXZKX526R]] over $\mathbb{K}$.
The matrix $A$ is *reducible* if some $n \times n$ [[permutation matrix|08SP3DF8NB]] $P$ gives
$$P^T A P = \begin{pmatrix} B & C \\ 0 & D \end{pmatrix},$$
where $B$ and $D$ are square matrices of size at least $1$.
The matrix $A$ is *irreducible* if it is not reducible.

## Remarks

Let $G(A)$ be the [[directed graph|0KFYGSHHF5]] with vertices $1, \ldots, n$ and an edge from $i$ to $j$ whenever $a_{ij} \ne 0$.
Then $A$ is irreducible if and only if $G(A)$ is strongly connected.
For a real nonnegative matrix $A$, this is also equivalent to $(I + A)^{n-1}$ having all entries positive.
Example: $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ is irreducible, because its graph has the edges $1 \to 2$ and $2 \to 1$.
Non-example: $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ is reducible with $P = I$, since it is already block upper triangular with $1 \times 1$ blocks.
Conventions for $1 \times 1$ matrices differ between authors.
