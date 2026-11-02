---
tag: VDTEARFVMB
kind: concept
name: Hausdorff content
msc: [28A78]
specializes: [BJ314H17HC]
sources:
  - url: https://en.wikipedia.org/wiki/Hausdorff_dimension
---

## Summary

The $s$-dimensional Hausdorff content of a set is the least total of the $s$-th powers of the diameters of countable covers of the set.
Unlike the [[Hausdorff measure|Q1TGZK8RN6]], it allows covers by sets of any size.
It is an [[outer measure|BJ314H17HC]] that is usually not additive, but it has the same null sets as the Hausdorff measure.
So it can be used to compute [[Hausdorff dimension|SSNFTHZ6YJ]], and it is easier to estimate.

## Explanations

### L1 human

To estimate the $s$-dimensional size of a set, cover it with countably many pieces and add up each diameter raised to the power $s$.
The Hausdorff content is the smallest total that one can reach.
For a segment of length $1$ and $s = 1$ it is $1$.
For a filled unit square and $s = 1$ it is at most $\sqrt 2$, the diameter of the square, although the square has infinite length.
This shows that the content does not see fine structure, but it still sees whether a set is negligible.
