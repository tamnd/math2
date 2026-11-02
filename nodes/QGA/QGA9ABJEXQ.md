---
tag: QGA9ABJEXQ
kind: concept
name: Vanishing mean oscillation
msc: [42B35, 30H35]
specializes: [QJYTXFT8Y4]
sources:
  - url: https://en.wikipedia.org/wiki/Bounded_mean_oscillation
---

## Summary

A function has vanishing mean oscillation if it has [[bounded mean oscillation|QJYTXFT8Y4]] and its mean oscillation over cubes tends to zero as the cubes shrink.
The space VMO plays, inside BMO, the role that continuous functions play inside bounded functions.
It contains all uniformly continuous functions in BMO, and also some unbounded functions.
It was introduced by Sarason, and it appears in the theory of Toeplitz and Hankel operators, of commutators, and of elliptic equations with discontinuous coefficients.

## Explanations

### L1 human

A BMO function may oscillate at every scale, as long as the oscillation stays bounded.
A VMO function must become calm at small scales: on tiny cubes it is nearly equal to its average.
Uniformly continuous functions with bounded oscillation have this property, but so do some functions with very mild singularities.
The function $\log \abs{x}$ is in BMO but not in VMO, because zooming in at $0$ shows the same oscillation at every scale.
