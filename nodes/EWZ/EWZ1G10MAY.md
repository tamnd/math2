---
tag: EWZ1G10MAY
kind: concept
name: Kodaira–Spencer map
msc: [32G05, 14D15]
sources:
  - url: https://en.wikipedia.org/wiki/Kodaira%E2%80%93Spencer_map
same_as:
  wikidata: Q6425091
  wikipedia: Kodaira–Spencer map
---

## Summary

The Kodaira–Spencer map of a [[deformation|VKQSM3BCE4]] measures how fast the complex structure of the fibre changes.
It sends a tangent vector of the base at $t$ to a class in $H^1(X_t, \Theta_{X_t})$.
Here $\Theta_{X_t}$ is the sheaf of holomorphic vector fields on the fibre $X_t$.
It vanishes identically for a trivial family, and it is the basic tool to decide whether a family is complete or effectively parametrized.
It is the first-order part of the deformation theory of compact complex manifolds.

## Explanations

### L1 human

A family of complex manifolds is glued, locally over the base, from pieces of a product.
Moving in the base changes the gluing maps, and the derivative of this change is a holomorphic vector field on each overlap.
These vector fields form a Čech cocycle, and its class in $H^1(X_t, \Theta_{X_t})$ does not depend on the choices.
If the class is zero, the complex structure does not change to first order in that direction.
For the family of elliptic curves $\C/(\Z + \tau\Z)$, the map is nonzero at every $\tau$.
