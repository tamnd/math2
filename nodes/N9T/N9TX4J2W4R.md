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
All four entries of $A$ are positive, and $A$ is symmetric, but $A$ is not positive definite.
We check this in three ways.

1. The form at one vector. For $x = (1, -1)$ we get $Ax = (1 - 2, 2 - 1) = (-1, 1)$, so
$$x^{\mathsf{T}} A x = 1 \cdot (-1) + (-1) \cdot 1 = -2 < 0.$$
2. So $A$ is not [[positive semidefinite|0880F9EQCP]], and so it is not [[positive definite|0QQCG3JWJ4]] either.
3. The eigenvalues. The characteristic polynomial is
$$\det(A - tI) = (1 - t)^2 - 4 = t^2 - 2t - 3 = (t - 3)(t + 1),$$
so the eigenvalues are $3$ and $-1$.
The negative eigenvalue fails [[the eigenvalue test|0HYC2RHD3M]], and its eigenvector is $(1, -1)$, the vector of step 1.
4. The determinant. It is $1 \cdot 1 - 2 \cdot 2 = -3 < 0$, while a positive definite matrix has a positive determinant, as the product of its positive eigenvalues.

## Remarks

The off-diagonal entries are too large compared with the diagonal.
For a real symmetric $\begin{pmatrix} a & b \\ b & c \end{pmatrix}$, positive definiteness needs $a > 0$ and $ac > b^2$, and here $ac = 1 < 4 = b^2$.
If we shrink the off-diagonal entry to $b$ with $\abs{b} < 1$, the matrix becomes positive definite, and at $b = 1$ it is the semidefinite [[all-ones matrix|YAAQD2E1BZ]].

The converse fails too: a positive definite matrix can have negative entries, as [[the tridiagonal example|RSQW92W4PD]] with entries $-1$ shows.
Matrices with positive entries are called *positive matrices*, and they belong to Perron-Frobenius theory, a different subject with a similar name.

## Explanations

### L1 human

Positive entries do not make a matrix positive definite.
This matrix has the entries $1, 2, 2, 1$, all positive.
At the vector $(1, -1)$ it gives the number $1 - 2 - 2 + 1 = -2$, which is negative.

### L2 human

The words "positive matrix" and "positive definite matrix" name two different properties.
The first is about the entries, the second is about the values of the form $x^{\mathsf{T}} A x$.
A quick test for a $2 \times 2$ symmetric matrix is to compare the product of the diagonal entries with the square of the off-diagonal entry.
Here $1 \cdot 1 < 2^2$, so the form takes negative values, and $x = (1, -1)$ is a vector that shows it.
