---
tag: ZBFZGA1J5G
kind: concept
name: Gowers norm
msc: [11B30, 05D10]
specializes: [0V2WP9B1MF]
sources:
  - url: https://en.wikipedia.org/wiki/Gowers_norm
same_as:
  wikidata: Q5590057
  wikipedia: Gowers norm
---

## Summary

The Gowers norms $\norm{f}_{U^k}$ are norms on complex-valued functions on a finite abelian group, one for each $k \ge 2$.
They average products of $f$ over $k$-dimensional parallelepipeds $x + \omega_1 h_1 + \dots + \omega_k h_k$.
A function with small $U^k$ norm behaves randomly for counting arithmetic progressions of length $k + 1$.
Gowers introduced them for his proof of [[Szemerédi's theorem|B23B0QEMN5]], and they are the basic objects of higher-order Fourier analysis.

## Explanations

### L1 human

The Gowers norm tests whether a function, such as the indicator of a set, looks random from the point of view of additive patterns.
The $U^2$ norm detects correlation with ordinary waves $e^{2\pi i a x / N}$, as in usual Fourier analysis.
The $U^3$ norm also detects quadratic waves $e^{2\pi i a x^2 / N}$, which the $U^2$ norm misses.
If a set has small $U^{k-1}$ norm after subtracting its density, it contains about as many progressions of length $k$ as a random set of the same density.
