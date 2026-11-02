---
tag: 4724KRNHAT
kind: concept
name: Palais–Smale compactness condition
msc: ["58E05", 47J30]
sources:
  - url: https://en.wikipedia.org/wiki/Palais–Smale_compactness_condition
same_as:
  wikidata: Q3686430
  wikipedia: Palais–Smale compactness condition
---

## Summary

The Palais–Smale condition is a compactness hypothesis on a continuously differentiable functional on a Banach space.
It asks that every sequence along which the functional stays bounded and its derivative tends to zero has a convergent subsequence.
It replaces the compactness of closed bounded sets, which fails in infinite dimensions, in the search for [[critical points|0YTCMFB4HC]].
It is the main hypothesis of the [[mountain pass theorem|EPXNCSP2MN]] and of many other minimax results.

## Explanations

### L1 human

To find a lowest point or a mountain pass of a landscape, one usually walks along points where the ground gets flatter and flatter.
In infinite dimensions such a walk can run away to infinity or spread out without ever reaching a point.
The Palais–Smale condition forbids this: every such walk with bounded heights must have a part that settles at an actual point.
For example, $f(x) = e^x$ on $\R$ fails it, since its slope tends to $0$ as $x \to -\infty$ while no flat point exists.
