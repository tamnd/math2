---
tag: Q1TGZK8RN6
kind: concept
name: Hausdorff measure
msc: [28A78, 28A80]
sources:
  - url: https://en.wikipedia.org/wiki/Hausdorff_measure
same_as:
  wikidata: Q1591095
  wikipedia: Hausdorff measure
---

## Summary

The $s$-dimensional Hausdorff measure of a subset of a [[metric space|0VKD1TP7F3]] measures its $s$-dimensional size, for any real $s \ge 0$.
It is built from covers by small sets, each counted by its [[diameter|0KW3PN547K]] to the power $s$.
For whole numbers $s = n$ it extends length, area and volume to rough sets, and in $\R^n$ it agrees with [[Lebesgue measure|2Z2QVWZ262]] up to a constant.
It defines Hausdorff dimension and is the basic measure of fractal geometry.

## Explanations

### L1 human

To measure the length of a curve, cover it by many tiny pieces and add up their sizes.
For area one adds the squares of the sizes, and for volume the cubes.
Hausdorff measure allows any power $s$, also non-integer powers such as $0.63$.
For a given set, there is one critical power: below it the measure is infinite, above it the measure is zero.
For example, a line segment of length $1$ has $1$-dimensional measure $1$ and $2$-dimensional measure $0$.
