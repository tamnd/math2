---
tag: W59B3PKZPP
kind: concept
name: Packing measure
msc: [28A78, 28A80]
sources:
  - url: https://en.wikipedia.org/wiki/Packing_dimension
---

## Summary

Packing measure gives the $s$-dimensional size of a set in a [[metric space|0VKD1TP7F3]].
It packs disjoint small balls centred in the set, instead of covering the set.
It is a dual of [[Hausdorff measure|Q1TGZK8RN6]], which uses covers.
It leads to the packing dimension, which is at least the Hausdorff dimension, and the two can differ for irregular fractals.

## Explanations

### L1 human

Hausdorff measure asks for the most economical way to cover a set by small pieces.
Packing measure asks the opposite question: how much room can one fill with disjoint small balls whose centres lie in the set.
Each ball counts by its diameter to the power $s$.
For a line segment of length $1$ and $s = 1$, the best packings fill the segment almost completely, and the packing measure is $1$.
