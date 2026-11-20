---
tag: MT2XRG51GF
kind: example
name: A linear equation whose solutions form a plane
msc: ["15A06"]
topics: [DXSXFVDMXQ]
audience: school
instance_of: [0Q3ZT8J05R]
uses: [0Q3ZT8J05R, 0V3XAMF3C1]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_equation
    locator: lead section
---

## Example

Consider the equation $x + 2y - z = 4$ over $\R$ in the unknowns $x, y, z$.
We check that it is a [[linear equation|0Q3ZT8J05R]] and describe its solutions.

1. The left side is $1 \cdot x + 2 \cdot y + (-1) \cdot z$, a sum of unknowns times real constants.
2. No unknown is squared and no two unknowns are multiplied, so the equation is linear with $a = (1, 2, -1)$ and $b = 4$.
3. The coefficient of $z$ is $-1 \ne 0$, so we solve for $z$: $z = x + 2y - 4$.
4. The unknowns $x$ and $y$ can take any values $s$ and $t$.
5. So the solutions are $(x, y, z) = (s, t, s + 2t - 4) = (0, 0, -4) + s(1, 0, 1) + t(0, 1, 2)$.
6. Check with $s = 1$, $t = 2$: the point is $(1, 2, 1)$, and $1 + 4 - 1 = 4$.
7. The solution set is the [[plane|0V3XAMF3C1]] through $(0, 0, -4)$ spanned by the directions $(1, 0, 1)$ and $(0, 1, 2)$.

## Remarks

The normal vector of this plane is the coefficient vector $(1, 2, -1)$.
Both direction vectors are perpendicular to it: $1 + 0 - 1 = 0$ and $0 + 2 - 2 = 0$.

## Explanations

### L1 human

One linear equation in three unknowns leaves two unknowns free.
We can choose $x$ and $y$ as we like, and then $z$ is fixed.
So the solutions make a flat sheet in space, a plane.

### L2 human

To find points on the plane quickly, pick easy values.

1. Take $x = 0$, $y = 0$: then $z = -4$, so $(0, 0, -4)$ is on the plane.
2. Take $x = 4$, $y = 0$: then $z = 0$, so $(4, 0, 0)$ is on the plane.
3. Take $x = 0$, $y = 2$: then $z = 0$, so $(0, 2, 0)$ is on the plane.

A trap: solving for $z$ needs its coefficient to be nonzero; if the equation were $x + 2y = 4$, you would solve for $x$ instead and $z$ would be free.
