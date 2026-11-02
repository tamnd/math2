---
tag: GK4P8G0PB2
kind: concept
name: Rank-one convexity
msc: [49J45, 26B25]
sources:
  - url: https://en.wikipedia.org/wiki/Quasiconvexity_(calculus_of_variations)
---

## Summary

A function on $m \times n$ matrices is rank-one convex if it is convex along every line in a rank-one direction $a \otimes b$.
It is the weakest of the convexity notions used in the vectorial calculus of variations.
Polyconvexity implies quasiconvexity, which implies rank-one convexity, and each is implied by ordinary [[convexity|07GR3TNW4H]].
For $C^2$ integrands it is the Legendre–Hadamard condition at every matrix.

## Explanations

### L1 human

Two matrices that differ by a rank-one matrix can be the gradients of one continuous map on the two sides of a flat interface.
Fine layers of two such gradients form a laminate, and a laminate can mimic the average gradient.
Rank-one convexity says that such layering never lowers the energy below its value at the average.
For $2 \times 2$ matrices the determinant is rank-one convex, in fact affine along rank-one lines, but it is not convex.
