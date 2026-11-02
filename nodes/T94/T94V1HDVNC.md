---
tag: T94V1HDVNC
kind: problem
name: Lebesgue's universal covering problem
msc: [52C15, 52A10, 52A40]
uses: [0KW3PN547K, 02AS45T3H9, 02HPP5VCZH]
about: [0KW3PN547K]
sources:
  - url: https://en.wikipedia.org/wiki/Lebesgue%27s_universal_covering_problem
same_as:
  wikidata: Q28456108
  wikipedia: Lebesgue's universal covering problem
history:
  posed_by: "Henri Lebesgue"
  first_stated: "1914"
---

## Problem

A *universal cover* is a [[convex set|02AS45T3H9]] $C$ in the plane with this property.
Every plane set of [[diameter|0KW3PN547K]] $1$ can be moved into $C$ by an [[isometry|02HPP5VCZH]] of the plane.
Find the smallest possible area of a universal cover.

## Remarks

The problem is open: the exact minimal area is not known.
Pál showed that the regular hexagon whose opposite sides are at distance $1$ is a universal cover; its area is $\sqrt{3}/2 \approx 0.866$.
Cutting suitable pieces off this hexagon gives smaller universal covers, and the best known upper bound is about $0.8441$.
A disc of diameter $1$ is not a universal cover: the equilateral triangle of side $1$ has diameter $1$ but circumradius $1/\sqrt{3} > 1/2$.
Lower bounds come from the fact that a universal cover must contain copies of several specific sets of diameter $1$ at once.
Examples are a disc of diameter $1$ and an equilateral triangle of side $1$.
The best known lower bound is about $0.832$.

## Explanations

### L1 human

Lebesgue asked for the smallest convex shape that can cover every shape of diameter one, after moving and turning it.
A regular hexagon of width one works, but it is not the smallest.
More than a century later the best possible area is still only known to lie between about $0.832$ and $0.8441$.
