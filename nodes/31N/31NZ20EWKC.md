---
tag: 31NZ20EWKC
kind: example
name: The product of the edge lengths is not the volume of a slanted box
msc: ["15A72", "97G70"]
topics: [VKVAJ94SKZ]
audience: school
not_instance_of:
  - target: 34VJYG6GVD
    note: the product of the lengths of the edges is not the scalar triple product and not the volume when the edges are not perpendicular
uses: [34VJYG6GVD, 0N5N15HWZ7, 0S52TNNTH9, 0XKBKGTCPC]
sources:
  - url: https://en.wikipedia.org/wiki/Parallelepiped
    locator: Volume
---

## Example

Let $a = (1, 0, 0)$, $b = (1, 1, 0)$ and $c = (0, 0, 1)$.
A common guess for the volume of the box on $a$, $b$, $c$ is the product of the edge lengths.
We show that this guess is wrong.

1. The [[lengths|0XKBKGTCPC]] are $\|a\| = 1$, $\|b\| = \sqrt{2}$ and $\|c\| = 1$, with the product $\sqrt{2}$.
2. [[Cross product|0N5N15HWZ7]]: $b \times c = (1 \cdot 1 - 0 \cdot 0, \; 0 \cdot 0 - 1 \cdot 1, \; 1 \cdot 0 - 1 \cdot 0) = (1, -1, 0)$.
3. [[Dot product|0S52TNNTH9]]: $a \cdot (b \times c) = 1$.
4. So the volume is $1$, by the [[volume theorem|7RMCRQ9ERC]], and not $\sqrt{2}$.
5. Geometric check: the base on $a$ and $b$ in the plane $z = 0$ has area $1$, and the height along $c$ is $1$.

## Remarks

The product of the lengths equals the volume only for perpendicular edges, as for a cuboid.
In general $|[a, b, c]| \leq \|a\| \, \|b\| \, \|c\|$, which is the case $n = 3$ of Hadamard's inequality.
Here $a$ and $b$ make the angle $\tfrac{\pi}{4}$, and $\sqrt{2} \sin \tfrac{\pi}{4} = 1$ is the area of the base.

## Explanations

### L1 human

Push the top of a box sideways, and the box leans.
The edges get longer, but the box holds the same amount of space.
So the lengths of the edges do not give the volume of a leaning box; the triple product does.

### L2 human

The volume is base times height, not the product of three edges.
For the base on $a$ and $b$, the area is $\|a\| \, \|b\| \sin \theta = 1 \cdot \sqrt{2} \cdot \tfrac{\sqrt{2}}{2} = 1$.
A trap: the formula $\|a\| \, \|b\| \, \|c\|$ from a cuboid fails as soon as one angle between edges is not a right angle.
