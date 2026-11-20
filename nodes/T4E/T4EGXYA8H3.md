---
tag: T4EGXYA8H3
kind: example
name: The symmetric and skew-symmetric parts of a 2 × 2 matrix
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: ug1
instance_of: [0PBY4E9GQF]
illustrates: [K284W6D15Z]
uses: [03RNVFDEAN, 0N28QN4CYA]
sources:
  - url: https://en.wikipedia.org/wiki/Symmetric_matrix
    locator: Decomposition into symmetric and skew-symmetric
---

## Example

Let $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ over $\mathbb{Q}$, so $A^{\mathsf{T}} = \begin{pmatrix} 1 & 3 \\ 2 & 4 \end{pmatrix}$.

1. $A + A^{\mathsf{T}} = \begin{pmatrix} 2 & 5 \\ 5 & 8 \end{pmatrix}$, so $S = \tfrac12 (A + A^{\mathsf{T}}) = \begin{pmatrix} 1 & 5/2 \\ 5/2 & 4 \end{pmatrix}$.
2. $A - A^{\mathsf{T}} = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$, so $K = \tfrac12 (A - A^{\mathsf{T}}) = \begin{pmatrix} 0 & -1/2 \\ 1/2 & 0 \end{pmatrix}$.
3. $S$ is [[symmetric|0N28QN4CYA]], and $K$ is [[skew-symmetric|03RNVFDEAN]] with zero diagonal.
4. Entry by entry, $S + K = \begin{pmatrix} 1 + 0 & 5/2 - 1/2 \\ 5/2 + 1/2 & 4 + 0 \end{pmatrix} = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} = A$.

## Remarks

The [[decomposition theorem|K284W6D15Z]] says that no other pair works.
For $x = (x_1, x_2)$, $x^{\mathsf{T}} A x = x_1^2 + 5 x_1 x_2 + 4 x_2^2 = x^{\mathsf{T}} S x$.
So the skew part $K$ contributes nothing to the quadratic form.

## Explanations

### L1 human

The symmetric part averages the two mirror entries $2$ and $3$ to get $5/2$.
The skew part keeps the difference, $\pm 1/2$, with opposite signs.

### L2 human

The diagonal of $A$ goes entirely into $S$, because a skew-symmetric matrix over $\mathbb{Q}$ has zero diagonal.
The entries $1/2$ show why the theorem needs $2$ to be invertible.
