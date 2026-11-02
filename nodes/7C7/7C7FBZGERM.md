---
tag: 7C7FBZGERM
kind: concept
name: Nonlinear difference equation
msc: [39A05, 39A20]
specializes: [0FYX44GP92]
sources:
  - url: https://en.wikipedia.org/wiki/Recurrence_relation
---

## Summary

A nonlinear difference equation is a [[recurrence relation|0FYX44GP92]] in which the next term is not an affine function of the earlier terms.
Products, powers, quotients or other nonlinear functions of the earlier terms may appear.
Unlike linear recurrences, such equations rarely have closed-form solutions, and their solutions can converge, oscillate, or behave chaotically.
They model population dynamics, iterative numerical methods and many discrete-time systems.

## Explanations

### L1 human

In a linear recurrence, the next term is a weighted sum of earlier terms plus a known amount.
In a nonlinear one, the rule may square terms, multiply them, or divide by them.
The [[logistic map|QN9X9BNKTX]] $x_{n+1} = r x_n (1 - x_n)$ is a famous example.
For $r = 2$ and $x_0 = 0.1$ the values settle at $1/2$, but for $r = 4$ they jump around without any pattern.
