---
tag: 6J9FXT6HAV
kind: concept
name: Limit-point and limit-circle
msc: [34B20, 34B24, 34L05]
sources:
  - url: https://en.wikipedia.org/wiki/Sturm–Liouville_theory
---

## Summary

For a singular [[Sturm–Liouville|7WV6B2502K]] equation, each singular endpoint is either in the limit-point case or in the limit-circle case.
In the limit-circle case every solution is square integrable near the endpoint; in the limit-point case some solution is not.
This dichotomy, found by Hermann Weyl, tells whether a boundary condition is needed at that endpoint to get a self-adjoint operator.
At a limit-point end no boundary condition is needed, and at a limit-circle end one must be imposed.

## Explanations

### L1 human

Near a bad endpoint, such as $+\infty$, solutions of the equation may be small enough to be square integrable or may be too big.
If all of them are small, the endpoint behaves almost like an ordinary endpoint and one must choose a boundary condition there.
If some of them are too big, the endpoint chooses for itself.
For $-y'' = 0$ on $(0, \infty)$ the solutions $1$ and $x$ are not square integrable near $\infty$, so $\infty$ is a limit-point end.
The name comes from Weyl's picture of a shrinking family of circles in the complex plane, which tend either to a point or to a circle.
