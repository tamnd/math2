---
tag: HZY2EWWKB5
kind: definition
name: Translation plane
msc: ["51A40", "51E15"]
defines: JZ5J6REAMD
uses: [DANFNN8C4Y, V7PRPN24CV, JQ22QH86DE]
sources:
  - url: https://en.wikipedia.org/wiki/Translation_plane
---

## Definition

Let $\Pi$ be a [[projective plane|DANFNN8C4Y]] and let $\ell$ be a line of $\Pi$.
An *elation with axis $\ell$* is a [[collineation|V7PRPN24CV]] $\alpha$ of $\Pi$ with two properties.
It fixes every point of $\ell$, and for some point $C$ on $\ell$ it maps every line through $C$ to itself.
The plane $\Pi$ is a *translation plane with respect to $\ell$* if the following holds.
For any two points $P$ and $Q$ not on $\ell$, some elation with axis $\ell$ maps $P$ to $Q$.
The line $\ell$ is then a *translation line* of $\Pi$.

## Remarks

Example: let $F$ be a field and let $\Pi$ be the projective plane over $F$, with $\ell$ the line at infinity.
For $(a, b) \in F^2$, the translation $(x, y) \mapsto (x + a, y + b)$ of $F^2$ maps lines to parallel lines, so it extends to a collineation of $\Pi$ that fixes every point at infinity.
If $(a, b) \ne (0, 0)$, it maps each line of direction $(a, b)$ to itself.
So it fixes every line through the point at infinity $C$ of that direction, and it is an elation with axis $\ell$.
The translation by $Q - P$ maps $P$ to $Q$, so $\Pi$ is a translation plane with respect to $\ell$.

Non-example: the Hughes plane of order $9$ is a projective plane that is not a translation plane with respect to any of its lines.

When $\Pi$ is a translation plane with respect to $\ell$, the elations with axis $\ell$ form an abelian group that acts regularly on the points off $\ell$.
The translation planes are exactly the planes coordinatized by [[quasifields|JQ22QH86DE]].
