---
tag: 9ZSMF6NYKM
kind: concept
name: Differential inclusion
msc: [34A60, 49J21]
sources:
  - url: https://en.wikipedia.org/wiki/Differential_inclusion
same_as:
  wikidata: Q1054638
  wikipedia: Differential inclusion
---

## Summary

A differential inclusion is a relation $x'(t) \in F(t, x(t))$, where $F$ is a [[multivalued function|03CPD1HGF3]] that gives a set of allowed velocities at each time and state.
It generalizes the [[ordinary differential equation|0NT64JV96A]] $x' = f(t, x)$, which is the case where each set $F(t, x)$ has one element.
Differential inclusions describe control systems, equations with discontinuous right side, and systems with uncertain data.

## Explanations

### L1 human

An ordinary differential equation prescribes one velocity at each point.
A differential inclusion only prescribes a set of possible velocities, and a solution may choose any of them at each moment.
So there are usually many solutions from one starting point, like the many paths of a driver who may choose any speed below a limit.
For example, the solutions of $x'(t) \in [-1, 1]$ are the functions whose slope never exceeds $1$ in absolute value, such as $x(t) = \sin t$ or $x(t) = \abs{t}$.
