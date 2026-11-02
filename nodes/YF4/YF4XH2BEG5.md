---
tag: YF4XH2BEG5
kind: concept
name: Limit set
msc: [37C10, 34C05, 34D45]
sources:
  - url: https://en.wikipedia.org/wiki/Limit_set
same_as:
  wikidata: Q1825444
  wikipedia: Limit set
---

## Summary

The $\omega$-limit set of a point is the set of states that its solution approaches again and again as time goes to $+\infty$.
The $\alpha$-limit set is the same notion for time going to $-\infty$.
Limit sets describe the long-time behaviour of a dynamical system: they can be equilibria, [[periodic orbits|0AA97XA70K]] or more complicated sets.
They are closed [[invariant sets|WWZTW11664]], and for a bounded forward orbit the $\omega$-limit set is nonempty, compact and connected.

## Explanations

### L1 human

Run the system for a long time and watch where the state keeps returning.
Those places form the $\omega$-limit set.
For the equation $x' = -x$, every solution tends to $0$, so the $\omega$-limit set of every point is $\set{0}$.
For a system whose solutions spiral onto the unit circle, the $\omega$-limit set of every point except the origin is the whole circle.
It is the "final destination" of the motion, even when the motion never stops.
