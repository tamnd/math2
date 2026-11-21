---
tag: AW7Q0F3M8J
kind: example
name: Rotations in space are not vectors
msc: ["51N20", "97G70"]
topics: [VKVAJ94SKZ]
audience: ug1
not_instance_of:
  - target: 0QN3D80AWP
    note: a rotation has a size and an axis, but the composition of two rotations depends on their order, while the sum of two vectors does not
uses: [0QN3D80AWP]
sources:
  - url: https://en.wikipedia.org/wiki/Euclidean_vector
    locator: Generalizations
  - url: https://en.wikipedia.org/wiki/Rotation_matrix
    locator: Basic 3D rotations
---

## Example

A rotation of space about an axis through the origin has a size, its angle, and a direction, its axis.
So it looks like a quantity with a size and a direction, the informal description of a [[vector|0QN3D80AWP]].
We show that rotations do not combine the way vectors add, because the result of two rotations depends on their order.

1. Let $R_x$ be the quarter turn about the $x$-axis, $R_x(x, y, z) = (x, -z, y)$. It sends $(0, 1, 0)$ to $(0, 0, 1)$, so it turns the $y$-axis into the $z$-axis.
2. Let $R_y$ be the quarter turn about the $y$-axis, $R_y(x, y, z) = (z, y, -x)$. It sends $(0, 0, 1)$ to $(1, 0, 0)$, so it turns the $z$-axis into the $x$-axis.
3. Apply $R_x$ first and then $R_y$ to $e_1 = (1, 0, 0)$. The first turn fixes $e_1$, since it lies on the axis, and the second turn gives
   $$R_y(R_x(e_1)) = R_y(1, 0, 0) = (0, 0, -1).$$
4. Apply $R_y$ first and then $R_x$ to $e_1$:
   $$R_x(R_y(e_1)) = R_x(0, 0, -1) = (0, 1, 0).$$
5. The results $(0, 0, -1)$ and $(0, 1, 0)$ differ, so the result of the two rotations depends on their order.
6. Vector addition does not depend on the order, because $u + v = v + u$. So no rule of the form "rotation plus rotation" can be the vector sum.

## Remarks

"A size and a direction" is not enough to make a vector.
A vector quantity must also combine with others by the parallelogram rule, and in particular in either order.
For small angles the two orders give almost the same result, and the difference shrinks faster than the angles do.
That is why angular velocity, which describes rotation over a very short time, is a vector, while a finite rotation is not.

## Explanations

### L1 human

Hold a book flat, turn it a quarter turn forward, and then a quarter turn to the side.
Start again, and do the two turns in the other order.
The book ends in a different position.
Moves along vectors never do this: 3 steps east and then 4 steps north end at the same place as 4 steps north and then 3 steps east.

### L2 human

The formulas in steps 1 and 2 come from the right-hand rule: with the thumb along the positive $x$-axis, the fingers turn the $y$-axis toward the $z$-axis.
The check in steps 3 and 4 needs only the substitution of numbers into these formulas.
Watch out: a quantity with a size and a direction is a vector only when it also combines by vector addition, and order-dependent quantities such as rotations fail that test.
