---
tag: D96BEM2GMS
kind: example
name: There is no cross product on the plane
msc: ["15A72", "97G70"]
topics: [VKVAJ94SKZ]
audience: ug1
not_instance_of:
  - target: 0N5N15HWZ7
    note: on R^2 no product of two vectors can be perpendicular to both factors and have the parallelogram area as its length
uses: [0N5N15HWZ7, 0S52TNNTH9, 0XKBKGTCPC]
sources:
  - url: https://en.wikipedia.org/wiki/Seven-dimensional_cross_product
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Cross_product
    locator: Generalizations
---

## Example

Assume that an operation $\times$ on $\mathbb{R}^2$ has two properties of the [[cross product|0N5N15HWZ7]]: $u \times v$ is perpendicular to $u$ and to $v$, and $\|u \times v\|$ is the area of the parallelogram on $u$ and $v$.
We show that no such operation exists.

1. Let $u = (1, 0)$ and $v = (0, 1)$, and let $w = u \times v = (w_1, w_2)$.
2. Perpendicularity to $u$ gives $w \cdot u = w_1 = 0$, by the [[dot product|0S52TNNTH9]].
3. Perpendicularity to $v$ gives $w \cdot v = w_2 = 0$.
4. So $w = (0, 0)$, and its [[length|0XKBKGTCPC]] is $\|w\| = 0$.
5. The parallelogram on $u$ and $v$ is the unit square, with area $1$.
6. The second property requires $\|w\| = 1$, which contradicts step 4. So no such operation exists on $\mathbb{R}^2$.

## Remarks

The obstacle is a lack of room.
Two independent vectors of the plane already fill it, so the only vector perpendicular to both is $0$.
The same argument rules out, in every dimension $n \geq 2$, a product of $n$ independent vectors that is perpendicular to all of them and has their volume as its length.
For two factors in $\mathbb{R}^n$ with $n \geq 3$ the argument says nothing, because two vectors leave room for a perpendicular direction.
Still, a bilinear product of two vectors with both properties exists only in $\mathbb{R}^3$ and $\mathbb{R}^7$, apart from the trivial dimensions $0$ and $1$.

What the plane has instead is a number, the signed area $u_1 v_2 - u_2 v_1$.
It is the third component of $(u_1, u_2, 0) \times (v_1, v_2, 0)$.

## Explanations

### L1 human

In the plane, an arrow at a right angle to both the $x$-axis and the $y$-axis would have to stick out of the plane.
No arrow in the plane does this, except the zero arrow.
So the plane has no room for a cross product.
In space there is a third direction, and the cross product uses it.

### L2 human

To use the cross product for plane problems, add a third component $0$, sending $(u_1, u_2)$ to $(u_1, u_2, 0)$.
Then
$$u \times v = (0, 0, \; u_1 v_2 - u_2 v_1),$$
and its length is the area of the parallelogram in the plane.
Watch out: the result is a vector in space, pointing out of the plane, not a vector of the plane.
