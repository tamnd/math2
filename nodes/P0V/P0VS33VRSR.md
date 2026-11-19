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

Let $P_1$ be the plane $x + y = 1$ and let $P_2$ be the plane $y + z = 2$ in $\mathbb{R}^3$.
We compute the angle between them and their line of intersection.

1. Normals from the [[general form|07SDJ5DNE4]]: $n_1 = (1, 1, 0)$ and $n_2 = (0, 1, 1)$.
2. [[Dot product|0S52TNNTH9]]: $n_1 \cdot n_2 = 0 + 1 + 0 = 1$, and $\|n_1\| = \|n_2\| = \sqrt{2}$.
3. $\cos \varphi = \dfrac{|1|}{\sqrt{2} \cdot \sqrt{2}} = \tfrac{1}{2}$.
4. So the [[angle|0ZEHZY85E6]] between the planes is $\varphi = \tfrac{\pi}{3}$, or $60^\circ$.
5. The line of intersection has the direction $n_1 \times n_2 = (1 \cdot 1 - 0 \cdot 1, \; 0 \cdot 0 - 1 \cdot 1, \; 1 \cdot 1 - 1 \cdot 0) = (1, -1, 1)$.
6. A common point: put $y = 0$; then $x = 1$ and $z = 2$. So the line is $(1, 0, 2) + t(1, -1, 1)$.
7. Check: $(1 + t) + (-t) = 1$ and $(-t) + (2 + t) = 2$ for all $t$.

## Remarks

The angle between the planes is the angle between their normals, or its supplement if that is obtuse.
With $n_2$ replaced by $-n_2 = (0, -1, -1)$, the normals make the angle $\tfrac{2\pi}{3}$, but the planes still make the angle $\tfrac{\pi}{3}$.
The direction of the line of intersection is perpendicular to both normals, so it lies in both planes.

## Explanations

### L1 human

Two walls that meet make an angle, like the pages of a half-open book.
The pencils that stick straight out of the two walls make the same angle.
So we measure the angle between the normals, which is a dot product computation.

### L2 human

Steps 1 to 4 are the method for the angle, and steps 5 and 6 are the method for the line of intersection.
The absolute value in step 3 chooses the acute angle, because a plane has two opposite normals.
A trap: the angle between two planes is not the angle between two direction vectors chosen in them; such vectors can make any angle.
