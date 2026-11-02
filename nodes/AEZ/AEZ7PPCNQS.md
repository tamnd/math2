---
tag: AEZ7PPCNQS
kind: concept
name: Perron method
msc: [31B20, 31A25, 35J25]
sources:
  - url: https://en.wikipedia.org/wiki/Perron_method
same_as:
  wikidata: Q7169664
  wikipedia: Perron method
---

## Summary

The Perron method solves the [[Dirichlet problem|8D56GQ4AG8]] for the Laplacian on an arbitrary bounded open set.
It takes the upper envelope of all [[subharmonic functions|Z1MHMGFNFW]] that lie below the boundary data at the boundary.
This envelope is always harmonic; the only question is whether it takes the right boundary values.
That question is local and leads to barriers and regular boundary points.

## Explanations

### L1 human

You want a harmonic function with given values on the boundary.
Look at all subharmonic functions that stay below these values near the boundary, and at each point take the largest value any of them reaches.
Subharmonic functions sag below harmonic ones, so this supremum is the best harmonic candidate.
On the unit disc with boundary values $\cos\theta$, the supremum is the harmonic function $x$.
