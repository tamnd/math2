---
tag: QCCD2JNFBT
kind: statement
role: theorem
name: Hopf–Rinow theorem
msc: [53C22, 53C20]
uses: [7CBT4SM83Y, B4QR306D8G, Y7Z0AGY1A7, NSYMQMHPDN, 0BY52JW6NK, 0TVJZYB6SH, 09QSZVVM26, 0ZCK8DQYN1]
about: [B4QR306D8G, NSYMQMHPDN]
sources:
  - url: https://en.wikipedia.org/wiki/Hopf%E2%80%93Rinow_theorem
same_as:
  wikidata: Q2094241
  wikipedia: Hopf–Rinow theorem
---

## Statement

Let $(M, g)$ be a connected [[Riemannian manifold|7CBT4SM83Y]] with [[Riemannian distance|B4QR306D8G]] $d$.
The following are equivalent:

1. the metric space $(M, d)$ is [[complete|0BY52JW6NK]];
2. every [[closed|0ZCK8DQYN1]] and [[bounded|09QSZVVM26]] subset of $M$ is [[compact|0TVJZYB6SH]];
3. there is a point $p \in M$ such that the [[exponential map|Y7Z0AGY1A7]] $\exp_p$ is defined on all of $T_pM$;
4. for every point $p \in M$, $\exp_p$ is defined on all of $T_pM$;
5. $M$ is geodesically complete: every [[geodesic|NSYMQMHPDN]] $\gamma$ can be extended to a geodesic defined on all of $\R$.

If these conditions hold, then any two points $p, q \in M$ are joined by a geodesic of length $d(p, q)$.

## Remarks

The key step is to show that if $\exp_p$ is defined on all of $T_pM$, then every $q$ is reached by a minimizing geodesic from $p$.
Choose a point $x$ nearest to $q$ on a small sphere around $p$, and follow the geodesic from $p$ through $x$.
One shows that it decreases the distance to $q$ at unit rate until it reaches $q$.
From this, bounded closed sets are closed subsets of images of compact balls under $\exp_p$, which gives the other conditions.
Example: $\R^n$ and every compact Riemannian manifold satisfy the conditions.
The open disc $\set{x \in \R^2 : \abs{x} < 1}$ with the Euclidean metric fails them: a radial geodesic leaves the disc in finite time, and the sequence $(1 - 1/k, 0)$ is Cauchy with no limit.
The last conclusion can hold without completeness, as in the open disc, so it is not equivalent to the conditions.

## Explanations

### L1 human

For a curved space, several natural meanings of "having no holes or missing edges" turn out to be the same.
One can never fall off the space by walking straight; Cauchy sequences converge; closed bounded regions are compact.
And when this holds, any two points are joined by a shortest path that is a geodesic.

### L2 human

The theorem is used constantly in global Riemannian geometry.
Completeness is a standing hypothesis in the theorems of Myers, Cartan–Hadamard and others, and one can check it in whichever form is easiest.
For example, compact manifolds and homogeneous Riemannian manifolds are complete.
It also shows that $\exp_p$ is surjective for complete $M$, which is the starting point for the study of the [[cut locus|X5WKGC5Q6T]].
The theorem fails for pseudo-Riemannian manifolds, where geodesic completeness and connection by geodesics behave differently.
