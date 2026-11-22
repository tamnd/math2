---
tag: HFW74NJ8G3
kind: example
name: Schur form of a real matrix with a repeated eigenvalue
msc: ["15A23", "15A18"]
topics: [3YM9EK6VMB]
audience: ug1
not_instance_of:
  - target: 07SQCNV233
    note: the eigenvalue 3 has algebraic multiplicity 2 but its eigenspace is the line spanned by (1, 1), so A is not diagonalizable
  - target: 0C8BR8XRTR
    note: the Schur form has the nonzero entry 4 above the diagonal, so A is not normal
illustrates: [V1JG4C7R7B]
uses: [0QRBVFJ50X, 0N4XY7Z3NN, 0XYKE8BE7X]
sources:
  - url: https://en.wikipedia.org/wiki/Schur_decomposition
    locator: Statement
  - book: isbn:9783031410253
    locator: Chapter 6
---

## Example

Let $A = \begin{pmatrix} 1 & 2 \\ -2 & 5 \end{pmatrix}$ act on $\mathbb{R}^2$ with the dot product.
We find an [[orthogonal matrix|0QRBVFJ50X]] $Q$ for which $Q^{\mathsf{T}} A Q$ is [[upper triangular|0N4XY7Z3NN]], although $A$ cannot be diagonalized.

1. The characteristic polynomial is $(1 - t)(5 - t) + 4 = t^2 - 6t + 9 = (t - 3)^2$. So $3$ is the only eigenvalue, with algebraic multiplicity $2$.
2. The matrix $A - 3I = \begin{pmatrix} -2 & 2 \\ -2 & 2 \end{pmatrix}$ has rank $1$, and its kernel is the line spanned by $(1, 1)$. So the eigenspace is one line, and $A$ has no basis of eigenvectors.
3. Take the unit eigenvector $q_1 = \tfrac{1}{\sqrt{2}}(1, 1)$ and the unit vector $q_2 = \tfrac{1}{\sqrt{2}}(-1, 1)$ orthogonal to it. The matrix $Q = \tfrac{1}{\sqrt{2}} \begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix}$ with these columns has $Q^{\mathsf{T}} Q = I$.
4. The first column of $Q^{\mathsf{T}} A Q$ comes from $A q_1 = 3 q_1$, so its entries are $q_1^{\mathsf{T}} A q_1 = 3$ and $q_2^{\mathsf{T}} A q_1 = 0$.
5. For the second column, $A(-1, 1) = (-1 + 2, 2 + 5) = (1, 7)$, so $A q_2 = \tfrac{1}{\sqrt{2}}(1, 7)$. Then $q_1^{\mathsf{T}} A q_2 = \tfrac{1}{2}(1 + 7) = 4$ and $q_2^{\mathsf{T}} A q_2 = \tfrac{1}{2}(-1 + 7) = 3$.
6. Putting the four entries together gives
$$Q^{\mathsf{T}} A Q = \begin{pmatrix} 3 & 4 \\ 0 & 3 \end{pmatrix}.$$

Check: the triangular matrix has trace $6$ and determinant $9$, and so does $A$, since $1 + 5 = 6$ and $5 + 4 = 9$.

## Remarks

The diagonal holds the eigenvalue $3$ twice, as [[the Schur decomposition|V1JG4C7R7B]] says, and the eigenvalues of this real matrix are real, so the real Schur form is a genuine triangle with no $2 \times 2$ blocks.

The entry $4$ cannot be removed by any orthogonal or unitary change of basis.
Such a change keeps the sum of the squares of the absolute values of all entries, and here that sum is $1 + 4 + 4 + 25 = 34$ for $A$.
A Schur form has $3$ and $3$ on the diagonal, so the entry above the diagonal has absolute value $\sqrt{34 - 18} = 4$ in every Schur form.
Because this entry is not $0$, the matrix $A$ is not a [[normal matrix|0XYKE8BE7X]].
A direct check agrees:
$$A A^{\mathsf{T}} = \begin{pmatrix} 5 & 8 \\ 8 & 29 \end{pmatrix}, \qquad A^{\mathsf{T}} A = \begin{pmatrix} 5 & -8 \\ -8 & 29 \end{pmatrix}.$$

The Schur form is not unique.
With $q_2 = \tfrac{1}{\sqrt{2}}(1, -1)$ in place of $\tfrac{1}{\sqrt{2}}(-1, 1)$, the entry above the diagonal changes sign, and the Schur form becomes $\begin{pmatrix} 3 & -4 \\ 0 & 3 \end{pmatrix}$.
If you change the entry $-2$ of $A$ to $2$, the matrix becomes symmetric, with eigenvalues $3 \pm 2\sqrt{2}$, and then the Schur form is diagonal.

## Explanations

### L1 human

This matrix has only one stretch factor, $3$, and only one special direction, the direction of $(1, 1)$.
So no choice of axes makes it a pure stretch along each axis.
In a turned pair of perpendicular axes, its table of numbers becomes a triangle, with $3$ twice on the diagonal.
The number $4$ in the corner shows that the matrix also shears the plane.

### L2 human

The recipe for a $2 \times 2$ real matrix with real eigenvalues has three steps.
First find one eigenvalue and a unit eigenvector $q_1$.
Then turn $q_1$ by a right angle to get $q_2$.
Last compute the four numbers $q_i^{\mathsf{T}} A q_j$, where the entry $q_2^{\mathsf{T}} A q_1$ is $0$ because $A q_1$ is a multiple of $q_1$.
For this matrix the recipe needed one eigenvector and four dot products, and no inverse matrix, since $Q^{-1} = Q^{\mathsf{T}}$.
Watch out: the result is triangular, not diagonal, and the method works also for matrices that cannot be diagonalized.
