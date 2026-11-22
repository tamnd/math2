---
tag: W9GA3QFG24
kind: example
name: Composites of a rotation and a reflection of the plane
msc: ["15A04"]
topics: [9080WQTZ3M]
audience: ug1
instance_of: [00BKRZKMSS]
uses: [05YBKMRVAR, FSXBBV9C76, 076JGP6R3T]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_map
    locator: Definition and first consequences
  - url: https://en.wikipedia.org/wiki/Transformation_matrix
    locator: Composing and inverting transformations
---

## Example

A quarter turn and a flip of the plane give two different results in the two orders, so this pair is the smallest picture of a non-commutative composition.
Let $R$ be the rotation of $\R^2$ by a right angle and $S$ the reflection in the $x$-axis, with matrices
$$A = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}, \qquad B = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}.$$
By the [[theorem on composites|FSXBBV9C76]], $R \circ S$ has matrix $AB$ and $S \circ R$ has matrix $BA$.

1. The first row of $AB$ is $(0 \cdot 1 + (-1) \cdot 0, \; 0 \cdot 0 + (-1)(-1)) = (0, 1)$, and the second row is $(1 \cdot 1 + 0 \cdot 0, \; 1 \cdot 0 + 0 \cdot (-1)) = (1, 0)$.
2. So $AB = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$, which swaps the two coordinates, and this is the reflection in the line $y = x$.
3. The first row of $BA$ is $(1 \cdot 0 + 0 \cdot 1, \; 1 \cdot (-1) + 0 \cdot 0) = (0, -1)$, and the second row is $(0 \cdot 0 + (-1) \cdot 1, \; 0 \cdot (-1) + (-1) \cdot 0) = (-1, 0)$.
4. So $BA = \begin{pmatrix} 0 & -1 \\ -1 & 0 \end{pmatrix}$, which sends $(x, y)$ to $(-y, -x)$, and this is the reflection in the line $y = -x$.
5. As a direct check on $e_1 = (1, 0)$, we get $(R \circ S)(e_1) = R(1, 0) = (0, 1)$ and $(S \circ R)(e_1) = S(0, 1) = (0, -1)$.

So $R \circ S \ne S \circ R$, and the order of composition matters.

## Remarks

Both composites are reflections, and this is no accident.
A rotation has determinant $1$ and a reflection has determinant $-1$, so each composite has determinant $1 \cdot (-1) = -1$, and every linear map of the plane that keeps lengths and has determinant $-1$ is a reflection.

What changes if both maps are rotations?
Two rotations about the origin, by angles $\alpha$ and $\beta$, give the rotation by $\alpha + \beta$ in either order, so they commute.
A non-commuting pair in the plane therefore needs at least one map that is not a rotation.

The two maps also satisfy $S \circ S = \id$ and $R^4 = \id$.
Together they generate the symmetry group of the square, which has $8$ elements: four rotations and four reflections.

## Explanations

### L1 human

Flip the plane over the $x$-axis and then turn it a quarter turn: the point $(1, 0)$ ends at $(0, 1)$.
Turn first and then flip: the same point ends at $(0, -1)$.
So the order of two linear maps changes the result.

### L2 human

Each composite can be found in two ways, and doing both is a good habit.
One way multiplies the matrices, as in steps 1 to 4.
The other follows $e_1$ and $e_2$ through both maps: for $S \circ R$, the vector $e_2$ turns to $(-1, 0)$, and the flip leaves it at $(-1, 0)$, which is the second column of $BA$.
Watch out: $R \circ S$ means "first $S$", because the map on the right acts first.
