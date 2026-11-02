---
tag: JGT7T3A9PD
kind: statement
role: theorem
name: Fáry's theorem
msc: [05C10, 05C62]
uses: [0NC9R64TXP, CG91WNMG2T, HFJCAPWWD4]
about: [0NC9R64TXP]
sources:
  - url: https://en.wikipedia.org/wiki/Fáry%27s_theorem
same_as:
  wikidata: Q4455031
  wikipedia: Fáry's theorem
---

## Statement

Let $G$ be a finite simple [[planar graph|0NC9R64TXP]].
Then $G$ has an [[embedding|CG91WNMG2T]] in the plane in which every edge is a straight line segment.

## Remarks

The idea of the proof is induction on the number of vertices.
Add edges until $G$ is maximal planar, so that every face, including the outer one, is a triangle.
For at least four vertices, Euler's formula gives a vertex $v$ of degree at most $5$ that is not on the outer triangle.
Remove $v$, triangulate the face it leaves, and draw the smaller graph with straight edges by induction.
Delete the added diagonals; the face left by $v$ is a polygon with at most $5$ sides.
Such a polygon always contains a point that sees all its corners, so $v$ can be placed there and joined by straight segments.

The theorem is named after István Fáry; Klaus Wagner had proved it earlier, and Sherman Stein proved it independently.
The result needs $G$ to be simple: a multigraph with two parallel edges cannot be drawn with both edges straight.

## Explanations

### L1 human

If a network can be drawn on paper without crossing lines, using curvy lines if needed, then it can also be drawn without crossings using only straight lines.
So curves give no extra power for planar drawings.

### L2 human

Fáry's theorem lets one treat planar graphs as plane [[geometric graphs|HFJCAPWWD4]].
Stronger versions exist: every planar graph with $n$ vertices has a straight-line drawing with vertices on an $O(n) \times O(n)$ integer grid.
By the Koebe–Andreev–Thurston theorem, every planar graph is the contact graph of a family of discs with disjoint interiors.
Tutte's spring embedding gives a straight-line drawing of every $3$-connected planar graph with convex faces.
