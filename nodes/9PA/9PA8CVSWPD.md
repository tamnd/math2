---
tag: 9PA8CVSWPD
kind: concept
name: Elimination theory
msc: [13P15, 13P10]
sources:
  - url: https://en.wikipedia.org/wiki/Elimination_theory
same_as:
  wikidata: Q3526789
  wikipedia: Elimination theory
---

## Summary

Elimination theory studies how to remove some variables from a system of polynomial equations, so as to obtain the equations satisfied by the remaining variables.
Its basic object is the elimination ideal, the set of consequences of the system that involve only the remaining variables.
Classical tools are resultants; the modern tool is a [[Gröbner basis|C83KPT47R0]] for a lexicographic order.
Geometrically, elimination computes the closure of the projection of the solution set to fewer coordinates.

## Explanations

### L1 human

From $x = t$ and $y = t^2$, one can eliminate $t$ and get $y = x^2$, the equation of a parabola.
Elimination theory makes this process systematic for any system of polynomial equations.
It answers questions such as: which values of some variables extend to a solution of the whole system?
This is the algebraic form of solving a system by substitution, as one does in school for linear equations.
