---
tag: DT49GKR9AS
kind: concept
name: Essentially self-adjoint operator
msc: [47B25]
specializes: [H971WGMV6C]
sources:
  - url: https://en.wikipedia.org/wiki/Self-adjoint_operator
---

## Summary

An essentially self-adjoint operator is a symmetric operator on a Hilbert space whose closure is self-adjoint.
Such an operator has exactly one self-adjoint extension, so it determines a unique quantum observable and a unique spectral theory.
In practice, differential operators are first defined on small spaces of smooth functions, and essential self-adjointness is what makes this choice harmless.

## Explanations

### L1 human

Unbounded operators, such as derivatives, can only be defined on part of a Hilbert space, and the choice of this part matters.
A symmetric operator on a small domain may admit many self-adjoint extensions, which correspond to different boundary conditions and different physics.
An essentially self-adjoint operator leaves no choice: there is exactly one way to extend it to a self-adjoint operator.
For example, $-i \, d/dx$ on smooth compactly supported functions on the whole line $\R$ is essentially self-adjoint, because the line has no boundary where a condition could be imposed.
