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
$$A = \begin{pmatrix} 1 & 2 & 3 \\ 0 & 4 & 5 \\ 0 & 0 & 6 \end{pmatrix}, \qquad B = \begin{pmatrix} 2 & 0 & 1 \\ 0 & 1 & -1 \\ 0 & 0 & 3 \end{pmatrix}$$
over $\mathbb{R}$.
Both have zeros in the three positions $(2, 1)$, $(3, 1)$ and $(3, 2)$, so both are [[upper triangular|0MKABWDRNC]].
We compute $AB$ row by row with the [[product rule|076JGP6R3T]], taking row $i$ of $A$ against each column of $B$.

1. Row 1 of $A$ is $(1, 2, 3)$:
$$\bigl(1 \cdot 2,\ 1 \cdot 0 + 2 \cdot 1,\ 1 \cdot 1 + 2 \cdot (-1) + 3 \cdot 3\bigr) = (2, 2, 8).$$
2. Row 2 of $A$ is $(0, 4, 5)$:
$$\bigl(0,\ 4 \cdot 1,\ 4 \cdot (-1) + 5 \cdot 3\bigr) = (0, 4, 11).$$
3. Row 3 of $A$ is $(0, 0, 6)$, which gives $(0, 0, 6 \cdot 3) = (0, 0, 18)$.
4. So
$$AB = \begin{pmatrix} 2 & 2 & 8 \\ 0 & 4 & 11 \\ 0 & 0 & 18 \end{pmatrix},$$
which is upper triangular.
5. The diagonal of $AB$ is $(2, 4, 18) = (1 \cdot 2, 4 \cdot 1, 6 \cdot 3)$, the products of the diagonal entries in the same places, as the [[product theorem|45RET2Y995]] says.

## Remarks

The diagonal entries are simple, but the entries above the diagonal are not.
The entry $8$ uses three terms, $1 \cdot 1 + 2 \cdot (-1) + 3 \cdot 3$, and it depends on entries of $A$ and $B$ off the diagonal.

In the other order, $BA$ is also upper triangular with the same diagonal $(2, 4, 18)$.
Its entry $(1, 3)$ is $2 \cdot 3 + 0 \cdot 5 + 1 \cdot 6 = 12$, which is not $8$, so $AB \neq BA$.
Triangular matrices do not commute in general, even though their diagonals do.

The example also shows a case of the product rule for determinants.
The [[determinant of a triangular matrix|0K1KKMFHYH]] is the product of its diagonal, so $\det A = 24$, $\det B = 6$ and $\det(AB) = 2 \cdot 4 \cdot 18 = 144 = 24 \cdot 6$.

## Explanations

### L1 human

Both matrices have zeros below the diagonal, and so does their product.
To get the diagonal of the product you only need to multiply the diagonals: $1 \cdot 2$, $4 \cdot 1$ and $6 \cdot 3$.

### L2 human

Why are the three entries below the diagonal of $AB$ zero?
Take $(AB)_{21} = 0 \cdot 2 + 4 \cdot 0 + 5 \cdot 0$: row 2 of $A$ starts with a zero, and column 1 of $B$ is zero below its top entry, so every term has a zero factor.
The same thing happens in each position below the diagonal.
The typical use is a quick check of a hand computation: if a product of upper triangular matrices has a nonzero entry below the diagonal, there is an error.
