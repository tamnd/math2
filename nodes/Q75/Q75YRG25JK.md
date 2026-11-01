---
tag: Q75YRG25JK
kind: concept
name: Polynomial greatest common divisor
msc: [13F20, 13A05]
specializes: [0ZAF9KHDDF]
sources:
  - url: https://en.wikipedia.org/wiki/Polynomial_greatest_common_divisor
same_as:
  wikidata: Q7226640
  wikipedia: Polynomial greatest common divisor
---

## Summary

The greatest common divisor of two polynomials over a field is the monic common divisor that every common divisor divides.
It is the [[greatest common divisor|0ZAF9KHDDF]] in the ring $K[x]$, made unique by asking it to be monic.
The [[Euclidean algorithm|023VY493K0]] computes it with repeated [[long division|D6D0SR1FK3]].
It detects common roots, and $\gcd(f, f')$ detects [[repeated roots|067F8YVYMH]].

## Explanations

### L1 human

Two polynomials may share factors, as two integers may share prime factors.
The greatest common divisor is the product of all the shared factors, counted as often as both contain them.
For example, $x^2 - 1 = (x - 1)(x + 1)$ and $x^2 - 3x + 2 = (x - 1)(x - 2)$ share only $x - 1$, which is their greatest common divisor.
The [[definition|99J1WXG3F7]] gives the conditions.
