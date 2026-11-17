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

Claim: in each triangle $ABC$, the [[median|0XW8HX8VEV]] from $A$ is also the [[altitude|0C9MZY2RNA]] from $A$.
A student tests the claim on a figure.

1. The student draws a triangle with $B = (0, 0)$, $C = (4, 0)$ and $A = (2, 3)$, because this triangle is easy to draw.
2. The midpoint of $BC$ is $M = (2, 0)$, so the median from $A$ is the segment from $(2, 3)$ to $(2, 0)$.
3. This segment is vertical, and $BC$ is horizontal, so the median is perpendicular to $BC$. On the figure, the median is the altitude.
4. The student concludes that the claim holds.

The conclusion is false.
The figure is not in general position: $|AB| = |AC| = \sqrt{13}$, so the triangle is isosceles.
We check a triangle in general position.

1. Take $B = (0, 0)$, $C = (4, 0)$ and $A = (1, 3)$. The sides are $|AB| = \sqrt{10}$, $|AC| = \sqrt{18}$ and $|BC| = 4$, all different.
2. The midpoint of $BC$ is $M = (2, 0)$.
3. The altitude from $A$ is perpendicular to the horizontal side $BC$, so it is vertical, and its foot is $H = (1, 0)$.
4. $M \neq H$, so the median $AM$ and the altitude $AH$ are different segments. Their lengths are $|AM| = \sqrt{1 + 9} = \sqrt{10}$ and $|AH| = 3$.

So the claim fails for this triangle, and the heuristic [[draw a figure|6CVYB413ER]] misled the student because the figure was too special.

## Remarks

The median from $A$ is the altitude from $A$ exactly when $|AB| = |AC|$.
Indeed, with $B = (0, 0)$, $C = (2m, 0)$ and $A = (p, q)$, the median is vertical exactly when $p = m$, and $|AB|^2 - |AC|^2 = p^2 - (p - 2m)^2 = 4m(p - m)$, which is $0$ exactly when $p = m$.
So the student's figure lies in the one special family where the claim is true.
A figure drawn "to be easy" is often isosceles, right-angled or equilateral, and each of these shapes has extra properties.
The rule of the heuristic is to draw a figure that looks as general as the hypotheses allow.

## Explanations

### L1 human

The line from a corner of a triangle to the middle of the opposite side is called a median.
The line from the same corner that meets the opposite side at a right angle is called an altitude.
In a triangle with two equal sides, drawn standing on the third side, the two lines are the same.
In a lopsided triangle they are different: one goes to the middle, the other goes straight down.
A picture of a too-tidy triangle can make us believe something that is false for most triangles.

### L2 human

We give a test that catches a too-special figure.

1. List the special properties of the figure: here $|AB| = |AC|$.
2. Ask whether the hypotheses of the claim give these properties. Here the claim is about each triangle, so they do not.
3. Draw a second figure without these properties, or vary a coordinate: move $A$ from $(2, 3)$ to $(1, 3)$.
4. Check the claim on the new figure. If it fails, the claim is false; if it holds, the figure is still only evidence.

The typical use: before trusting a relation seen on a figure, change the figure a little and look again.

A trap: a second figure that agrees with the claim does not prove it; only a proof does.
