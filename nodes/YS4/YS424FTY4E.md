---
tag: YS424FTY4E
kind: concept
name: Curse of dimensionality
msc: [65Y20, 41A63, 65D30]
sources:
  - url: https://en.wikipedia.org/wiki/Curse_of_dimensionality
same_as:
  wikidata: Q1430460
  wikipedia: Curse of dimensionality
---

## Summary

The curse of dimensionality is the exponential growth in the dimension $d$ of the cost of solving a numerical problem to a fixed accuracy.
The phrase is due to Richard Bellman.
In integration and approximation it means that the number of function values needed for error $\varepsilon$ grows like $c^d$ with $c > 1$.
Methods such as [[sparse grids|84BR7X6HET]], Monte Carlo and quasi-Monte Carlo methods, and restrictions to special classes of functions are ways to avoid it.

## Explanations

### L1 human

To sample a line segment with spacing $0.1$ one needs $10$ points, a square needs $100$, and a cube needs $1000$.
In $d$ dimensions the same spacing needs $10^d$ points, which is hopeless for $d = 50$.
High-dimensional space is so large that any reasonable set of sample points leaves most of it far from every point.
So an unknown function can hide almost anything between the samples.
Take the functions on $[0, 1]^d$ bounded by $1$ and with Lipschitz constant $1$.
For example, no method that uses at most $2^{d-1}$ of their values can always compute the integral with error below $1/8$.
