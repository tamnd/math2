---
tag: 5VGVPENA0F
kind: concept
name: Trigamma function
msc: ["33B15"]
specializes: [3J3QGKPMZQ]
sources:
  - url: https://en.wikipedia.org/wiki/Trigamma_function
same_as:
  wikidata: Q1244426
  wikipedia: Trigamma function
---

## Summary

The trigamma function $\psi_1$ is the derivative of the [[digamma function|HWRRXB0YXS]], the second derivative of $\log \Gamma$.
It is the [[polygamma function|3J3QGKPMZQ]] of order $1$ and equals $\sum_{k \ge 0} (z+k)^{-2}$.
It is positive on the positive real axis, which expresses the log-convexity of the [[gamma function|0H5SYBSED9]].

## Explanations

### L1 human

The trigamma function measures how fast the slope of $\log \Gamma$ changes, that is, the bending of the graph of $\log \Gamma$.
It is a sum of squares of reciprocals: $\frac{1}{z^2} + \frac{1}{(z+1)^2} + \frac{1}{(z+2)^2} + \cdots$.
For $z = 1$ this is the famous Basel sum $1 + \frac14 + \frac19 + \cdots = \frac{\pi^2}{6}$.
Since every term is positive for $z > 0$, the graph of $\log \Gamma$ always bends upward there.
