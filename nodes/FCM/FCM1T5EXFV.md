---
tag: FCM1T5EXFV
kind: concept
name: Primary obstruction
msc: [55S35]
specializes: [ZZWHGGFB4P]
sources:
  - url: https://en.wikipedia.org/wiki/Obstruction_theory
---

## Summary

The primary obstruction is the first obstruction that appears when one tries to extend a map into an $(n-1)$-connected space over a CW complex.
It is a single cohomology class in degree $n + 1$ with coefficients in $\pi_n$ of the target, and it does not depend on any choice.
Many characteristic classes, such as the Euler class of an oriented sphere bundle, are primary obstructions.

## Explanations

### L1 human

If the target space $Y$ has no holes in dimensions below $n$, a map can always be extended over cells of dimension at most $n$.
The first real difficulty comes with the cells of dimension $n + 1$.
The primary obstruction is the cohomology class that measures this difficulty.
Try to build a nonvanishing vector field on a closed oriented surface.
It can always be built over the vertices and edges, and the primary obstruction lives on the top cells.
There it equals the Euler characteristic of the surface times a generator.
