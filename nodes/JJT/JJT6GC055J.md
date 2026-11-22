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
proofs: [7TTA01BTBJ]
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

To approximate a matrix as well as possible by a matrix of lower rank, keep the largest terms of its singular value decomposition and drop the rest.

Let $A$ be an $m \times n$ complex matrix with [[singular value decomposition|000NPTMX6J]] $A = \sum_{i=1}^{r} \sigma_i u_i v_i^*$.
Here $r$ is the [[rank|0ZC9YTXZRY]] of $A$, $\sigma_1 \ge \sigma_2 \ge \cdots \ge \sigma_r > 0$ are its [[singular values|09VMDSRXWJ]], and $u_1, \dots, u_r$ and $v_1, \dots, v_r$ are orthonormal families in $\C^m$ and $\C^n$.
Let $0 \le k < r$, and let $A_k = \sum_{i=1}^{k} \sigma_i u_i v_i^*$ be the truncated SVD, with $A_0 = 0$.
Then $\operatorname{rank} A_k = k$, and every $m \times n$ complex matrix $B$ of rank at most $k$ satisfies the following.

1. In the [[operator norm|06EKW1AKXF]] $\norm{\cdot}_2$ for the Euclidean norms, $\norm{A - B}_2 \ge \norm{A - A_k}_2 = \sigma_{k+1}$.
2. In the [[Frobenius norm|JT8Q204E4R]] $\norm{\cdot}_F$, $\norm{A - B}_F \ge \norm{A - A_k}_F = \left(\sigma_{k+1}^2 + \cdots + \sigma_r^2\right)^{1/2}$.

So $A_k$ is a best approximation of $A$ among the matrices of rank at most $k$, in both norms at once.

## Remarks

### A first use

[[The rank-one approximation of a 2 by 2 matrix|RFHTECHY4J]] takes $A = \begin{pmatrix} 3 & 0 \\ 4 & 5 \end{pmatrix}$, with singular values $\sigma_1 = 3\sqrt5$ and $\sigma_2 = \sqrt5$.
Keeping the first term gives
$$A_1 = \begin{pmatrix} 1.5 & 1.5 \\ 4.5 & 4.5 \end{pmatrix}, \qquad A - A_1 = \begin{pmatrix} 1.5 & -1.5 \\ -0.5 & 0.5 \end{pmatrix}.$$
Check: $\norm{A - A_1}_F^2 = 2.25 + 2.25 + 0.25 + 0.25 = 5 = \sigma_2^2$.
The obvious rank-one guess, keeping the first column of $A$, has error $5$, more than twice $\sqrt5 \approx 2.24$.

With one dropped value the two errors agree, but in general they differ.
For $A = \operatorname{diag}(4, 3, 2)$ and $k = 1$, the truncation is $\operatorname{diag}(4, 0, 0)$, the operator norm error is $3$, and the Frobenius error is $\sqrt{9 + 4} = \sqrt{13}$.

### Why each hypothesis is needed

The singular values must be kept in decreasing order.
If we keep $k$ terms that are not the largest, the error grows: for $A = \operatorname{diag}(3, 2, 1)$ and $k = 1$, keeping only the term with $\sigma_3 = 1$ leaves the error $3$ in the operator norm instead of $2$.

The bound $k < r$ only excludes the case where $A$ itself has rank at most $k$, so that $B = A$ has error $0$.

The two norms matter, because both are unitarily invariant: $\norm{P M Q} = \norm{M}$ for unitary $P$ and $Q$.
For the norm that takes the largest absolute value of an entry, the theorem fails.
Take $A = \operatorname{diag}(2, 1)$ and $k = 1$, so $A_1 = \operatorname{diag}(2, 0)$ has entry error $1$.
The matrix $B = \begin{pmatrix} 2 & 1/2 \\ 1/2 & 1/8 \end{pmatrix}$ has determinant $\tfrac14 - \tfrac14 = 0$, so its rank is $1$, and $A - B$ has entries $0$, $-\tfrac12$, $-\tfrac12$ and $\tfrac78$, so its entry error is $\tfrac78 < 1$.

