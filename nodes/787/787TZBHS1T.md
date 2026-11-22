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
It turns each vector of the plane a quarter turn counterclockwise, because $A(x_1, x_2)^{\mathsf{T}} = (-x_2, x_1)^{\mathsf{T}}$; for example $(1, 0)$ goes to $(0, 1)$.
Let $B = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$, the quarter turn clockwise.

1. Multiply row by column:
$$AB = \begin{pmatrix} 0 \cdot 0 + (-1)(-1) & 0 \cdot 1 + (-1) \cdot 0 \\ 1 \cdot 0 + 0 \cdot (-1) & 1 \cdot 1 + 0 \cdot 0 \end{pmatrix} = I_2.$$
2. In the other order:
$$BA = \begin{pmatrix} 0 \cdot 0 + 1 \cdot 1 & 0 \cdot (-1) + 1 \cdot 0 \\ (-1) \cdot 0 + 0 \cdot 1 & (-1)(-1) + 0 \cdot 0 \end{pmatrix} = I_2.$$
3. By steps 1 and 2 and the [[definition|0TWTS88TWN]], $A$ is invertible and $A^{-1} = B$.
4. Two quarter turns make a half turn: $A^2 = \begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix} = -I_2$.
5. So $A^3 = A^2 A = -A = B$ and $A^4 = (-I_2)^2 = I_2$, which means three quarter turns counterclockwise also undo one.

## Remarks

The inverse $B$ equals $-A$, and it also equals the transpose $A^{\mathsf{T}}$.
The second fact holds for every rotation matrix, because rotations keep lengths and angles; such matrices are the orthogonal matrices of the sub-area on [[isometries|AZS5BPF5H3]].
The example also shows that an inverse can be a power of the matrix: here $A^{-1} = A^3$ because $A^4 = I_2$.

If we replace the entry $-1$ by $0$, the matrix becomes $\begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}$, which sends $(0, 1)$ to $(0, 0)$ and is singular.

## Explanations

### L1 human

Turning a picture a quarter turn to the left is undone by turning it a quarter turn to the right.
The matrices of the two turns are inverses of each other.
Four quarter turns to the left bring the picture back, so three turns to the left also undo one turn.

### L2 human

The point of the example is that a matrix with zeros on its diagonal can still be invertible.
The test is the product with the candidate, not the look of the entries.
Watch out: the inverse is not the matrix of inverted entries, which here does not even exist because of the zero entries.
