---
tag: SXA7G1N6HZ
kind: example
name: A figure that is too special suggests that a median is an altitude
msc: ["00A35", "51M04"]
topics: [X1NSTVGDNQ]
audience: school
not_instance_of:
  - target: 6CVYB413ER
    note: the figure is drawn in a special position (isosceles), so it shows a relation that fails for a general triangle; the heuristic asks for a figure in general position
uses: [6CVYB413ER, 0XW8HX8VEV, 0C9MZY2RNA]
sources:
  - url: https://en.wikipedia.org/wiki/Median_(geometry)
    locator: lead section
---

## Example

A student meets the claim that in every triangle $ABC$ the [[median|0XW8HX8VEV]] from $A$ is also the [[altitude|0C9MZY2RNA]] from $A$, and tests it on a figure.

1. The student draws the triangle with $B = (0, 0)$, $C = (4, 0)$ and $A = (2, 3)$, because it is easy to draw.
2. The midpoint of $BC$ is $M = (2, 0)$, so the median from $A$ runs from $(2, 3)$ to $(2, 0)$.
3. This segment is vertical and $BC$ is horizontal, so on the figure the median is perpendicular to $BC$ and is the altitude.
4. The student concludes that the claim holds.

The conclusion is false.
The figure is not in general position, since $|AB| = |AC| = \sqrt{13}$ makes the triangle isosceles.
We check a triangle in general position.

1. Take $B = (0, 0)$, $C = (4, 0)$ and $A = (1, 3)$, with sides $|AB| = \sqrt{10}$, $|AC| = \sqrt{18}$ and $|BC| = 4$, all different.
2. The midpoint of $BC$ is still $M = (2, 0)$.
3. The altitude from $A$ is perpendicular to the horizontal side $BC$, so it is vertical, and its foot is $H = (1, 0)$.
4. Since $M \ne H$, the median $AM$ and the altitude $AH$ are different segments, with lengths $|AM| = \sqrt{1 + 9} = \sqrt{10}$ and $|AH| = 3$.

So the claim fails, and the advice to [[draw a figure|6CVYB413ER]] misled the student because the figure was too special.

## Remarks

The median from $A$ is the altitude from $A$ exactly when $|AB| = |AC|$.
To see this, put $B = (0, 0)$, $C = (2m, 0)$ and $A = (p, q)$.
The median is vertical exactly when $p = m$, and
$$|AB|^2 - |AC|^2 = p^2 - (p - 2m)^2 = 4m(p - m),$$
which is $0$ exactly when $p = m$.
So the student's figure lies in the one special family where the claim is true.

A figure drawn to be easy is often isosceles, right-angled or equilateral, and each of these shapes has extra properties.
The advice is to draw a figure that looks as general as the hypotheses allow.

## Explanations

### L1 human

The line from a corner of a triangle to the middle of the opposite side is a median.
The line from the same corner that meets the opposite side at a right angle is an altitude.
In a triangle with two equal sides, standing on the third side, the two lines are the same.
In a lopsided triangle they differ: one goes to the middle, the other goes straight down.
A picture of a too-tidy triangle can make you believe something that is false for most triangles.

### L2 human

Here is a test that catches a too-special figure.
First list the special properties of the figure, here $|AB| = |AC|$.
Then ask whether the hypotheses of the claim give these properties; the claim is about every triangle, so they do not.
Now vary the figure, for example move $A$ from $(2, 3)$ to $(1, 3)$, and check the claim again.
If it fails, the claim is false.

Before you trust a relation seen in a figure, change the figure a little and look again.
A second figure that agrees with the claim is still only evidence, and only a proof settles the claim.
