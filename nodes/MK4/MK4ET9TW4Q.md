---
tag: MK4ET9TW4Q
kind: example
name: Orthogonal diagonalization of a symmetric 2 × 2 matrix
msc: ["15A18", "15B57"]
topics: [3YM9EK6VMB]
audience: ug1
instance_of: [0NEGN5CRSC]
illustrates: [06J4PXRG22, 0DGZBQWZWN, 0JHGAV9H25, D5KVBA1K9R]
uses: [0N28QN4CYA, 0QRBVFJ50X, 0Q8HZTJC7G]
sources:
  - url: https://en.wikipedia.org/wiki/Spectral_theorem
    locator: Hermitian maps and Hermitian matrices
  - book: isbn:9780134860244
    locator: Section 6.4
---

## Example

Let $A = \begin{pmatrix} 5 & 2 \\ 2 & 2 \end{pmatrix}$ act on $\mathbb{R}^2$ with the dot product.
The matrix is [[symmetric|0N28QN4CYA]], so the map $x \mapsto Ax$ is self-adjoint, and we find an orthogonal matrix that makes it diagonal.

1. The eigenvalues. Expand the characteristic polynomial:
$$\det(A - tI) = (5 - t)(2 - t) - 2 \cdot 2 = t^2 - 7t + 6 = (t - 6)(t - 1).$$
So the eigenvalues are $6$ and $1$, with the sum $7 = 5 + 2$, the trace, and the product $6 = 10 - 4$, the determinant.
2. An eigenvector for $6$. The matrix $A - 6I$ has the rows $(-1, 2)$ and $(2, -4)$, so its kernel is spanned by $(2, 1)$. Check: $A(2, 1) = (10 + 2, 4 + 2) = (12, 6) = 6 \cdot (2, 1)$.
3. An eigenvector for $1$. The matrix $A - I$ has the rows $(4, 2)$ and $(2, 1)$, so its kernel is spanned by $(1, -2)$. Check: $A(1, -2) = (5 - 4, 2 - 4) = (1, -2)$.
4. Orthogonality. The dot product is $(2, 1) \cdot (1, -2) = 2 - 2 = 0$, and both vectors have length $\sqrt{5}$.
5. The orthogonal matrix. Divide each vector by $\sqrt{5}$ and use the results as columns:
$$Q = \frac{1}{\sqrt{5}} \begin{pmatrix} 2 & 1 \\ 1 & -2 \end{pmatrix}, \qquad Q^{\mathsf{T}} A Q = \begin{pmatrix} 6 & 0 \\ 0 & 1 \end{pmatrix}.$$
The columns are orthonormal, so $Q$ is an [[orthogonal matrix|0QRBVFJ50X]] and $Q^{-1} = Q^{\mathsf{T}}$.
6. The projections. The [[orthogonal projections|0Q8HZTJC7G]] onto the two eigenlines are $P_1 = \tfrac{1}{5} (2, 1)^{\mathsf{T}} (2, 1)$ and $P_2 = \tfrac{1}{5} (1, -2)^{\mathsf{T}} (1, -2)$:
$$P_1 = \frac{1}{5} \begin{pmatrix} 4 & 2 \\ 2 & 1 \end{pmatrix}, \qquad P_2 = \frac{1}{5} \begin{pmatrix} 1 & -2 \\ -2 & 4 \end{pmatrix}.$$
7. The decomposition. Adding gives $P_1 + P_2 = I$, multiplying gives $P_1 P_2 = 0$, and
$$6 P_1 + 1 \cdot P_2 = \frac{1}{5} \begin{pmatrix} 24 + 1 & 12 - 2 \\ 12 - 2 & 6 + 4 \end{pmatrix} = \begin{pmatrix} 5 & 2 \\ 2 & 2 \end{pmatrix} = A.$$

## Remarks

Steps 2 to 5 are the [[real spectral theorem|06J4PXRG22]] at work, and step 4 is an instance of [[orthogonality of eigenspaces|0JHGAV9H25]].
Step 7 is the [[spectral decomposition|D5KVBA1K9R]] $A = 6 P_1 + P_2$.
Since a real symmetric matrix is Hermitian, the same $Q$ is also a unitary diagonalization in the sense of the [[spectral theorem for Hermitian matrices|0DGZBQWZWN]].

The decomposition makes functions of $A$ easy.
Squaring acts on the eigenvalues only, so
$$A^2 = 36 P_1 + P_2 = \frac{1}{5} \begin{pmatrix} 145 & 70 \\ 70 & 40 \end{pmatrix} = \begin{pmatrix} 29 & 14 \\ 14 & 8 \end{pmatrix},$$
which agrees with the direct product, whose first entry is $25 + 4 = 29$.
In the same way $\sqrt{6}\, P_1 + P_2$ is a symmetric matrix whose square is $A$.
The projection is even a polynomial in $A$: $P_1 = \tfrac{1}{5}(A - I)$, because $A - I$ kills the eigenvector for $1$ and multiplies the eigenvector for $6$ by $5$.

The quadratic form shows the geometry.
In the coordinates $y = Q^{\mathsf{T}} x$, the form $5 x_1^2 + 4 x_1 x_2 + 2 x_2^2$ becomes $6 y_1^2 + y_2^2$, so its level curves are ellipses with axes along $(2, 1)$ and $(1, -2)$.
If you change the off-diagonal entry $2$ to some other number $c$, the eigenvectors turn, but they stay perpendicular, because the matrix stays symmetric.

## Explanations

### L1 human

This matrix stretches the direction $(2, 1)$ by a factor of $6$ and leaves the direction $(1, -2)$ as it is.
The two directions are perpendicular, as they are for every symmetric matrix.
In coordinates along these two directions, the matrix is simply the diagonal matrix with entries $6$ and $1$.

### L2 human

The example follows a recipe that works for every real symmetric matrix.
First find the eigenvalues from the characteristic polynomial, then one eigenvector for each eigenvalue, and check that the eigenvectors are orthogonal.
Then divide each eigenvector by its length and put them as the columns of $Q$, and $Q^{\mathsf{T}} A Q$ is diagonal with the eigenvalues in the order of the columns.
Watch out for the normalization.
Without it, the matrix $P$ with the columns $(2, 1)$ and $(1, -2)$ satisfies $P^{\mathsf{T}} P = 5I$, not $I$, and $P^{\mathsf{T}} A P = \operatorname{diag}(30, 5)$.
