---
tag: ASWF03X5AM
kind: concept
name: Minimax approximation
msc: [41A50, 41A10, 65D15]
specializes: [7N4988HN3P]
sources:
  - url: https://en.wikipedia.org/wiki/Minimax_approximation_algorithm
---

## Summary

Fix a continuous function $f$ on an interval and a degree $n$.
A minimax approximation of $f$ is a polynomial $p$ of degree at most $n$ that makes the largest error $\max \abs{f - p}$ as small as possible.
It is the [[best approximation|7N4988HN3P]] for the uniform norm, so it controls the error at every point and not only on average.
Minimax polynomials are used to build the routines that compute $\sin$, $\exp$ and other functions in software libraries.

## Explanations

### L1 human

Draw the graph of $f$ and a thin band around it of the same width $\varepsilon$ everywhere.
A polynomial approximates $f$ within $\varepsilon$ when its graph stays inside the band.
The minimax polynomial is the polynomial of the given degree that fits inside the thinnest possible band.
For example, the best constant approximation of $f(x) = x$ on $[0, 1]$ is the constant $1/2$, with largest error $1/2$.
Any other constant $c$ is farther than $1/2$ from $0$ or from $1$.
