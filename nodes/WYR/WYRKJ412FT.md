---
tag: WYRKJ412FT
kind: concept
name: Minkowski–Bouligand dimension
msc: [28A80, 28A75]
sources:
  - url: https://en.wikipedia.org/wiki/Minkowski%E2%80%93Bouligand_dimension
same_as:
  wikidata: Q2555655
  wikipedia: Minkowski–Bouligand dimension
---

## Summary

The Minkowski–Bouligand dimension is also called the box-counting dimension.
For a bounded set, it measures how fast the number of small boxes needed to cover the set grows as the boxes shrink.
If about $\varepsilon^{-d}$ boxes of side $\varepsilon$ are needed, the dimension is $d$.
It is easy to estimate numerically, and it is at least the [[Hausdorff dimension|SSNFTHZ6YJ]].

## Explanations

### L1 human

Lay a grid of squares of side $\varepsilon$ over a picture of the set and count the squares that meet it.
For a segment, halving $\varepsilon$ doubles the count; for a filled square, it multiplies the count by four.
The exponent in this growth is the box-counting dimension: $1$ for the segment and $2$ for the square.
For the middle-thirds Cantor set, dividing $\varepsilon$ by $3$ doubles the count, which gives dimension $\log 2 / \log 3$.
