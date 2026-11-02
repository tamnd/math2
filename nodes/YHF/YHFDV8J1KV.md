---
tag: YHFDV8J1KV
kind: definition
name: Hilbert's axioms
msc: [51M05, 51F05, 03B30]
defines: KM1FB8XZ2R
uses: [0MP9BCF6DP, 0V3XAMF3C1, CE8GX6ADZS, KJT98G16Y4, PR7Q3QMEHZ]
sources:
  - url: https://en.wikipedia.org/wiki/Hilbert%27s_axioms
---

## Definition

The primitive objects are points, lines and planes.
The primitive relations are incidence, betweenness of three points, and congruence $\cong$ of segments and of angles.
*Hilbert's axioms* are the following five groups of axioms on these notions.

1. Incidence: two distinct points lie on exactly one [[line|0MP9BCF6DP]]. Three non-collinear points lie on exactly one [[plane|0V3XAMF3C1]]. A line with two points in a plane lies in the plane. Two planes with a common point have a second common point. Each line has at least two points, each plane has three non-collinear points, and there are four points not in one plane.
2. Order: the [[betweenness|CE8GX6ADZS]] relation is symmetric in $A$ and $C$ and holds only for three distinct collinear points. For distinct $A$ and $C$ some point $B$ has $C$ between $A$ and $B$. Of three collinear points, at most one lies between the other two. [[Pasch's axiom|KJT98G16Y4]] holds.
3. Congruence: a segment can be laid off on a given ray in a unique way, and congruence of segments is transitive. Congruent adjacent segments add up to congruent segments. An angle can be laid off on a given side of a given ray in a unique way. If two triangles have two sides and the included angle congruent, then the other angles are congruent too.
4. Parallels: [[Playfair's axiom|PR7Q3QMEHZ]] holds.
5. Continuity: the axiom of Archimedes holds for segments. The points of a line admit no extension that keeps all the other axioms (line completeness).

## Remarks

Example: $\R^3$ with its usual points, lines, planes, betweenness and congruence by isometries is a model.
For instance, Pasch's axiom holds there because a line in a plane is the zero set of an affine function.
Up to isomorphism, it is the only model, so the system is categorical.
Non-example: the space $\Q^3$ with the same notions fails the first congruence axiom.
The segment from $(0,0,0)$ to $(1,1,0)$ has length $\sqrt 2$, so it cannot be laid off on the positive $x$-axis from the origin, since $(\sqrt 2, 0, 0) \notin \Q^3$.
The plane version keeps only the axioms of groups 1 to 5 that speak of one plane.
