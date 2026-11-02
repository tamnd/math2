---
tag: 2HVC5G0H5K
kind: concept
name: Poincaré asymptotic series
msc: [41A60, "30E15", "34E05"]
specializes: [BJQTEPEZ9G]
sources:
  - url: https://en.wikipedia.org/wiki/Asymptotic_expansion
---

## Summary

A Poincaré asymptotic series of a function $f$ at infinity is a formal power series $\sum a_n z^{-n}$ with one property.
Every partial sum approximates $f$ with an error smaller than the last power used.
It is the [[asymptotic expansion|BJQTEPEZ9G]] for the [[asymptotic scale|XEGB8Y44GG]] of the powers $z^{-n}$, as defined by Poincaré in 1886.
The series may diverge for every $z$, and still give very accurate approximations.
The coefficients are unique when they exist, but different functions can have the same series.

## Explanations

### L1 human

Think of a series in powers of $1/z$ that is useful for large $z$ even though it may never converge.
The rule is: stop after any finite number of terms, and the error goes to zero faster than the last term you kept.
For example, $\frac{1}{z - 1} = \frac1z + \frac{1}{z^2} + \frac{1}{z^3} + \cdots$ is a Poincaré series at infinity that happens to converge.
The series $\sum_{n \ge 0} (-1)^n n!\, z^{-n-1}$ of the [[exponential integral|EV6ZDQ0NDY]] $e^z E_1(z)$ is one that diverges for every $z$.
