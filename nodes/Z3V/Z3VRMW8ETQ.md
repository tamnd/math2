---
tag: Z3VRMW8ETQ
kind: statement
role: theorem
name: Myers–Steenrod theorem
msc: [53C20, "22E15"]
uses: [7CBT4SM83Y, B4QR306D8G, R9YWQS15AA, 0TVJZYB6SH]
about: [R9YWQS15AA]
sources:
  - url: https://en.wikipedia.org/wiki/Myers%E2%80%93Steenrod_theorem
same_as:
  wikidata: Q6947443
  wikipedia: Myers–Steenrod theorem
---

## Statement

Let $(M, g)$ and $(N, h)$ be connected [[Riemannian manifolds|7CBT4SM83Y]] with [[Riemannian distances|B4QR306D8G]] $d_g$ and $d_h$.

1. If $\varphi \colon M \to N$ is a surjective map with $d_h(\varphi(p), \varphi(q)) = d_g(p, q)$ for all $p, q \in M$, then $\varphi$ is smooth and is an [[isometry of Riemannian manifolds|R9YWQS15AA]].
2. The group $\operatorname{Isom}(M, g)$ of all isometries of $(M, g)$ onto itself, with the compact-open topology, is a Lie group, and its action on $M$ is smooth.
3. If $M$ is [[compact|0TVJZYB6SH]], then $\operatorname{Isom}(M, g)$ is compact.

## Remarks

The idea of part 1 is that a distance-preserving map sends minimizing geodesics to minimizing geodesics, so in normal coordinates it acts as a linear isometry, and this forces smoothness.
For part 2, note that an isometry of a connected Riemannian manifold is determined by its value and its differential at one point.
So $\operatorname{Isom}(M, g)$ embeds in the orthonormal frame bundle of $M$, and one shows that the image is a closed submanifold.
For the round sphere $S^n$, the theorem gives $\operatorname{Isom}(S^n) = O(n + 1)$, a compact Lie group of dimension $n(n + 1)/2$.
The theorem is about Riemannian (positive definite) metrics; a pseudo-Riemannian metric defines no distance function.

## Explanations

### L1 human

If a map between two curved spaces keeps all distances, it automatically keeps the whole smooth geometry, with no further hypothesis.
Also, the symmetries of a curved space form a group that behaves like a group of matrices, with a finite number of independent directions of motion.

### L2 human

Part 1 lets one pass freely between the metric-space view of a Riemannian manifold and its smooth view.
Part 2 is the starting point for the study of homogeneous and symmetric spaces.
A Riemannian manifold whose isometry group acts transitively is $G/H$, with $G$ a Lie group and $H$ a compact subgroup.
The Lie algebra of $\operatorname{Isom}(M, g)$ is identified with the complete [[Killing vector fields|5AKNNW3W4Z]] of $M$.
