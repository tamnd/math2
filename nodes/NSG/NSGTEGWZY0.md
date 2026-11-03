---
tag: NSGTEGWZY0
kind: concept
name: Zeros and poles of a system
msc: [93C05, 93C80]
specializes: [1TE3QF8EYC]
sources:
  - url: https://en.wikipedia.org/wiki/Zeros_and_poles
---

## Summary

The poles of a linear time-invariant system are the points where its [[transfer function|86JKV3TRFD]] becomes infinite, and its zeros are the points where it vanishes.
They are the [[zeros and poles|1TE3QF8EYC]] of the transfer function as a rational function of the complex variable $s$.
The poles determine the natural modes and the stability of the system.
The zeros determine which input signals are blocked, and they limit what feedback can achieve.
For a minimal state-space model, the poles are the eigenvalues of the dynamics matrix.

## Explanations

### L1 human

Each pole corresponds to a natural motion of the system, like $e^{-t}$ for a pole at $-1$ or a growing $e^{t}$ for a pole at $1$.
A system is stable when all its poles lie in the left half of the complex plane, so that all natural motions die out.
A zero at $s_0$ means that the input $e^{s_0 t}$ produces no output in steady state.
For $G(s) = (s - 1)/((s + 1)(s + 2))$ the poles are $-1$ and $-2$, and the zero is $1$.
