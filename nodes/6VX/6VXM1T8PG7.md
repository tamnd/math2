---
tag: 6VXM1T8PG7
kind: statement
role: theorem
name: Singular values, rank and the operator norm
msc: [15A18, 15A03]
topics: [SS4EVPKT3A]
audience: ug1
about: [09VMDSRXWJ, 0ZC9YTXZRY]
uses: [0K2TX12X58, 0EWQEYRVA8, 0S9GGTR0EX]
proofs: [KXFDT8R18J]
sources:
  - url: https://en.wikipedia.org/wiki/Singular_value
    locator: Basic properties
  - url: https://en.wikipedia.org/wiki/Singular_value_decomposition
    locator: Based on the spectral theorem
  - book: isbn:9780321982384
    locator: Section 7.4
---

## Statement

A matrix sends an orthonormal eigenbasis of $A^* A$ to orthogonal vectors whose lengths are the singular values, and this one fact gives the rank, the norms and the main subspaces of the matrix.

Let $A$ be an $m \times n$ complex matrix, and give $\C^n$ and $\C^m$ the standard inner product $\ip{x}{y} = y^* x$.
Let $v_1, \dots, v_n$ be an [[orthonormal basis|0S9GGTR0EX]] of $\C^n$ of eigenvectors of $A^* A$, with $A^* A v_i = \lambda_i v_i$ and $\lambda_1 \ge \dots \ge \lambda_n \ge 0$.
Let $\sigma_i = \sqrt{\lambda_i}$ be the [[singular values|09VMDSRXWJ]] of $A$, and let $r$ be the number of nonzero $\sigma_i$.

1. $\norm{A v_i} = \sigma_i$ for every $i$, and $\ip{A v_i}{A v_j} = 0$ for $i \ne j$.
2. The vectors $A v_1, \dots, A v_r$ form an orthogonal basis of the column space of $A$, and $v_{r+1}, \dots, v_n$ form an orthonormal basis of the null space of $A$.
3. $\rank A = r$, so the [[rank|0ZC9YTXZRY]] of $A$ is the number of nonzero singular values.
4. With the Euclidean norm, $\max_{\norm x = 1} \norm{Ax} = \sigma_1$ and $\min_{\norm x = 1} \norm{Ax} = \sigma_n$.
5. $\norm{A}_F^2 = \sigma_1^2 + \dots + \sigma_n^2$, where $\norm{A}_F$ is the [[Frobenius norm|JT8Q204E4R]].
6. $A^* A$ and $A A^*$ have the same nonzero eigenvalues with the same multiplicities, so $A$ and $A^*$ have the same nonzero singular values.

The [[proof|KXFDT8R18J]] computes $\ip{A v_i}{A v_j}$ and expands vectors in the basis $v_i$.

## Remarks

### A first check

Take the [[tall matrix with rows (1, 1), (1, 0), (0, 1)|GK1B93DKD3]].
Its matrix $A^{\mathsf{T}} A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$ has the unit eigenvectors $v_1 = \tfrac{1}{\sqrt2}(1, 1)$ for $3$ and $v_2 = \tfrac{1}{\sqrt2}(1, -1)$ for $1$.
Apply $A$:
$$A v_1 = \tfrac{1}{\sqrt2}(2, 1, 1), \qquad A v_2 = \tfrac{1}{\sqrt2}(0, 1, -1).$$
Check: the lengths are $\sqrt{6/2} = \sqrt3$ and $\sqrt{2/2} = 1$, and the dot product is $\tfrac12(0 + 1 - 1) = 0$, as part 1 says.
Both singular values are nonzero, so part 3 gives rank $2$, and part 4 says that no unit vector is stretched by more than $\sqrt3$.

### Why each hypothesis is needed

