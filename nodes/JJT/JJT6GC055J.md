---
tag: JJT6GC055J
kind: statement
role: theorem
name: Eckart-Young-Mirsky theorem
msc: [15A18, 15A60, 65F55]
topics: [SS4EVPKT3A]
audience: ug2
uses: [000NPTMX6J, 09VMDSRXWJ, 0ZC9YTXZRY, JT8Q204E4R, 06EKW1AKXF]
about: [000NPTMX6J, 0ZC9YTXZRY]
proofs: [~ad4b833d]
sources:
  - url: https://en.wikipedia.org/wiki/Low-rank_approximation
    locator: Basic low-rank approximation problem
  - url: https://en.wikipedia.org/wiki/Low-rank_approximation
    locator: Proof of Eckart–Young–Mirsky theorem (for spectral norm)
  - url: https://en.wikipedia.org/wiki/Low-rank_approximation
    locator: Proof of Eckart–Young–Mirsky theorem (for Frobenius norm)
  - url: https://en.wikipedia.org/wiki/Singular_value_decomposition
    locator: Low-rank matrix approximation
  - book: isbn:9781733146678
    locator: Chapter 7
---

## Statement

Let $A$ be an $m \times n$ complex matrix with [[singular value decomposition|000NPTMX6J]] $A = \sum_{i=1}^{r} \sigma_i u_i v_i^*$.
Here $r$ is the [[rank|0ZC9YTXZRY]] of $A$, $\sigma_1 \ge \sigma_2 \ge \cdots \ge \sigma_r > 0$ are its [[singular values|09VMDSRXWJ]], and $u_1, \dots, u_r$ and $v_1, \dots, v_r$ are orthonormal families in $\C^m$ and $\C^n$.
Let $0 \le k < r$ and put $A_k = \sum_{i=1}^{k} \sigma_i u_i v_i^*$, the truncated SVD.
Then $\operatorname{rank} A_k = k$, and for every $m \times n$ complex matrix $B$ of rank at most $k$:

1. $\norm{A - B}_2 \ge \norm{A - A_k}_2 = \sigma_{k+1}$, where $\norm{\cdot}_2$ is the [[operator norm|06EKW1AKXF]] for the Euclidean norms.
2. $\norm{A - B}_F \ge \norm{A - A_k}_F = \left(\sigma_{k+1}^2 + \cdots + \sigma_r^2\right)^{1/2}$, where $\norm{\cdot}_F$ is the [[Frobenius norm|JT8Q204E4R]].

So $A_k$ is a best approximation of $A$ of rank at most $k$ in both norms.

## Remarks

### Why each hypothesis is needed

- The singular values must be in decreasing order. If we keep $k$ terms that are not the largest, the error is larger. For $A = \operatorname{diag}(3, 2, 1)$ and $k = 1$, keeping the term $1$ gives the error $3$ in the operator norm instead of $2$.
- The bound $k < r$ only excludes the case $B = A$, where the error is $0$.
- The norms must be unitarily invariant. Take the largest absolute value of an entry as the norm, $A = \operatorname{diag}(2, 1)$ and $k = 1$. Then $A_1 = \operatorname{diag}(2, 0)$ has error $1$.
- In that norm, the rank-one matrix $B = \begin{pmatrix} 2 & 1/2 \\ 1/2 & 1/8 \end{pmatrix}$ does better: $A - B$ has the entries $0, -\tfrac12, -\tfrac12, \tfrac78$, so the error is $\tfrac78 < 1$.

### Consequences

- The distance from $A$ to the matrices of rank at most $k$ is $\sigma_{k+1}$ in the operator norm.
- For a square invertible $A$, the smallest singular value $\sigma_n$ is the distance in the operator norm to the singular matrices.
- [[The rank-one approximation of a $2 \times 2$ matrix|~90df945c]] computes $A_1$ and checks that both errors equal $\sigma_2$.
- Truncated SVD is the basis of [[principal component analysis|ABXD13M340]] in statistics and of low-rank compression in numerical linear algebra.

### Converse

The best approximation is not always unique.
In the operator norm, for $A = \operatorname{diag}(3, 2, 1)$ and $k = 1$, every $B = \operatorname{diag}(3 + t, 0, 0)$ with $\abs{t} \le 2$ has error $2 = \sigma_2$.
In the Frobenius norm, the best approximation is unique exactly when $\sigma_k > \sigma_{k+1}$; this fact is not proved here.
For $A = I_2$ and $k = 1$, both $\operatorname{diag}(1, 0)$ and $\operatorname{diag}(0, 1)$ have Frobenius error $1$.

### Generalizations

Mirsky extended the result to every unitarily invariant norm, for example the Schatten norms and the Ky Fan norms.
Schmidt solved the problem for integral operators, and the same proof works for compact operators on Hilbert spaces.
These belong to matrix analysis and functional analysis.

## History

The Wikipedia article on low-rank approximation states that Schmidt solved the problem for integral operators.
It states that Eckart and Young rediscovered the result, and that Mirsky generalized it to all unitarily invariant norms.
The Wikipedia article on the SVD dates the proof of Eckart and Young to 1936.

## Explanations

### L1 human

The theorem says how to approximate a matrix as well as possible by a simpler matrix of low rank.
Write the matrix as a sum of rank-one pieces from its singular value decomposition, and keep the largest pieces.
The error depends only on the singular values that we drop.

### L2 human

To compute a best rank-$k$ approximation, find the SVD and keep the first $k$ terms $\sigma_i u_i v_i^*$.
The error in the operator norm is the first dropped singular value $\sigma_{k+1}$.
The error in the Frobenius norm is the square root of the sum of the squares of all dropped singular values.
A trap: the best approximation does not keep $k$ columns or $k$ entries of $A$; it usually changes every entry.

### L3 human

The set of matrices of rank at most $k$ is not convex, so the theorem is not a projection theorem in the usual sense.
Still, the SVD reduces it to a diagonal problem, and the answer is to keep the largest diagonal entries.
For the operator norm, the proof is a dimension count: a matrix of rank $k$ has a large kernel, and this kernel meets the span of the first $k + 1$ right singular vectors.
For the Frobenius norm, the proof reduces to an inequality of Ky Fan type for the sum $\sum_i \sigma_i^2 c_i$ with weights $0 \le c_i \le 1$.
