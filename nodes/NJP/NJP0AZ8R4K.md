---
tag: NJP0AZ8R4K
kind: problem
name: Minkowski problem
msc: [52A20, 52A39, 35J96]
uses: [437FSG3419, T62369RFH6, Q1TGZK8RN6, SQVQ5DQT6W, 14AKAC0S0T]
about: [437FSG3419]
sources:
  - url: https://en.wikipedia.org/wiki/Minkowski_problem
same_as:
  wikidata: Q4183831
  wikipedia: Minkowski problem
history:
  posed_by: "Hermann Minkowski"
  first_stated: "1897"
---

## Problem

Let $n \ge 2$, and let $S^{n-1}$ be the unit [[sphere|T62369RFH6]] of $\R^n$.
Let $\mathcal{H}^{n-1}$ be the $(n-1)$-dimensional [[Hausdorff measure|Q1TGZK8RN6]].
Let $K \subseteq \R^n$ be a [[convex body|437FSG3419]] and $\omega \subseteq S^{n-1}$ a Borel set.
Let $N_K(\omega)$ be the set of boundary points of $K$ with an outer unit normal in $\omega$.
The *surface area measure* of $K$ is the Borel measure $S_K(\omega) = \mathcal{H}^{n-1}(N_K(\omega))$ on $S^{n-1}$.
Let $\mu$ be a finite Borel measure on $S^{n-1}$.
Find a convex body $K$ with $S_K = \mu$, and decide when such a body exists and whether it is unique.

## Remarks

The problem is solved.
A convex body $K$ with $S_K = \mu$ exists if and only if $\mu$ is not concentrated on a great subsphere of $S^{n-1}$ and $\int_{S^{n-1}} u \, d\mu(u) = 0$.
The body is then unique up to translation.
Minkowski solved the case of polytopes.
Let $u_1, \ldots, u_m$ be distinct unit vectors spanning $\R^n$, and let $a_1, \ldots, a_m > 0$ with $\sum_i a_i u_i = 0$.
Then there is a polytope, unique up to translation, whose facets have outer normals $u_i$ and areas $a_i$.
The general case is due to Minkowski, Alexandrov, and Fenchel and Jessen.
When $\mu$ has a positive density $f$, the problem asks for a body whose [[Gaussian curvature|SQVQ5DQT6W]] at the point with outer normal $u$ is $1 / f(u)$.
This is a [[Monge–Ampère equation|14AKAC0S0T]] on the sphere.
The regularity of its solutions was studied by Pogorelov and by Cheng and Yau.
Example: the uniform measure $\mu = c \, \sigma$ on $S^{n-1}$, with $\sigma$ the surface measure and $c > 0$, is the surface area measure of a ball of radius $c^{1/(n-1)}$.

## Explanations

### L1 human

Suppose you know, for each direction, how much of the surface of a convex shape faces that direction.
Can you rebuild the shape?
Minkowski's answer is yes, up to sliding it around, provided the data are balanced: the outward pulls of all the pieces of surface must cancel.
For a polyhedron, the data are the directions and areas of its faces.
