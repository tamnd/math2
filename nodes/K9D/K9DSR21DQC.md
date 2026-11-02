---
tag: K9DSR21DQC
kind: concept
name: Hypoelliptic operator
msc: [35H10]
sources:
  - url: https://en.wikipedia.org/wiki/Hypoelliptic_operator
same_as:
  wikidata: Q4138816
  wikipedia: Hypoelliptic operator
---

## Summary

A hypoelliptic operator is a linear differential operator $P$ with smooth coefficients such that every distribution $u$ with $Pu$ smooth is itself smooth.
So $P$ cannot create singularities in its solutions that are not already in the right-hand side.
[[Elliptic operators|XY8GEQSWPR]] with smooth coefficients are hypoelliptic, and so is the heat operator, which is not elliptic.
Hörmander characterized hypoelliptic operators with constant coefficients and gave a wide class of hypoelliptic sums of squares of vector fields.

## Explanations

### L1 human

Some equations smooth things out: any solution of $\Delta u = 0$, even a very rough one at first sight, turns out to be infinitely differentiable.
Hypoelliptic operators are those with this smoothing property, whatever smooth right-hand side one puts in.
The heat operator $\partial_t - \Delta$ is one: temperature profiles are smooth even if the operator only involves one time derivative.
The wave operator is not: a sharp wave front $u(x, t) = H(x - t)$, with $H$ the jump function, solves the one-dimensional wave equation and keeps its jump forever.
