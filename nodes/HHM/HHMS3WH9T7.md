---
tag: HHMS3WH9T7
kind: concept
name: Ordered vector space
msc: ["46A40", "06F20"]
specializes: [000AYPA9AJ]
sources:
  - url: https://en.wikipedia.org/wiki/Ordered_vector_space
same_as:
  wikidata: Q1503340
  wikipedia: Ordered vector space
---

## Summary

An ordered vector space is a real [[vector space|000AYPA9AJ]] with a compatible [[partial order|0QV2JS9RJ3]].
The order is preserved by adding a vector and by multiplying by a nonnegative scalar.
Such an order is the same as a [[positive cone|Z344RY5XX1]], the set of vectors that are at least $0$.
Spaces of real functions, of sequences and of self-adjoint operators carry natural orders of this kind.
Ordered vector spaces are the setting of positive linear maps, and [[Riesz spaces|99709K2NJM]] are the case where the order is a lattice.

## Explanations

### L1 human

In $\R^2$ say that $(a, b) \le (c, d)$ when $a \le c$ and $b \le d$.
Moving both points by the same vector keeps this relation, and so does stretching both by a positive factor.
Some pairs of vectors are not comparable, such as $(1, 0)$ and $(0, 1)$.
An ordered vector space is any real vector space with an order that behaves like this.
