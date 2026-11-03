---
tag: 4YDCBSAJZ0
kind: concept
name: Dennis trace map
msc: [19D55, "16E40"]
sources:
  - url: https://en.wikipedia.org/wiki/Cyclic_homology
---

## Summary

The Dennis trace map is a natural homomorphism $K_n(R) \to HH_n(R)$ from the algebraic [[K-groups|5GVFZWMWC8]] of a ring to its [[Hochschild homology|S5H153HFWC]].
It extends the trace of matrices to higher K-theory.
It is the simplest of the trace maps that compare K-theory with homology theories that are easier to compute.
It lifts to negative [[cyclic homology|676K167XS8]], and in topology to topological Hochschild homology and topological cyclic homology.

## Explanations

### L1 human

The trace of a matrix is the sum of its diagonal entries, and it does not change under conjugation.
K-theory is built from invertible matrices up to conjugation and elementary moves, so a trace is a natural thing to apply to it.
The Dennis trace does this in every degree, with values in Hochschild homology.
In degree one, for a commutative ring, it sends a unit $u$ to the differential form $du/u$, a logarithmic derivative.
