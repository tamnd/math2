---
tag: H971WGMV6C
kind: concept
name: Symmetric operator
msc: [47B25, 47B02]
specializes: [BCJHNHKQFG]
sources:
  - url: https://en.wikipedia.org/wiki/Self-adjoint_operator
---

## Summary

A symmetric operator is a densely defined linear operator $T$ on a Hilbert space with $\ip{Tx}{y} = \ip{x}{Ty}$ for all $x, y$ in its domain.
For bounded operators defined on the whole space, symmetric is the same as self-adjoint.
For unbounded operators, such as differential operators, symmetry is weaker than self-adjointness.
The gap between the two is the subject of the theory of self-adjoint extensions.

## Explanations

### L1 human

A symmetric operator can move from one side of the inner product to the other, as a symmetric matrix does.
Think of $-i \tfrac{d}{dx}$ acting on smooth functions that vanish near the ends of an interval: integration by parts moves the derivative across the inner product with no boundary terms.
The operator is symmetric, but it is only defined on a small set of functions.
Choosing a larger domain on which it becomes self-adjoint is a real question, and the answer depends on boundary conditions.
