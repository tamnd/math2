---
tag: DPS8QZBVB0
kind: concept
name: Relaxation of a variational problem
msc: [49J45]
sources:
  - url: https://en.wikipedia.org/wiki/Relaxation_(approximation)
---

## Summary

The relaxation of a variational problem replaces a functional $J$ that has no minimiser by its lower semicontinuous envelope $\bar J$.
This is the largest lower semicontinuous functional below $J$.
The relaxed problem has the same infimum as the original one.
Every limit of a minimising sequence of the original problem, in the topology used, is a minimiser of the relaxed problem.
For integral functionals, relaxation typically replaces the integrand by its convex or quasiconvex envelope in the gradient variable.

## Explanations

### L1 human

Sometimes a minimisation problem has no solution because minimising sequences oscillate faster and faster, like a zigzag with ever finer teeth.
The limit of such a sequence is a smooth function, but the original energy undervalues what the zigzags achieved.
Relaxation fixes the energy so that it assigns to each function the best value that nearby functions can approach.
Then the limit becomes a true minimiser of the corrected energy.
For the double-well cost $(\xi^2 - 1)^2$, relaxation replaces it by $0$ on $[-1, 1]$, because zigzags of slopes $\pm 1$ can produce any average slope in between at no cost.