The basis must consist of eigenvectors of $A^* A$; an orthonormal basis alone is not enough.
For $A = \operatorname{diag}(2, 1)$, the orthonormal vectors $\tfrac{1}{\sqrt2}(1, 1)$ and $\tfrac{1}{\sqrt2}(1, -1)$ go to $\tfrac{1}{\sqrt2}(2, 1)$ and $\tfrac{1}{\sqrt2}(2, -1)$.
Their lengths are both $\sqrt{5/2}$, which is not a singular value, and their dot product is $\tfrac{3}{2} \ne 0$.

The eigenvalues of $A$ itself do not count the rank, so part 3 really needs the singular values.
The nilpotent matrix $\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ has only the eigenvalue $0$, but it has rank $1$ and singular values $1$ and $0$.

### What it gives you

For $i \le r$ the vectors $u_i = A v_i / \sigma_i$ are orthonormal and satisfy $A v_i = \sigma_i u_i$.
This is the core of the [[singular value decomposition|000NPTMX6J]], which adds the missing $u_i$ to make a square unitary matrix.
Part 4 says that the [[operator norm|06EKW1AKXF]] of $A$ for the Euclidean norms is $\sigma_1$.
For a square $A$, part 4 also gives the test "$A$ is invertible exactly when $\sigma_n > 0$", since $\sigma_n = 0$ means $A v_n = 0$.
Parts 3 and 6 together give $\rank(A^* A) = \rank A$, a fact that the [[normal equations|4D7MRG4D91]] of least squares use.

### The converse and the middle values

Part 3 reads in both directions: if $\rank A = r$, then exactly $r$ singular values are nonzero.
Part 4 describes only the largest and the smallest value.
The middle ones are min-max values of $\norm{Ax}$ over subspaces, by the Courant-Fischer theorem for $A^* A$, which belongs to matrix analysis.

### Generalizations

For a linear map $T \colon V \to W$ between finite-dimensional inner product spaces, the same statements hold with $T^* T$ in place of $A^* A$, where $T^*$ is the adjoint.
For compact operators on Hilbert spaces, part 2 becomes the Schmidt expansion of functional analysis.

## History

These facts form the first step of the proof of the singular value decomposition from the spectral theorem.
They are standard facts of matrix theory and carry no single author's name.

## Explanations

### L1 human

The eigenvectors $v_i$ of $A^{\mathsf{T}} A$ are perpendicular directions in the input space.
The matrix sends them to perpendicular arrows $A v_i$, and the arrow from $v_i$ has length $\sigma_i$.
The directions with $\sigma_i = 0$ are crushed to zero.
The other arrows fill the column space, so the number of nonzero $\sigma_i$ is the rank.

### L2 human

Here is a typical use: find the rank, the null space and the norm of $A = \begin{pmatrix} 1 & 1 \\ 2 & 2 \end{pmatrix}$.
Form $A^{\mathsf{T}} A = \begin{pmatrix} 5 & 5 \\ 5 & 5 \end{pmatrix}$, with the unit eigenvectors $v_1 = \tfrac{1}{\sqrt2}(1, 1)$ for $10$ and $v_2 = \tfrac{1}{\sqrt2}(1, -1)$ for $0$.
So $\sigma_1 = \sqrt{10}$ and $\sigma_2 = 0$, the rank is $1$, and the null space is the line through $(1, -1)$.
Check: $A(1, -1) = (0, 0)$, and $A v_1 = \tfrac{1}{\sqrt2}(2, 4)$ has length $\sqrt{20/2} = \sqrt{10}$, the largest stretch.
Watch out: in floating point arithmetic a matrix of low rank often shows tiny nonzero $\sigma_i$, so the numerical rank needs a tolerance.

### L3 human

The theorem is the spectral theorem for $A^* A$, carried through $A$.
The identity $\ip{A v_i}{A v_j} = \ip{A^* A v_i}{v_j}$ turns orthogonality in the input space into orthogonality in the output space.
Part 6 is the finite-dimensional case of the fact that $T^* T$ and $T T^*$ are unitarily equivalent on the orthogonal complements of their kernels.
