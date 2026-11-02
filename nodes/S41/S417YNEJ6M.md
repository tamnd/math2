---
tag: S417YNEJ6M
kind: concept
name: Kernel
msc: [18A30, "18E05"]
sources:
  - url: https://en.wikipedia.org/wiki/Kernel_(category_theory)
same_as:
  wikidata: Q2920416
  wikipedia: Kernel (category theory)
---

## Summary

In a category with zero morphisms, the kernel of a morphism $f$ is the universal morphism $k$ with $f \circ k = 0$.
It is the [[equalizer|CTJ5AD8ST5]] of $f$ and the zero morphism.
In categories of groups, modules or vector spaces it is the inclusion of the usual [[kernel|0W88CEGQP1]], the set of elements sent to zero.
Kernels and their dual notion, cokernels, are the building blocks of abelian categories.

## Explanations

### L1 human

The kernel of a linear map is the set of vectors that it sends to zero.
Category theory cannot look at elements, so it describes this subspace by a property of its inclusion map.
The inclusion is killed by $f$, and every other map that is killed by $f$ passes through it in exactly one way.
For the map $\Z \to \Z/2$ that reduces mod $2$, the kernel is the inclusion of the even integers $2\Z \to \Z$.
