---
tag: XEAVQFJR1B
kind: concept
name: Criss-cross algorithm
msc: [90C05, 90C49]
sources:
  - url: https://en.wikipedia.org/wiki/Criss-cross_algorithm
same_as:
  wikidata: Q17006040
  wikipedia: Criss-cross algorithm
---

## Summary

The criss-cross algorithm is a pivoting method for linear programming that moves between bases which need be neither primal feasible nor dual feasible.
Unlike the [[simplex algorithm|MH272QHWPM]], it needs no feasible starting basis and does not keep the objective monotone.
Its least-index form uses choices in the spirit of [[Bland's rule|YM58206VR1]].
In this form it ends after finitely many pivots with an optimal basis or a proof that no optimum exists.
Its worst-case number of steps is exponential, as for the simplex method.

## Explanations

### L1 human

The simplex method insists on staying inside the feasible region at every step.
The criss-cross method drops that rule: it may visit "bases" that break some constraints, and it repairs one violated condition at a time.
Each step looks for the lowest-numbered thing that is wrong, either a negative variable or an improving direction, and fixes it by one exchange.
This plain rule is enough to guarantee that it stops, and it starts from any basis, so no separate first phase is needed.
