---
tag: FZK2M8KGXQ
kind: concept
name: Trigonometric series
msc: [42A20, 42A32]
sources:
  - url: https://en.wikipedia.org/wiki/Trigonometric_series
same_as:
  wikidata: Q1149336
  wikipedia: Trigonometric series
---

## Summary

A trigonometric series is an infinite series $\sum_{n \in \Z} c_n e^{inx}$, or $\frac{a_0}{2} + \sum_{n \ge 1} (a_n \cos nx + b_n \sin nx)$, with arbitrary coefficients.
Its partial sums are [[trigonometric polynomials|J3NJQ5FZJ5]].
Every [[Fourier series|G12KXDHPPS]] is a trigonometric series, but not every trigonometric series is the Fourier series of an integrable function.
The study of these series led Cantor to set theory, through the question of uniqueness of the coefficients.

## Explanations

### L1 human

A trigonometric series is an infinite sum of waves with whole-number frequencies, each with its own amplitude.
Nothing says in advance that the sum converges or that it comes from a given function.
For example, $\sum_{n \ge 1} \frac{\sin nx}{n^2}$ converges at every $x$, since its terms are bounded by $1/n^2$.
A Fourier series is the special case where the amplitudes are computed from a function by integrals.
