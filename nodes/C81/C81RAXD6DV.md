---
tag: C81RAXD6DV
kind: concept
name: Tutte polynomial
msc: [05C31, 05B35]
sources:
  - url: https://en.wikipedia.org/wiki/Tutte_polynomial
same_as:
  wikidata: Q7857002
  wikipedia: Tutte polynomial
---

## Summary

The Tutte polynomial $T(x, y)$ is a polynomial in two variables attached to a graph or, more generally, to a [[matroid|PX31ZNYS3Z]].
It is the most general invariant that satisfies the deletion–contraction recurrence, and many counting invariants are specializations of it.
Among them are the number of [[spanning trees|0S4ZEZM7KE]], the [[chromatic polynomial|0B621RBVS9]], the flow polynomial and the reliability polynomial.
The partition function of the Potts model in statistical physics is another specialization.

## Explanations

### L1 human

Many questions about a graph can be answered by removing one edge or squeezing one edge to a point and combining the answers for the two smaller graphs.
The Tutte polynomial records all such answers at once.
Plugging in particular numbers gives particular counts: for example, $T(1, 1)$ is the number of spanning trees of a connected graph.
For a triangle, $T(x, y) = x^2 + x + y$, and $T(1, 1) = 3$ is its number of spanning trees.
