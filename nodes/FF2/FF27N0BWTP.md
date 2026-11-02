---
tag: FF27N0BWTP
kind: concept
name: Pseudo-differential operator
msc: [35S05, 47G30]
sources:
  - url: https://en.wikipedia.org/wiki/Pseudo-differential_operator
same_as:
  wikidata: Q1644451
  wikipedia: Pseudo-differential operator
---

## Summary

A pseudo-differential operator is an operator of the form $u \mapsto \int e^{i x \cdot \xi} a(x, \xi) \hat{u}(\xi) \, d\xi / (2\pi)^n$, where the symbol $a$ belongs to a [[symbol class|AM4RNWVV4Q]].
Linear differential operators with smooth bounded coefficients are the case where $a$ is a polynomial in $\xi$.
Pseudo-differential operators form an algebra that also contains approximate inverses of elliptic operators.
They are a basic tool of microlocal analysis and of the theory of linear partial differential equations.

## Explanations

### L1 human

The [[Fourier transform|DPVM34ADZV]] turns differentiation into multiplication: $\partial_x$ becomes multiplication by $i\xi$.
So a differential operator is the same as multiplication by a polynomial in frequency space.
A pseudo-differential operator allows other functions of frequency, such as $\sqrt{1 + \xi^2}$, and lets them depend on position too.
This makes it possible to divide by a symbol, and so to invert an elliptic operator up to a small error.
For example, $(1 - \Delta)^{-1}$ is the pseudo-differential operator with symbol $(1 + \abs{\xi}^2)^{-1}$.
