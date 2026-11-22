---
tag: X7MB7BJTSZ
kind: example
name: Left and right eigenvectors of a triangular matrix
msc: ["15A18"]
topics: [6R1D6QPY3S]
audience: ug2
instance_of: [32M8VY9A1M]
uses: [32M8VY9A1M, 0B5H4208Z9, 039HF58KQ5, 0K1KKMFHYH]
sources:
  - url: https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors
    locator: Left and right eigenvectors
---

## Example

Let $A = \begin{pmatrix} 1 & 1 \\ 0 & 2 \end{pmatrix}$ over $\mathbb{R}$.
We find its eigenvalues, its right and [[left eigenvectors|32M8VY9A1M]], and we check that the two kinds pair up as biorthogonality says.

1. The matrix $tI - A$ is upper triangular, so by the [[determinant of a triangular matrix|0K1KKMFHYH]]
$$p_A(t) = \det \begin{pmatrix} t - 1 & -1 \\ 0 & t - 2 \end{pmatrix} = (t - 1)(t - 2).$$
   Check with trace and determinant: $\operatorname{tr} A = 3$ and $\det A = 2$ give $t^2 - 3t + 2$, the same polynomial.
2. Right [[eigenvectors|0B5H4208Z9]]: the first column says $A(1, 0)^{\mathsf{T}} = (1, 0)^{\mathsf{T}}$, and
$$A \begin{pmatrix} 1 \\ 1 \end{pmatrix} = \begin{pmatrix} 1 + 1 \\ 0 + 2 \end{pmatrix} = 2 \begin{pmatrix} 1 \\ 1 \end{pmatrix}.$$
3. Left eigenvectors: a row $y = (y_1, y_2)$ is multiplied with the columns of $A$, so $yA = (y_1, \; y_1 + 2y_2)$.
   For $\lambda = 1$ we need $y_1 + 2y_2 = y_2$, so $y_2 = -y_1$ and $y = (1, -1)$; for $\lambda = 2$ we need $y_1 = 2y_1$, so $y_1 = 0$ and $y = (0, 1)$.
   Check: $(1, -1)A = (1, -1)$ and $(0, 1)A = (0, 2) = 2(0, 1)$.
4. Biorthogonality: a left eigenvector and a right eigenvector of different eigenvalues have product $0$:
$$(1, -1) \begin{pmatrix} 1 \\ 1 \end{pmatrix} = 0, \qquad (0, 1) \begin{pmatrix} 1 \\ 0 \end{pmatrix} = 0.$$
   The pairs with the same eigenvalue give $(1, -1)(1, 0)^{\mathsf{T}} = 1$ and $(0, 1)(1, 1)^{\mathsf{T}} = 1$.
5. Let $S = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$, with the right eigenvectors as columns.
   Then $S^{-1} = \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix}$, whose rows are the left eigenvectors of step 3, and step 4 is the equation $S^{-1} S = I$.
6. Check the diagonalization:
$$S^{-1} A = \begin{pmatrix} 1 & -1 \\ 0 & 2 \end{pmatrix}, \qquad S^{-1} A S = \begin{pmatrix} 1 & -1 \\ 0 & 2 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 2 \end{pmatrix}.$$

## Remarks

For the same eigenvalue, the left and right eigenvectors differ: for $1$ they are $(1, -1)$ and $(1, 0)^{\mathsf{T}}$.
They would agree up to transpose if $A$ were symmetric, and the entry $1$ above the diagonal is what breaks the symmetry; the [[right eigenvector that is not a left eigenvector|RQ2FE7RVVZ]] looks at that failure directly.

Change the corner entry from $1$ to a number $c$.
The right eigenvector for $2$ becomes $(c, 1)^{\mathsf{T}}$, and the left eigenvector for $1$ becomes $(1, -c)$, so their product $c - c$ is still $0$.
For $c = 0$ the matrix is diagonal and both kinds of eigenvectors are the standard ones.

## Explanations

### L1 human

A left eigenvector is a row that the matrix only stretches when the row stands to the left of the matrix.
For this matrix the rows $(1, -1)$ and $(0, 1)$ do that, while the columns that work are $(1, 0)$ and $(1, 1)$.
So the left and the right eigenvectors are different.
But each left eigenvector has product zero with the right eigenvector of the other eigenvalue.

### L2 human

Step 5 is the practical shortcut.
Once you have the right eigenvectors as the columns of $S$ and $S^{-1}AS$ is diagonal, the left eigenvectors are the rows of $S^{-1}$, and no second system needs to be solved.
The reason is that $S^{-1}AS = D$ gives $S^{-1}A = DS^{-1}$, which says row by row that row $i$ of $S^{-1}$ times $A$ is $d_i$ times row $i$.
Watch out: transposing the columns of $S$ gives the rows $(1, 0)$ and $(1, 1)$, which are not left eigenvectors, since $(1, 0)A = (1, 1)$.
