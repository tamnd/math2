---
tag: YDN0T4MEX0
kind: concept
name: Error of best approximation
msc: [41A50, 41A25, 41A10]
sources:
  - url: https://en.wikipedia.org/wiki/Approximation_theory
---

## Summary

The error of best approximation of $x$ from a set $A$ is the distance from $x$ to $A$, the infimum of $\norm{x - a}$ over $a \in A$.
For a function $f$ and the polynomials of degree at most $n$ it is written $E_n(f)$.
It measures how well $f$ can be approximated at all, whether or not a [[best approximation|7N4988HN3P]] exists.
Its decay as $n \to \infty$ reflects the smoothness of $f$.

## Explanations

### L1 human

It is the smallest gap you can achieve with the tools you are allowed to use.
For $f(x) = x^2$ on $[0, 1]$ and uniform distance, the best constant is $1/2$ with gap $1/2$, the best line has gap $1/8$, and a quadratic gives gap $0$.
Allowing more complicated tools never makes the gap larger, so $E_0(f) \ge E_1(f) \ge E_2(f) \ge \cdots$.
For a continuous function on a closed interval these numbers tend to $0$.
