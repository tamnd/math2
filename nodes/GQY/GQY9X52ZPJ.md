---
tag: GQY9X52ZPJ
kind: example
name: The distance between two skew lines and their closest points
msc: ["51N20", "97G70"]
topics: [VKVAJ94SKZ]
audience: school
instance_of: [C6GAS92QHX]
illustrates: [Q6YGYNSY5H]
uses: [C6GAS92QHX, 0N5N15HWZ7, 0S52TNNTH9, 0399QFDFS8]
sources:
  - url: https://en.wikipedia.org/wiki/Skew_lines
    locator: Distance
---

## Example

Let $L_1 = (1, 0, 0) + t(1, 1, 0)$ and $L_2 = (0, 0, 2) + s(0, 1, 1)$, so $a = (1, 0, 0)$, $d = (1, 1, 0)$, $b = (0, 0, 2)$, $e = (0, 1, 1)$.
We compute the [[distance|C6GAS92QHX]] between these skew [[lines|0399QFDFS8]] and the closest points.

1. [[Cross product|0N5N15HWZ7]]: $m = d \times e = (1 \cdot 1 - 0 \cdot 1, \; 0 \cdot 0 - 1 \cdot 1, \; 1 \cdot 1 - 1 \cdot 0) = (1, -1, 1)$, with $\|m\| = \sqrt{3}$.
2. $b - a = (-1, 0, 2)$ and $(b - a) \cdot m = -1 + 0 + 2 = 1$, by the [[dot product|0S52TNNTH9]].
3. By the [[distance theorem|Q6YGYNSY5H]], the distance is $\dfrac{1}{\sqrt{3}} = \dfrac{\sqrt{3}}{3} \approx 0.577$.
4. Closest points: the connecting vector $x = (b + s e) - (a + t d) = (-1 - t, \; s - t, \; 2 + s)$ must be a multiple of $m$.
5. So $x \cdot d = 0$ and $x \cdot e = 0$: $(-1 - t) + (s - t) = 0$ and $(s - t) + (2 + s) = 0$.
6. These are $s - 2t = 1$ and $2s - t = -2$. They give $t = -\tfrac{4}{3}$ and $s = -\tfrac{5}{3}$.
7. The points are $a - \tfrac{4}{3} d = (-\tfrac{1}{3}, -\tfrac{4}{3}, 0)$ and $b - \tfrac{5}{3} e = (0, -\tfrac{5}{3}, \tfrac{1}{3})$.
8. Their difference is $(\tfrac{1}{3}, -\tfrac{1}{3}, \tfrac{1}{3}) = \tfrac{1}{3} m$, with the length $\tfrac{\sqrt{3}}{3}$. This agrees with step 3.

## Remarks

The base points $a$ and $b$ have the distance $\sqrt{5} \approx 2.24$, far more than the distance between the lines.
The [[classification example|NNEBK2BSBB]] shows that these lines are skew.
In the proof, $b - a = -\tfrac{4}{3} d + \tfrac{5}{3} e + \tfrac{1}{3} m$, and the closest points are at $t = -\tfrac{4}{3}$ and $s = -\tfrac{5}{3}$.

## Explanations

### L1 human

Two straight wires pass each other in space without touching.
The shortest bridge between them makes a right angle with both wires.
Here it has the length $\tfrac{1}{\sqrt{3}}$, a bit more than half a unit.

### L2 human

Steps 1 to 3 give the distance with one cross product and one dot product.
Steps 4 to 8 find the closest points with a $2 \times 2$ linear system, and step 8 checks the distance.
A trap: the sign of $(b - a) \cdot m$ does not matter; the distance takes its absolute value.
