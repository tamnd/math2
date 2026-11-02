---
tag: D2GQNNQ7FR
kind: definition
name: Order of a projective plane
msc: ["51E15", "05B25"]
defines: K2YVMTGTBB
uses: [DANFNN8C4Y, 2HWB7P1DZN, QQ8GW1ASZM]
sources:
  - url: https://en.wikipedia.org/wiki/Projective_plane
    locator: Finite projective planes
---

## Definition

Let $\Pi$ be a [[projective plane|DANFNN8C4Y]] with a finite set of points.
The *order* of $\Pi$ is the integer $n$ such that one line of $\Pi$, and then every line, contains exactly $n + 1$ points.

## Remarks

The definition does not depend on the line.
Given two distinct lines $\ell$ and $m$, choose a point $O$ on neither; the map $P \mapsto OP \cap m$ is a bijection from the points of $\ell$ to the points of $m$.
For a point $P$ and a line $\ell$ not through $P$, the map $Q \mapsto PQ$ is a bijection from the points of $\ell$ to the lines through $P$.
So every point lies on exactly $n + 1$ lines.
Since a projective plane has four points with no three on a line, every line has at least three points, so $n \ge 2$.

Example: in the [[Fano plane|QQ8GW1ASZM]] each line has $3$ points, so its order is $2$.
In $PG(2, q)$, a line is a $2$-dimensional subspace of $\F_q^3$, which contains $(q^2 - 1)/(q - 1) = q + 1$ one-dimensional subspaces; so the order is $q$.

Non-example: the real projective plane has infinitely many points on each line, so it has no order in this sense.

In Mathlib the order of a finite projective plane is `Configuration.ProjectivePlane.order`, defined through the number of lines through a point, which gives the same number.
