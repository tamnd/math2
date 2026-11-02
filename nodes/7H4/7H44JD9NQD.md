---
tag: 7H44JD9NQD
kind: concept
name: Holonomic function
msc: [33F10, 34M03, 12H05]
sources:
  - url: https://en.wikipedia.org/wiki/Holonomic_function
same_as:
  wikidata: Q5884209
  wikipedia: Holonomic function
---

## Summary

A holonomic function, also called a D-finite function, is a function or [[formal power series|033WGN00BF]] that satisfies a [[linear differential equation|0QQRP17Z7S]] whose coefficients are polynomials.
Many [[special functions|HWY72ZK273]] are holonomic, for example the exponential, the sine, the logarithm, the [[hypergeometric function|463X5V31D9]] and the [[Bessel functions|CZCMRDWDYW]].
The class is closed under sums and products, and the coefficients of a holonomic power series satisfy a [[recurrence|0FYX44GP92]] with polynomial coefficients.
For this reason such a differential equation is a finite data structure for the function, which computer algebra uses to prove identities automatically.

## Explanations

### L1 human

Some functions can be described by a short rule that ties the function to its own derivatives.
A holonomic function is one for which this rule is linear and has polynomials as coefficients.
For example $f(x) = e^{x^2}$ satisfies $f'(x) - 2x f(x) = 0$, so it is holonomic.
Knowing the equation and a few starting values pins down the function completely.
The [[gamma function|0H5SYBSED9]] is a well known function that is not holonomic.
