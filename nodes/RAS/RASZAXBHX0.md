---
tag: RASZAXBHX0
kind: concept
name: Reduced K-theory of a space
msc: [55N15, 55R50]
sources:
  - url: https://en.wikipedia.org/wiki/Topological_K-theory
---

## Summary

The reduced K-theory $\tilde{K}(X)$ of a pointed compact space $X$ is the part of $K(X)$ that ignores the rank at the base point.
It is the kernel of the restriction map from $K(X)$ to the K-theory of the base point, which is $\Z$.
It plays the role of reduced cohomology, and it is the form of K-theory in which [[Bott periodicity|WN2DCBSX1C]] and the [[K-theory of spheres|4NH8D0BDX0]] are stated.

## Explanations

### L1 human

Every vector bundle has a rank, and the rank alone gives an uninteresting copy of $\Z$ inside $K(X)$.
Reduced K-theory removes this copy and keeps only the information about how bundles twist.
One way to see it: two bundles are called stably equivalent when they become isomorphic after adding trivial bundles.
The stable equivalence classes form the group $\tilde{K}(X)$.
For example, on the $2$-sphere the twisting of the tautological line bundle $H$ gives the element $[H] - 1$, which generates $\tilde{K}(S^2) \cong \Z$.
