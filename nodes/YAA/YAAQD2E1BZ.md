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
We show that $A$ is positive semidefinite but not positive definite.

1. $A$ is real and symmetric.
2. For $x = (x_1, x_2)$, the form is a perfect square:
$$x^{\mathsf{T}} A x = x_1^2 + 2x_1 x_2 + x_2^2 = (x_1 + x_2)^2 \ge 0.$$
So $A$ is [[positive semidefinite|0880F9EQCP]].
3. At $x = (1, -1) \ne 0$ the form is $(1 - 1)^2 = 0$. So the strict inequality fails, and $A$ is not [[positive definite|0QQCG3JWJ4]].
4. The eigenvalues are the roots of $(1 - t)^2 - 1 = t(t - 2)$, so they are $0$ and $2$. Both are nonnegative and one is zero, as [[the eigenvalue test|0HYC2RHD3M]] predicts for a matrix that is semidefinite and not definite.
5. With $B = \begin{pmatrix} 1 & 1 \end{pmatrix}$, a $1 \times 2$ matrix, we get $A = B^{\mathsf{T}} B$. The two columns of $B$ are equal, so they are dependent, as [[the Gram matrix theorem|0AM050KCAW]] predicts.

Check: $B^{\mathsf{T}} B = \begin{pmatrix} 1 \\ 1 \end{pmatrix} \begin{pmatrix} 1 & 1 \end{pmatrix}$ has every entry equal to $1 \cdot 1 = 1$.

## Remarks

The example shows the gap between "$\ge 0$" and "$> 0$".
Every test shows the same gap: the eigenvalue $0$, the determinant $0$ and the dependent columns of $B$.
The leading minors are $1$ and $0$, so Sylvester's test for definiteness fails.
The principal minors are $a_{11} = 1$, $a_{22} = 1$ and $\det A = 0$, all nonnegative, so the test for semidefiniteness passes.

The null space of $A$ is spanned by $(1, -1)$, the vector of step 3.
This is general: a positive semidefinite matrix is positive definite exactly when its null space is $\{0\}$.
If we add $\varepsilon I$ for any $\varepsilon > 0$, the eigenvalues become $\varepsilon$ and $2 + \varepsilon$, and the matrix becomes positive definite.

## Explanations

### L1 human

This matrix never gives a negative number $x^{\mathsf{T}} A x$, because the number is the square $(x_1 + x_2)^2$.
But it gives $0$ at the nonzero vector $(1, -1)$.
So the matrix is semidefinite, and not definite.

### L2 human

The graph of $(x_1 + x_2)^2$ is a valley with a flat floor along the line $x_1 + x_2 = 0$, not a bowl with a single lowest point.
That flat floor is the null space of $A$, and it is why the matrix is singular.
Watch out: a singular positive semidefinite matrix has no Cholesky factor with a positive diagonal, since such a factor would be invertible.
It still has factorizations $A = LL^{\mathsf{T}}$ with $L$ lower triangular, such as $L = \begin{pmatrix} 1 & 0 \\ 1 & 0 \end{pmatrix}$.
