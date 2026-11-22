---
tag: VR8VKQA9BN
kind: example
name: The symmetric matrices AᵀA, AAᵀ and A + Aᵀ for a 2 × 2 matrix
msc: ["15A99", "15B57"]
topics: [Y1ESNQ2V52]
audience: ug1
instance_of: [0VR671PHE5]
uses: [0N28QN4CYA, 09GK5PS824]
sources:
  - url: https://en.wikipedia.org/wiki/Symmetric_matrix
    locator: Properties
---

## Example

Let
$$A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}, \qquad A^{\mathsf{T}} = \begin{pmatrix} 1 & 3 \\ 2 & 4 \end{pmatrix}$$
over $\mathbb{R}$.
The matrix $A$ is not symmetric, since $a_{12} = 2$ and $a_{21} = 3$, but we build three symmetric matrices from it.

1. Multiply $A^{\mathsf{T}}$ by $A$:
$$A^{\mathsf{T}} A = \begin{pmatrix} 1 \cdot 1 + 3 \cdot 3 & 1 \cdot 2 + 3 \cdot 4 \\ 2 \cdot 1 + 4 \cdot 3 & 2 \cdot 2 + 4 \cdot 4 \end{pmatrix} = \begin{pmatrix} 10 & 14 \\ 14 & 20 \end{pmatrix}.$$
2. Multiply in the other order:
$$A A^{\mathsf{T}} = \begin{pmatrix} 1 \cdot 1 + 2 \cdot 2 & 1 \cdot 3 + 2 \cdot 4 \\ 3 \cdot 1 + 4 \cdot 2 & 3 \cdot 3 + 4 \cdot 4 \end{pmatrix} = \begin{pmatrix} 5 & 11 \\ 11 & 25 \end{pmatrix}.$$
3. Add $A$ and its transpose:
$$A + A^{\mathsf{T}} = \begin{pmatrix} 2 & 5 \\ 5 & 8 \end{pmatrix}.$$
4. In each of the three matrices the entries at $(1, 2)$ and $(2, 1)$ are equal, so each is [[symmetric|0N28QN4CYA]].
5. The matrices in steps 1 and 2 differ, so $A^{\mathsf{T}} A \neq A A^{\mathsf{T}}$.

## Remarks

The numbers follow a general argument with the [[transpose of a product|09GK5PS824]]:
$$(A^{\mathsf{T}} A)^{\mathsf{T}} = A^{\mathsf{T}} (A^{\mathsf{T}})^{\mathsf{T}} = A^{\mathsf{T}} A, \qquad (A + A^{\mathsf{T}})^{\mathsf{T}} = A^{\mathsf{T}} + A.$$
The same argument works for $A A^{\mathsf{T}}$, and for $A^{\mathsf{T}} A$ it needs no squareness: for an $m \times n$ matrix $A$, the matrix $A^{\mathsf{T}} A$ is a symmetric $n \times n$ matrix.

The entries of $A^{\mathsf{T}} A$ have a meaning.
Entry $(i, j)$ is the [[dot product|0S52TNNTH9]] of column $i$ and column $j$ of $A$, so the diagonal holds the squared lengths $1^2 + 3^2 = 10$ and $2^2 + 4^2 = 20$ of the columns, and the entry $14 = 1 \cdot 2 + 3 \cdot 4$ is the dot product of the two columns.
Both matrices have the same trace, $10 + 20 = 5 + 25 = 30$, which is the sum of the squares of all four entries of $A$.

## Explanations

### L1 human

Multiplying a matrix by its transpose, in either order, gives a symmetric matrix.
Adding a matrix to its transpose also gives a symmetric matrix.
The computed entries show the mirror pattern across the diagonal: $14$ and $14$, $11$ and $11$, $5$ and $5$.

### L2 human

The typical use is the matrix $A^{\mathsf{T}} A$ in least squares, where it is the Gram matrix of the columns of $A$.
Its symmetry is not a coincidence of the numbers: the dot product of column $i$ with column $j$ is the same as that of column $j$ with column $i$.
Watch out: $A^{\mathsf{T}} A$ and $A A^{\mathsf{T}}$ are usually different matrices, here with diagonals $(10, 20)$ and $(5, 25)$, and for a non-square $A$ they even have different sizes.
