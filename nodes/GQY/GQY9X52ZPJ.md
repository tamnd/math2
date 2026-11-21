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

The shortest segment between two skew lines is perpendicular to both, so it points along the cross product of their directions.
Let $L_1 = (1, 0, 0) + t(1, 1, 0)$ and $L_2 = (0, 0, 2) + s(0, 1, 1)$, so $a = (1, 0, 0)$, $d = (1, 1, 0)$, $b = (0, 0, 2)$ and $e = (0, 1, 1)$.
We compute the [[distance|C6GAS92QHX]] between these skew [[lines|0399QFDFS8]] and then find the closest points.

1. The [[cross product|0N5N15HWZ7]] of the directions is
   $$m = d \times e = (1 \cdot 1 - 0 \cdot 1, \; 0 \cdot 0 - 1 \cdot 1, \; 1 \cdot 1 - 1 \cdot 0) = (1, -1, 1),$$
   with $\|m\| = \sqrt{3}$.
2. The [[dot product|0S52TNNTH9]] of $b - a = (-1, 0, 2)$ with $m$ is $-1 + 0 + 2 = 1$.
3. By the [[distance theorem|Q6YGYNSY5H]], the distance is $\dfrac{1}{\sqrt{3}} = \dfrac{\sqrt{3}}{3} \approx 0.577$.
4. For the closest points, the connecting vector $x = (b + s e) - (a + t d) = (-1 - t, \; s - t, \; 2 + s)$ must be perpendicular to both lines, so $x \cdot d = 0$ and $x \cdot e = 0$.
5. These read $(-1 - t) + (s - t) = 0$ and $(s - t) + (2 + s) = 0$, that is, $s - 2t = 1$ and $2s - t = -2$.
6. The solution is $t = -\tfrac{4}{3}$ and $s = -\tfrac{5}{3}$.
7. The closest points are $a - \tfrac{4}{3} d = (-\tfrac{1}{3}, -\tfrac{4}{3}, 0)$ on $L_1$ and $b - \tfrac{5}{3} e = (0, -\tfrac{5}{3}, \tfrac{1}{3})$ on $L_2$.
8. Their difference is $(\tfrac{1}{3}, -\tfrac{1}{3}, \tfrac{1}{3}) = \tfrac{1}{3} m$, of length $\tfrac{\sqrt{3}}{3}$, which agrees with step 3.

## Remarks

The [[classification example|NNEBK2BSBB]] shows that these lines are skew, and this example measures how close they come.
The base points $a$ and $b$ are $\sqrt{5} \approx 2.24$ apart, far more than the distance between the lines.

In the proof of the distance theorem, $b - a$ is split along $d$, $e$ and $m$.
Here the split is
$$b - a = -\tfrac{4}{3} d + \tfrac{5}{3} e + \tfrac{1}{3} m,$$
and its coefficients reappear as the parameters $t = -\tfrac{4}{3}$ and $s = -\tfrac{5}{3}$ of the closest points.

## Explanations

### L1 human

Two straight wires pass each other in space without touching.
The shortest bridge between them makes a right angle with both wires.
Here it has length $\tfrac{1}{\sqrt{3}}$, a bit more than half a unit.

### L2 human

Steps 1 to 3 give the distance with one cross product and one dot product.
Steps 4 to 7 find the closest points with a $2 \times 2$ linear system, and step 8 checks the distance.
If only the distance is asked for, stop after step 3.
Watch out: the sign of $(b - a) \cdot m$ carries no meaning for the distance, which takes its absolute value; a value of $-1$ would give the same answer.
