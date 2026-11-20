---
tag: N9TX4J2W4R
kind: example
name: A matrix with positive entries that is not positive definite
msc: [15B57, 15B48]
topics: [SS4EVPKT3A]
audience: ug1
not_instance_of:
  - target: 0KX66CZMBB
    note: all entries are positive, but the form is -2 at (1, -1)
  - target: 01MMVW8CKC
    note: the form is negative at (1, -1), so the matrix is not even positive semidefinite
illustrates: [0HYC2RHD3M]
uses: [0QQCG3JWJ4, 0880F9EQCP]
sources:
  - url: https://en.wikipedia.org/wiki/Definite_matrix
    locator: Examples
---

## Example

Let $A = \begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix}$.
All entries of $A$ are positive, and $A$ is symmetric.

1. For $x = (1, -1)$, we get $Ax = (1 - 2, 2 - 1) = (-1, 1)$.
2. So $x^T A x = 1 \cdot (-1) + (-1) \cdot 1 = -2 < 0$.
3. So $A$ is not [[positive semidefinite|0880F9EQCP]], and so it is not [[positive definite|0QQCG3JWJ4]] either.
4. The characteristic polynomial is $(1 - t)^2 - 4 = (t - 3)(t + 1)$. The eigenvalues are $3$ and $-1$.
5. The eigenvalue $-1$ is negative, which agrees with [[the eigenvalue test|0HYC2RHD3M]]. Its eigenvector is $(1, -1)$, the vector of step 1.

## Remarks

- The determinant is $1 - 4 = -3 < 0$. A positive definite matrix has a positive determinant, so this also shows that $A$ is not positive definite.
- Matrices with positive entries are called positive matrices. They are the subject of the Perron-Frobenius theory, which is a different notion.
- The converse also fails: [[the tridiagonal example|RSQW92W4PD]] is positive definite and has negative entries.

## Explanations

### L1 human

Positive entries do not make a matrix positive definite.
This matrix has the entries $1, 2, 2, 1$.
At the vector $(1, -1)$ it gives the negative number $-2$.

### L2 human

The off-diagonal entries are large compared with the diagonal.
For a $2 \times 2$ symmetric matrix $\begin{pmatrix} a & b \\ b & c \end{pmatrix}$, positive definiteness needs $a > 0$ and $ac > b^2$.
Here $ac = 1 < 4 = b^2$, so the test fails.
A trap: "positive matrix" and "positive definite matrix" are two different notions with similar names.
