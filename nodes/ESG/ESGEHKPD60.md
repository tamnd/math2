---
tag: ESGEHKPD60
kind: statement
role: theorem
name: Gauss–Bonnet theorem
msc: [53A05, 53C45, 57M50]
uses: [6080X3FAD4, SQVQ5DQT6W, 550P8PFMVC, RNDDWDAFJ5, 0TD904MG06]
about: [SQVQ5DQT6W, RNDDWDAFJ5]
sources:
  - url: https://en.wikipedia.org/wiki/Gauss–Bonnet_theorem
same_as:
  wikidata: Q742833
  wikipedia: Gauss–Bonnet theorem
---

## Statement

Let $S \subset \R^3$ be an [[oriented|0TD904MG06]] [[regular surface|6080X3FAD4]], and let $R \subset S$ be a compact region.
Assume that the boundary $\partial R$ is a finite union of simple closed, piecewise regular curves $C_1, \ldots, C_m$, positively oriented.
Let $\theta_1, \ldots, \theta_p$ be the external angles at the vertices of these curves.
Let $K$ be the [[Gaussian curvature|SQVQ5DQT6W]] of $S$, and let $k_g$ be the [[geodesic curvature|550P8PFMVC]] of the curves $C_i$.
Let $\chi(R)$ be the [[Euler characteristic|RNDDWDAFJ5]] of $R$.
Then
$$\int_R K \, dA + \sum_{i=1}^{m} \int_{C_i} k_g \, ds + \sum_{l=1}^{p} \theta_l = 2\pi \chi(R).$$
In particular, if $S$ is compact, then
$$\int_S K \, dA = 2\pi \chi(S).$$

## Remarks

The proof starts from the local case of a small simple region in one coordinate patch.
There the formula follows from Green's theorem, applied to the turning of a tangent vector along the boundary.
One then takes a [[triangulation|YH170WBQ6M]] of $R$ fine enough that each triangle lies in one patch, and adds the local formulas.
Interior edges are traversed twice in opposite directions, so their geodesic curvature terms cancel.
The angle terms then add up to $2\pi(V - E + F) = 2\pi\chi(R)$.

For the round sphere of radius $r$, one has $K = 1/r^2$ and area $4\pi r^2$, so the total curvature is $4\pi = 2\pi \cdot 2$, and indeed $\chi(S^2) = 2$.
For any torus in $\R^3$, the total curvature is $0$, since $\chi = 0$.
Compactness is needed for the second formula: the plane has $K = 0$ but $\chi = 1$.

The theorem extends to compact two-dimensional Riemannian manifolds, and the [[Chern–Gauss–Bonnet theorem|GG6NYPKMHX]] extends it to all even dimensions.

## Explanations

### L1 human

Gaussian curvature measures how a surface bends at each point.
The theorem says that if you add up all the curvature over a closed surface, you get $2\pi$ times a whole number that depends only on the topological shape.
So a sphere, however you dent it, always has total curvature $4\pi$.
A local, metric quantity is tied to a global, topological one.

### L2 human

The formula is the standard bridge between the local geometry and the topology of surfaces.
It shows that a compact surface with $K > 0$ everywhere must have $\chi > 0$, so it is a sphere when orientable.
Applied to a geodesic triangle, where $k_g = 0$, it gives $\int_T K \, dA = \alpha + \beta + \gamma - \pi$ for the interior angles $\alpha, \beta, \gamma$.
This explains why angle sums exceed $\pi$ on a sphere and fall short of $\pi$ on surfaces of negative curvature.
It is also the first case of the theory of characteristic classes, where the Euler class is represented by a curvature form.
