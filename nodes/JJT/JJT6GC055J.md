---
tag: JJT6GC055J
kind: statement
role: theorem
name: Eckart–Young theorem
msc: [15A18, 15A60, 65F55]
uses: [000NPTMX6J, 09VMDSRXWJ, 0ZC9YTXZRY, JT8Q204E4R, 06EKW1AKXF]
about: [000NPTMX6J, 0ZC9YTXZRY]
sources:
  - url: https://en.wikipedia.org/wiki/Low-rank_approximation
---

## Statement

Let $A$ be an $m \times n$ complex matrix with [[singular value decomposition|000NPTMX6J]] $A = \sum_{i=1}^{r} \sigma_i u_i v_i^*$.
Here $r$ is the [[rank|0ZC9YTXZRY]] of $A$, $\sigma_1 \ge \sigma_2 \ge \cdots \ge \sigma_r > 0$ are its [[singular values|09VMDSRXWJ]], and $u_1, \dots, u_r$ and $v_1, \dots, v_r$ are orthonormal families in $\C^m$ and $\C^n$.
Let $0 \le k < r$ and put $A_k = \sum_{i=1}^{k} \sigma_i u_i v_i^*$.
Then for every $m \times n$ complex matrix $B$ of rank at most $k$:

1. $\norm{A - B}_2 \ge \norm{A - A_k}_2 = \sigma_{k+1}$, where $\norm{\cdot}_2$ is the [[operator norm|06EKW1AKXF]] for the Euclidean norms.
2. $\norm{A - B}_F \ge \norm{A - A_k}_F = \left(\sigma_{k+1}^2 + \cdots + \sigma_r^2\right)^{1/2}$, where $\norm{\cdot}_F$ is the [[Frobenius norm|JT8Q204E4R]].

## Remarks

For the operator norm, the kernel of $B$ has dimension at least $n - k$, so it meets the span of $v_1, \dots, v_{k+1}$ in a unit vector $x$.
Then $\norm{(A - B)x} = \norm{Ax} \ge \sigma_{k+1}$.
The Frobenius case follows from Weyl's inequalities for singular values, $\sigma_{i+j-1}(A) \le \sigma_i(A - B) + \sigma_j(B)$, applied with $j = k+1$.
For example, if $A = \operatorname{diag}(3, 2, 1)$, the best rank one approximation is $\operatorname{diag}(3, 0, 0)$, with operator norm error $2$ and Frobenius error $\sqrt{5}$.
The minimiser $A_k$ is unique in the Frobenius norm when $\sigma_k > \sigma_{k+1}$; in the operator norm it is not unique in general.
The same result holds for real matrices with real singular value decompositions.

## Explanations

### L1 human

The theorem says how to approximate a matrix as well as possible by a simpler matrix of low rank.
Write the matrix as a sum of rank one pieces from its singular value decomposition, and keep the largest ones.
The error is controlled by the singular values that were thrown away.

### L2 human

This is the theoretical basis of principal component analysis and of truncated SVD compression.
Mirsky extended it to every unitarily invariant norm, so it is often called the Eckart–Young–Mirsky theorem.
It also shows that $\sigma_{k+1}$ is the distance from $A$ to the set of matrices of rank at most $k$.
In particular, for a square invertible $A$, the smallest singular value is the distance to the singular matrices.
