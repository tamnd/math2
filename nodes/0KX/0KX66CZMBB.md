---
tag: 0KX66CZMBB
kind: concept
name: Positive definite matrix
msc: [15B57, 15A63]
topics: [SS4EVPKT3A]
audience: ug1
specializes: [01MMVW8CKC]
uses: [0QQCG3JWJ4, 0EKZCX4K3P, 0EX045E2BP]
sources:
  - url: https://en.wikipedia.org/wiki/Definite_matrix
    locator: Definitions
  - url: https://en.wikipedia.org/wiki/Definite_matrix
    locator: Extension for non-Hermitian square matrices
  - book: isbn:9783031410253
    locator: Chapter 7
  - book: isbn:9780321982384
inventory: [2Z8JQJ3GJZ]
---

## Summary

Let $A$ be an $n \times n$ complex [[Hermitian matrix|0P17NGQQMQ]], so $A^* = A$, where $A^*$ is the [[conjugate transpose|0DXKE10PHF]].
The matrix $A$ is positive definite when $x^* A x > 0$ for every nonzero vector $x \in \C^n$.
For a real [[symmetric matrix|0VR671PHE5]] the condition is $x^T A x > 0$ for every nonzero $x \in \R^n$.
The [[formal definition|0QQCG3JWJ4]] states this.
Positive definite matrices are the matrices that behave like positive numbers: they give inner products, they have positive eigenvalues, and they have square roots.

## Motivation

A positive number $a$ gives a function $x \mapsto a x^2$ that is positive for every $x \neq 0$.
In several variables, the same role is played by a function $x \mapsto x^T A x$, which is a sum of terms $a_{ij} x_i x_j$.
We want to know when this function is positive at every nonzero vector.
The question appears in many places.
An [[inner product|0NB0AWGJBW]] on $\R^n$ is exactly a function $\ip{x}{y} = y^T A x$ with $A$ symmetric and positive definite.
At a critical point of a function of several variables, a positive definite [[Hessian matrix|0693Y2METT]] gives a strict local minimum.
In least squares, the matrix $A^T A$ of the [[normal equations|4D7MRG4D91]] is positive definite when the columns of $A$ are independent.

## Notation

- We write $A \succ 0$ or $A > 0$ for "$A$ is positive definite". Some books write $A \gg 0$, but other books use this for matrices with positive entries.
- The order $A \succ B$ means $A - B \succ 0$. It is the strict part of the [[Loewner order|9G9S92T1VJ]], which belongs to matrix analysis.
- Mathlib writes `Matrix.PosDef A`. Its definition asks that $A$ is Hermitian and that the form is positive at nonzero vectors.
- Books differ on symmetry. Most books, and this page, require $A$ to be Hermitian (real symmetric in the real case). Some books call a real matrix positive definite when only $x^T A x > 0$ holds for $x \neq 0$, without symmetry. Always check which convention a book uses.

## Remarks

### Examples

- The identity matrix $I_n$ is positive definite, since $x^* I_n x = \sum_i \abs{x_i}^2 > 0$ for $x \neq 0$.
- A diagonal matrix with positive real diagonal entries $d_1, \dots, d_n$ is positive definite, since $x^* D x = \sum_i d_i \abs{x_i}^2$.
- [[The tridiagonal $3 \times 3$ matrix with entries $2$ and $-1$|RSQW92W4PD]] is positive definite. Sylvester's test gives the leading minors $2, 3, 4$.
- [[The matrix of a Cholesky example|M3YVJ6CFJ5]] is positive definite, because it equals $L L^T$ with $L$ invertible.
- The [[Hilbert matrix|2DTWB6F5TA]] $\left(\frac{1}{i + j - 1}\right)$ is positive definite, because it is the Gram matrix of the independent functions $1, t, \dots, t^{n-1}$ on $[0, 1]$.
- For a matrix $B$ with linearly independent columns, $B^* B$ is positive definite, by [[the Gram matrix theorem|0AM050KCAW]].

### Non-examples

- [[The matrix $\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$|YAAQD2E1BZ]] is positive semidefinite but not positive definite. Strict positivity fails at $x = (1, -1)$, where the form is $0$.
- [[The matrix $\begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix}$|N9TX4J2W4R]] has positive entries, but the form is $-2$ at $x = (1, -1)$. Positivity of the form fails.
- [[The matrix $\begin{pmatrix} 1 & -3 \\ 0 & 1 \end{pmatrix}$|VB4AQ8TKVP]] is not symmetric, so the Hermitian condition fails. Its leading minors are $1$ and $1$, but the form is $-1$ at $x = (1, 1)$.
- The matrix $-I_n$ is Hermitian, but $x^*(-I_n)x = -\norm{x}^2 < 0$ for $x \neq 0$.

