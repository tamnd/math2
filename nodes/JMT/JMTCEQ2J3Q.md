---
tag: JMTCEQ2J3Q
kind: concept
name: Complementarity theory
msc: [90C33]
sources:
  - url: https://en.wikipedia.org/wiki/Complementarity_theory
same_as:
  wikidata: Q5156417
  wikipedia: Complementarity theory
---

## Summary

Complementarity theory studies problems of finding a vector $x$ such that $x$ and $F(x)$ are nonnegative and orthogonal.
Then in each coordinate at least one of them is zero.
Such conditions express equilibrium: a price is positive only where supply equals demand, a contact force acts only where two bodies touch.
They arise as optimality conditions in [[nonlinear programming|RAQB00X634]], as in [[complementary slackness|EB54YVJ7SM]] and the [[Karush–Kuhn–Tucker conditions|HDWEPH4YG4]].
The [[linear complementarity problem|8G30AFBZNQ]] is the central special case, and complementarity problems over cones are special [[variational inequalities|6QS7X5GVMY]].

## Explanations

### L1 human

Think of pairs of switches: in each pair, at least one switch must be off.
For a vector $x$ and a vector $w = F(x)$, both with nonnegative entries, complementarity asks that $x_i w_i = 0$ for every $i$.
For example, with one variable and $F(x) = x - 1$, the solution is $x = 1$: there $x > 0$ and $F(x) = 0$.
