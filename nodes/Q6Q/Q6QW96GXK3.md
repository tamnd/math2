---
tag: Q6QW96GXK3
kind: example
name: Area of a triangle in space by the cross product
msc: ["15A72", "51N20", "97G70"]
topics: [VKVAJ94SKZ]
audience: school
instance_of: [0N5N15HWZ7]
illustrates: [SAZ353S8W0]
uses: [0N5N15HWZ7, 0XKBKGTCPC]
sources:
  - url: https://en.wikipedia.org/wiki/Cross_product
    locator: Geometric meaning
---

## Example

Let $A = (1, 0, 0)$, $B = (0, 2, 0)$ and $C = (0, 0, 3)$, the points where a plane meets the three axes.
We compute the area of the triangle $ABC$ with the [[cross product|0N5N15HWZ7]].

1. Two sides from $A$ are $u = B - A = (-1, 2, 0)$ and $v = C - A = (-1, 0, 3)$.
2. The first component of $u \times v$ is $2 \cdot 3 - 0 \cdot 0 = 6$.
3. The second component is $0 \cdot (-1) - (-1) \cdot 3 = 3$.
4. The third component is $(-1) \cdot 0 - 2 \cdot (-1) = 2$.
5. So $u \times v = (6, 3, 2)$, and its [[length|0XKBKGTCPC]] is $\sqrt{36 + 9 + 4} = \sqrt{49} = 7$.
6. By the [[length formula|SAZ353S8W0]], $7$ is the area of the parallelogram on $u$ and $v$.
7. The triangle is half of this parallelogram, so its area is $\tfrac{7}{2}$.

## Remarks

The vector $(6, 3, 2)$ is also a normal vector of the plane through $A$, $B$ and $C$, which is $6x + 3y + 2z = 6$.

The components have a meaning of their own.
The shadows of the triangle on the three coordinate planes are right triangles with areas
$$\tfrac{1}{2} \cdot 2 \cdot 3 = 3, \qquad \tfrac{1}{2} \cdot 1 \cdot 3 = \tfrac{3}{2}, \qquad \tfrac{1}{2} \cdot 1 \cdot 2 = 1,$$
which are half the components $6$, $3$ and $2$.
So Lagrange's sum of squares becomes a Pythagorean theorem for areas: $3^2 + (\tfrac{3}{2})^2 + 1^2 = \tfrac{49}{4} = (\tfrac{7}{2})^2$.

Any two sides of the triangle give the same length.
For example, $(C - B) \times (A - B)$ equals $(6, 3, 2)$ again, and reversing the order only flips the sign.

## Explanations

### L1 human

A triangle that floats in space is hard to measure with a ruler.
The cross product of two sides gives an arrow whose length is twice the area of the triangle.
Here the arrow is $(6, 3, 2)$ with length $7$, so the triangle has area $3.5$.

### L2 human

The method works for any three points in space: take two side vectors, compute their cross product, and halve its length.
The remark on the shadows is a three-dimensional Pythagorean theorem for areas.
Watch out: the cross product must be taken of side vectors such as $B - A$, not of the position vectors $A$ and $B$.
Here $A \times B = (0, 0, 2)$, which has nothing to do with the area of $ABC$.
