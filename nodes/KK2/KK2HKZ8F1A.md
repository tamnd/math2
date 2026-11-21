---
tag: KK2HKZ8F1A
kind: example
name: An obtuse angle between two vectors in the plane
msc: ["51N20", "97G70"]
topics: [VKVAJ94SKZ]
audience: school
instance_of: [0ZEHZY85E6]
uses: [0ZEHZY85E6, 0S52TNNTH9, 0XKBKGTCPC]
sources:
  - url: https://en.wikipedia.org/wiki/Dot_product
    locator: Geometric definition
---

## Example

Let $u = (1, 2)$ and $v = (-3, 1)$.
We compute the [[angle|0ZEHZY85E6]] $\theta$ between $u$ and $v$.

1. The [[dot product|0S52TNNTH9]] is $u \cdot v = 1 \cdot (-3) + 2 \cdot 1 = -1$.
2. The dot product is negative, so the angle is obtuse, before any further work.
3. The [[lengths|0XKBKGTCPC]] are $\|u\| = \sqrt{1 + 4} = \sqrt{5}$ and $\|v\| = \sqrt{9 + 1} = \sqrt{10}$.
4. Divide the dot product by the product of the lengths:
   $$\cos \theta = \frac{-1}{\sqrt{5} \, \sqrt{10}} = -\frac{1}{\sqrt{50}} = -\frac{1}{5\sqrt{2}} \approx -0.1414.$$
5. A calculator in degree mode gives $\theta = \arccos(-0.1414) \approx 98.13^\circ$.

## Remarks

The angle is only a little more than a right angle, because the dot product $-1$ is small compared with $\|u\| \, \|v\| = \sqrt{50} \approx 7.07$.
Small changes of $v$ show how the sign controls the type of angle.
For $v = (-2, 1)$ the dot product becomes $-2 + 2 = 0$, and the angle is exactly $90^\circ$.
For $v = (3, -1)$, the reverse of the original $v$, the dot product becomes $1$, and the angle is $180^\circ - 98.13^\circ = 81.87^\circ$.

## Explanations

### L1 human

The vector $(1, 2)$ points up and a little to the right.
The vector $(-3, 1)$ points to the left and a little up.
The opening between them is a bit more than a right angle.
The negative dot product $-1$ tells you this before you compute the angle.

### L2 human

The sign of the dot product gives the type of the angle at once, and the size of the angle needs the lengths.
That is the quick way to classify the angles of a triangle: three dot products, one at each corner.
Watch out: $\arccos$ on a calculator returns values in $[0^\circ, 180^\circ]$, so it never returns a negative angle, and here its answer needs no correction.
