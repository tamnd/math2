---
tag: J3NJQ5FZJ5
kind: concept
name: Trigonometric polynomial
msc: [42A05, 42A10]
sources:
  - url: https://en.wikipedia.org/wiki/Trigonometric_polynomial
same_as:
  wikidata: Q1969650
  wikipedia: Trigonometric polynomial
---

## Summary

A trigonometric polynomial is a finite linear combination of the functions $e^{inx}$, $n \in \Z$, or equivalently of $1$, $\cos nx$ and $\sin nx$.
Trigonometric polynomials are the partial sums of [[Fourier series|G12KXDHPPS]].
They are dense in the continuous $2\pi$-periodic functions, so they play for periodic functions the role that ordinary polynomials play on a closed interval.

## Explanations

### L1 human

A trigonometric polynomial is a sum of finitely many pure waves, each with a whole-number frequency.
Its graph repeats itself after every interval of length $2\pi$.
An example is $T(x) = 1 + 2\cos x - 3 \sin 2x$, which has degree $2$, the largest frequency present.
Writing $z = e^{ix}$ turns it into a sum of powers $z^n$ with $n$ positive or negative, which explains the word polynomial.
