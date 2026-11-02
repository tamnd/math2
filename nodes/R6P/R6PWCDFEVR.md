---
tag: R6PWCDFEVR
kind: definition
name: Tetrahedron
msc: [51M20, 52B10]
defines: JFX8ASQS3E
uses: [0FQSDC2EQ2, 0V3XAMF3C1, 0XPR1E85W0]
sources:
  - url: https://en.wikipedia.org/wiki/Tetrahedron
---

## Definition

Let $A$, $B$, $C$, $D$ be four points of the [[Euclidean space|0XPR1E85W0]] $\R^3$ that do not lie in one [[plane|0V3XAMF3C1]].
The *tetrahedron* $ABCD$ is the [[convex hull|0FQSDC2EQ2]] of $\set{A, B, C, D}$.
Its vertices are the four points, its edges are the six segments between them, and its faces are the four triangles on three of them.

## Remarks

The four points do not lie in one plane exactly when the vectors $B - A$, $C - A$, $D - A$ are linearly independent.
Then the volume of $ABCD$ is
$$V = \frac{1}{6} \abs{\det(B - A, C - A, D - A)}.$$
A tetrahedron is a 3-dimensional [[simplex|YX1DJK2QAG]], and its four vertices always lie on one [[circumsphere|MRC4WMVTAH]].
It is regular when all six edges have the same length; the regular tetrahedron is a [[Platonic solid|017E5PRS1Q]].

Example: $(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)$.
The determinant of the three standard basis vectors is $1$, so the points are not coplanar and the volume is $1/6$.

Non-example: $(0, 0, 0), (1, 0, 0), (0, 1, 0), (1, 1, 0)$ all lie in the plane $z = 0$.
Their convex hull is a flat unit square, not a tetrahedron.
