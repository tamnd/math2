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

The trace of $A^{\mathsf{T}} B$ multiplies matching entries of $A$ and $B$ and adds the products, so it is the dot product of the two matrices.
Let
$$A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}, \qquad B = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}.$$
The Frobenius inner product is $\langle A, B \rangle_F = \operatorname{tr}(A^{\mathsf{T}} B)$.

1. The [[transpose|0W809K6AW0]] is $A^{\mathsf{T}} = \begin{pmatrix} 1 & 3 \\ 2 & 4 \end{pmatrix}$, and the [[product|076JGP6R3T]] is
$$A^{\mathsf{T}} B = \begin{pmatrix} 1 & 3 \\ 2 & 4 \end{pmatrix} \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 3 & 1 \\ 4 & 2 \end{pmatrix}.$$
2. By the [[definition of the trace|07PTPSZPME]], $\operatorname{tr}(A^{\mathsf{T}} B) = 3 + 2 = 5$.
3. The sum of the products of matching entries is the same number:
$$1 \cdot 0 + 2 \cdot 1 + 3 \cdot 1 + 4 \cdot 0 = 5.$$
4. In general, $(A^{\mathsf{T}} B)_{jj} = \sum_i (A^{\mathsf{T}})_{ji} b_{ij} = \sum_i a_{ij} b_{ij}$, and summing over $j$ gives
$$\operatorname{tr}(A^{\mathsf{T}} B) = \sum_{i,j} a_{ij} b_{ij}.$$
5. Let $C = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$. Then $\langle B, C \rangle_F = 0 \cdot 0 + 1 \cdot 1 + 1 \cdot (-1) + 0 \cdot 0 = 0$, so the symmetric $B$ and the skew-symmetric $C$ are orthogonal.

## Remarks

### What the formula says

Step 4 shows that $\langle A, B \rangle_F$ is the dot product of $A$ and $B$ written as vectors in $\mathbb{R}^{n^2}$.
So the Frobenius inner product is an inner product on $M_n(\mathbb{R})$, and $\langle A, A \rangle_F$ is the square of the [[Frobenius norm|JT8Q204E4R]].
For $A$ above, $\langle A, A \rangle_F = 1 + 4 + 9 + 16 = 30$.
The same formula works for $m \times n$ matrices, since $A^{\mathsf{T}} B$ is then square of order $n$.

### Symmetric and skew-symmetric parts

Step 5 is a case of a general fact.
If $S$ is [[symmetric|0VR671PHE5]] and $K$ is [[skew-symmetric|0PBY4E9GQF]], then $\operatorname{tr}(SK) = \operatorname{tr}((SK)^{\mathsf{T}}) = \operatorname{tr}(K^{\mathsf{T}} S^{\mathsf{T}}) = -\operatorname{tr}(KS) = -\operatorname{tr}(SK)$, so $\langle S, K \rangle_F = \operatorname{tr}(SK) = 0$.
Every real square matrix is a symmetric matrix plus a skew-symmetric one, so the two subspaces are orthogonal complements for this inner product.

## Explanations

### L1 human

Multiply the matching entries of two matrices of the same size and add the products.
The trace of $A^{\mathsf{T}} B$ gives exactly this number.
It is the dot product you already know, with the entries of each matrix read off as one long list.

### L2 human

The trace turns the matrix product into an inner product on the space of matrices.
This inner product does not change when both matrices are multiplied on the left by the same orthogonal matrix $Q$, because
$$\langle QA, QB \rangle_F = \operatorname{tr}(A^{\mathsf{T}} Q^{\mathsf{T}} Q B) = \operatorname{tr}(A^{\mathsf{T}} B).$$
On the right it also does not change, since $\operatorname{tr}(Q^{\mathsf{T}} A^{\mathsf{T}} B Q) = \operatorname{tr}(A^{\mathsf{T}} B Q Q^{\mathsf{T}}) = \operatorname{tr}(A^{\mathsf{T}} B)$ by the cyclic property.
