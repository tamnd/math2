---
tag: XZ3BMJARBR
kind: definition
name: Fermat point
msc: [51M04, 51M16]
defines: QM0CGSQ4TF
uses: [0CTNFGYMM2, 0NPPGHQNXQ]
sources:
  - url: https://en.wikipedia.org/wiki/Fermat_point
---

## Definition

Let $ABC$ be a [[triangle|0CTNFGYMM2]] in the Euclidean plane, and let $d$ be the [[Euclidean distance|0NPPGHQNXQ]].
The *Fermat point* of $ABC$ is the unique point $F$ of the plane that minimises
$$f(P) = d(P, A) + d(P, B) + d(P, C).$$

## Remarks

A minimiser exists because $f$ is continuous and tends to infinity far away; it is unique because $f$ is strictly convex when $A$, $B$, $C$ are not collinear.
If each angle of $ABC$ is less than $120^\circ$, then $F$ is the interior point with $\angle AFB = \angle BFC = \angle CFA = 120^\circ$.
In that case $F$ is also the common point of the lines that join each vertex to the apex of the outward equilateral triangle on the opposite side.
If the angle at a vertex is at least $120^\circ$, then $F$ is that vertex.
The point is also called the Torricelli point.

Example: in an equilateral triangle the centre $O$ sees each side under $120^\circ$ by symmetry, so $F = O$.

Non-example: take $A = (0, 0)$, $B = (1, 0)$, $C = (0, 1)$ and the [[centroid|0X7EEWES5G]] $G = (1/3, 1/3)$.
Then $f(G) = (\sqrt 2 + 2\sqrt 5)/3 \approx 1.962$.
All angles are below $120^\circ$, and the minimum of $f$ is $\sqrt{2 + \sqrt 3} \approx 1.932$, so $G$ is not the Fermat point.
