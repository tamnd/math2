---
tag: KC7XFCE6T1
kind: example
name: Sums and multiples of two linear maps of the plane
msc: ["15A04"]
topics: [9080WQTZ3M]
audience: ug1
instance_of: [0X9MBPP2Z3]
uses: [0VPCJWGMP9, 0RJF668P1T, 0YQSGNYE3K]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_map
    locator: Vector space of linear maps
  - url: https://en.wikipedia.org/wiki/Transformation_matrix
    locator: Examples in 2 dimensions
---

## Example

Adding a quarter turn of the plane to a doubling gives a new linear map, whose matrix is the sum of the two matrices.
Let $R, S \colon \R^2 \to \R^2$ be the rotation by $90°$ and the scaling by $2$,
$$R(x, y) = (-y, \; x), \qquad S(x, y) = (2x, \; 2y).$$
Both are [[linear maps|0RJF668P1T]], with matrices $A_R = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ and $A_S = \begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix}$.

1. By the [[definition of the operations|0VPCJWGMP9]], $(R + S)(x, y) = (-y, x) + (2x, 2y) = (2x - y, \; x + 2y)$.
2. So $R + S$ is the map $v \mapsto Bv$ with $B = \begin{pmatrix} 2 & -1 \\ 1 & 2 \end{pmatrix}$, which is linear.
3. We have $B = A_R + A_S$, so the [[matrix|0YQSGNYE3K]] of the sum is the sum of the matrices.
4. The multiple $3R$ is $(x, y) \mapsto (-3y, \; 3x)$, with matrix $3A_R$.
5. The difference $R - R$ is the zero map, the zero vector of $\Hom(\R^2, \R^2)$.

Check at $(1, 1)$: $R(1, 1) = (-1, 1)$ and $S(1, 1) = (2, 2)$ have sum $(1, 3)$, and $B(1, 1)^{\mathsf T} = (2 - 1, \; 1 + 2) = (1, 3)$.

## Remarks

The matrix $B$ has the form $\begin{pmatrix} a & -b \\ b & a \end{pmatrix}$ with $a = 2$ and $b = 1$, so $R + S$ is a rotation followed by a scaling.
The scaling factor is $\sqrt{a^2 + b^2} = \sqrt 5$, and the angle is $\arctan(1/2)$.

The composite $R \circ S$ is a different map, $(R \circ S)(x, y) = R(2x, 2y) = (-2y, \; 2x)$, with matrix $A_R A_S$, not $A_R + A_S$.
If we replace $S$ by $-S$, we get $(R - S)(x, y) = (-2x - y, \; x - 2y)$, which is again linear.

## Explanations

### L1 human

Rotate a vector by a quarter turn, and separately double it.
Adding the two results gives a new map of the plane.
It is again linear, and its matrix is the sum of the two matrices.

### L2 human

The example shows the vector space operations of $\Hom(\R^2, \R^2)$ in coordinates.
Sums of maps correspond to sums of matrices, and multiples to multiples.
Watch out: the composite of two maps corresponds to the product of their matrices, not to the sum.
