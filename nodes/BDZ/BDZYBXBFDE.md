---
tag: BDZYBXBFDE
kind: concept
name: Topological entropy
msc: [37B40]
sources:
  - url: https://en.wikipedia.org/wiki/Topological_entropy
same_as:
  wikidata: Q3055355
  wikipedia: Topological entropy
---

## Summary

Topological entropy is a nonnegative number, possibly infinite, that measures the exponential growth rate of the number of distinguishable orbits of a continuous map.
It is an invariant of topological conjugacy, so it can show that two systems are not conjugate.
Positive entropy is a common sign of complicated, chaotic behaviour.
Through the [[variational principle|HHR8HP3R6G]] it equals the supremum of the measure-theoretic entropies of the invariant measures.

## Explanations

### L1 human

Suppose you can only see the state of a system up to a fixed small precision.
Count how many different orbit segments of length $n$ you can tell apart.
If this number grows like $e^{hn}$, the topological entropy is $h$.
For a rotation, nearby points stay close forever, so the count does not grow and the entropy is $0$.
For the doubling map of the circle, the count doubles at each step, and the entropy is $\log 2$.
