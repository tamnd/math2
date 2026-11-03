---
tag: 1ZHHZPX2NE
kind: definition
name: Parity-check matrix
msc: [94B05]
defines: Y4JB44WWFG
uses: [E85KREWV60, 8TXKFC5PRD, 0VD9ZSWWJG, 0S23E6YE83, 09DXWYRD43, 0ZC9YTXZRY]
sources:
  - url: https://en.wikipedia.org/wiki/Parity-check_matrix
---

## Definition

Let $C$ be a [[linear code|E85KREWV60]] of length $n$ and dimension $k < n$ over the finite field $\F_q$.
A *parity-check matrix* of $C$ is an $(n - k) \times n$ [[matrix|0VD9ZSWWJG]] $H$ over $\F_q$ such that
$$C = \set{x \in \F_q^n : Hx^T = 0},$$
where $x^T$ is the [[transpose|09DXWYRD43]] of the row vector $x$.
In other words, $C$ is the [[kernel|0S23E6YE83]] of the linear map $x \mapsto Hx^T$, and $H$ has [[rank|0ZC9YTXZRY]] $n - k$.

## Remarks

If $G = (I_k \mid P)$ is a [[generator matrix|8TXKFC5PRD]] of $C$ in standard form, then $H = (-P^T \mid I_{n-k})$ is a parity-check matrix of $C$.
Indeed $GH^T = -P + P = 0$, so every codeword passes the checks, and the kernel of $H$ has dimension $n - (n - k) = k = \dim C$.
Example: for the binary $[3, 1, 3]$ code $\set{000, 111}$ with $G = (1 \mid 1\ 1)$, this gives
$$H = \begin{pmatrix} 1 & 1 & 0 \\ 1 & 0 & 1 \end{pmatrix},$$
whose kernel in $\F_2^3$ is $\set{000, 111}$.
Non-example: the single row $(1, 1, 0)$ is not a parity-check matrix of this code: it has only $1 = n - k - 1$ row, and its kernel also contains $001$.
The minimum distance of $C$ is the least number $d$ such that some $d$ columns of $H$ are linearly dependent.
