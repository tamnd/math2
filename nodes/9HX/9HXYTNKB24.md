---
tag: 9HXYTNKB24
kind: concept
name: Pontryagin–Thom construction
msc: [57R90, 55N22, 57R75]
sources:
  - url: https://en.wikipedia.org/wiki/Cobordism
---

## Summary

The Pontryagin–Thom construction starts from a closed submanifold with a tubular neighbourhood.
It gives a map from the ambient manifold to the [[Thom space|5MNYT3AFPH]] of the normal bundle.
It collapses everything outside the tubular neighbourhood to a point.
Pontryagin used it to identify framed [[cobordism|T8BVGPPSZP]] classes of submanifolds of spheres with [[homotopy groups of spheres|YD6VAXXSBM]].
Thom used it to compute cobordism groups as homotopy groups of Thom spaces, see [[Thom's cobordism theorem|HM23BV561Z]].

## Explanations

### L1 human

Picture a closed curve sitting inside a sphere, with a thin tube around it.
Squash everything outside the tube to a single point.
What remains is the tube with its outer wall glued to that point, and this only depends on the curve and how the tube is twisted.
Running the construction backwards, a map to a sphere gives back a submanifold as the preimage of a point.
For a single point in $S^n$ with a small ball around it, the construction gives a map $S^n \to S^n$ of degree $\pm 1$.
