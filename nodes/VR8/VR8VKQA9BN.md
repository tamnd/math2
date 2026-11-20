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

Let $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$, so $A^{\mathsf{T}} = \begin{pmatrix} 1 & 3 \\ 2 & 4 \end{pmatrix}$.
The matrix $A$ is not symmetric.

1. $A^{\mathsf{T}} A = \begin{pmatrix} 1 \cdot 1 + 3 \cdot 3 & 1 \cdot 2 + 3 \cdot 4 \\ 2 \cdot 1 + 4 \cdot 3 & 2 \cdot 2 + 4 \cdot 4 \end{pmatrix} = \begin{pmatrix} 10 & 14 \\ 14 & 20 \end{pmatrix}$.
2. $A A^{\mathsf{T}} = \begin{pmatrix} 1 \cdot 1 + 2 \cdot 2 & 1 \cdot 3 + 2 \cdot 4 \\ 3 \cdot 1 + 4 \cdot 2 & 3 \cdot 3 + 4 \cdot 4 \end{pmatrix} = \begin{pmatrix} 5 & 11 \\ 11 & 25 \end{pmatrix}$.
3. $A + A^{\mathsf{T}} = \begin{pmatrix} 2 & 5 \\ 5 & 8 \end{pmatrix}$.
4. Each of the three matrices has equal entries at $(1, 2)$ and $(2, 1)$, so each is [[symmetric|0N28QN4CYA]].
5. $A^{\mathsf{T}} A \neq A A^{\mathsf{T}}$, so the two constructions give different matrices.

## Remarks

The general reason is the [[transpose of a product|09GK5PS824]]: $(A^{\mathsf{T}} A)^{\mathsf{T}} = A^{\mathsf{T}} (A^{\mathsf{T}})^{\mathsf{T}} = A^{\mathsf{T}} A$.
Also $(A + A^{\mathsf{T}})^{\mathsf{T}} = A^{\mathsf{T}} + A$.
The diagonal of $A^{\mathsf{T}} A$ holds the squared lengths $10$ and $20$ of the columns of $A$.
The off-diagonal entry $14$ is the dot product of the two columns.

## Explanations

### L1 human

Every matrix gives symmetric matrices when we multiply it by its transpose or add its transpose.
The computed entries show the mirror pattern across the diagonal.

### L2 human

The entries of $A^{\mathsf{T}} A$ are the dot products of the columns of $A$, and a dot product does not depend on the order.
This matrix is the Gram matrix of the columns, used in least squares.
