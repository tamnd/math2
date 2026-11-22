---
tag: RQ2FE7RVVZ
kind: example
name: A right eigenvector that is not a left eigenvector
msc: ["15A18"]
topics: [6R1D6QPY3S]
audience: ug2
not_instance_of:
  - target: 32M8VY9A1M
    note: "The row vector (1, 0) is the transpose of a right eigenvector of A, but (1, 0)A = (1, 1) is not a multiple of (1, 0)"
uses: [32M8VY9A1M, 0B5H4208Z9]
sources:
  - url: https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors
    locator: Left and right eigenvectors
---

## Example

Let $A = \begin{pmatrix} 1 & 1 \\ 0 & 2 \end{pmatrix}$, the matrix of [[left and right eigenvectors of a triangular matrix|X7MB7BJTSZ]].
We show that the transpose of a right eigenvector of $A$ need not be a [[left eigenvector|32M8VY9A1M]].

1. The first column of $A$ is $(1, 0)^{\mathsf{T}}$, so
$$A \begin{pmatrix} 1 \\ 0 \end{pmatrix} = \begin{pmatrix} 1 \\ 0 \end{pmatrix},$$
   and $(1, 0)^{\mathsf{T}}$ is a right [[eigenvector|0B5H4208Z9]] for the eigenvalue $1$.
2. Now put the transposed row $(1, 0)$ on the left of $A$.
   Each entry of the product is the row times a column of $A$:
$$(1, 0) A = (1 \cdot 1 + 0 \cdot 0, \; 1 \cdot 1 + 0 \cdot 2) = (1, 1).$$
3. A left eigenvector would need $(1, 0)A = \lambda (1, 0) = (\lambda, 0)$ for some $\lambda$.
   The second entry of $(1, 1)$ is $1 \ne 0$, so no $\lambda$ works, and $(1, 0)$ is not a left eigenvector of $A$.
4. The left eigenvector for $1$ is $(1, -1)$ instead, since $(1, -1)A = (1, \; 1 - 2) = (1, -1)$.

## Remarks

The left eigenvectors of $A$ are the transposes of the right eigenvectors of $A^{\mathsf{T}}$, not of $A$.
Here $A^{\mathsf{T}} = \begin{pmatrix} 1 & 0 \\ 1 & 2 \end{pmatrix}$, and indeed $A^{\mathsf{T}}(1, -1)^{\mathsf{T}} = (1, -1)^{\mathsf{T}}$.
The failure comes from the entry $1$ above the diagonal.
If we replace it by $0$, the matrix becomes $\operatorname{diag}(1, 2)$, which is symmetric, and then $(1, 0)$ is both a right and a left eigenvector.
For every real symmetric matrix the two kinds agree up to transpose, because $A^{\mathsf{T}} = A$.

## Explanations

### L1 human

A row placed to the left of a matrix is combined with the columns of the matrix, not with its rows.
So a column that the matrix only stretches can turn into a row that the matrix turns.
Here the column $(1, 0)$ is only stretched, by the factor $1$, while the row $(1, 0)$ becomes $(1, 1)$.

### L2 human

The lesson is to compute left eigenvectors from $A^{\mathsf{T}}$, or from $y(A - \lambda I) = 0$, and never by transposing right eigenvectors.
Watch out: for a symmetric matrix the shortcut gives the right answer, which makes the habit easy to pick up and wrong for every matrix like this one.
