---
tag: ~b7a5de3d
kind: example
name: Equations and point triples that give no plane
msc: ["51N20", "97G70"]
topics: [VKVAJ94SKZ]
audience: school
not_instance_of:
  - target: 07SDJ5DNE4
    note: an equation with zero coefficient vector is not a plane, and three collinear points do not determine a plane
uses: [07SDJ5DNE4, 0N5N15HWZ7]
sources:
  - url: https://en.wikipedia.org/wiki/Euclidean_planes_in_three-dimensional_space
    locator: Point–normal form and general form of the equation of a plane
---

## Example

We show two ways in which the [[equation of a plane|07SDJ5DNE4]] fails.

**Case 1: a zero normal.** Consider $0x + 0y + 0z = d$.

1. For every point $(x, y, z)$, the left side is $0$.
2. If $d = 5$, no point satisfies the equation, so the set is empty.
3. If $d = 0$, every point satisfies it, so the set is all of $\mathbb{R}^3$.
4. Neither set is a plane, so the condition $n \neq 0$ in the definition is needed.

**Case 2: three points on one line.** Let $A = (1, 1, 1)$, $B = (2, 3, 4)$ and $C = (3, 5, 7)$.

5. The edge vectors are $u = B - A = (1, 2, 3)$ and $v = C - A = (2, 4, 6) = 2u$.
6. The [[cross product|0N5N15HWZ7]] is $u \times v = (2 \cdot 6 - 3 \cdot 4, \; 3 \cdot 2 - 1 \cdot 6, \; 1 \cdot 4 - 2 \cdot 2) = (0, 0, 0)$.
7. The method gives the equation $0x + 0y + 0z = 0$, which is Case 1 with $d = 0$.
8. Indeed $A$, $B$, $C$ lie on the line $A + t u$, and infinitely many planes contain this line.

## Remarks

Two such planes are $x - 2y + z = 0$ and $3x - z = 2$; each contains $A$, $B$ and $C$.
Check for the first: $1 - 2 + 1 = 0$, $2 - 6 + 4 = 0$ and $3 - 10 + 7 = 0$.
Check for the second: $3 - 1 = 2$, $6 - 4 = 2$ and $9 - 7 = 2$.

## Explanations

### L1 human

A plane needs a direction that sticks out of it, and the zero arrow has no direction.
Three points on one line are like a stool with all three legs in a row: it can tip in many ways.
So the three points do not fix one plane.

### L2 human

Before the cross product method, check that the three points are not on one line.
The method itself gives this check: the points are on one line exactly when the cross product of the edge vectors is $0$.
A trap: a computed normal $(0, 0, 0)$ is not a wrong answer to fix; it means that the plane is not unique.
