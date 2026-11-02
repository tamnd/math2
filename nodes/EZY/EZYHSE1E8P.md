---
tag: EZYHSE1E8P
kind: concept
name: Steenrod reduced power
msc: [55S10, 55S05]
specializes: [K8T15QHN3W]
sources:
  - url: https://en.wikipedia.org/wiki/Steenrod_algebra
---

## Summary

For an odd prime $p$, the Steenrod reduced powers $P^i$ are [[cohomology operations|K8T15QHN3W]] on mod $p$ [[singular cohomology|6N7BC70CX0]] that raise degree by $2i(p-1)$.
They play for odd primes the role that the Steenrod squares play for the prime $2$.
Together with the Bockstein homomorphism they generate all stable mod $p$ cohomology operations.
They detect maps that ordinary cohomology groups and [[cup products|JX47MS1R1H]] cannot see.

## Explanations

### L1 human

Cohomology with coefficients in $\F_p$ already has a product, so a class $x$ has a $p$-th power $x^p$.
The reduced power $P^i$ is a natural way to produce new classes from $x$ that interpolate between $x$ itself and $x^p$.
If $x$ has degree $2i$, then $P^i x = x^p$, and if the degree of $x$ is less than $2i$, then $P^i x = 0$.
For example, on $\C P^\infty$ with generator $x$ of degree $2$, one has $P^1 x = x^p$.
Because these operations commute with every map of spaces, a space where they act differently from another space cannot be homotopy equivalent to it.
