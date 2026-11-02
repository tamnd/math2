---
tag: N1Q0BJAEFX
kind: concept
name: Eulerian poset
msc: [06A07, 52B05]
specializes: [1C7TKGTB2F]
sources:
  - url: https://en.wikipedia.org/wiki/Eulerian_poset
same_as:
  wikidata: Q5409003
  wikipedia: Eulerian poset
---

## Summary

An Eulerian poset is a finite [[graded poset|1C7TKGTB2F]] with a least and a greatest element.
In it, every interval of positive length has as many elements of even rank as of odd rank.
Equivalently, its [[Möbius function|2Y75S8NG5B]] is $\mu(x, y) = (-1)^{\rho(y) - \rho(x)}$, where $\rho$ is the rank.
Face lattices of convex polytopes are Eulerian, and the condition encodes the Euler–Poincaré relation for their face numbers.

## Explanations

### L1 human

Count the elements in an interval of the poset, sorted by their level.
In an Eulerian poset the levels with even numbers and the levels with odd numbers always hold the same total.
The subsets of a finite set form an Eulerian poset: a set with $k \ge 1$ elements has as many subsets of even size as of odd size.
This is the same balance as $V - E + F = 2$ for a convex polyhedron.
