---
tag: XDY1GDM2JW
kind: concept
name: Fox–Wright function
msc: ["33C20", "33E12"]
sources:
  - url: https://en.wikipedia.org/wiki/Fox%E2%80%93Wright_function
same_as:
  wikidata: Q5477346
  wikipedia: Fox–Wright function
---

## Summary

The Fox–Wright function ${}_p\Psi_q$ is a power series whose coefficients are ratios of products of values $\Gamma(a + A n)$.
Here $\Gamma$ is the [[gamma function|0H5SYBSED9]] and the scale factors $A$ are positive.
When all scale factors equal $1$ it reduces to a [[generalized hypergeometric function|VDBAW9PN88]], up to a constant factor.
It contains the [[Mittag-Leffler function|12G9M694YG]] and the Wright function as special cases, and it is a special case of the [[Fox H-function|EAZMKENA4N]].

## Explanations

### L1 human

In a hypergeometric series, the $n$-th coefficient is built from rising factorials such as $a(a+1)\cdots(a+n-1) = \Gamma(a+n)/\Gamma(a)$.
The Fox–Wright function allows $\Gamma(a + An)$ instead, so the argument of the gamma function may grow at any positive speed $A$.
This one extra parameter per factor covers many functions of fractional calculus.
For example, one numerator factor $\Gamma(1 + n)$ and one denominator factor $\Gamma(\beta + \alpha n)$ give the Mittag-Leffler function $\sum z^n / \Gamma(\alpha n + \beta)$.
