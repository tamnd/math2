---
tag: Z8FABSYQTS
kind: concept
name: Finite-rank operator
msc: [47B07, 47A05]
sources:
  - url: https://en.wikipedia.org/wiki/Finite-rank_operator
same_as:
  wikidata: Q5450385
  wikipedia: Finite-rank operator
---

## Summary

A finite-rank operator is a bounded linear map between normed spaces whose image is finite-dimensional.
Such operators behave like matrices, even when the spaces are infinite-dimensional.
They are the simplest operators of functional analysis, and many other classes, such as compact and trace class operators, are built as limits of them.

## Explanations

### L1 human

A finite-rank operator takes a possibly huge space and squeezes it into a finite-dimensional piece.
Picture a projector that casts every object of a large room onto one flat wall: the shadows live in a small space.
For a concrete example, on the space of square-summable sequences, the map $(x_1, x_2, x_3, \ldots) \mapsto (x_1 + x_2, 0, 0, \ldots)$ has image the multiples of the first unit vector.
Its image has dimension $1$, so it is an operator of rank $1$.