### Basic properties

- A Hermitian matrix is positive definite if and only if all its eigenvalues are positive. This is [[the eigenvalue test|0HYC2RHD3M]].
- A Hermitian matrix is positive definite if and only if all its leading principal minors are positive. This is [[Sylvester's criterion|0WKEF78PMV]].
- A matrix is positive definite if and only if it equals $B^* B$ for some $B$ with independent columns, by [[the Gram matrix theorem|0AM050KCAW]].
- A matrix is positive definite if and only if it has a [[Cholesky decomposition|0WKG8CYY6A]] $A = L L^*$ with $L$ lower triangular with positive diagonal.
- A positive definite matrix has a unique positive definite [[square root|EQ98KW1ZN4]].
- A positive definite matrix is invertible, its determinant and its trace are positive, and its inverse is positive definite. The first three facts follow from the eigenvalue test.
- The diagonal entries are positive, because $a_{ii} = e_i^* A e_i > 0$ for the standard basis vector $e_i$.
- If $A \succ 0$ and $P$ is invertible, then $P^* A P \succ 0$, because $x^* P^* A P x = (Px)^* A (Px)$ and $Px \neq 0$ for $x \neq 0$.
- Sums of positive definite matrices are positive definite, and so are positive multiples. So they form a convex cone.
- On an inner product space, a [[self-adjoint operator|0NEGN5CRSC]] $T$ with $\ip{Tv}{v} > 0$ for all $v \neq 0$ is called positive definite. Its matrix in an orthonormal basis is a positive definite matrix. The operator version on Hilbert spaces is the [[positive operator|77020CY5ZW]] of functional analysis.

### History

The Wikipedia article on definite matrices notes that some authors drop the symmetry condition, and it treats those matrices in a separate section.
The test by leading minors carries the name of Sylvester, by the Wikipedia article on [[Sylvester's criterion|0WKEF78PMV]].

### Common errors

- Students think that positive entries make a matrix positive definite. [[The matrix with entries $1, 2, 2, 1$|N9TX4J2W4R]] shows that this is false.
- Students apply Sylvester's test to a matrix that is not symmetric. [[The non-symmetric example|VB4AQ8TKVP]] has positive leading minors and a negative value of the form.
- Students check only $x^T A x > 0$ at the standard basis vectors. This only shows that the diagonal entries are positive.

## Explanations

### L1 human

A positive definite matrix acts like a positive number.
For a positive number $a$, the value $a x^2$ is positive for every $x$ that is not zero.
For a matrix $A$, we put a vector $x$ on both sides and get one number, $x^T A x$.
The matrix is positive definite when this number is positive for every nonzero vector.
For example, with $A = \begin{pmatrix} 2 & 0 \\ 0 & 3 \end{pmatrix}$ the number is $2x_1^2 + 3x_2^2$, and this is positive unless $x_1 = x_2 = 0$.
The graph of such a function is a bowl that opens upward.

### L2 human

Worked example: is $A = \begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix}$ positive definite?

1. $A$ is real and symmetric, so the definition applies.
2. For $x = (x_1, x_2)$, the form is $x^T A x = 2x_1^2 - 2x_1 x_2 + 2x_2^2$.
3. Completing the square gives $2\left(x_1 - \tfrac12 x_2\right)^2 + \tfrac32 x_2^2$.
4. Both terms are at least $0$. If the sum is $0$, then $x_2 = 0$ and then $x_1 = 0$.
5. So $x^T A x > 0$ for every $x \neq 0$, and $A$ is positive definite.

The typical use is to prove that a quadratic function has a strict minimum, or that a matrix gives an inner product.
In practice the fastest tests are [[the eigenvalue test|0HYC2RHD3M]] for small matrices and the [[Cholesky decomposition|0WKG8CYY6A]] for large ones.
A trap: the test must use all nonzero vectors, not only a few chosen ones.

### L3 human

The positive definite $n \times n$ matrices form an open convex cone in the real vector space of Hermitian matrices.
It is the interior of the closed cone of [[positive semidefinite matrices|01MMVW8CKC]].
The group $GL_n(\C)$ acts on the cone by $A \mapsto P^* A P$, and the action has one orbit: every positive definite $A$ equals $L L^*$ by Cholesky.
So the cone is the homogeneous space $GL_n(\C) / U(n)$, where $U(n)$ is the [[unitary group|0R9R0Y1HDK]].
Positive definite matrices are the same as inner products on $\C^n$, and the [[simultaneous diagonalization with a positive definite matrix|K559AQ9H67]] is the spectral theorem for a second inner product.
In functional analysis the same notion gives positive operators, and in probability it gives covariance matrices of nondegenerate random vectors.
