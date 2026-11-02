---
tag: QS9PG4MNTR
kind: statement
role: theorem
name: Jordan curve theorem for polygons
msc: [51M04, 54D05]
uses: [045YFKRW0P, 0V032VWTHD]
about: [045YFKRW0P]
sources:
  - url: https://en.wikipedia.org/wiki/Jordan_curve_theorem
---

## Statement

Let $C \subset \R^2$ be a simple closed polygonal curve.
That is, $C$ is a closed polygonal chain that meets itself only where its last side ends at the start of its first side.
Then $\R^2 \setminus C$ has exactly two connected components.
One component is bounded and the other is unbounded, and $C$ is the boundary of each of them.

## Remarks

The proof uses parity of crossings.
For a point $x \notin C$, take a ray from $x$ in a direction that avoids the vertices of $C$, and count how many times it crosses $C$.
The parity of this count does not depend on the ray, and it is constant along paths that avoid $C$.
So points of even and odd parity lie in different [[components|0V032VWTHD]].
Conversely, two points of the same parity can be joined by a path that runs close to $C$, so there are exactly two components.
Points far away have even parity and form the unbounded one.

This crossing count is also the standard test of whether a point lies inside a polygon.

## Explanations

### L1 human

A closed loop made of straight pieces that never crosses itself splits the plane into an inside and an outside.
To go from inside to outside, a path has to cross the loop.
A point is inside when a ray from it crosses the loop an odd number of times.

### L2 human

This is the special case of the [[Jordan curve theorem|687RGCHBTP]] for polygonal curves, and its proof is elementary.
The general theorem for arbitrary [[closed curves|045YFKRW0P]] without self-intersections is usually proved by approximating the curve by polygons or by homology.
The polygonal case is what is used for simple polygons in [[polygon triangulation|Q6KKBP3RRP]] and other parts of computational geometry.
