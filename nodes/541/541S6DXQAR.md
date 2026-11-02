---
tag: 541S6DXQAR
kind: definition
name: Orthocentric system
msc: [51M04]
defines: 8K5FT58EK5
uses: [0JDB8YJBSR, 0QMYQ1X03H]
sources:
  - url: https://en.wikipedia.org/wiki/Orthocentric_system
---

## Definition

A set $S$ of points of the Euclidean plane is an *orthocentric system* if both conditions hold.

1. $S$ has exactly four points.
2. Some three points of $S$ form a [[triangle|0JDB8YJBSR]] whose [[orthocentre|0QMYQ1X03H]] is the fourth point.

## Remarks

Condition 1 forces the triangle in condition 2 to have no right angle.
For a right triangle the orthocentre is the vertex of the right angle, so only three distinct points would remain.

Example: let $A = (0, 2)$, $B = (-1, 0)$, $C = (1, 0)$ and $H = (0, \frac{1}{2})$.
The altitude from $A$ is the line $x = 0$.
The altitude from $B$ is perpendicular to $C - A = (1, -2)$, so it is the line $(x + 1) - 2y = 0$, which meets $x = 0$ at $(0, \frac{1}{2})$.
So $H$ is the orthocentre of $ABC$, and $\set{A, B, C, H}$ is an orthocentric system.

Non-example: $(0, 0)$, $(1, 0)$, $(0, 1)$ and $(1, 1)$.
The orthocentre of each three of them is a vertex of that triangle, since each such triangle has a right angle, so condition 2 fails.

If $\set{A, B, C, H}$ is an orthocentric system, then each point is the orthocentre of the other three.
Indeed, $H$ is the orthocentre of $ABC$ when $AH \perp BC$, $BH \perp CA$ and $CH \perp AB$.
The same three relations say that $A$ is the orthocentre of $HBC$, and similarly for $B$ and $C$.
