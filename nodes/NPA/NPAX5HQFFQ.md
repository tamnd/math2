---
tag: NPAX5HQFFQ
kind: concept
name: Tame symbol
msc: [19F15, 19C20]
sources:
  - url: https://en.wikipedia.org/wiki/Symbol_(number_theory)
---

## Summary

The tame symbol is a Steinberg symbol attached to a discrete valuation on a field, with values in the multiplicative group of the residue field.
It induces the boundary map from $K_2$ of the field to $K_1$ of the residue field.
Tame symbols at all primes are the main tool in Tate's computation of $K_2(\Q)$.
The Legendre symbol modulo an odd prime $p$ can be read off from the tame symbol at $p$.

## Explanations

### L1 human

Take two nonzero rational numbers and a prime $p$.
Combine them, with suitable powers, into a number with no factor $p$ in the numerator or denominator, and reduce it modulo $p$.
The result is the tame symbol, a nonzero residue modulo $p$.
For example, at $p$, the pair $(p, u)$ with $u$ prime to $p$ gives the residue of $u^{-1}$ modulo $p$.
