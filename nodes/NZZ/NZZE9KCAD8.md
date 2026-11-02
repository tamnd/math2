---
tag: NZZE9KCAD8
kind: concept
name: Unique ergodicity
msc: [37A25, 37B05]
sources:
  - url: https://en.wikipedia.org/wiki/Ergodicity
---

## Summary

A continuous map of a compact metric space is uniquely ergodic when it has exactly one invariant Borel probability measure.
That measure is then automatically [[ergodic|AZRPHS478B]].
For a uniquely ergodic map, time averages of every continuous function converge to the space average at every point, not only at almost every point.
Unique ergodicity is the dynamical form of equidistribution, as in [[Weyl's equidistribution theorem|NCCGNTBEYV]].

## Explanations

### L1 human

Every continuous map of a compact space has at least one invariant probability measure, a way of spreading mass that the map leaves unchanged.
Usually there are many: each fixed point carries its own point mass, for instance.
A uniquely ergodic map leaves no choice at all, so there is only one invariant way to spread the mass.
A rotation of the circle by an irrational angle is uniquely ergodic, and its only invariant measure is arc length.
A rotation by a quarter turn is not, because putting mass $1/4$ on each point of any orbit of four points gives an invariant measure.
