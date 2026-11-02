---
tag: Z3AY2NEVW3
kind: definition
name: Plane curve
msc: [14H50]
defines: EWS4WFTA7W
uses: [XJM2MT4S3Y, ZT9A6JK8QF, 2C3PAQ7H50, 0SDC934R52]
sources:
  - url: https://en.wikipedia.org/wiki/Plane_curve
---

## Definition

Let $k$ be a field.
A *projective plane curve* over $k$ is the closed subscheme $C = V(F)$ of the [[projective plane|ZT9A6JK8QF]] $\mathbb{P}^2_k$ defined by a nonconstant [[homogeneous polynomial|2C3PAQ7H50]] $F \in k[x, y, z]$.
Its *degree* is $\deg F$.
An *affine plane curve* is the closed subscheme $V(f) \subset \mathbb{A}^2_k$ defined by a nonconstant polynomial $f$ in the [[polynomial ring|0SDC934R52]] $k[x, y]$.

## Remarks

The polynomial is determined by $C$ up to a nonzero scalar factor.
A plane curve is an [[algebraic curve|XJM2MT4S3Y]]: it has dimension $1$.
It is reduced exactly when $F$ has no repeated irreducible factor, and integral exactly when $F$ is irreducible.
Example: $F = x^2 + y^2 - z^2$ defines a conic of degree $2$ in $\mathbb{P}^2$, the projective closure of the circle $x^2 + y^2 = 1$.
Non-example: the twisted cubic $\set{[s^3 : s^2 t : s t^2 : t^3]} \subset \mathbb{P}^3$ is a curve in $\mathbb{P}^3$ that lies in no plane of $\mathbb{P}^3$, so it is not a plane curve inside $\mathbb{P}^3$.
As an abstract curve it is isomorphic to $\mathbb{P}^1$, which is a line in $\mathbb{P}^2$; being a plane curve is a property of the embedding.
A nonzero linear form vanishing on it would give a linear relation among $s^3, s^2 t, s t^2, t^3$, and there is none.
