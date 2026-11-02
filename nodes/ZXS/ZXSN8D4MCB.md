---
tag: ZXSN8D4MCB
kind: concept
name: Reduced scheme
msc: [14A15]
specializes: [5A35TYZD02]
sources:
  - url: https://en.wikipedia.org/wiki/Glossary_of_algebraic_geometry
---

## Summary

A reduced scheme is a [[scheme|5A35TYZD02]] whose rings of functions have no nonzero [[nilpotent elements|0ZB2JG1M9C]].
On a reduced scheme, a function is determined by its values at all points.
Classical varieties are reduced, while non-reduced schemes record extra infinitesimal structure, such as a double point.

## Explanations

### L1 human

On a scheme a function can be nonzero and still have value zero at every point.
This happens when the function is nilpotent, like $x$ in the ring $k[x]/(x^2)$, where $x^2 = 0$.
That scheme is a single point "thickened" in one direction, which remembers a tangent direction.
A reduced scheme is one with no such thickening, like the line $\operatorname{Spec} k[x]$ itself.
