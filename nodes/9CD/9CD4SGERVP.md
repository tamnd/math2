---
tag: 9CD4SGERVP
kind: definition
name: Ovoid
msc: ["51E20", "51E21"]
defines: HNTE5FPS14
uses: [ZT9A6JK8QF, Q3Q4FF23VG, 7B03TB64N9, 0ZXZ82FTX2]
sources:
  - url: https://en.wikipedia.org/wiki/Ovoid_(projective_geometry)
---

## Definition

Let $\mathcal{P}$ be a [[projective space|ZT9A6JK8QF]] of dimension at least $3$.
A line $g$ is *tangent* to a set $O$ of points at $P \in O$ if $g \cap O = \set{P}$.
An *ovoid* of $\mathcal{P}$ is a set $O$ of points such that:

1. every line meets $O$ in at most two points;
2. for every point $P \in O$, the union of the tangent lines to $O$ at $P$ is exactly a hyperplane through $P$.

## Remarks

The hyperplane in clause 2 is the tangent hyperplane of $O$ at $P$.
In a projective plane the same two conditions define an [[oval|7B03TB64N9]].

Example: in $\mathrm{PG}(3, q)$ over the [[finite field|0ZXZ82FTX2]] $\F_q$, an elliptic [[quadric|Q3Q4FF23VG]] is an ovoid.
It contains no line, so a line meets it in at most two points.
At each point, the tangent lines are the lines through that point in its tangent plane.
It has $q^2 + 1$ points.
In real projective $3$-space, a sphere is an ovoid.

Non-example: a hyperbolic quadric $x_0 x_1 = x_2 x_3$ contains whole lines, such as $x_0 = x_2 = 0$, so clause 1 fails.

In $\mathrm{PG}(3, q)$ every ovoid has $q^2 + 1$ points.
For $q = 2^{2e+1}$ with $e \ge 1$, Tits found ovoids that are not quadrics.
In finite projective spaces of dimension at least $4$ there are no ovoids.
