---
tag: 37TRG5DBQC
kind: concept
name: Koopman operator
msc: [37A30, 47B33, 37A05]
specializes: [CFASPSF7BB]
sources:
  - url: https://en.wikipedia.org/wiki/Composition_operator
---

## Summary

The Koopman operator of a [[measure-preserving transformation|556WBDAHNP]] $T$ acts on functions by $f \mapsto f \circ T$.
It is the [[composition operator|CFASPSF7BB]] with symbol $T$ on the space $L^2$ of the invariant measure.
There it is an isometry, and a [[unitary operator|MM0EJ2GDE4]] when $T$ is invertible.
It turns a nonlinear dynamical system into a linear operator on a Hilbert space.
Ergodicity, weak mixing and mixing all become properties of this operator, which is the starting point of the [[spectral theory of dynamical systems|Z7GZ6SPFA5]].

## Explanations

### L1 human

Instead of following points, follow measurements.
A measurement is a function $f$ on the space, and after one step of the system the new measurement is $f \circ T$: measure where the point has moved to.
This rule is linear in $f$ even when $T$ is very nonlinear.
For a rotation $T(x) = x + \alpha$ of the circle, the function $e^{2\pi i x}$ becomes $e^{2\pi i \alpha} e^{2\pi i x}$, so it is an eigenfunction with eigenvalue $e^{2\pi i \alpha}$.
