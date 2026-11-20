---
tag: 787TZBHS1T
kind: example
name: The quarter turn is invertible
msc: ["15A09"]
topics: [P8J6QR66TJ]
audience: school
instance_of: [0EB9N0S33C]
uses: [0TWTS88TWN, 032Q9FB8MT, 06DW9BAWB1]
sources:
  - url: https://en.wikipedia.org/wiki/Rotation_matrix
    locator: In two dimensions
  - url: https://en.wikipedia.org/wiki/Invertible_matrix
    locator: Definition
---

## Example

Let $A = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ over $\mathbb{R}$.
The map $x \mapsto Ax$ turns each vector of the plane by a quarter turn counterclockwise: $A(x_1, x_2)^{\mathsf{T}} = (-x_2, x_1)^{\mathsf{T}}$.
Let $B = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$, the quarter turn clockwise.

1. $AB = \begin{pmatrix} 0 \cdot 0 + (-1)(-1) & 0 \cdot 1 + (-1) \cdot 0 \\ 1 \cdot 0 + 0 \cdot (-1) & 1 \cdot 1 + 0 \cdot 0 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I_2$.
2. $BA = \begin{pmatrix} 0 \cdot 0 + 1 \cdot 1 & 0 \cdot (-1) + 1 \cdot 0 \\ (-1) \cdot 0 + 0 \cdot 1 & (-1)(-1) + 0 \cdot 0 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I_2$.
3. By steps 1 and 2 and the [[definition|0TWTS88TWN]], $A$ is invertible and $A^{-1} = B$.
4. $A^2 = \begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix} = -I_2$, the half turn.
5. So $A^3 = A^2 A = -A = B$ and $A^4 = (-I_2)^2 = I_2$. The inverse is three quarter turns.

## Remarks

The inverse $B = -A$ is also the transpose $A^{\mathsf{T}}$.
This holds for each rotation matrix, because rotations keep lengths and angles; such matrices are the orthogonal matrices of the sub-area on [[isometries|AZS5BPF5H3]].
The example also shows that $A^{-1}$ can be a power of $A$: here $A^{-1} = A^3$, since $A^4 = I_2$.

## Explanations

### L1 human

Turning a picture a quarter turn to the left is undone by turning it a quarter turn to the right.
The matrices of the two turns are inverses of each other.
Four quarter turns to the left bring the picture back, so three turns to the left also undo one turn.

### L2 human

The point of the example is that a matrix with zeros on the diagonal can still be invertible.
The test is the product, not the look of the entries.
A trap: the inverse is not the matrix with each entry inverted, which here does not even exist because of the zero entries.
