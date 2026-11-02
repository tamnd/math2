---
tag: CHEQ235HW9
kind: concept
name: Stability of a difference equation
msc: [39A30]
sources:
  - url: https://en.wikipedia.org/wiki/Lyapunov_stability
---

## Summary

An [[equilibrium|D62PEKHRV5]] of a difference equation is stable if solutions that start close to it stay close to it at all later times.
It is asymptotically stable if, in addition, nearby solutions converge to it.
These notions are the discrete-time versions of [[Lyapunov stability|0F2SYCKDT2]] for differential equations.
They decide which equilibria can be observed in practice, for example which population levels persist in a model.

## Explanations

### L1 human

Put a ball at the bottom of a bowl and nudge it: it stays near the bottom, so the bottom is stable.
Balance it on top of a hill and nudge it: it rolls away, so the top is unstable.
For the rule $x_{n+1} = x_n / 2$, the equilibrium $0$ is asymptotically stable: every solution halves at each step and tends to $0$.
For $x_{n+1} = 2 x_n$, the equilibrium $0$ is unstable: every nonzero start doubles away.
