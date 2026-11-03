---
tag: NS0Q42Y3FX
kind: concept
name: Optimization problem
msc: [90C99, 90C30]
sources:
  - url: https://en.wikipedia.org/wiki/Optimization_problem
same_as:
  wikidata: Q984063
  wikipedia: Optimization problem
---

## Summary

An optimization problem asks for a best element of a set of allowed choices.
Here "best" means the smallest or largest value of a given objective function.
It consists of a set of candidates, [[constraints|X3663P90AE]] that cut out the [[feasible region|1TTKMRW8PD]], and the objective function.
A solution is a feasible point at which the objective attains its [[minimum or maximum|5X1YMSR204]] over the feasible region.
Linear programs, integer programs and shortest path problems are all optimization problems.

## Explanations

### L1 human

An optimization problem has three parts: what you may choose, which rules your choice must obey, and a score to make as small or as large as possible.
A delivery company chooses a route, must visit every customer, and wants the shortest total distance.
Some problems have no best choice.
If every positive number is allowed and the score is the number itself, you can always do a little better, but you never reach $0$.
A small example is to minimize $x^2 - 2x$ over all real $x$; the best choice is $x = 1$, with value $-1$.
