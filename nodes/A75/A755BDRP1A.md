---
tag: A755BDRP1A
kind: concept
name: Melnikov method
msc: [34C37, 34C28, 37C29]
sources:
  - url: https://en.wikipedia.org/wiki/Melnikov_distance
---

## Summary

The Melnikov method is a test for whether a [[homoclinic orbit|6DBSQKZK4W]] of a planar system survives a small periodic perturbation.
It reduces the question to the zeros of one explicit integral, the Melnikov function.
A simple zero of this function means that the stable and unstable manifolds of the perturbed saddle cross transversally.
Such a crossing forces chaotic dynamics nearby, so the method is a standard way to prove chaos in forced oscillators.
See the [[definition|BW7NGTGXAY]].

## Explanations

### L1 human

Think of an unforced system with a saddle point and a loop that leaves the saddle and comes back to it.
A small periodic push splits this loop into two curves: the set of points that go to the saddle and the set that come from it.
The Melnikov function measures, to first order in the size of the push, the signed gap between the two curves.
If the gap changes sign, the curves cross, and the crossings create very complicated motion.
For the forced, damped [[Duffing equation|SGQQGP261M]], the method says that crossings occur when the forcing is large enough compared with the damping.
