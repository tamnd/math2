---
tag: VWQQY7NFED
kind: statement
role: theorem
name: Routh's theorem
msc: [51M04, 51M25]
uses: [0CTNFGYMM2, 065JWMZW86]
about: [0CTNFGYMM2]
sources:
  - url: https://en.wikipedia.org/wiki/Routh%27s_theorem
same_as:
  wikidata: Q1789863
  wikipedia: Routh's theorem
---

## Statement

Let $ABC$ be a [[triangle|0CTNFGYMM2]] in the Euclidean plane with area $S$.
Let $D$, $E$, $F$ be points in the interiors of the sides $BC$, $CA$, $AB$, and let $x = BD/DC$, $y = CE/EA$ and $z = AF/FB$.
Then the three segments $AD$, $BE$, $CF$ bound a triangle whose [[area|065JWMZW86]] is
$$S \cdot \frac{(xyz - 1)^2}{(xy + x + 1)(yz + y + 1)(zx + z + 1)}.$$
When $xyz = 1$, this triangle degenerates to a point.

## Remarks

A proof places the triangle in barycentric coordinates, computes the three intersection points of the cevians, and takes the ratio of determinants.
Example: with $x = y = z = 2$, the area is $S \cdot 49/343 = S/7$, the well-known one-seventh triangle.
The case $xyz = 1$ is exactly the condition of [[Ceva's theorem|0KN93VDSXA]] for the three cevians to be concurrent, and Routh's formula gives area $0$ there.

## Explanations

### L1 human

Draw three lines from the corners of a triangle to points on the opposite sides.
In general the three lines enclose a small triangle in the middle.
Routh's theorem tells exactly how big that small triangle is, using only the ratios in which the sides are cut.

### L2 human

Routh's theorem refines Ceva's theorem: Ceva says when the inner triangle is a point, and Routh measures it in all other cases.
Because affine maps preserve ratios of areas and ratios along lines, it is enough to prove it for one triangle, for example $A = (0, 0)$, $B = (1, 0)$, $C = (0, 1)$.
The theorem is a good exercise in barycentric coordinates and in the use of the [[determinant|00KDZRW4C0]] to compute areas.
