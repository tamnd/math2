---
tag: 1H92CYA4ZC
kind: concept
name: Support function
msc: [52A20, 52A41]
sources:
  - url: https://en.wikipedia.org/wiki/Support_function
same_as:
  wikidata: Q3075191
  wikipedia: Support function
---

## Summary

The support function of a nonempty set $A \subseteq \R^n$ assigns to each vector $x$ the [[supremum|0R3H5PANRQ]] of the [[dot products|0S52TNNTH9]] $x \cdot a$ over $a \in A$.
It is a [[sublinear function|K3356N0SAX]], and it determines a nonempty compact [[convex set|02AS45T3H9]] completely.
Support functions turn geometric operations into analytic ones: the support function of a Minkowski sum is the sum of the support functions.
They are a basic tool in the study of [[convex bodies|437FSG3419]].

## Explanations

### L1 human

Fix a direction $u$ of length $1$ and push a flat wall, perpendicular to $u$, towards the set from far away in direction $u$.
The value of the support function at $u$ is the signed distance from the origin to the wall at the moment it first touches the set.
For the unit disc centred at the origin, the wall always touches at distance $1$, so the support function is $h(u) = 1$ on unit vectors, and $h(x) = \abs{x}$ in general.
For the segment from $(-1, 0)$ to $(1, 0)$, one gets $h(x_1, x_2) = \abs{x_1}$.
