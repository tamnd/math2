---
tag: B1N13NEAJQ
kind: example
name: The plane through three points by the cross product
msc: ["51N20", "97G70"]
topics: [VKVAJ94SKZ]
audience: school
instance_of: [07SDJ5DNE4]
uses: [07SDJ5DNE4, 0N5N15HWZ7, 0S52TNNTH9]
sources:
  - url: https://en.wikipedia.org/wiki/Euclidean_planes_in_three-dimensional_space
    locator: Describing a plane through three points
---

## Example

Three points not on one line fix a plane, and the cross product of two edges turns them into an equation.
Let $A = (1, 0, 0)$, $B = (0, 2, 0)$ and $C = (0, 0, 3)$.
We find the [[equation of the plane|07SDJ5DNE4]] through $A$, $B$ and $C$.

1. Two directions in the plane are the edges from $A$:
   $$u = B - A = (-1, 2, 0), \qquad v = C - A = (-1, 0, 3).$$
2. The [[cross product|0N5N15HWZ7]] gives a normal:
   $$n = u \times v = (2 \cdot 3 - 0 \cdot 0, \; 0 \cdot (-1) - (-1) \cdot 3, \; (-1) \cdot 0 - 2 \cdot (-1)) = (6, 3, 2).$$
3. Check with the [[dot product|0S52TNNTH9]]: $n \cdot u = -6 + 6 + 0 = 0$ and $n \cdot v = -6 + 0 + 6 = 0$.
4. The constant is $d = n \cdot A = 6$, so the plane is $6x + 3y + 2z = 6$.
5. Check the other two points: $B$ gives $0 + 6 + 0 = 6$ and $C$ gives $0 + 0 + 6 = 6$.
6. The same plane in parametric form is $r = (1, 0, 0) + s(-1, 2, 0) + t(-1, 0, 3)$.

## Remarks

Dividing by $6$ gives the intercept form
$$\frac{x}{1} + \frac{y}{2} + \frac{z}{3} = 1,$$
which shows the three points where the plane crosses the axes; that is no accident, since $A$, $B$ and $C$ were chosen on the axes.

The equation also tells the two sides of the plane apart.
The point $(1, 2, 3)$ gives $6 + 6 + 6 = 18$, which is more than $6$, so it lies on the side into which $n$ points.
And the normal carries one more fact: $\|n\| = 7$ is the area of the parallelogram on $u$ and $v$, so the triangle $ABC$ has area $\tfrac{7}{2}$, as in the [[area example|Q6QW96GXK3]].

## Explanations

### L1 human

Three points that are not on one line fix a plane, like a three-legged stool on a floor.
Two arrows from $A$ lie in the plane, and their cross product sticks straight out of it.
That arrow, $(6, 3, 2)$, gives the left side of the equation, and the point $A$ gives the right side.

### L2 human

The method has three moves: two edge vectors from one point, their cross product as the normal, and then $d = n \cdot A$.
The checks in steps 3 and 5 catch most arithmetic errors, and they cost only a few multiplications.
Watch out: if the three points lie on one line, the cross product in step 2 is $0$, and there is no single plane to find.
