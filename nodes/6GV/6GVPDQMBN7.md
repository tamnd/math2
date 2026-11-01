---
tag: 6GVPDQMBN7
kind: definition
name: QR algorithm
msc: [65F15, 15A18, 15A23]
defines: B6F8YWHYZ5
uses: [0VD9ZSWWJG, 0ERWG4NXQ9, 0W02QESPJQ, 0N4XY7Z3NN, 0E89HQATM8, 0BQAA2BK3Q]
sources:
  - url: https://en.wikipedia.org/wiki/QR_algorithm
---

## Definition

Let $A$ be an $n \times n$ real [[matrix|0VD9ZSWWJG]].
The (unshifted) *QR algorithm* builds a sequence of matrices $A_0, A_1, A_2, \ldots$ as follows.

1. Set $A_0 = A$.
2. For $k \ge 0$, compute a [[QR decomposition|0ERWG4NXQ9]] $A_k = Q_k R_k$, with $Q_k$ an [[orthogonal matrix|0W02QESPJQ]] and $R_k$ [[upper triangular|0N4XY7Z3NN]].
3. Set $A_{k+1} = R_k Q_k$.

The same definition applies to complex matrices with unitary $Q_k$.

## Remarks

Since $R_k = Q_k^T A_k$, one has $A_{k+1} = Q_k^T A_k Q_k$, so every $A_k$ is [[similar|0E89HQATM8]] to $A$ and has the same [[eigenvalues|0BQAA2BK3Q]].
Suppose the eigenvalues of $A$ have pairwise distinct absolute values, and a mild condition on the eigenvectors holds.
Then the entries of $A_k$ below the diagonal tend to $0$, and the diagonal entries tend to the eigenvalues.
Example: for $A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$, $Q_0 = \tfrac{1}{\sqrt5}\begin{pmatrix} 2 & -1 \\ 1 & 2 \end{pmatrix}$ and $R_0 = \tfrac{1}{\sqrt5}\begin{pmatrix} 5 & 4 \\ 0 & 3 \end{pmatrix}$.
So $A_1 = R_0 Q_0 = \tfrac15 \begin{pmatrix} 14 & 3 \\ 3 & 6 \end{pmatrix}$; the trace stays $4$ and the off-diagonal entry drops from $1$ to $0.6$.
Non-example of convergence: for the rotation $A = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$, which is orthogonal, one may take $Q_0 = A$, $R_0 = I$, so $A_1 = A$ and the sequence is constant; its eigenvalues $\pm i$ have equal absolute value.
Practical versions first reduce $A$ to [[Hessenberg form|YCEEWJTX56]], use shifts $A_k - \sigma_k I = Q_k R_k$, $A_{k+1} = R_k Q_k + \sigma_k I$, and split off converged eigenvalues.
The algorithm was found independently by John G. F. Francis and Vera Kublanovskaya around 1960.
