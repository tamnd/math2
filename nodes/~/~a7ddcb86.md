---
tag: ~a7ddcb86
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

Let $S = T_{12}(3) = \begin{pmatrix} 1 & 3 \\ 0 & 1 \end{pmatrix}$ over $\mathbb{R}$, a [[transvection matrix|0NMN00FNW1]].

1. $S(x, y)^{\mathsf{T}} = (x + 3y, \; y)^{\mathsf{T}}$. Each point moves parallel to the $x$-axis by $3$ times its height $y$.
2. Points of the $x$-axis are fixed: $S(x, 0)^{\mathsf{T}} = (x, 0)^{\mathsf{T}}$.
3. $\det S = 1 \cdot 1 - 3 \cdot 0 = 1$, so areas are kept. The unit square goes to the parallelogram with corners $(0, 0)$, $(1, 0)$, $(4, 1)$ and $(3, 1)$, which has base $1$ and height $1$.
4. The inverse is $T_{12}(-3) = \begin{pmatrix} 1 & -3 \\ 0 & 1 \end{pmatrix}$. Check: $\begin{pmatrix} 1 & 3 \\ 0 & 1 \end{pmatrix}\begin{pmatrix} 1 & -3 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & -3 + 3 \\ 0 & 1 \end{pmatrix} = I_2$, and the product in the other order is $I_2$ by the same computation.
5. $S^2 = T_{12}(6)$: $\begin{pmatrix} 1 & 3 \\ 0 & 1 \end{pmatrix}^2 = \begin{pmatrix} 1 & 3 + 3 \\ 0 & 1 \end{pmatrix}$.

## Remarks

The example shows the law $T_{12}(a) T_{12}(b) = T_{12}(a + b)$ in steps 4 and 5.
If we change $3$ to $c$, then the shear moves points by $c y$, and $c = 0$ gives the identity.
The transpose $T_{21}(3) = \begin{pmatrix} 1 & 0 \\ 3 & 1 \end{pmatrix}$ is the vertical shear that fixes the $y$-axis.

## Explanations

### L1 human

Push the top of a stack of paper sideways, and keep the bottom in place.
Each sheet moves in proportion to its height, and the stack keeps its volume.
This is what the matrix does to the plane.

### L2 human

The point is that a shear is invertible with determinant $1$, and its inverse is the shear in the opposite direction.
A trap: the shear does not keep lengths or angles, only areas.
