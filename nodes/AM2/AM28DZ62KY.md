---
tag: AM28DZ62KY
kind: concept
name: Chance-constrained programming
msc: [90C15]
specializes: [2YW60J1GT6]
sources:
  - url: https://en.wikipedia.org/wiki/Chance_constrained_programming
same_as:
  wikidata: Q131124952
  wikipedia: Chance constrained programming
---

## Summary

Chance-constrained programming is the part of [[stochastic programming|2YW60J1GT6]] in which constraints with random data need only hold with a prescribed probability.
A typical requirement is that a system meets demand or stays safe with probability at least $95\%$.
This avoids both ignoring the risk and insisting on the worst case, as [[robust optimization|MRNW9644HH]] does.
The feasible sets can be nonconvex.
But for normal data in one linear constraint with risk level at most $50\%$, they have explicit convex forms.

## Explanations

### L1 human

A power company cannot be sure how much electricity people will use tomorrow.
Planning for the absolute worst case is too expensive, but being short too often is unacceptable.
A chance constraint says: be short on at most $1\%$ of days.
Chance-constrained programming finds the cheapest plan that keeps this promise.
