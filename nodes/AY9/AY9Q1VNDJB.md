---
tag: AY9Q1VNDJB
kind: concept
name: Penalty method
msc: [90C30, 65K05]
sources:
  - url: https://en.wikipedia.org/wiki/Penalty_method
same_as:
  wikidata: Q3411771
  wikipedia: Penalty method
---

## Summary

A penalty method replaces a [[constrained optimisation|0EPW94MJ1P]] problem by a sequence of unconstrained problems.
Each one minimizes the objective plus a penalty term that is zero on the feasible set and positive outside it, multiplied by a parameter.
As the parameter grows, the minimizers of the penalized problems approach a solution of the constrained problem.
The method is simple, but large parameters make the subproblems ill-conditioned, which motivates the augmented Lagrangian method.

## Explanations

### L1 human

Instead of forbidding infeasible points, you let the search go anywhere but charge a fine for breaking the rules.
The fine grows with how badly a constraint is broken, and you raise its price step by step.
To minimize $x$ subject to $x = 1$, you minimize $x + \frac{\mu}{2}(x - 1)^2$ instead.
Its minimizer is $1 - 1/\mu$, which tends to the true answer $1$ as the price $\mu$ grows.
