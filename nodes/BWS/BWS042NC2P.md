---
tag: BWS042NC2P
kind: concept
name: Decreasing rearrangement
msc: ["46E30", 28A20]
sources:
  - url: https://en.wikipedia.org/wiki/Symmetric_decreasing_rearrangement
---

## Summary

The decreasing rearrangement of a measurable function $f$ is the non-increasing, right-continuous function $f^*$ on $[0, \infty)$ that has the same distribution function as $\abs{f}$.
It sorts the values of $\abs{f}$ from the largest to the smallest.
Every norm that depends only on the distribution function, such as the $L^p$ norms, takes the same value on $f$ and on $f^*$.
It is the basic tool of Lorentz spaces and of rearrangement-invariant function spaces.

## Explanations

### L1 human

Imagine the values of a function as piles of sand placed along a line.
The decreasing rearrangement moves the piles so that the tallest come first and the heights go down from left to right.
No sand is added or removed, so the amount of land above each height stays the same.
For example, on $[0, 1]$ the function $f(x) = x$ has decreasing rearrangement $f^*(t) = 1 - t$ for $0 \le t < 1$ and $f^*(t) = 0$ for $t \ge 1$.
