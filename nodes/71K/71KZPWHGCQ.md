---
tag: 71KZPWHGCQ
kind: concept
name: Corner transfer matrix
msc: [82B23, 82B20]
sources:
  - url: https://en.wikipedia.org/wiki/Corner_transfer_matrix
same_as:
  wikidata: Q5171639
  wikipedia: Corner transfer matrix
---

## Summary

A corner transfer matrix is the partition function of one quarter of a square-lattice region.
It is viewed as a matrix indexed by the spins on the two edges of the quarter that meet at the centre.
Four such matrices, one per quadrant, multiply to give the partition function of the whole region.
Inserting a spin at the centre gives one-point functions such as the magnetization.
Baxter introduced them in 1968, and for models that satisfy the star–triangle relation they can be diagonalized in the infinite-volume limit.
This led to exact formulas for order parameters, for example in the [[hard hexagon model|7MJQ2ZBQ66]].

## Explanations

### L1 human

Cut a square grid into four quarters through its centre.
Each quarter, summed over its inside spins, behaves like a matrix that takes the spins on one cut edge to the spins on the other.
Going around the centre through the four quarters multiplies four matrices, and the trace gives the whole partition function.
The method focuses on the centre spin, which is exactly what one needs to compute a magnetization.
