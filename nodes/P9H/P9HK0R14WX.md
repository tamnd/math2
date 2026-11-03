---
tag: P9HK0R14WX
kind: concept
name: Lagrangian relaxation
msc: [90C46, 90C10, 90C27]
sources:
  - url: https://en.wikipedia.org/wiki/Lagrangian_relaxation
same_as:
  wikidata: Q3424292
  wikipedia: Lagrangian relaxation
---

## Summary

Lagrangian relaxation removes difficult constraints of an optimization problem and adds them to the objective with a penalty price, a Lagrange multiplier.
For every choice of nonnegative multipliers, the relaxed problem gives a bound on the optimal value of the original problem.
The best such bound is the value of the Lagrangian dual, a convex problem usually solved by the [[subgradient method|890BD5TQ0H]].
For [[integer programs|9GX3WH5EQF]] it gives bounds at least as strong as the [[linear programming relaxation|PYMHHM5Z6F]], and it is the integer counterpart of [[Lagrangian duality|QRXXH28W3A]].

## Explanations

### L1 human

Some constraints make a problem hard, for example a budget shared by many otherwise separate projects.
Lagrangian relaxation drops the shared budget and instead charges a price for each unit of budget used.
With the price in place, the projects can be planned separately and easily.
The result is always at least as good as the true best plan, so it is a bound.
Adjusting the price to make this bound as tight as possible gives a close estimate, and often a near-feasible plan.
