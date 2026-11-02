---
tag: AXS7YYF1YY
kind: definition
name: Polygon
msc: [51M04, 52B05]
defines: 8VEFWD3EJB
uses: [0XW7V9ZZ05, 0AFNNTRTJE]
sources:
  - url: https://en.wikipedia.org/wiki/Polygon
---

## Definition

Let $n \ge 3$ be an integer.
A *polygon* with $n$ vertices in the [[Euclidean plane|0XW7V9ZZ05]] is a cyclic sequence of points $P_1, \ldots, P_n$, with indices taken modulo $n$, such that:

1. $P_i \ne P_{i+1}$ for every $i$.
2. $P_{i-1}$, $P_i$, $P_{i+1}$ are not [[collinear|0AFNNTRTJE]] for every $i$.

The points $P_i$ are its *vertices* and the segments $P_i P_{i+1}$ are its *edges*.
The polygon is *simple* if two edges meet only when they are consecutive, and then only in their common vertex.

## Remarks

By the [[Jordan curve theorem|687RGCHBTP]], a simple polygon bounds one bounded region of the plane, its interior.
Many authors use the word polygon for this closed region rather than for the boundary.
A polygon with $3$ vertices is a [[triangle|0CTNFGYMM2]], and one with $4$ vertices is a quadrilateral.
A simple polygon is convex if its interior is a [[convex set|02AS45T3H9]].

Example: $(0, 0), (1, 0), (1, 1), (0, 1)$ is a simple polygon, the unit square.
Consecutive vertices differ, and no three consecutive ones lie on a line.

Non-example: $(0, 0), (1, 0), (2, 0), (1, 1)$ fails clause 2.
The three consecutive vertices $(0, 0), (1, 0), (2, 0)$ are collinear, so the figure is a triangle with an extra point on one edge.
