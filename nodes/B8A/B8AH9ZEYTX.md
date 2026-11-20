---
tag: B8AH9ZEYTX
kind: example
name: The scalar matrix 3I commutes with every 2 × 2 matrix
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: school
instance_of: [067NKSBEWT]
uses: [0FRM62SG7D, 076JGP6R3T]
sources:
  - url: https://en.wikipedia.org/wiki/Diagonal_matrix
    locator: Scalar matrix
---

## Example

Let $S = 3I_2 = \begin{pmatrix} 3 & 0 \\ 0 & 3 \end{pmatrix}$, a [[scalar matrix|0FRM62SG7D]], and let $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$ be any real matrix.

1. By the [[product rule|076JGP6R3T]], $SA = \begin{pmatrix} 3a + 0c & 3b + 0d \\ 0a + 3c & 0b + 3d \end{pmatrix} = \begin{pmatrix} 3a & 3b \\ 3c & 3d \end{pmatrix} = 3A$.
2. In the same way, $AS = \begin{pmatrix} 3a & 3b \\ 3c & 3d \end{pmatrix} = 3A$.
3. So $SA = AS$ for every $A$.
4. For $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$, both products are $\begin{pmatrix} 3 & 6 \\ 9 & 12 \end{pmatrix}$.
5. As a map, $S$ sends $(x, y)^{\mathsf{T}}$ to $(3x, 3y)^{\mathsf{T}}$, a stretch by the factor $3$.

## Remarks

The products in steps 1 and 2 are the scalar multiple $3A$, so the matrix $3I$ and the number $3$ act in the same way.
Only scalar matrices have this property, by the [[lemma on matrix units|TX4J5JR205]].

## Explanations

### L1 human

Multiplying by $3I$ triples every entry, whether we multiply on the left or on the right.
So the order does not matter for this matrix.

### L2 human

A stretch by the same factor in all directions commutes with every linear map.
A stretch by different factors in different directions does not, as the [[diagonal non-example|RGEJG5KD95]] shows.
