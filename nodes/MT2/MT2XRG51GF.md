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

Consider the equation $x + 2y - z = 4$ over $\mathbb{R}$ in the unknowns $x, y, z$.
We check that it is a [[linear equation|0Q3ZT8J05R]], and then we describe all its solutions.

1. The left side is $1 \cdot x + 2 \cdot y + (-1) \cdot z$, a sum of unknowns times real constants. No unknown is squared and no two unknowns are multiplied, so the equation is linear with coefficient vector $a = (1, 2, -1)$ and constant term $b = 4$.
2. The coefficient of $z$ is $-1 \ne 0$, so we can solve for $z$. This gives $z = x + 2y - 4$.
3. The unknowns $x$ and $y$ can take any values $s$ and $t$, and then $z$ is fixed. So the solutions are
$$(x, y, z) = (s, t, s + 2t - 4) = (0, 0, -4) + s(1, 0, 1) + t(0, 1, 2).$$
4. Check with $s = 1$ and $t = 2$: the point is $(1, 2, 1)$, and $1 + 4 - 1 = 4$.
5. The two directions $(1, 0, 1)$ and $(0, 1, 2)$ are not multiples of each other. So the solution set is the [[plane|0V3XAMF3C1]] through $(0, 0, -4)$ with these two directions.

## Remarks

The example shows how one equation in three unknowns leaves two of them free, and two free unknowns give a plane.
The coefficient vector $(1, 2, -1)$ is a normal vector of this plane.
Both directions are perpendicular to it:
$$(1, 0, 1) \cdot (1, 2, -1) = 1 - 1 = 0, \qquad (0, 1, 2) \cdot (1, 2, -1) = 2 - 2 = 0.$$
If you change only the constant term $4$, the plane moves parallel to itself, because the normal vector stays the same.
If you add a second independent equation, the plane is cut down to a line.

## Explanations

### L1 human

One linear equation in three unknowns leaves two unknowns free.
We can choose $x$ and $y$ as we like, and then $z$ is fixed.
So the solutions make a flat sheet in space, a plane.

### L2 human

To find points on the plane quickly, set two of the unknowns to zero.
With $x = y = 0$ we get $z = -4$, so $(0, 0, -4)$ is on the plane.
With $y = z = 0$ we get $x = 4$, and with $x = z = 0$ we get $y = 2$.
These three points are where the plane meets the three axes.
Watch out: solving for $z$ needs a nonzero coefficient of $z$.
For the equation $x + 2y = 4$ in $x, y, z$, you would solve for $x$ instead, and $z$ would be free.
