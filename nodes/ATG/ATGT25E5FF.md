---
tag: ATGT25E5FF
kind: concept
name: Projection-valued measure
msc: [47B15, 28B05, 46C05]
sources:
  - url: https://en.wikipedia.org/wiki/Projection-valued_measure
same_as:
  wikidata: Q339722
  wikipedia: Projection-valued measure
---

## Summary

A projection-valued measure assigns to each measurable set an orthogonal projection on a Hilbert space, in a way that is additive like a measure.
It is the object that the spectral theorem attaches to a self-adjoint or normal operator, and it allows one to integrate functions against an operator.
In quantum mechanics, projection-valued measures describe sharp measurements: the projection of a set corresponds to the event that the measured value lies in that set.

## Explanations

### L1 human

An ordinary measure gives each set a number, its size.
A projection-valued measure gives each set a projection, a way to cut out a piece of the Hilbert space.
Disjoint sets give perpendicular pieces, and the whole set gives the whole space.
For example, on $\C^2$ with the standard basis $e_1, e_2$, send a subset $B$ of $\R$ to the projection onto the span of those $e_k$ with $k \in B$.
This splits $\C^2$ into the pieces attached to the points $1$ and $2$, as the eigenspaces of the matrix $\operatorname{diag}(1, 2)$ do.
