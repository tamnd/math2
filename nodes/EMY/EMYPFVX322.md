---
tag: EMYPFVX322
kind: definition
name: Incomplete LU factorization
msc: [65F08, 65F50, 65F10]
defines: XBPK7Y559D
uses: [JGACZYEEY7, GTG8MJGDKC, 0RKG5YW66Y, DNKXHMGQY1, QYYCFQ8E5D]
sources:
  - url: https://en.wikipedia.org/wiki/Incomplete_LU_factorization
---

## Definition

Let $A$ be a real $n \times n$ [[sparse matrix|JGACZYEEY7]].
Let $P \subseteq \set{1, \dots, n}^2$ be a set of positions that contains every diagonal position $(i, i)$.
An *incomplete LU factorization* of $A$ with pattern $P$ is a pair $(L, U)$ such that:

1. $L$ is unit [[lower triangular|GTG8MJGDKC]] and $U$ is upper triangular;
2. $l_{ij} = 0$ and $u_{ij} = 0$ for every position $(i, j) \notin P$;
3. $(L U)_{ij} = a_{ij}$ for every $(i, j) \in P$.

When $P$ is the set of positions with $a_{ij} \ne 0$ together with the diagonal, it is called *ILU(0)*.

## Remarks

If $P$ is the set of all positions and $A$ has an [[LU decomposition|0RKG5YW66Y]] with unit lower triangular $L$, the two factorizations coincide.
Example: if $A$ is tridiagonal and has an LU decomposition, its exact factors are bidiagonal.
They vanish outside the pattern of $A$, so they form the ILU(0) factorization.
Non-example: let $A$ be the $2 \times 2$ identity, let $P$ be all positions, and let $L$ have rows $(1, 0)$ and $(1, 1)$, with $U = I$.
Clauses 1 and 2 hold, but clause 3 fails, since $(L U)_{21} = 1 \ne 0 = a_{21}$.
The factors are computed by Gaussian elimination in which each update outside $P$ is discarded.
For a general matrix a zero pivot can occur, and then the factorization does not exist.
It exists for every pattern when $A$ is an [[M-matrix|DNKXHMGQY1]].
For symmetric positive definite $A$ the symmetric analogue is the [[incomplete Cholesky factorization|QYYCFQ8E5D]].
Variants use levels of fill, written ILU($k$), or thresholds, written ILUT.
