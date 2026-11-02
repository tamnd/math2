---
tag: ZCDWXVMDFN
kind: statement
role: theorem
name: Alexandrov's theorem on polyhedra
msc: [52B10, 53C45, 52C25]
uses: [0VKD1TP7F3, 300K6CB1KH, 0325SGSJAR]
about: [300K6CB1KH]
sources:
  - url: https://en.wikipedia.org/wiki/Alexandrov%27s_theorem_on_polyhedra
same_as:
  wikidata: Q17003552
  wikipedia: Alexandrov's theorem on polyhedra
---

## Statement

Let $M$ be a [[metric space|0VKD1TP7F3]] that is homeomorphic to the sphere $S^2$.
Assume that the distance between two points of $M$ is the infimum of the lengths of paths joining them.
Suppose that there is a finite set $S \subseteq M$ such that:

1. each point of $M \setminus S$ has a neighbourhood isometric to an open subset of the Euclidean plane;
2. each point $s \in S$ has a neighbourhood isometric to a neighbourhood of the apex of a Euclidean cone with total angle $\theta_s < 2\pi$.

Then there is a three-dimensional [[convex polytope|300K6CB1KH]] $P \subseteq \R^3$, or a doubly covered convex polygon $P$ in a plane, with the following property.
The surface of $P$, with its intrinsic path metric, is isometric to $M$.
This $P$ is unique up to an isometry of $\R^3$, and its vertices are exactly the points of $S$.

## Remarks

Uniqueness follows from a variant of [[Cauchy's rigidity theorem|CJ7KCDDF31]], applied to the two polytopes cut into matching triangles.
Alexandrov proved existence by a continuity argument.
Polytopes with $k$ vertices and metrics with $k$ cone points form spaces of the same dimension.
The map that sends a polytope to its surface metric is injective by the uniqueness part.
An invariance of domain argument then shows that it reaches every metric.
Bobenko and Izmestiev later gave a proof that is closer to a construction, but finding the edges of $P$ from $M$ is not easy in general.

Example: glue two copies of a unit square along their boundaries.
The result is a sphere with four cone points of angle $\pi$, and the theorem returns the doubly covered square itself.

The total angle condition is needed.
By [[Descartes's theorem on total angular defect|PT67C5ANSD]], the defects $2\pi - \theta_s$ of a convex polytope are positive and add up to $4\pi$.
So a metric with a cone point of angle larger than $2\pi$ cannot come from a convex polytope.

## Explanations

### L1 human

Cut out flat polygons and tape them together along their edges into a closed bag.
At each corner the paper angles must add up to less than a full turn.
Alexandrov's theorem says that the bag can be blown up into exactly one convex solid.
The creases of that solid need not be along the tape lines, which is the surprising part.

### L2 human

The theorem characterises the intrinsic metrics of convex polyhedral surfaces: they are exactly the polyhedral metrics on the sphere with positive curvature at every cone point.
It complements [[Cauchy's rigidity theorem|CJ7KCDDF31]], which gives uniqueness when the faces are known.
It has a smooth analogue, the Weyl problem, and it is used in computational geometry to fold a given net into a convex polyhedron.
