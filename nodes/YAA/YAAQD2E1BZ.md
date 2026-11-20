---
tag: YAAQD2E1BZ
kind: example
name: The all-ones 2 × 2 matrix is semidefinite but not definite
msc: [15B57]
topics: [SS4EVPKT3A]
audience: ug1
instance_of: [01MMVW8CKC]
not_instance_of:
  - target: 0KX66CZMBB
    note: the all-ones matrix is positive semidefinite, but the form is 0 at the nonzero vector (1, -1)
illustrates: [0HYC2RHD3M, 0AM050KCAW]
uses: [0880F9EQCP, 0QQCG3JWJ4]
sources:
  - url: https://en.wikipedia.org/wiki/Definite_matrix
    locator: Examples
---

## Example

Let $A = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$.

1. $A$ is real and symmetric.
2. For $x = (x_1, x_2)$, the form is $x^T A x = x_1^2 + 2x_1x_2 + x_2^2 = (x_1 + x_2)^2 \ge 0$. So $A$ is [[positive semidefinite|0880F9EQCP]].
3. At $x = (1, -1) \ne 0$, the form is $(1 - 1)^2 = 0$. So $x^T A x > 0$ fails, and $A$ is not [[positive definite|0QQCG3JWJ4]].
4. The eigenvalues are the roots of $(1 - t)^2 - 1 = t(t - 2)$, so they are $0$ and $2$. Both are nonnegative, and one is $0$, which agrees with [[the eigenvalue test|0HYC2RHD3M]].
5. $A = B^T B$ with $B = \begin{pmatrix} 1 & 1 \end{pmatrix}$, since $B^T B = \begin{pmatrix} 1 \\ 1 \end{pmatrix}\begin{pmatrix} 1 & 1 \end{pmatrix}$. The two columns of $B$ are equal, so they are dependent, as [[the Gram matrix theorem|0AM050KCAW]] predicts.

## Remarks

- The leading minors are $1$ and $\det A = 0$. They are not all positive, so Sylvester's test for definiteness fails.
- All principal minors are $1$, $1$ and $0$, so they are all nonnegative, and the semidefinite test passes.
- The null space of $A$ is spanned by $(1, -1)$. A positive semidefinite matrix is positive definite exactly when its null space is $\set{0}$.

## Explanations

### L1 human

This matrix never gives a negative number $x^T A x$, because the number is a square $(x_1 + x_2)^2$.
But it gives $0$ at the nonzero vector $(1, -1)$.
So the matrix is semidefinite and not definite.

### L2 human

The example shows the gap between "$\ge 0$" and "$> 0$".
The eigenvalue $0$ and the determinant $0$ both show the gap.
A trap: a positive semidefinite matrix with a zero eigenvalue is not invertible, so it has no Cholesky factor with positive diagonal.
