---
tag: FP5GVCN8GV
kind: concept
name: Seminorm
msc: [46A03]
specializes: [K3356N0SAX]
sources:
  - url: https://en.wikipedia.org/wiki/Seminorm
same_as:
  wikidata: Q1416088
  wikipedia: Seminorm
---

## Summary

A seminorm on a real or complex vector space has all the properties of a [[norm|0V2WP9B1MF]], except that it may vanish on nonzero vectors.
Seminorms are the building blocks of [[locally convex spaces|B6GY2KJMWW]]: a family of seminorms defines a topology, and every locally convex topology arises in this way.
Many function spaces are described by seminorms rather than by one norm.
An example is the space of continuous functions on $\R$ with uniform convergence on compact sets.

## Explanations

### L1 human

A seminorm measures the size of a vector, but it is allowed to be blind to some directions.
It still scales correctly and still obeys the triangle inequality.
On $\R^2$, the function $p(x, y) = \abs{x}$ is a seminorm: it measures only the first coordinate.
It gives $p(0, 5) = 0$ although $(0, 5) \ne 0$, so it is not a norm.
On functions, $p(f) = \abs{f(0)}$ is a seminorm that only looks at the value at $0$.
