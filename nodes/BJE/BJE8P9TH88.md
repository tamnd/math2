---
tag: BJE8P9TH88
kind: statement
role: theorem
name: Divide-and-conquer eigenvalue algorithm
msc: [65F15]
uses: [DARX1KZRHZ, 0VR671PHE5, 044JNC7ZAA, 0BQAA2BK3Q, 0N6960W0BV, 0W02QESPJQ]
about: [HCJ2ETX89Z]
sources:
  - url: https://en.wikipedia.org/wiki/Divide-and-conquer_eigenvalue_algorithm
same_as:
  wikidata: Q5283998
  wikipedia: Divide-and-conquer eigenvalue algorithm
---

## Statement

Let $T \in \R^{n \times n}$ be a symmetric [[tridiagonal matrix|DARX1KZRHZ]] with diagonal entries $a_1, \dots, a_n$ and off-diagonal entries $b_1, \dots, b_{n-1}$, and let $1 \le k < n$ with $\beta = b_k$.

1. (Splitting.) Let $T_1$ be the leading $k \times k$ block of $T$ with $a_k$ replaced by $a_k - \beta$, and $T_2$ the trailing $(n-k) \times (n-k)$ block with $a_{k+1}$ replaced by $a_{k+1} - \beta$. With $u = e_k + e_{k+1}$,
$$T = \begin{pmatrix} T_1 & 0 \\ 0 & T_2 \end{pmatrix} + \beta \, u u^T.$$
If $T_i = Q_i D_i Q_i^T$ with $Q_i$ [[orthogonal|0W02QESPJQ]] and $D_i$ [[diagonal|044JNC7ZAA]], then $T = Q (D + \beta z z^T) Q^T$ with $Q = \mathrm{diag}(Q_1, Q_2)$, $D = \mathrm{diag}(D_1, D_2)$ and $z = Q^T u$.
2. (Secular equation.) Let $D = \mathrm{diag}(d_1, \dots, d_n)$ with $d_1 < d_2 < \cdots < d_n$, let $z \in \R^n$ have all entries nonzero, and let $\beta > 0$. Then the [[eigenvalues|0BQAA2BK3Q]] of $D + \beta z z^T$ are the $n$ roots of
$$f(\lambda) = 1 + \beta \sum_{i=1}^{n} \frac{z_i^2}{d_i - \lambda},$$
they satisfy $d_1 < \lambda_1 < d_2 < \lambda_2 < \cdots < d_n < \lambda_n$, and $(D - \lambda_j I)^{-1} z$ is an [[eigenvector|0N6960W0BV]] for $\lambda_j$.

## Remarks

Part 1 is a direct check of entries: $u u^T$ has ones exactly in positions $(k, k)$, $(k, k+1)$, $(k+1, k)$, $(k+1, k+1)$.
For part 2, if $(D + \beta z z^T) x = \lambda x$ and $\lambda$ is not a $d_i$, then $x = -\beta (z^T x)(D - \lambda I)^{-1} z$ with $z^T x \ne 0$, and taking the inner product with $z$ gives $f(\lambda) = 0$.
Since $f'(\lambda) = \beta \sum_i z_i^2/(d_i - \lambda)^2 > 0$ and $f$ goes from $-\infty$ to $+\infty$ between consecutive poles, and from $-\infty$ to $1$ after $d_n$, there is exactly one root in each of these $n$ intervals.
For $\beta < 0$ the interlacing is reversed: $\lambda_1 < d_1 < \lambda_2 < \cdots < \lambda_n < d_n$.
If some $z_i = 0$ or some $d_i$ coincide, then some $d_i$ is already an eigenvalue and the problem is reduced in size first; this step is called deflation.

The algorithm applies the splitting recursively, solves the small problems directly, and merges with the secular equation.
Each root is found by a safeguarded Newton-type iteration on $f$ in its interval.
Computing the eigenvectors in a numerically orthogonal way needs a careful recomputation of $z$, due to Gu and Eisenstat.

## Explanations

### L1 human

To find the eigenvalues of a big symmetric tridiagonal matrix, cut it into two halves at one entry.
Solve the two halves, possibly by cutting them again, and then glue the answers.
Gluing changes the matrix by a simple rank-one piece.
The new eigenvalues are the roots of one scalar equation, with exactly one root between each pair of neighboring old eigenvalues.

### L2 human

Symmetric eigenvalue problems are first reduced to tridiagonal form by orthogonal transformations, so this algorithm handles the core step.
It is among the fastest methods when all eigenvalues and eigenvectors are wanted, because deflation is frequent in practice and the merges use matrix multiplication.
The interlacing in part 2 is a rank-one analogue of the [[Cauchy interlacing theorem|8QQPVNR80F]].
The method was proposed by Cuppen in 1981.
