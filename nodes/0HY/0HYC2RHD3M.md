---
tag: 0HYC2RHD3M
kind: statement
role: theorem
name: Eigenvalue test for definiteness
msc: [15B57, 15A18]
topics: [SS4EVPKT3A]
audience: ug1
about: [0KX66CZMBB, 01MMVW8CKC]
uses: [0QQCG3JWJ4, 0880F9EQCP, 0ZND7NQ970, 0EKZCX4K3P]
proofs: [RPGNQMC7BB]
formal:
  - system: lean4
    library: mathlib
    decl: Matrix.PosDef.eigenvalues_pos
    match: weaker
sources:
  - url: https://en.wikipedia.org/wiki/Definite_matrix
    locator: Eigenvalues
  - book: isbn:9783031410253
    locator: Chapter 7
  - book: isbn:9780321982384
---

## Statement

The eigenvalue test replaces a condition on all vectors by a condition on $n$ numbers: a Hermitian matrix is positive definite exactly when its eigenvalues are positive.

Let $A$ be an $n \times n$ complex [[Hermitian matrix|0P17NGQQMQ]].
Its [[eigenvalues|0BQAA2BK3Q]] are real.

1. $A$ is [[positive definite|0KX66CZMBB]] if and only if every eigenvalue of $A$ is positive.
2. $A$ is [[positive semidefinite|01MMVW8CKC]] if and only if every eigenvalue of $A$ is nonnegative.

The same holds for a real [[symmetric matrix|0VR671PHE5]], with the real definitions.
The [[proof|RPGNQMC7BB]] uses the spectral theorem.

## Remarks

### A first use

Take $A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$.
Its characteristic polynomial is $(2 - t)^2 - 1 = (t - 3)(t - 1)$, so the eigenvalues are $3$ and $1$, with eigenvectors $(1, 1)$ and $(1, -1)$.
Both are positive, so $A$ is positive definite.
The proof turns this into a sum of squares in the eigenvector directions:
$$2x_1^2 + 2x_1 x_2 + 2x_2^2 = \tfrac32 (x_1 + x_2)^2 + \tfrac12 (x_1 - x_2)^2.$$
Check: the right side is $\tfrac32 (x_1^2 + 2x_1 x_2 + x_2^2) + \tfrac12 (x_1^2 - 2x_1 x_2 + x_2^2) = 2x_1^2 + 2x_1 x_2 + 2x_2^2$.
The coefficients $\tfrac32$ and $\tfrac12$ are the eigenvalues divided by $2$, the squared length of each eigenvector.
[[The tridiagonal example|RSQW92W4PD]] runs the same test on a $3 \times 3$ matrix, and [[the all-ones matrix|YAAQD2E1BZ]] shows part 2 with the eigenvalues $0$ and $2$.

### Why each hypothesis is needed

The matrix must be Hermitian.
[[The matrix with rows (1, -3) and (0, 1)|VB4AQ8TKVP]] is triangular, so its eigenvalues are its diagonal entries $1$ and $1$, but its form is $-1$ at $x = (1, 1)$.
For a matrix that is not Hermitian, the eigenvalues can even be complex, and then the test has no meaning.

The test needs every eigenvalue.
[[The matrix with entries 1, 2, 2, 1|N9TX4J2W4R]] has the positive eigenvalue $3$, but it also has the eigenvalue $-1$, and its form is $-2$ at the eigenvector $(1, -1)$.

### What it gives you

A positive definite matrix has $\det A > 0$, because the [[determinant is the product of the eigenvalues|0C2F40MEBC]], and so it is invertible.
It has $\tr A > 0$, because the [[trace is the sum of the eigenvalues|0NMXDCNNKR]].
Its inverse is Hermitian with eigenvalues $1/\lambda_i > 0$, so the inverse is positive definite too.
A positive semidefinite matrix is positive definite exactly when it is invertible, since both conditions say that $0$ is not an eigenvalue.

For a $2 \times 2$ real symmetric matrix the test becomes very short.
The two eigenvalues are positive exactly when their product $\det A$ and their sum $\tr A$ are positive.
For real symmetric matrices of any size, the signs of the eigenvalues also sort the [[definiteness classes|5Q0QZ4J01Y]]: negative definite, negative semidefinite and indefinite.

### The converse

Both parts are already equivalences.
The Mathlib lemma `Matrix.PosDef.eigenvalues_pos` gives only the direction from positive definite to positive eigenvalues, which is why its match is marked as weaker.
That direction needs no spectral theorem: if $Ax = \lambda x$ with $x \ne 0$, then $0 < x^* A x = \lambda \, x^* x$ and $x^* x > 0$, so $\lambda > 0$.

### Generalizations

On a finite-dimensional inner product space, a [[self-adjoint operator|0NEGN5CRSC]] $T$ satisfies $\ip{Tv}{v} > 0$ for all $v \ne 0$ exactly when all its eigenvalues are positive, with the same proof in an orthonormal basis of eigenvectors.
For a bounded self-adjoint operator on a Hilbert space, $\ip{Tv}{v} \ge 0$ for all $v$ is equivalent to the spectrum lying in $[0, \infty)$, but the spectrum need not consist of eigenvalues there, and this belongs to functional analysis.

## History

The test rests on the fact that a real symmetric matrix has real eigenvalues and an orthonormal basis of eigenvectors.
Cauchy proved that the eigenvalues of a real symmetric matrix are real in 1829.

## Explanations

### L1 human

A symmetric matrix is positive definite exactly when all its eigenvalues are positive.
For example, $\begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$ has eigenvalues $3$ and $1$, so it is positive definite.
The matrix $\begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix}$ has eigenvalues $3$ and $-1$, so it is not.

### L2 human

Here is a typical use: for which real $c$ is $A = \begin{pmatrix} 1 & c \\ c & 4 \end{pmatrix}$ positive definite?
The eigenvalues are the roots of $t^2 - 5t + (4 - c^2)$, and their sum is $5 > 0$.
Two real numbers with a positive sum are both positive exactly when their product is positive, so we need $4 - c^2 > 0$, that is, $-2 < c < 2$.
At $c = 2$ the eigenvalues are $0$ and $5$, and the matrix is semidefinite but not definite.
The test is the fastest one when the eigenvalues are easy to find, as for $2 \times 2$ matrices and for block diagonal matrices with small blocks.
Watch out: for a matrix that is not symmetric, the eigenvalues say nothing about the sign of $x^{\mathsf{T}} A x$.

### L3 human

By the spectral theorem, a Hermitian matrix is a real diagonal matrix in a suitable orthonormal basis, and in that basis the form is $\sum_i \lambda_i \abs{y_i}^2$.
So the sign pattern of the form is the sign pattern of the eigenvalues.
This is the Hermitian case of [[Sylvester's law of inertia|0WFED3K3DQ]]: the numbers of positive, negative and zero eigenvalues are invariants of the form under every change of basis $A \mapsto P^* A P$, not only the unitary ones.
The same idea gives the second derivative test in several variables and the classification of quadrics by the signs of the eigenvalues.
