---
tag: RSZFWWYP9E
kind: concept
name: Dissipative system
msc: [93D30, 93C10, 93D25]
sources:
  - url: https://en.wikipedia.org/wiki/Dissipative_system
---

## Summary

In systems and control theory, a dissipative system is a [[control system|ZPDTVZQN5K]] that cannot store more energy than is supplied to it from outside.
The stored energy is measured by a storage function on the state space.
The power supplied is measured by a supply rate, a function of the input and the output.
The theory, introduced by Jan C. Willems, generalizes [[Lyapunov functions|01REYCJ371]] to systems with inputs and outputs.
It contains passivity as the case where the supply rate is the product of input and output.
In physics, the term dissipative system also names open systems far from thermodynamic equilibrium, a different notion.

## Explanations

### L1 human

Think of an electrical circuit made of resistors, capacitors and coils.
The energy stored in it can only grow by the power pushed in at its terminals, and the resistors waste some of it as heat.
A dissipative system is any system with an energy-like quantity that obeys this rule.
For example, for $x' = -x + u$ with output $y = x$, the quantity $V = x^2/2$ changes at rate $-x^2 + uy$, which is never more than the supplied power $uy$.
