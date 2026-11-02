---
tag: HNW4WRSEEX
kind: concept
name: Riesz projector
msc: [47A10, 47A60]
specializes: [033DA1WE8Y]
sources:
  - url: https://en.wikipedia.org/wiki/Riesz_projector
same_as:
  wikidata: Q96401996
  wikipedia: Riesz projector
---

## Summary

The Riesz projector of an operator $T$ for an isolated part of its spectrum is a projection.
It is obtained by integrating the resolvent of $T$ around that part.
It splits the space into two closed invariant subspaces on which $T$ has the separated pieces of the spectrum.
It generalises the projection onto a generalised eigenspace of a matrix along the other generalised eigenspaces.

## Explanations

### L1 human

For a matrix, one can split the space into the generalised eigenspace of one eigenvalue and the sum of the others.
The Riesz projector does this for operators, for any part of the spectrum that is separated from the rest by a gap.
It is computed by a contour integral around that part, as in Cauchy's integral formula.
For the diagonal matrix with entries $1$ and $2$, the Riesz projector for $\set{1}$ keeps the first coordinate and kills the second.
