---
tag: HYK8J56PSH
kind: concept
name: Chebyshev nodes
msc: [65D05, 41A05, 33C45]
sources:
  - url: https://en.wikipedia.org/wiki/Chebyshev_nodes
same_as:
  wikidata: Q1052508
  wikipedia: Chebyshev nodes
---

## Summary

Chebyshev nodes are the zeros of a [[Chebyshev polynomial|M6EAR1JHPP]], possibly moved to an interval $[a, b]$ by an affine map.
They crowd near the ends of the interval.
They are the standard choice of points for [[polynomial interpolation|SS1YMS2NPC]], because they avoid the large errors that equally spaced points cause.

## Explanations

### L1 human

Take points spaced evenly around the upper half of a circle and drop them straight down onto the diameter.
The shadows are the Chebyshev nodes: sparse in the middle and dense near the two ends.
For $n = 2$ the nodes in $[-1, 1]$ are $\pm 1/\sqrt{2}$, about $\pm 0.707$.
Interpolating at these points keeps the polynomial under control near the ends, where equally spaced points let it oscillate wildly.
