---
tag: ~e199abaf
kind: example
name: The square of the rotation by a right angle is minus the identity
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: school
instance_of: [032Q9FB8MT]
uses: [076JGP6R3T, 0CCQV3884B]
sources:
  - url: https://en.wikipedia.org/wiki/Rotation_matrix
    locator: In two dimensions
---

## Example

Let
$$R = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}.$$

1. $R(x, y)^{\mathsf{T}} = (-y, x)^{\mathsf{T}}$, by the [[matrix-vector product|0CCQV3884B]]. This turns the plane by $90^\circ$ counterclockwise.
2. By the [[product rule|076JGP6R3T]], $R^2 = \begin{pmatrix} 0 \cdot 0 + (-1) \cdot 1 & 0 \cdot (-1) + (-1) \cdot 0 \\ 1 \cdot 0 + 0 \cdot 1 & 1 \cdot (-1) + 0 \cdot 0 \end{pmatrix} = \begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix} = -I$.
3. Geometrically, two turns by $90^\circ$ are one turn by $180^\circ$, which is $v \mapsto -v$.
4. So $R^4 = (R^2)^2 = (-I)^2 = I$, and $R^3 = -R$.
5. Hence $R^{-1} = R^3 = -R = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$, the turn by $90^\circ$ clockwise.

## Remarks

The real matrix $R$ satisfies $R^2 = -I$, so it behaves like the imaginary unit $i$.
The matrices $aI + bR = \begin{pmatrix} a & -b \\ b & a \end{pmatrix}$ form a copy of the complex numbers inside the [[matrix ring|~de637a64]] $M_2(\mathbb{R})$.
No real number has square $-1$, but this real matrix does.

## Explanations

### L1 human

The matrix $R$ turns every vector by a quarter turn.
Doing it twice turns by a half turn, which points every vector the other way.
So $R$ times $R$ is $-I$.

### L2 human

Products of matrices compute composites of maps, and here the composite is easy to see geometrically.
The computation in step 2 confirms the picture.
