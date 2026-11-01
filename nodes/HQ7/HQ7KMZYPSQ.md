---
tag: HQ7KMZYPSQ
kind: concept
name: Primitive polynomial over a finite field
msc: [11T06, "12E20"]
sources:
  - url: https://en.wikipedia.org/wiki/Primitive_polynomial_(field_theory)
same_as:
  wikidata: Q1458669
  wikipedia: Primitive polynomial (field theory)
---

## Summary

A primitive polynomial over a [[finite field|0ZXZ82FTX2]] $\F_q$ is the minimal polynomial of a [[primitive element|00QSK85Y2X]] of some extension $\F_{q^m}$.
With such a polynomial, every nonzero element of $\F_{q^m}$ is a power of one root, which makes multiplication easy to compute.
Primitive polynomials over $\F_2$ give linear feedback shift registers of maximal period.
This notion differs from the [[primitive polynomial|0TXNRQZY0H]] of ring theory, whose coefficients have no common factor.

## Explanations

### L1 human

Take a root $\alpha$ of an irreducible polynomial and look at its powers $\alpha, \alpha^2, \alpha^3, \dots$.
The polynomial is primitive when these powers run through every nonzero element of the field before they come back to $1$.
Over $\F_2$, the polynomial $x^2 + x + 1$ is primitive: its root $\omega$ gives $\omega$, $\omega^2 = \omega + 1$ and $\omega^3 = 1$, which are the three nonzero elements of $\F_4$.
