---
tag: 3VE9BSJQJA
kind: concept
name: Bilevel optimization
msc: [90C26, 91A65, 90C30]
sources:
  - url: https://en.wikipedia.org/wiki/Bilevel_optimization
same_as:
  wikidata: Q4907693
  wikipedia: Bilevel optimization
---

## Summary

Bilevel optimization studies problems in which one optimization problem is nested inside another as a constraint.
An upper-level decision maker, the leader, chooses variables knowing that a lower-level decision maker, the follower, will then optimize its own objective.
It models Stackelberg games, pricing and toll setting, and hyperparameter tuning in machine learning.
Bilevel problems are nonconvex in general, and even linear bilevel problems are NP-hard.

## Explanations

### L1 human

A city sets road tolls, and then drivers choose their routes to save money.
The city wants good revenue or low congestion, but it must predict how drivers will react to each choice of tolls.
So the city's problem contains the drivers' problem inside it.
Bilevel optimization is the study of such "optimize, knowing that someone else will then optimize" problems.
