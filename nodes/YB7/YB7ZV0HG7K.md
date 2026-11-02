---
tag: YB7ZV0HG7K
kind: concept
name: Incomplete gamma function
msc: ["33B20"]
sources:
  - url: https://en.wikipedia.org/wiki/Incomplete_gamma_function
same_as:
  wikidata: Q1319246
  wikipedia: Incomplete gamma function
---

## Summary

The incomplete gamma functions split the integral of the [[gamma function|0H5SYBSED9]] at a point $x$.
The lower one $\gamma(s, x)$ integrates $t^{s-1} e^{-t}$ from $0$ to $x$, and the upper one $\Gamma(s, x)$ integrates it from $x$ to $\infty$.
Their sum is $\Gamma(s)$.
They give the distribution function of the [[gamma distribution|0B80PAQD3C]] and contain the [[exponential integral|EV6ZDQ0NDY]] and the [[error function|7Y56QCZSZJ]] as special cases.

## Explanations

### L1 human

The gamma function is the area under the curve $t^{s-1} e^{-t}$ on the whole positive half line.
Cut this area at a point $x$.
The part on the left is the lower incomplete gamma function, and the part on the right is the upper one.
For $s = 1$ the curve is $e^{-t}$, and the two parts are $1 - e^{-x}$ and $e^{-x}$.
