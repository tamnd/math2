---
tag: P0VS33VRSR
kind: example
name: The angle between two planes
msc: ["51N20", "97G70"]
topics: [VKVAJ94SKZ]
audience: school
instance_of: [07SDJ5DNE4]
uses: [07SDJ5DNE4, 0ZEHZY85E6, 0S52TNNTH9, 0N5N15HWZ7]
sources:
  - url: https://en.wikipedia.org/wiki/Euclidean_planes_in_three-dimensional_space
    locator: Angle between two planes
---

## Example

The angle between two planes is read off from their normals, and the cross product of the normals points along the line where the planes meet.
Let $P_1$ be the plane $x + y = 1$ and let $P_2$ be the plane $y + z = 2$ in $\mathbb{R}^3$.
We compute the angle between them and their line of intersection.

1. The [[general form|07SDJ5DNE4]] gives the normals $n_1 = (1, 1, 0)$ and $n_2 = (0, 1, 1)$.
2. The [[dot product|0S52TNNTH9]] is $n_1 \cdot n_2 = 0 + 1 + 0 = 1$, and $\|n_1\| = \|n_2\| = \sqrt{2}$.
3. So
   $$\cos \varphi = \frac{|n_1 \cdot n_2|}{\|n_1\| \, \|n_2\|} = \frac{1}{\sqrt{2} \cdot \sqrt{2}} = \frac{1}{2},$$
   and the [[angle|0ZEHZY85E6]] between the planes is $\varphi = \tfrac{\pi}{3}$, or $60^\circ$.
4. The line of intersection lies in both planes, so its direction is perpendicular to both normals. The [[cross product|0N5N15HWZ7]] gives one:
   $$n_1 \times n_2 = (1 \cdot 1 - 0 \cdot 1, \; 0 \cdot 0 - 1 \cdot 1, \; 1 \cdot 1 - 1 \cdot 0) = (1, -1, 1).$$
5. For a common point, put $y = 0$; then $x = 1$ and $z = 2$. So the line is $(1, 0, 2) + t(1, -1, 1)$.
6. Check: $(1 + t) + (-t) = 1$ and $(-t) + (2 + t) = 2$ for all $t$.

## Remarks

A plane has two opposite normals, and the absolute value in step 3 makes the answer independent of which one we pick.
With $n_2$ replaced by $-n_2 = (0, -1, -1)$, the normals make the angle $\tfrac{2\pi}{3}$, yet the planes still meet at $\tfrac{\pi}{3}$.
So the angle between two planes is the acute one of the two angles between their normals.

## Explanations

### L1 human

Two walls that meet make an angle, like the pages of a half-open book.
The pencils that stick straight out of the two walls make the same angle.
So we measure the angle between the normals, which is a dot product computation.

### L2 human

Steps 1 to 3 are the method for the angle, and steps 4 and 5 are the method for the line of intersection.
Any value of one coordinate works in step 5, as long as the two equations can then be solved for the other two.
Watch out: the angle between two planes is not the angle between two direction vectors chosen in them.
Such vectors can make any angle at all, while the normals are fixed up to sign.
