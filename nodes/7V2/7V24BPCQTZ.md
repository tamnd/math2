---
tag: 7V24BPCQTZ
kind: definition
name: Incomplete Cholesky factorization
msc: [65F08, 65F50, 65F10]
defines: QYYCFQ8E5D
uses: [0KX66CZMBB, JGACZYEEY7, GTG8MJGDKC, 0WKG8CYY6A, DNKXHMGQY1]
sources:
  - url: https://en.wikipedia.org/wiki/Incomplete_Cholesky_factorization
---

## Definition

Let $A$ be a real symmetric [[positive definite|0KX66CZMBB]] $n \times n$ [[sparse matrix|JGACZYEEY7]].
Let $S \subseteq \set{(i, j) : 1 \le j \le i \le n}$ be a set of positions that contains every diagonal position $(i, i)$.
An *incomplete Cholesky factorization* of $A$ with pattern $S$ is a [[lower triangular|GTG8MJGDKC]] matrix $L$ with positive diagonal such that:

1. $l_{ij} = 0$ for every $i \ge j$ with $(i, j) \notin S$;
2. $(L L^T)_{ij} = a_{ij}$ for every $(i, j) \in S$.

When $S$ is the set of positions $(i, j)$ with $i \ge j$ and $a_{ij} \ne 0$, the factorization is called *IC(0)*.

## Remarks

If $S$ contains all positions with $i \ge j$, the incomplete factor is the exact [[Cholesky factor|0WKG8CYY6A]].
Example: let $A$ be tridiagonal and symmetric positive definite.
Its exact Cholesky factor is lower bidiagonal, so it vanishes outside the pattern of $A$.
Hence the IC(0) factor exists and is the exact factor.
Non-example: for the $2 \times 2$ identity matrix, the matrix $L$ with rows $(1, 0)$ and $(1, 1)$ and the pattern of all positions satisfies clause 1.
It fails clause 2, since $(L L^T)_{21} = 1 \ne 0 = a_{21}$.
The factor is computed by the Cholesky recurrences with each update outside $S$ discarded.
For a general symmetric positive definite $A$, the process can meet a nonpositive pivot, and then no such $L$ is produced.
It exists for every pattern when $A$ is a symmetric [[M-matrix|DNKXHMGQY1]], a result of Meijerink and van der Vorst.
Variants choose $S$ by levels of fill or drop entries below a threshold.
