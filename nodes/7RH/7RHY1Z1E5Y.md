---
tag: 7RHY1Z1E5Y
kind: example
name: The transpose of a 2 × 3 matrix and the rules of the transpose
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: school
instance_of: [09DXWYRD43]
uses: [0W809K6AW0, 0BVXADM10P]
sources:
  - url: https://en.wikipedia.org/wiki/Transpose
    locator: Properties
---

## Example

Let
$$A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{pmatrix}, \qquad B = \begin{pmatrix} 0 & 1 & 0 \\ 2 & 0 & -1 \end{pmatrix}$$
over $\mathbb{R}$.
We compute a transpose and check the three linear rules of the transpose with numbers.

1. By the [[definition|0W809K6AW0]], $(A^{\mathsf{T}})_{ij} = a_{ji}$, so
$$A^{\mathsf{T}} = \begin{pmatrix} 1 & 4 \\ 2 & 5 \\ 3 & 6 \end{pmatrix},$$
a $3 \times 2$ matrix whose column 2 is row 2 of $A$, namely $(4, 5, 6)$.
2. Transposing again turns the columns of $A^{\mathsf{T}}$ back into rows, so $(A^{\mathsf{T}})^{\mathsf{T}} = A$.
3. The [[sum|0BVXADM10P]] is $A + B = \begin{pmatrix} 1 & 3 & 3 \\ 6 & 5 & 5 \end{pmatrix}$, so
$$(A + B)^{\mathsf{T}} = \begin{pmatrix} 1 & 6 \\ 3 & 5 \\ 3 & 5 \end{pmatrix}.$$
4. Transposing first and then adding gives the same matrix:
$$A^{\mathsf{T}} + B^{\mathsf{T}} = \begin{pmatrix} 1 & 4 \\ 2 & 5 \\ 3 & 6 \end{pmatrix} + \begin{pmatrix} 0 & 2 \\ 1 & 0 \\ 0 & -1 \end{pmatrix} = \begin{pmatrix} 1 & 6 \\ 3 & 5 \\ 3 & 5 \end{pmatrix}.$$
5. For a scalar multiple,
$$(2A)^{\mathsf{T}} = \begin{pmatrix} 2 & 4 & 6 \\ 8 & 10 & 12 \end{pmatrix}^{\mathsf{T}} = \begin{pmatrix} 2 & 8 \\ 4 & 10 \\ 6 & 12 \end{pmatrix} = 2A^{\mathsf{T}}.$$

## Remarks

The product $AB$ is not defined, because $A$ has 3 columns and $B$ has 2 rows.
But $AB^{\mathsf{T}}$ is a $2 \times 3$ matrix times a $3 \times 2$ matrix, and
$$AB^{\mathsf{T}} = \begin{pmatrix} 2 & -1 \\ 5 & 2 \end{pmatrix}, \qquad BA^{\mathsf{T}} = \begin{pmatrix} 2 & 5 \\ -1 & 2 \end{pmatrix}.$$
The second matrix is the transpose of the first, as the [[transpose of a product|09GK5PS824]] predicts: $(AB^{\mathsf{T}})^{\mathsf{T}} = (B^{\mathsf{T}})^{\mathsf{T}} A^{\mathsf{T}} = BA^{\mathsf{T}}$.

The rules in steps 3 to 5 hold because the transpose only moves entries, and adding or scaling entries does not care where they sit.
They make the transpose a linear map from the $2 \times 3$ matrices to the $3 \times 2$ matrices, and step 2 shows that this map is a bijection.

## Explanations

### L1 human

The rows of $A$ become the columns of $A^{\mathsf{T}}$.
Adding two matrices and then flipping gives the same result as flipping each one and then adding.
Doubling and then flipping is the same as flipping and then doubling.

### L2 human

The typical use of these rules is to simplify an expression before you compute it.
For example, $(3A - B)^{\mathsf{T}} = 3A^{\mathsf{T}} - B^{\mathsf{T}}$, and its entry $(1, 2)$ is $3 a_{21} - b_{21} = 3 \cdot 4 - 2 = 10$.
Watch out: the size changes, so you can add $A^{\mathsf{T}}$ to another $3 \times 2$ matrix, but not to $A$ itself.
