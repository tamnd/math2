---
tag: ~f8b3ecc3
kind: statement
role: theorem
name: Singular values, rank and the operator norm
msc: [15A18, 15A03]
topics: [SS4EVPKT3A]
audience: ug1
about: [09VMDSRXWJ, 0ZC9YTXZRY]
uses: [0K2TX12X58, 0EWQEYRVA8, 0S9GGTR0EX]
proofs: [~fb527235]
sources:
  - url: https://en.wikipedia.org/wiki/Singular_value
    locator: Basic properties
  - url: https://en.wikipedia.org/wiki/Singular_value_decomposition
    locator: Based on the spectral theorem
  - book: isbn:9780321982384
    locator: Section 7.4
---

## Statement

Let $A$ be an $m \times n$ complex matrix.
Let $v_1, \dots, v_n$ be an [[orthonormal basis|0S9GGTR0EX]] of $\C^n$ of eigenvectors of $A^* A$, with $A^* A v_i = \lambda_i v_i$ and $\lambda_1 \ge \dots \ge \lambda_n \ge 0$.
Let $\sigma_i = \sqrt{\lambda_i}$ be the [[singular values|09VMDSRXWJ]] of $A$, and let $r$ be the number of nonzero $\sigma_i$.

1. $\norm{A v_i} = \sigma_i$ for every $i$, and $\ip{A v_i}{A v_j} = 0$ for $i \ne j$.
2. The vectors $A v_1, \dots, A v_r$ form an orthogonal basis of the column space of $A$, and $v_{r+1}, \dots, v_n$ form an orthonormal basis of the null space of $A$.
3. $\rank A = r$: the [[rank|0ZC9YTXZRY]] of $A$ is the number of nonzero singular values.
4. $\max_{\norm x = 1} \norm{Ax} = \sigma_1$ and $\min_{\norm x = 1} \norm{Ax} = \sigma_n$, with the Euclidean norm.
5. $\norm{A}_F^2 = \sigma_1^2 + \dots + \sigma_n^2$, where $\norm{A}_F$ is the [[Frobenius norm|JT8Q204E4R]].
6. $A^* A$ and $A A^*$ have the same nonzero eigenvalues with the same multiplicities. So $A$ and $A^*$ have the same nonzero singular values.

## Remarks

### Why each hypothesis is needed

- The basis $v_i$ must be orthonormal for part 1. For $A = \operatorname{diag}(2, 1)$, the vectors $(1, 0)$ and $(1, 1)$ are a basis, but $A(1, 1) = (2, 1)$ has length $\sqrt5$, which is not a singular value.
- In part 3, eigenvalues of $A$ do not count the rank. The nilpotent $\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ has only the eigenvalue $0$, but rank $1$ and singular values $1, 0$.

### Consequences

- The vectors $u_i = A v_i / \sigma_i$ for $i \le r$ are orthonormal, and $A v_i = \sigma_i u_i$. This is the core of the [[singular value decomposition|000NPTMX6J]].
- The operator norm of $A$ for the Euclidean norms is $\sigma_1$, by part 4.
- An $n \times n$ matrix is invertible if and only if $\sigma_n > 0$.
- The rank of $A^* A$ equals the rank of $A$, since both are $r$.

### Converse

Part 3 can be read backwards: if $\rank A = r$, then exactly $r$ singular values are nonzero.
Part 4 gives the extreme values; the intermediate singular values are min-max values of $\norm{Ax}$, which belongs to matrix analysis.

### Generalizations

- For a linear map $T \colon V \to W$ between finite-dimensional inner product spaces, the same statements hold with $T^* T$ in place of $A^* A$.
- For compact operators on Hilbert spaces, part 2 becomes the Schmidt expansion; this belongs to functional analysis.

## History

The Wikipedia article on the singular value decomposition derives the decomposition from the spectral theorem in the same way, starting with the eigenvectors of $A^* A$.

## Explanations

### L1 human

The eigenvectors $v_i$ of $A^T A$ are perpendicular directions in the input space.
The matrix $A$ sends them to perpendicular vectors $A v_i$ with lengths $\sigma_i$.
The directions with $\sigma_i = 0$ are crushed to zero.
The others give the column space, so the number of nonzero $\sigma_i$ is the rank.

### L2 human

To find the rank of $A$ and bases of its column space and null space:

1. Diagonalize $A^* A$ with an orthonormal basis $v_1, \dots, v_n$.
2. The $v_i$ with $\lambda_i = 0$ span the null space.
3. The vectors $A v_i$ with $\lambda_i > 0$ form an orthogonal basis of the column space.

For [[the $3 \times 2$ example|~461482fa]], $\lambda = 3, 1$, so the rank is $2$ and the null space is $\set{0}$.
A trap: in floating point arithmetic, tiny nonzero $\sigma_i$ appear for rank deficient matrices, and a tolerance is needed; this belongs to numerical linear algebra.

### L3 human

The theorem is the spectral theorem for $A^* A$, moved through $A$.
The identity $\ip{Av_i}{Av_j} = \ip{A^* A v_i}{v_j}$ turns orthogonality in the input space into orthogonality in the output space.
Part 6 is the finite-dimensional case of the fact that $T^* T$ and $T T^*$ are unitarily equivalent off their kernels.
