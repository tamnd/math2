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

Let $A$ be an $n \times n$ complex [[Hermitian matrix|0P17NGQQMQ]].

1. $A$ is [[positive definite|0KX66CZMBB]] if and only if every [[eigenvalue|0BQAA2BK3Q]] of $A$ is positive.
2. $A$ is [[positive semidefinite|01MMVW8CKC]] if and only if every eigenvalue of $A$ is nonnegative.

The same holds for a real [[symmetric matrix|0VR671PHE5]] with the real definitions.

## Remarks

### Why each hypothesis is needed

- The matrix must be Hermitian. [[The non-symmetric matrix $\begin{pmatrix} 1 & -3 \\ 0 & 1 \end{pmatrix}$|VB4AQ8TKVP]] has the eigenvalues $1, 1$, but $x^T M x = -1$ at $x = (1, 1)$.
- The test needs every eigenvalue. [[The matrix $\begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix}$|N9TX4J2W4R]] has the positive eigenvalue $3$ and the negative eigenvalue $-1$.

### Consequences

- A positive definite matrix has $\det A > 0$, since the [[determinant is the product of the eigenvalues|0C2F40MEBC]]. So it is invertible.
- A positive definite matrix has $\tr A > 0$, since the [[trace is the sum of the eigenvalues|0NMXDCNNKR]].
- A positive semidefinite matrix is positive definite if and only if it is invertible, since both conditions say that $0$ is not an eigenvalue.
- The inverse of a positive definite matrix is positive definite, since its eigenvalues are $1/\lambda_i > 0$ and it is Hermitian.
- For real symmetric matrices, the same signs sort [[definiteness classes of quadratic forms|5Q0QZ4J01Y]], including negative definite and indefinite matrices.

### Converse

The statement is already an equivalence in both parts.
The Mathlib lemma `Matrix.PosDef.eigenvalues_pos` gives only the direction "positive definite implies positive eigenvalues".

### Generalizations

- On a finite-dimensional inner product space, a [[self-adjoint operator|0NEGN5CRSC]] $T$ has $\ip{Tv}{v} > 0$ for all $v \ne 0$ if and only if all its eigenvalues are positive. The proof is the same.
- For bounded self-adjoint operators on a Hilbert space, positivity is equivalent to the spectrum lying in $[0, \infty)$. This belongs to functional analysis.

## History

The Wikipedia article on definite matrices states both parts of the test in its section on eigenvalues.

## Explanations

### L1 human

A symmetric matrix is positive definite exactly when all its eigenvalues are positive.
For example, $\begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$ has eigenvalues $3$ and $1$, so it is positive definite.
The matrix $\begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix}$ has eigenvalues $3$ and $-1$, so it is not.

### L2 human

The test turns a condition on all vectors into a condition on $n$ numbers.
Recipe:

1. Check that $A$ is Hermitian, or real symmetric.
2. Compute the eigenvalues, for example as roots of the characteristic polynomial.
3. If all are positive, $A$ is positive definite. If all are at least $0$, $A$ is positive semidefinite.

For a $2 \times 2$ symmetric matrix, both eigenvalues are positive if and only if $\det A > 0$ and $\tr A > 0$.
A trap: for a non-symmetric matrix, the eigenvalues say nothing about the sign of $x^T A x$.

### L3 human

By the spectral theorem, a Hermitian matrix is a real diagonal matrix in a suitable orthonormal basis.
In that basis the form is $\sum_i \lambda_i \abs{y_i}^2$, and its sign behaviour can be read off.
This is the Hermitian case of Sylvester's law of inertia: the numbers of positive, negative and zero eigenvalues are invariants of the form.
The [[law of inertia|0WFED3K3DQ]] is treated with quadratic forms.
