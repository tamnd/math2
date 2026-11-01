---
tag: 8QQPVNR80F
kind: statement
role: theorem
name: Cauchy interlacing theorem
msc: [15A42, 15A18]
uses: [0P17NGQQMQ, 0BQAA2BK3Q, CJK2HS2508]
about: [0BQAA2BK3Q, 0P17NGQQMQ]
sources:
  - url: https://en.wikipedia.org/wiki/Min-max_theorem
---

## Statement

Let $1 \le m \le n$, and let $A$ be an $n \times n$ [[Hermitian matrix|0P17NGQQMQ]] with [[eigenvalues|0BQAA2BK3Q]] $\alpha_1 \ge \dots \ge \alpha_n$.
Let $P$ be an $n \times m$ complex matrix with $P^* P = I_m$, and let $B = P^* A P$, with eigenvalues $\beta_1 \ge \dots \ge \beta_m$.
Then, for $j = 1, \dots, m$,
$$\alpha_j \ge \beta_j \ge \alpha_{j + n - m}.$$
In particular, if $B$ is obtained from $A$ by deleting row $i$ and column $i$ for some $i$, then
$$\alpha_1 \ge \beta_1 \ge \alpha_2 \ge \beta_2 \ge \dots \ge \alpha_{n-1} \ge \beta_{n-1} \ge \alpha_n.$$

## Remarks

Both inequalities follow from the [[Courant–Fischer min-max theorem|CJK2HS2508]].
A subspace $W$ of $\C^m$ of dimension $j$ maps to the subspace $PW$ of $\C^n$ of dimension $j$, and $P$ preserves the Rayleigh quotient: $R_B(w) = R_A(Pw)$.
So the max-min for $\beta_j$ runs over fewer subspaces than the one for $\alpha_j$, which gives $\beta_j \le \alpha_j$.
The min-max form gives the other inequality.

Example: $A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$ has eigenvalues $3$ and $1$.
Deleting the second row and column leaves $(2)$, and indeed $3 \ge 2 \ge 1$.

## Explanations

### L1 human

Remove one row and the matching column from a symmetric matrix.
The eigenvalues of the smaller matrix fit between those of the larger one, one in each gap.
So a principal submatrix cannot have eigenvalues far from those of the whole matrix.

### L2 human

Interlacing is used to bound eigenvalues of graphs: the adjacency matrix of an induced subgraph is a principal submatrix.
Applied repeatedly, it compares the eigenvalues of $A$ with those of each of its principal submatrices.
The converse holds too: any two interlacing sequences arise from a Hermitian matrix and a principal submatrix of size one less.
