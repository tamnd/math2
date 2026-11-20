---
tag: Z88VRHAS1X
kind: example
name: The Frobenius inner product of two 2 × 2 matrices
msc: ["15A15", "15A63"]
topics: [Y1ESNQ2V52]
audience: ug1
instance_of: [0XC1RDBY7A]
uses: [07PTPSZPME, 0W809K6AW0, 076JGP6R3T]
sources:
  - url: https://en.wikipedia.org/wiki/Frobenius_inner_product
    locator: lead section
---

## Example

Let $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ and $B = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$.
The Frobenius inner product is $\langle A, B \rangle_F = \operatorname{tr}(A^{\mathsf{T}} B)$.

1. $A^{\mathsf{T}} B = \begin{pmatrix} 1 & 3 \\ 2 & 4 \end{pmatrix} \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 3 & 1 \\ 4 & 2 \end{pmatrix}$.
2. By the [[definition|07PTPSZPME]], $\operatorname{tr}(A^{\mathsf{T}} B) = 3 + 2 = 5$.
3. The sum of the entrywise products is $1 \cdot 0 + 2 \cdot 1 + 3 \cdot 1 + 4 \cdot 0 = 5$, the same number.
4. In general, $(A^{\mathsf{T}} B)_{jj} = \sum_i a_{ij} b_{ij}$, so $\operatorname{tr}(A^{\mathsf{T}} B) = \sum_{i,j} a_{ij} b_{ij}$.
5. Let $C = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$. Then $\langle B, C \rangle_F = 0 + 1 - 1 + 0 = 0$, so the symmetric $B$ and the skew-symmetric $C$ are orthogonal.

## Remarks

Step 4 shows that $\langle A, B \rangle_F$ is the dot product of $A$ and $B$ written as vectors in $\mathbb{R}^{n^2}$.
So the Frobenius inner product is an inner product on $M_n(\mathbb{R})$, and $\langle A, A \rangle_F$ is the square of the [[Frobenius norm|JT8Q204E4R]].
Step 5 is a case of a general fact: the [[symmetric|0VR671PHE5]] and the [[skew-symmetric|0PBY4E9GQF]] matrices are orthogonal complements for this inner product.

## Explanations

### L1 human

Multiply the matching entries of two matrices of the same size and add the products.
The trace of $A^{\mathsf{T}} B$ gives exactly this number.

### L2 human

The trace turns the matrix product into an inner product on the space of matrices.
This inner product does not change when both matrices are multiplied by the same orthogonal matrix.