### What it gives you

The distance from $A$ to the set of matrices of rank at most $k$ is exactly $\sigma_{k+1}$ in the operator norm.
For an invertible $n \times n$ matrix and $k = n - 1$, this says that the smallest singular value $\sigma_n$ is the distance to the nearest singular matrix, which is why $\sigma_1 / \sigma_n$, the [[condition number|AB3S6MHJ8X]], measures how close $A$ is to losing its inverse.

The truncated SVD is also the basis of [[principal component analysis|ABXD13M340]] in statistics and of [[image compression by the SVD|9QB82PPEMV]].
For an image stored as an $m \times n$ matrix, the rank-$k$ truncation needs $k(m + n + 1)$ numbers instead of $mn$, and the theorem says that no other rank-$k$ matrix fits the image better in the Frobenius norm.

### The converse and uniqueness

The best approximation need not be unique.
In the operator norm, for $A = \operatorname{diag}(3, 2, 1)$ and $k = 1$, every $B = \operatorname{diag}(3 + t, 0, 0)$ with $\abs{t} \le 2$ has $A - B = \operatorname{diag}(-t, 2, 1)$ and error $2 = \sigma_2$.
In the Frobenius norm, the best approximation is unique exactly when $\sigma_k > \sigma_{k+1}$, a fact that we do not prove here.
For $A = I_2$ and $k = 1$, the two values are equal, and both $\operatorname{diag}(1, 0)$ and $\operatorname{diag}(0, 1)$ have Frobenius error $1$.

### Generalizations

Mirsky extended the result to every unitarily invariant norm, for example the Schatten norms and the Ky Fan norms.
Schmidt solved the same problem for integral operators, and the argument works for compact operators on Hilbert spaces.
These versions belong to matrix analysis and functional analysis.

## History

Schmidt solved the approximation problem for integral operators.
Eckart and Young found the matrix version again in 1936.
Mirsky later generalized it to all unitarily invariant norms, which is why the three names appear together.

## Explanations

### L1 human

Many large tables of numbers are close to a simpler table built from a few patterns.
The SVD writes a matrix as a sum of rank-one pieces, each a column pattern times a row pattern, ordered from the most important piece to the least important one.
The theorem says that the best way to keep only $k$ pieces is to keep the first $k$.
The error is then made only of the pieces that you drop, so you can read it from the dropped singular values.

### L2 human

Here is a typical use: the best rank-one approximation of $A = \operatorname{diag}(4, 3, 2)$.
The singular values are $4$, $3$ and $2$, with singular vectors $e_1$, $e_2$, $e_3$, so the first term of the SVD is
$$A_1 = 4 e_1 e_1^{\mathsf{T}} = \operatorname{diag}(4, 0, 0), \qquad A - A_1 = \operatorname{diag}(0, 3, 2).$$
The operator norm error is the largest stretch of $A - A_1$, which is $3 = \sigma_2$.
The Frobenius error is $\sqrt{0 + 9 + 4} = \sqrt{13}$, the root of the sum of the squares of all dropped singular values.
No matrix of rank one comes closer in either norm.
Watch out: the best approximation does not simply keep $k$ columns or $k$ entries of $A$, and for a matrix that is not diagonal it usually changes every entry.

### L3 human

The set of matrices of rank at most $k$ is not convex, so the theorem is not a projection theorem in the usual sense.
Still, the SVD reduces it to a diagonal problem, and the answer is to keep the largest diagonal entries.
For the operator norm, the proof is a dimension count: a matrix of rank $k$ has a null space of dimension at least $n - k$, and it must meet the span of the first $k + 1$ right singular vectors.
For the Frobenius norm, the proof reduces to maximizing $\sum_i \sigma_i^2 c_i$ over weights $0 \le c_i \le 1$ whose sum is at most $k$, an inequality of Ky Fan type.
The same picture explains the [[Moore-Penrose inverse|0YY8VX28JR]] in floating point: truncating small singular values before inverting is an Eckart-Young approximation followed by a pseudoinverse.
