---
tag: VJ3BVREDWN
kind: concept
name: Lindeberg's condition
msc: [60F05]
sources:
  - url: https://en.wikipedia.org/wiki/Lindeberg%27s_condition
same_as:
  wikidata: Q1825985
  wikipedia: Lindeberg's condition
---

## Summary

Lindeberg's condition is a condition on a sequence of independent random variables with finite variances.
It says that no single variable contributes a non-negligible part of the total variance through its large values.
Under this condition, the normalised sums satisfy the [[central limit theorem|0EPZC4Z1FC]], even when the variables do not have the same distribution.
It is close to necessary: by a theorem of Feller, it is necessary when each variance is a negligible part of the total.

## Explanations

### L1 human

The central limit theorem says that a sum of many small independent effects looks normal.
For this, no single effect may dominate the sum.
Lindeberg's condition makes "no effect dominates" precise: the extreme values of each variable, taken together, carry almost none of the total variance.
For example, a sum of independent coin flips with different biases satisfies it as long as the total variance grows without bound.
