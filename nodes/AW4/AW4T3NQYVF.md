---
tag: AW4T3NQYVF
kind: concept
name: Fréchet algebra
msc: [46H05, 46A04]
specializes: [3GAA614673]
sources:
  - url: https://en.wikipedia.org/wiki/Fr%C3%A9chet_algebra
same_as:
  wikidata: Q5506659
  wikipedia: Fréchet algebra
---

## Summary

A Fréchet algebra is an associative algebra that is also a [[Fréchet space|3GAA614673]], with a jointly continuous multiplication.
It generalizes a Banach algebra: the topology comes from a countable family of [[seminorms|FP5GVCN8GV]] instead of a single norm.
Algebras of smooth functions, of holomorphic functions, and of continuous functions on the real line are Fréchet algebras but not Banach algebras.

## Explanations

### L1 human

Sometimes no single norm can measure the functions of interest, for example all continuous functions on the real line, which may be unbounded.
Instead one measures a function by its maximum on $[-1, 1]$, on $[-2, 2]$, on $[-3, 3]$, and so on.
A sequence converges when it converges uniformly on each of these intervals.
With this notion of convergence, the continuous functions on $\R$ form a Fréchet algebra.
