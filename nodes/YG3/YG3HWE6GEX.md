---
tag: YG3HWE6GEX
kind: concept
name: Finite field arithmetic
msc: ["12E20", 11T71, "12-08"]
sources:
  - url: https://en.wikipedia.org/wiki/Finite_field_arithmetic
same_as:
  wikidata: Q5450398
  wikipedia: Finite field arithmetic
---

## Summary

Finite field arithmetic is the way to add, multiply and divide elements of a [[finite field|0ZXZ82FTX2]] in practice.
The usual model of $\F_{p^n}$ is the set of polynomials of degree less than $n$ over $\F_p$.
One computes with them modulo a fixed [[irreducible polynomial|03FKX7Z5DC]] of degree $n$.
It is the basis of error-correcting codes and of much of modern cryptography.

## Explanations

### L1 human

In $\F_p$ one computes with integers modulo a prime $p$.
For a field with $p^n$ elements, one computes with polynomials instead, and one reduces modulo a fixed polynomial, as one reduces integers modulo $p$.
Over $\F_2$, an element of $\F_{2^8}$ is a string of $8$ bits, and addition is the bitwise exclusive or.
For example, in $\F_8$ built with $x^3 + x + 1$, one has $x^3 = x + 1$, so $(x^2 + 1)(x + 1) = x^3 + x^2 + x + 1 = x^2$.
