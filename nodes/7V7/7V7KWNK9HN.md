---
tag: 7V7KWNK9HN
kind: concept
name: Lebesgue constant
msc: [41A05, 65D05, 41A10]
sources:
  - url: https://en.wikipedia.org/wiki/Lebesgue_constant
same_as:
  wikidata: Q6511317
  wikipedia: Lebesgue constant
---

## Summary

The Lebesgue constant of a set of interpolation nodes measures how much [[polynomial interpolation|SS1YMS2NPC]] at these nodes can amplify errors.
It is the [[operator norm|06EKW1AKXF]] of the interpolation map on continuous functions with the uniform norm.
It compares the interpolation error with the error of best approximation, and it measures the sensitivity of interpolation to errors in the data.
For equally spaced nodes it grows exponentially with the degree, while for [[Chebyshev nodes|HYK8J56PSH]] it grows only like a logarithm.

## Explanations

### L1 human

Suppose the data values at the nodes are each wrong by at most $\varepsilon$.
The interpolating polynomial may then be wrong by up to $\Lambda \varepsilon$ somewhere, where $\Lambda$ is the Lebesgue constant.
For the nodes $-1, 0, 1$ the constant is $5/4$, so the amplification is mild.
For $20$ equally spaced nodes it is already in the thousands, which is one cause of Runge's phenomenon.
