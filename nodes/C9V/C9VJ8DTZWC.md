---
tag: C9VJ8DTZWC
kind: definition
name: M-matrix
msc: [15B48, 15A18]
defines: DNKXHMGQY1
uses: [0JXZKX526R, JPQCCFCY8X, 9V7YQA85PC, 06DW9BAWB1]
sources:
  - url: https://en.wikipedia.org/wiki/M-matrix
---

## Definition

Let $n \ge 1$ and let $A = (a_{ij})$ be a real $n \times n$ [[matrix|0JXZKX526R]].
The matrix $A$ is a *Z-matrix* if $a_{ij} \le 0$ for all $i \ne j$.
The matrix $A$ is an *M-matrix* if it can be written as $A = sI - B$, where:

1. $I$ is the $n \times n$ [[identity matrix|06DW9BAWB1]] and $s$ is a real number.
2. $B$ is a [[nonnegative matrix|JPQCCFCY8X]].
3. $s \ge \rho(B)$, where $\rho(B)$ is the [[spectral radius|9V7YQA85PC]] of $B$.

An M-matrix is *nonsingular* if moreover $s > \rho(B)$.

## Remarks

Every M-matrix is a Z-matrix.
For a Z-matrix the choice of $s$ does not matter: whenever $s \ge \max_i a_{ii}$, the number $s - \rho(sI - A)$ is the same.
Example: $A = \begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix} = 2I - B$ with $B = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$.
The eigenvalues of $B$ are $\pm 1$, so $\rho(B) = 1 < 2$, and $A$ is a nonsingular M-matrix.
Non-example: $A = \begin{pmatrix} 1 & -2 \\ -2 & 1 \end{pmatrix} = I - B$ with $B = \begin{pmatrix} 0 & 2 \\ 2 & 0 \end{pmatrix}$.
Here $\rho(B) = 2 > 1$, so clause 3 fails; indeed $A$ has the negative eigenvalue $-1$.
For a Z-matrix $A$, each of the following conditions is equivalent to $A$ being a nonsingular M-matrix.

1. $A$ is invertible and $A^{-1}$ is nonnegative.
2. Every [[eigenvalue|0BQAA2BK3Q]] of $A$ has positive real part.
3. All leading principal minors of $A$ are positive.
