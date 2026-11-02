---
tag: MK5JGVDPS9
kind: concept
name: Backward difference operator
msc: [39A70, 39A12]
specializes: [7JSQZ126BP]
sources:
  - url: https://en.wikipedia.org/wiki/Finite_difference
---

## Summary

The backward difference operator $\nabla_h$ sends a function $f$ to the function $x \mapsto f(x) - f(x - h)$.
It looks one step back instead of one step ahead.
It is natural in time-stepping and interpolation schemes that use only values already computed.

## Explanations

### L1 human

The backward difference compares the value now with the value one step earlier.
If $u_n$ is the balance of an account at the end of month $n$, then $\nabla u_n = u_n - u_{n-1}$ is the change during month $n$.
For the squares $0, 1, 4, 9, 16$ the backward differences at $n = 1, 2, 3, 4$ are $1, 3, 5, 7$.
It is the forward difference read from the other end of the step: $\nabla_h f(x) = \Delta_h f(x - h)$.
