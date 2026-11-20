---
tag: NFJP659QFK
kind: example
name: A product of two 3 × 3 upper triangular matrices
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: school
instance_of: [0N4XY7Z3NN]
illustrates: [45RET2Y995]
uses: [0MKABWDRNC, 076JGP6R3T]
sources:
  - url: https://en.wikipedia.org/wiki/Triangular_matrix
    locator: Properties
---

## Example

Let
$$A = \begin{pmatrix} 1 & 2 & 3 \\ 0 & 4 & 5 \\ 0 & 0 & 6 \end{pmatrix}, \qquad B = \begin{pmatrix} 2 & 0 & 1 \\ 0 & 1 & -1 \\ 0 & 0 & 3 \end{pmatrix}.$$
Both are [[upper triangular|0MKABWDRNC]].

1. Row 1 of $AB$: $(1 \cdot 2,\ 1 \cdot 0 + 2 \cdot 1,\ 1 \cdot 1 + 2 \cdot (-1) + 3 \cdot 3) = (2, 2, 8)$.
2. Row 2 of $AB$: $(0,\ 4 \cdot 1,\ 4 \cdot (-1) + 5 \cdot 3) = (0, 4, 11)$.
3. Row 3 of $AB$: $(0, 0, 6 \cdot 3) = (0, 0, 18)$.
4. So $AB = \begin{pmatrix} 2 & 2 & 8 \\ 0 & 4 & 11 \\ 0 & 0 & 18 \end{pmatrix}$, which is upper triangular.
5. The diagonal of $AB$ is $(2, 4, 18) = (1 \cdot 2, 4 \cdot 1, 6 \cdot 3)$, as the [[product theorem|45RET2Y995]] predicts.
6. The entries above the diagonal, such as $8$, depend on several entries of $A$ and $B$.

## Remarks

The product $BA$ is also upper triangular with the same diagonal $(2, 4, 18)$.
Its entry $(1, 3)$ is $2 \cdot 3 + 0 \cdot 5 + 1 \cdot 6 = 12 \neq 8$, so $AB \neq BA$.

## Explanations

### L1 human

The zeros below the diagonal stay zero in the product.
The diagonal of the product is found by multiplying the diagonals.

### L2 human

The determinant of $AB$ is $2 \cdot 4 \cdot 18 = 144 = 24 \cdot 6 = \det A \cdot \det B$.
For triangular matrices, this case of the multiplicativity of the [[determinant|0K1KKMFHYH]] follows from step 5.
