---
tag: 40ED6BYH7W
kind: concept
name: Control-Lyapunov function
msc: [93D30, 93D15, 93C10]
sources:
  - url: https://en.wikipedia.org/wiki/Control-Lyapunov_function
same_as:
  wikidata: Q5165805
  wikipedia: Control-Lyapunov function
---

## Summary

A control-Lyapunov function is a positive definite function $V$ on the state space of a [[control system|ZPDTVZQN5K]].
At each nonzero state, some input makes $V$ decrease.
It extends the idea of a [[Lyapunov function|01REYCJ371]] from systems without input to systems with input.
By [[Artstein's theorem|VH43JKVEQ1]], for control-affine systems its existence is equivalent to stabilizability by feedback, and [[Sontag's universal formula|NZB9W7J7DH]] turns it into an explicit feedback law.

## Explanations

### L1 human

Think of $V$ as an energy that is zero at the target state and positive elsewhere.
For a Lyapunov function the energy goes down by itself.
For a control-Lyapunov function it need not go down by itself, but at every state away from the target one can push with the control so that it goes down.
For $x' = x + u$ on the real line, the function $V(x) = x^2$ works: with $u = -2x$ one gets $V' = 2x(x + u) = -2x^2 < 0$ for $x \ne 0$.
