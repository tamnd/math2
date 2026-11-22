---
tag: DRW0DE4TM2
kind: example
name: A shear of the plane is a transvection
msc: ["15A23"]
topics: [P8J6QR66TJ]
audience: school
instance_of: [0DTCBCKEJP]
uses: [0NMN00FNW1, 032Q9FB8MT, 0CCQV3884B]
sources:
  - url: https://en.wikipedia.org/wiki/Shear_mapping
    locator: Definition
---

## Example

The horizontal shear by $3$ is the [[transvection matrix|0NMN00FNW1]]
$$S = T_{12}(3) = \begin{pmatrix} 1 & 3 \\ 0 & 1 \end{pmatrix}, \qquad S \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} x + 3y \\ y \end{pmatrix}$$
over $\mathbb{R}$.
Each point moves parallel to the $x$-axis by $3$ times its height $y$, and the points of the $x$-axis, where $y = 0$, stay fixed.

The unit square goes to the parallelogram with corners
$$S(0, 0) = (0, 0), \quad S(1, 0) = (1, 0), \quad S(1, 1) = (4, 1), \quad S(0, 1) = (3, 1).$$
It has base $1$ and height $1$, so its area is $1$, which matches $\det S = 1 \cdot 1 - 3 \cdot 0 = 1$.

The shear in the opposite direction undoes $S$:
$$\begin{pmatrix} 1 & 3 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & -3 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & -3 + 3 \\ 0 & 1 \end{pmatrix} = I_2,$$
and the product in the other order is $I_2$ by the same computation, so $S^{-1} = T_{12}(-3)$.
Shearing twice by $3$ is shearing once by $6$:
$$S^2 = \begin{pmatrix} 1 & 3 + 3 \\ 0 & 1 \end{pmatrix} = T_{12}(6).$$

## Remarks

The last two computations are cases of the addition rule $T_{12}(a)\,T_{12}(b) = T_{12}(a + b)$, with $(a, b) = (3, -3)$ and $(3, 3)$.
If we change $3$ to any $c$, the shear moves points by $cy$, and $c = 0$ gives the identity.
The transpose $T_{21}(3) = \begin{pmatrix} 1 & 0 \\ 3 & 1 \end{pmatrix}$ is the vertical shear, which fixes the $y$-axis and moves points up by $3x$.

A shear keeps areas but not lengths or angles.
The side from $(0, 0)$ to $(0, 1)$ of the square, of length $1$, goes to the side from $(0, 0)$ to $(3, 1)$, of length $\sqrt{10}$, and the right angle at the origin is lost.

## Explanations

### L1 human

Push the top of a stack of paper sideways, and keep the bottom in place.
Each sheet moves in proportion to its height, and the stack keeps its volume.
This is what the matrix does to the plane.

### L2 human

The point is that a shear is invertible with determinant $1$, and its inverse is the shear by the same amount in the opposite direction.
A trap: since the shear keeps area, it is easy to think it keeps shape too, but the square becomes a slanted parallelogram.
