---
tag: 1P47PCRVTZ
kind: concept
name: Levin-type transformations
msc: [65B10, 65B05, 40A25]
specializes: [B1S2XJPGYD]
sources:
  - url: https://en.wikipedia.org/wiki/Series_acceleration
---

## Summary

Levin-type transformations are nonlinear [[series acceleration|B1S2XJPGYD]] methods that use explicit estimates of the remainder of a series.
They assume that the error of the $n$-th partial sum is a known estimate $\omega_n$ times a slowly varying correction.
They eliminate this correction exactly when it is a polynomial in $1/(n + \beta)$.
Levin's $t$- and $u$-transformations take $\omega_n$ from the terms of the series.
They work well both for alternating series and for many series with terms of one sign.
They can also assign values to some divergent series.

## Explanations

### L1 human

For a series, the next term is often a good guess for the size of the remaining error.
A Levin-type transformation uses such a guess $\omega_n$ and fits the rest of the error by a short expansion in powers of $1/n$.
Solving for the sum then removes several orders of the error at once.
For the geometric series $\sum x^n$ with $\abs{x} < 1$, the error after $n$ terms is exactly a constant times the last term, and the simplest Levin transformation returns the exact sum $\frac{1}{1 - x}$.
