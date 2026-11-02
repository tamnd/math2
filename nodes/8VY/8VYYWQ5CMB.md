---
tag: 8VYYWQ5CMB
kind: concept
name: Polyconvexity
msc: [49J45, 26B25, 74B20]
sources:
  - url: https://en.wikipedia.org/wiki/Polyconvex_function
same_as:
  wikidata: Q7226241
  wikipedia: Polyconvex function
---

## Summary

A function of an $m \times n$ matrix is polyconvex if it is a convex function of the matrix together with all its minors.
For $3 \times 3$ matrices the minors are the entries, the entries of the [[cofactor|0XPKR18APA]] matrix and the [[determinant|00KDZRW4C0]].
Polyconvexity implies [[Morrey quasiconvexity|DVJ17KVWXP]], and it is much easier to check.
It allows energies that blow up as the determinant tends to $0$, so it is the standard hypothesis on stored energies in nonlinear elasticity.

## Explanations

### L1 human

Convexity in the full gradient is too strong for elasticity, because it is incompatible with the fact that compressing a material to zero volume costs infinite energy.
Polyconvexity is a way around this.
One allows the energy to depend convexly on lengths, areas and volumes separately, that is, on the gradient, its cofactor and its determinant.
For example, for $2 \times 2$ matrices, $f(\xi) = \abs{\xi}^2 + (\det \xi)^2$ is polyconvex, since it is a convex function of $\xi$ and $\det \xi$.
