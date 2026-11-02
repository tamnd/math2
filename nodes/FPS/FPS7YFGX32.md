---
tag: FPS7YFGX32
kind: concept
name: Floquet multiplier
msc: [34C25, 34A30, 34D08]
specializes: [0BQAA2BK3Q]
sources:
  - url: https://en.wikipedia.org/wiki/Floquet_theory
---

## Summary

The Floquet multipliers of a linear system with periodic coefficients are the eigenvalues of its monodromy matrix, the map that advances solutions by one period.
They play the role that the values $e^{\lambda T}$ play for a system with constant coefficients.
They decide whether solutions grow, decay or stay bounded, and they measure the stability of a [[periodic orbit|0AA97XA70K]] of a nonlinear system.
They are the central notion of [[Floquet theory|BJVZXPB297]].
See the [[definition|GVSY2FZ8YW]].

## Explanations

### L1 human

Watch a solution of a periodic linear system only at the times $0, T, 2T, \ldots$, once per period.
From one snapshot to the next, the state is multiplied by a fixed matrix $M$.
The eigenvalues of $M$ are the Floquet multipliers.
If all have absolute value less than $1$, every solution shrinks to $0$; if one has absolute value greater than $1$, some solution grows without bound.
For the scalar equation $x' = (1 + \cos t)\, x$, one period multiplies $x$ by $e^{2\pi}$, so the multiplier is $e^{2\pi}$.
