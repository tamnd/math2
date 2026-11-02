---
tag: SASP14MA1Z
kind: concept
name: Lp space
msc: ["46E30", 28A25]
sources:
  - url: https://en.wikipedia.org/wiki/Lp_space
same_as:
  wikidata: Q305936
  wikipedia: Lp space
---

## Summary

For $1 \le p < \infty$, the space $L^p(\mu)$ consists of the measurable functions $f$ on a measure space with $\int \abs{f}^p \, d\mu < \infty$.
Two functions that agree almost everywhere count as the same element.
The norm is $\norm{f}_p = (\int \abs{f}^p \, d\mu)^{1/p}$, and with this norm $L^p(\mu)$ is a Banach space.
The case $p = 2$ is a Hilbert space.
These spaces are the basic function spaces of analysis, probability and partial differential equations.

## Explanations

### L1 human

The number $\norm{f}_p$ measures the size of a function by averaging the $p$-th power of its absolute value.
A larger $p$ gives more weight to the places where the function is large.
Two functions that differ only on a set of measure zero have the same size, so they are treated as the same element.
For example, $f(x) = x^{-1/3}$ on $(0, 1]$ lies in $L^2$, since $\int_0^1 x^{-2/3} \, dx = 3$, but not in $L^3$, since $\int_0^1 x^{-1} \, dx = \infty$.
