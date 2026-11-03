---
tag: 6XCFW7YGX8
kind: concept
name: Topological K-theory
msc: [55N15, 19L99]
specializes: [ZT11JGCWX0]
sources:
  - url: https://en.wikipedia.org/wiki/Topological_K-theory
same_as:
  wikidata: Q2111307
  wikipedia: Topological K-theory
---

## Summary

Topological K-theory assigns to a compact Hausdorff space $X$ the group $K^0(X)$ of formal differences of complex [[vector bundles|P4DZM975BV]] on $X$.
It extends to a [[generalized cohomology theory|H28PSZR7XG]] $K^n(X)$, which is periodic of period $2$ by the [[Bott periodicity theorem|WN2DCBSX1C]].
It was developed by Atiyah and Hirzebruch, following Grothendieck's work in algebraic geometry.
It gives short proofs of results such as the Hopf invariant one theorem and is the natural home of the Atiyah–Singer index theorem.

## Explanations

### L1 human

A vector bundle is a family of vector spaces, one over each point of a space, glued together continuously.
Over a sphere, such a family can be twisted, like a Möbius band is a twisted strip over a circle.
Topological K-theory counts vector bundles up to adding trivial ones, and turns this count into an abelian group.
For a point, the group is $\Z$, since a bundle over a point is just a vector space.
For the $2$-sphere, the group is $\Z \oplus \Z$: one copy for the dimension and one for the twisting.
