---
tag: 3THE3Q96KK
kind: statement
role: theorem
name: Brianchon's theorem
msc: [51A20, 51N15]
uses: [ZT9A6JK8QF, DANFNN8C4Y, 00HJCMC2CD, 01R1HW3Y42]
about: [00HJCMC2CD]
sources:
  - url: https://en.wikipedia.org/wiki/Brianchon%27s_theorem
same_as:
  wikidata: Q119450
  wikipedia: Brianchon's theorem
---

## Statement

Work in the real [[projective plane|DANFNN8C4Y]] $\mathbb{P}^2(\R)$, and let $\mathcal{C}$ be a nondegenerate [[conic|00HJCMC2CD]].
Let $t_1, \dots, t_6$ be six distinct lines [[tangent|01R1HW3Y42]] to $\mathcal{C}$.
Put $A = t_1 \cap t_2$, $B = t_2 \cap t_3$, $C = t_3 \cap t_4$, $D = t_4 \cap t_5$, $E = t_5 \cap t_6$ and $F = t_6 \cap t_1$.
Then the three lines $AD$, $BE$ and $CF$ pass through a common point.

## Remarks

So $ABCDEF$ is a hexagon whose sides touch the conic, and the statement says that its three main diagonals are concurrent.
No three tangent lines of a nondegenerate real conic pass through one point, which makes the six vertices distinct and the three diagonals well defined.

The theorem is the dual of [[Pascal's theorem|94AKWRHND0]].
The tangent lines of a nondegenerate conic form a nondegenerate conic of the dual plane, and the dual of the statement "three points are collinear" is "three lines are concurrent".
So the principle of [[duality|DCMP1A0138]] applied to Pascal's theorem gives Brianchon's theorem.

Example: for a regular hexagon circumscribed about a circle, the three main diagonals pass through the centre of the circle.

## Explanations

### L1 human

Draw six lines that just touch an ellipse, so that they enclose a hexagon around it.
Join opposite corners of the hexagon by three diagonals.
These three diagonals always meet at a single point.

### L2 human

Being the dual of Pascal's theorem, it is a classic illustration of projective [[duality|DCMP1A0138]].
It is used to construct tangent lines of a conic from five given tangent lines with a straightedge.
The same argument works over any field of characteristic different from $2$.
In characteristic $2$ all tangent lines of a nondegenerate conic pass through one point, so the hypotheses of the statement cannot be met there.
