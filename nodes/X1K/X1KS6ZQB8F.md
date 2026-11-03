---
tag: X1KS6ZQB8F
kind: definition
name: Gravitational singularity
msc: ["83C75", "53C50"]
defines: 45AE2YXWT3
uses: [BY4QYYS788, NSYMQMHPDN]
sources:
  - url: https://en.wikipedia.org/wiki/Gravitational_singularity
---

## Definition

A *spacetime* is a connected, time-oriented [[Lorentzian manifold|BY4QYYS788]] $(M, g)$ of dimension $4$.
A spacetime $(M, g)$ is *extendible* if it embeds isometrically onto an open subset of a spacetime $(M', g')$, other than all of $M'$.
A spacetime $(M, g)$ is *singular*, or *has a gravitational singularity*, if:

1. $(M, g)$ is not extendible, and
2. some inextendible causal [[geodesic|NSYMQMHPDN]] of $(M, g)$ is incomplete, that is, its affine parameter does not take all real values.

## Remarks

The definition locates the singularity by its effect, the geodesics that end, and not as a set of points of $M$.
Clause 1 rules out spacetimes that are incomplete only because part of a larger spacetime has been cut away.
Smoothness classes matter: one usually asks for extensions of class $C^2$, and other classes give other notions.

Example: the maximal analytic extension of the [[Schwarzschild metric|6Y50T68WKY]], in Kruskal–Szekeres coordinates, is inextendible.
A timelike geodesic falling radially inward reaches $r = 0$ in finite proper time.
So it is singular.
The [[Kretschmann scalar|62JFWFJ20F]] $48M^2/r^6$ blows up along such a geodesic, which shows that no $C^2$ extension exists.

Non-example: the exterior region $r > 2M$ of the Schwarzschild metric, with its usual coordinates, also has incomplete radial geodesics.
But it embeds as a proper open subset of the Kruskal–Szekeres spacetime, so it is extendible and fails clause 1.
The coordinate singularity at $r = 2M$ is not a gravitational singularity.
Minkowski space is geodesically complete and fails clause 2.
