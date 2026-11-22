---
tag: 6CKAMR5WK9
kind: example
name: Equivalent matrices that are not similar
msc: ["15A21"]
topics: [P8J6QR66TJ]
audience: ug1
instance_of: [0CMHSGTWXB]
uses: [0P21AVFFSP, 0E89HQATM8, T2H2QV0M06]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_equivalence
---

## Example

A shear and the identity matrix are equivalent, because both are invertible, but they are not similar, because nothing except the identity is similar to the identity.
Let $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ and $B = I_2$ over $\mathbb{Q}$.
The matrix $A$ is invertible, with
$$A^{-1} = \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix}.$$
Check: $\begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix}\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 1 - 1 \\ 0 & 1 \end{pmatrix} = I_2$.

1. With $P = A^{-1}$ and $Q = I_2$, we get $PAQ = I_2 = B$. So $A$ and $B$ are [[equivalent|0P21AVFFSP]], in agreement with the [[rank normal form theorem|T2H2QV0M06]], since both have rank $2$.
2. Suppose that $A$ and $B$ are [[similar|0E89HQATM8]], so $A = S B S^{-1}$ for an invertible $S$.
3. Then $A = S I_2 S^{-1} = S S^{-1} = I_2$.
4. But $A \ne I_2$, because entry $(1, 2)$ of $A$ is $1$. So $A$ and $B$ are not similar.

## Remarks

### The general pattern

The only matrix similar to $I_n$ is $I_n$ itself, while each invertible $n \times n$ matrix is equivalent to $I_n$.
So among invertible matrices, equivalence has one class and similarity has many.

### Watch out

Matching invariants do not prove similarity.
Here $A$ and $I_2$ have the same trace $2$, the same determinant $1$ and the same eigenvalues $1, 1$, but they are still not similar; the argument in step 3 shows this directly.

### Try it

Are $\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ and $\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$ equivalent, and are they similar?
Answer: both have rank $1$, so they are equivalent.
They are not similar, because the first matrix squares to $0$ and the second squares to itself, and $(SXS^{-1})^2 = SX^2S^{-1}$ shows that similarity keeps both properties.

## Explanations

### L1 human

Equivalence uses two different invertible matrices, one on each side.
Similarity uses one matrix and its inverse.
So equivalence is a much weaker relation, and here it identifies two matrices that similarity keeps apart.

### L2 human

For square matrices, similarity keeps the trace, the determinant and the eigenvalues, while equivalence keeps only the rank.
To show that two matrices are not similar, find one property that similarity keeps and that the two matrices do not share, or argue directly as in step 3.
