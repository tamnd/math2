---
tag: BTH3GSAWY3
kind: statement
role: theorem
name: Soul theorem
msc: [53C20, 53C21]
uses: [7CBT4SM83Y, 1X42JAA349, 0KZZ70ZHXP]
about: [1X42JAA349]
sources:
  - url: https://en.wikipedia.org/wiki/Soul_theorem
same_as:
  wikidata: Q4171386
  wikipedia: Soul theorem
---

## Statement

Let $(M, g)$ be a connected complete noncompact [[Riemannian manifold|7CBT4SM83Y]] with nonnegative [[sectional curvature|1X42JAA349]].
Then $M$ contains a compact, totally convex, totally geodesic embedded submanifold $S$ without boundary, called a *soul* of $M$.
Moreover, $M$ is [[diffeomorphic|0KZZ70ZHXP]] to the total space of the normal vector bundle of $S$ in $M$.

## Remarks

The theorem is due to Cheeger and Gromoll (1972).
The idea of the proof: fix a point $p$ and remove from $M$ the open balls $B(\gamma(t), t)$ for every ray $\gamma$ from $p$ and every $t > 0$.
The remaining set is compact, and it is totally convex by the Toponogov comparison theorem.
Shrinking this set step by step through levels of the distance to its boundary ends at a totally convex set without boundary, the soul.
A deformation along the gradient-like flow of the distance to $S$ gives the diffeomorphism with the normal bundle.

Example: the flat cylinder $S^1 \times \R$ has the soul $S^1 \times \set{0}$, and it is the normal bundle of this circle.
The paraboloid $z = x^2 + y^2$ has positive curvature, its soul is a single point, and it is diffeomorphic to $\R^2$.

A soul is not unique as a subset, but any two souls are isometric.
Perelman proved in 1994 the soul conjecture of Cheeger and Gromoll.
It says: if moreover the sectional curvature is positive at some point, then the soul is a point and $M$ is diffeomorphic to $\R^n$.

## Explanations

### L1 human

A complete, infinite space that is nowhere negatively curved has a compact core, the soul.
The whole space is this core with directions going off to infinity attached, like a cylinder around its central circle.
So the topology of the space is that of the soul.

### L2 human

The soul theorem reduces the topology of open manifolds with $K \ge 0$ to that of compact ones: $M$ is homotopy equivalent to its soul.
It is a main example of how Toponogov's comparison theorem is used to build convex sets.
