---
tag: MJBXNNFQGW
kind: definition
name: Tight and overtwisted contact structures
msc: [57K33, 53D10]
defines: WQQX6SAQ5A
uses: [HBQ8BZ7XB5, Q2DMSTWZYZ, R20TB2KEQQ]
sources:
  - url: https://en.wikipedia.org/wiki/Contact_geometry
---

## Definition

Let $M$ be a [[$3$-manifold|R20TB2KEQQ]] and let $\xi$ be a contact structure on $M$, so that $(M, \xi)$ is a [[contact manifold|HBQ8BZ7XB5]].
An *overtwisted disc* in $(M, \xi)$ is an embedded closed disc $D \subset M$ such that:

1. the boundary $\partial D$ is a [[Legendrian|Q2DMSTWZYZ]] curve, that is, tangent to $\xi$;
2. for every $x \in \partial D$, the plane $\xi_x$ equals the tangent plane $T_x D$.

The contact structure $\xi$ is *overtwisted* if $(M, \xi)$ contains an overtwisted disc, and *tight* otherwise.

## Remarks

Example: on $\R^3$ with cylindrical coordinates $(r, \theta, z)$, the form $\alpha = \cos r\, dz + r \sin r\, d\theta$ is a contact form.
The disc $D = \set{z = 0, \ r \le \pi}$ is overtwisted: on its boundary $r = \pi$ one has $\alpha = -dz$, so $\xi = \ker dz$ is the horizontal plane, which is $T_x D$, and the boundary circle is tangent to it.
So this contact structure is overtwisted.

Non-example: the standard contact structure $\ker(dz - y\,dx)$ on $\R^3$ is tight, by Bennequin's theorem, so no disc satisfies both clauses.

Clause 2 says that the framing of $\partial D$ given by the contact planes agrees with the framing given by $D$.
In other words, the Legendrian unknot $\partial D$ has Thurston–Bennequin number $0$.
Eliashberg proved that two overtwisted contact structures on a closed $3$-manifold are isotopic if and only if they are homotopic as plane fields.
He also proved that every homotopy class of plane fields contains an overtwisted contact structure.
Tight contact structures are much rarer; for example, $S^3$ has a unique tight contact structure up to isotopy, also by Eliashberg.
