---
tag: 01MMVW8CKC
kind: concept
name: Positive semidefinite matrix
msc: [15B57, 15A63]
topics: [SS4EVPKT3A]
audience: ug1
specializes: [0P17NGQQMQ]
uses: [0880F9EQCP, 0EKZCX4K3P, 0EX045E2BP]
sources:
  - url: https://en.wikipedia.org/wiki/Definite_matrix
    locator: Definitions
  - url: https://en.wikipedia.org/wiki/Definite_matrix
    locator: Decomposition
  - book: isbn:9783031410253
    locator: Chapter 7
  - book: isbn:9780521839402
    locator: Chapter 7
inventory: [8XQP955FKQ]
---

## Summary

Let $A$ be an $n \times n$ complex [[Hermitian matrix|0P17NGQQMQ]].
The matrix $A$ is positive semidefinite when $x^* A x \ge 0$ for every vector $x \in \C^n$.
For a real [[symmetric matrix|0VR671PHE5]] the condition is $x^T A x \ge 0$ for every $x \in \R^n$.
The [[formal definition|0880F9EQCP]] states this.
Positive semidefinite matrices are the matrix analogue of nonnegative numbers, and every [[positive definite matrix|0KX66CZMBB]] is one.

## Motivation

Many matrices that come from data are positive semidefinite without being positive definite.
The [[Gram matrix|00SPJSDT3Z]] of a list of vectors is positive semidefinite, and it is positive definite only when the vectors are independent.
A [[covariance matrix|0V7G6WMFK0]] is positive semidefinite, because a variance is never negative.
The matrices $A^* A$ and $A A^*$ are positive semidefinite for every matrix $A$, and the [[singular values|09VMDSRXWJ]] of $A$ come from them.
So a theory that allows the value $0$ is needed.

## Notation

- We write $A \succeq 0$ or $A \ge 0$ for "$A$ is positive semidefinite". The order $A \succeq B$ means $A - B \succeq 0$, which is the [[Loewner order|9G9S92T1VJ]].
- Mathlib writes `Matrix.PosSemidef A`, and its definition includes the condition that $A$ is Hermitian.
- As for positive definite matrices, some books do not ask for symmetry. This page always asks for it.

## Remarks

### Examples

- The zero matrix is positive semidefinite, and it is not positive definite for $n \ge 1$.
- [[The all-ones $2 \times 2$ matrix|YAAQD2E1BZ]] is positive semidefinite, with eigenvalues $0$ and $2$.
- [[The matrix $\begin{pmatrix} 5 & 4 \\ 4 & 5 \end{pmatrix}$ of the square root example|QTV6Y0710E]] is positive semidefinite, and in fact positive definite.
- An [[orthogonal projection|0B8KZRT28M]] matrix $P$ with $P^* = P = P^2$ is positive semidefinite, because $x^* P x = x^* P^* P x = \norm{Px}^2$.
- For every $m \times n$ matrix $B$, the matrix $B^* B$ is positive semidefinite, by [[the Gram matrix theorem|0AM050KCAW]].
- Every positive definite matrix, for example [[the tridiagonal example|RSQW92W4PD]], is positive semidefinite.

### Non-examples

- [[The matrix $\begin{pmatrix} 0 & 0 \\ 0 & -1 \end{pmatrix}$|9ZQ1GV2F0G]] has leading minors $0$ and $0$, but the form is $-1$ at $e_2$.
- [[The matrix $\begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix}$|N9TX4J2W4R]] has positive entries and an eigenvalue $-1$.
- The matrix $\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$ is Hermitian, and the form is $-1$ at $e_2$. Such a matrix is called indefinite.

### Basic properties

- A Hermitian matrix is positive semidefinite if and only if all its eigenvalues are nonnegative, by [[the eigenvalue test|0HYC2RHD3M]].
- A Hermitian matrix is positive semidefinite if and only if all its principal minors are nonnegative, by [[Sylvester's criterion|0WKEF78PMV]]. The leading minors alone are not enough.
- A matrix is positive semidefinite if and only if it equals $B^* B$ for some square $B$, by [[the Gram matrix theorem|0AM050KCAW]].
- A positive semidefinite matrix has a unique positive semidefinite [[square root|EQ98KW1ZN4]].
- A positive semidefinite matrix is positive definite if and only if it is invertible. This follows from the eigenvalue test, because $\det A$ is the product of the eigenvalues.
- The diagonal entries are nonnegative. If $a_{ii} = 0$, then row $i$ and column $i$ are zero; a $2 \times 2$ principal minor $a_{ii}a_{jj} - \abs{a_{ij}}^2 \ge 0$ forces $a_{ij} = 0$.
- If $A \succeq 0$, then $P^* A P \succeq 0$ for every $n \times k$ matrix $P$. In particular every principal submatrix is positive semidefinite.
- Sums and nonnegative multiples of positive semidefinite matrices are positive semidefinite. So they form a closed convex cone, which belongs to matrix analysis.

### History

The Wikipedia article on definite matrices gives the decomposition $A = B^* B$ as the main characterization, and it allows $B$ to be rectangular.
It also notes that some authors drop the symmetry condition.

### Common errors

- Students test only the leading principal minors. [[The matrix $\operatorname{diag}(0, -1)$|9ZQ1GV2F0G]] passes that test and is not positive semidefinite.
- Students expect a positive semidefinite matrix to be invertible. [[The all-ones matrix|YAAQD2E1BZ]] has determinant $0$.
- Students think that $x^* A x \ge 0$ and $x^* A x = 0$ imply $x = 0$. For the all-ones matrix, $x = (1, -1)$ gives $0$.

## Explanations

### L1 human

A positive semidefinite matrix never gives a negative number $x^T A x$.
It may give $0$ for a nonzero vector.
For example, $\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$ gives $(x_1 + x_2)^2$.
This is never negative, and it is $0$ for $x = (1, -1)$.
The graph of such a function is a bowl or a flat valley, and never a saddle.

### L2 human

The fastest tests are these.

1. Check that $A$ is Hermitian (real symmetric in the real case).
2. Find the eigenvalues. If all are at least $0$, then $A$ is positive semidefinite.
3. Or write $A = B^* B$ for some matrix $B$. Then $x^* A x = \norm{Bx}^2 \ge 0$.

The typical use: the matrix $A^T A$ of a least squares problem is positive semidefinite, so the least squares function $\norm{Ax - b}^2$ is convex.
A trap: for semidefiniteness, Sylvester's test needs all principal minors, not only the leading ones.

### L3 human

The positive semidefinite $n \times n$ matrices form a closed convex cone in the real space of Hermitian matrices.
The cone is self-dual for the trace inner product $\ip{A}{B} = \tr(AB)$.
Its interior is the cone of positive definite matrices, and its boundary is the set of singular positive semidefinite matrices.
Positive semidefinite matrices correspond to Gram matrices of vectors in some inner product space, and their rank is the dimension of the span.
In functional analysis the same notion gives positive operators, and in optimization it gives semidefinite programming.
