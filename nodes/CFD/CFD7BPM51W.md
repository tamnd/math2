---
tag: CFD7BPM51W
kind: concept
name: Harmonic measure
msc: [31A15, 30C85]
sources:
  - url: https://en.wikipedia.org/wiki/Harmonic_measure
same_as:
  wikidata: Q5659270
  wikipedia: Harmonic measure
---

## Summary

The harmonic measure of a domain, seen from a point $z$, is a probability measure on the boundary of the domain.
It is the measure that represents the value at $z$ of the solution of the [[Dirichlet problem|8D56GQ4AG8]] in terms of the boundary data.
Equivalently, it is the distribution of the first exit point of a Brownian motion started at $z$.
It is invariant under conformal maps, and it is a central tool for estimating harmonic and holomorphic functions near the boundary.

## Explanations

### L1 human

Release a random walker at a point $z$ inside a region and wait until it first hits the boundary.
The harmonic measure of a piece of the boundary is the probability that the walker hits that piece first.
Parts of the boundary that are near $z$ and in the open get a large measure, while parts hidden deep inside narrow fjords get a small one.
For the centre of a disc, every arc of the circle gets a measure proportional to its length.
