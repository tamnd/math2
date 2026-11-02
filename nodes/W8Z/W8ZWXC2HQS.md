---
tag: W8ZWXC2HQS
kind: concept
name: Frobenius method
msc: [34M03, 34A25]
sources:
  - url: https://en.wikipedia.org/wiki/Frobenius_method
same_as:
  wikidata: Q1340153
  wikipedia: Frobenius method
---

## Summary

The Frobenius method finds solutions of a second-order linear differential equation near a [[regular singular point|H96HXG6CA0]] in the form $(z - z_0)^r \sum_{k \ge 0} a_k (z - z_0)^k$.
The exponent $r$ comes from a quadratic equation, the indicial equation, and the coefficients $a_k$ from a recurrence.
It extends the [[power series method|08RT9GDDPQ]], which works only at ordinary points.
It produces Bessel functions, Legendre functions and hypergeometric functions.
See the [[definition|7D47PADY9N]].

## Explanations

### L1 human

Near a regular singular point the solutions look like a power $z^r$ times an ordinary power series.
The power $r$ need not be a whole number, and it is found first by looking at the lowest terms of the equation.
Then the series coefficients follow one after another.
For $z^2 y'' + z y' + (z^2 - \frac{1}{4}) y = 0$, the exponents are $r = \pm \frac{1}{2}$, and the method gives $z^{-1/2} \sin z$ and $z^{-1/2} \cos z$.
