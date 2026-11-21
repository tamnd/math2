---
tag: NNEBK2BSBB
kind: example
name: Parallel, intersecting and skew lines in space
msc: ["51N20", "97G70"]
topics: [VKVAJ94SKZ]
audience: school
instance_of: [0399QFDFS8]
uses: [0399QFDFS8, 0N5N15HWZ7]
sources:
  - url: https://en.wikipedia.org/wiki/Skew_lines
    locator: Testing for skewness
---

## Example

Two lines in space are parallel, meet in one point, or are skew, and two questions sort them: are the directions multiples, and do the equations have a common solution?
We classify three pairs of [[lines|0399QFDFS8]] in $\mathbb{R}^3$, one of each kind.

**Pair 1: parallel.**
Let $L_1 = (0, 0, 0) + t(1, 2, 2)$ and $L_2 = (1, 0, 0) + s(-2, -4, -4)$.

1. The directions satisfy $(-2, -4, -4) = -2 \, (1, 2, 2)$, so the lines are parallel.
2. Parallel lines either coincide or never meet, so test one point. Is $(1, 0, 0)$ on $L_1$? The $x$ equation gives $t = 1$, but then $y = 2 \neq 0$.
3. So the lines are parallel and distinct.

**Pair 2: intersecting.**
Let $L_1 = (1, 2, 0) + t(1, -1, 1)$ and $L_2 = (2, -1, -3) + s(0, 1, 2)$.

1. The directions are not multiples of each other, since the first has $x$ component $1$ and the second has $0$.
2. A common point needs $t$ and $s$ with
   $$1 + t = 2, \qquad 2 - t = -1 + s, \qquad t = -3 + 2s.$$
3. The first equation gives $t = 1$, and then the second gives $s = 2$.
4. The third equation checks: $1 = -3 + 4$. So the lines meet, at $(2, 1, 1)$.

**Pair 3: skew.**
Let $L_1 = (1, 0, 0) + t(1, 1, 0)$ and $L_2 = (0, 0, 2) + s(0, 1, 1)$.

1. The directions are not multiples of each other, so the lines are not parallel.
2. A common point needs
   $$1 + t = 0, \qquad t = s, \qquad 0 = 2 + s.$$
3. The first equation gives $t = -1$ and the second then gives $s = -1$, but the third needs $s = -2$.
4. The system has no solution, so the lines do not meet, and they are skew.

## Remarks

The [[coplanarity test|7RMCRQ9ERC]] gives the same answers for pairs 2 and 3 with one [[cross product|0N5N15HWZ7]] and one dot product.
Write $a$, $b$ for the base points and $d$, $e$ for the directions.
For pair 2,
$$d \times e = (-3, -2, 1), \qquad (b - a) \cdot (d \times e) = (1, -3, -3) \cdot (-3, -2, 1) = 0,$$
so the two lines lie in one plane, and since they are not parallel they meet.
For pair 3,
$$d \times e = (1, -1, 1), \qquad (b - a) \cdot (d \times e) = (-1, 0, 2) \cdot (1, -1, 1) = 1 \neq 0,$$
so the lines are skew.
That nonzero number also measures how far apart they are: the [[distance example|GQY9X52ZPJ]] finds the distance $\tfrac{1}{\sqrt{3}}$ between the lines of pair 3.

## Explanations

### L1 human

Two straight roads in space can run side by side, can cross, or can pass over each other like a bridge over a road.
The third case, skew lines, cannot happen in a flat plane.
To decide which case holds, first compare the directions, and then try to solve for a common point.

### L2 human

The method is the same every time.
Compare the directions first; if they are not parallel, set the two vector equations equal, with two different parameters.
This gives three equations in two unknowns.
Solve two of them and test the third.
Watch out: a solution of two of the three equations is not enough.
In pair 3 the first two equations have the solution $t = s = -1$, and only the third shows that the lines miss.
