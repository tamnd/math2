---
tag: P6E9RZNRBZ
kind: concept
name: Local solvability
msc: [35A01, 35A27]
sources:
  - url: https://en.wikipedia.org/wiki/Lewy%27s_example
---

## Summary

A linear differential operator $P$ is locally solvable at a point if $P u = f$ has a solution near that point for every smooth $f$.
Operators with constant coefficients are always locally solvable, but Hans Lewy found a first-order operator with polynomial coefficients that is locally solvable at no point.
This discovery started the study of necessary and sufficient conditions for local solvability.
See the [[definition|DQ0TSVK7ZT]].

## Explanations

### L1 human

For an ordinary differential equation such as $y' = f(x)$ one can always find a solution near any point, by integrating.
It was long expected that every reasonable linear partial differential equation also has local solutions.
Lewy's example shows that this is false: there is a simple first-order equation $L u = f$ in three variables, with smooth $f$, that has no solution in any open set.
Local solvability is the property that rules this out.
