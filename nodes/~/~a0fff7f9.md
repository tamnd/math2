---
tag: ~a0fff7f9
kind: example
name: Orthogonal diagonalization of a symmetric 2 × 2 matrix
msc: ["15A18", "15B57"]
topics: [3YM9EK6VMB]
audience: ug1
instance_of: [0NEGN5CRSC]
illustrates: [06J4PXRG22, 0DGZBQWZWN, 0JHGAV9H25, ~e55cbc04]
uses: [0N28QN4CYA, 0QRBVFJ50X, 0Q8HZTJC7G]
sources:
  - url: https://en.wikipedia.org/wiki/Spectral_theorem
    locator: Hermitian maps and Hermitian matrices
  - book: isbn:9780134860244
    locator: Section 6.4
---

## Example

Let $A = \begin{pmatrix} 5 & 2 \\ 2 & 2 \end{pmatrix}$ act on $\mathbb{R}^2$ with the dot product.
The matrix is [[symmetric|0N28QN4CYA]].

1. The characteristic polynomial is $(5 - t)(2 - t) - 4 = t^2 - 7t + 6 = (t - 6)(t - 1)$. So the eigenvalues are $6$ and $1$.
2. For $6$: $A (2, 1) = (10 + 2, 4 + 2) = (12, 6) = 6 \cdot (2, 1)$.
3. For $1$: $A (1, -2) = (5 - 4, 2 - 4) = (1, -2)$.
4. The dot product $(2, 1) \cdot (1, -2) = 2 - 2 = 0$, so the eigenvectors are orthogonal. Both have length $\sqrt{5}$.
5. Let $Q = \tfrac{1}{\sqrt{5}} \begin{pmatrix} 2 & 1 \\ 1 & -2 \end{pmatrix}$. Its columns are orthonormal, so $Q$ is an [[orthogonal matrix|0QRBVFJ50X]], and $Q^T A Q = \begin{pmatrix} 6 & 0 \\ 0 & 1 \end{pmatrix}$.
6. The [[orthogonal projections|0Q8HZTJC7G]] onto the two eigenlines are $P_1 = \tfrac{1}{5} \begin{pmatrix} 4 & 2 \\ 2 & 1 \end{pmatrix}$ and $P_2 = \tfrac{1}{5} \begin{pmatrix} 1 & -2 \\ -2 & 4 \end{pmatrix}$.
7. Then $P_1 + P_2 = I$, $P_1 P_2 = 0$, and $6 P_1 + P_2 = \tfrac{1}{5} \begin{pmatrix} 25 & 10 \\ 10 & 10 \end{pmatrix} = A$.

## Remarks

- Step 7 is [[the spectral decomposition|~e55cbc04]] $A = 6 P_1 + 1 \cdot P_2$.
- Functions of $A$ act on the eigenvalues. For example, $A^2 = 36 P_1 + P_2 = \begin{pmatrix} 29 & 14 \\ 14 & 8 \end{pmatrix}$, and $\sqrt{6}\, P_1 + P_2$ is a symmetric matrix whose square is $A$.
- The projection $P_1$ is a polynomial in $A$: $P_1 = \tfrac{1}{5}(A - I)$, because $A - I$ kills the eigenvector for $1$.
- With $y = Q^T x$, the quadratic form is $5 x_1^2 + 4 x_1 x_2 + 2 x_2^2 = 6 y_1^2 + y_2^2$. So its level curves are ellipses with axes along $(2, 1)$ and $(1, -2)$.

## Explanations

### L1 human

This matrix stretches the direction $(2, 1)$ by $6$ and keeps the direction $(1, -2)$.
The two directions are perpendicular, as for every symmetric matrix.
In coordinates along these two directions, the matrix is $\operatorname{diag}(6, 1)$.

### L2 human

The recipe for a real symmetric matrix:

1. Find the eigenvalues from the characteristic polynomial.
2. Find one eigenvector for each eigenvalue, and check that they are orthogonal.
3. Divide each eigenvector by its length, and put them as the columns of $Q$.
4. Then $Q^T A Q$ is diagonal, with the eigenvalues in the order of the columns.

A trap: without step 3, the matrix with the columns $(2, 1)$ and $(1, -2)$ satisfies $P^T P = 5I$, not $I$.
