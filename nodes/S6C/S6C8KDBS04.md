---
tag: S6C8KDBS04
kind: concept
name: Skew polynomial ring
msc: [16S36, 16W20]
specializes: [VF3PV13BA1]
sources:
  - url: https://en.wikipedia.org/wiki/Ore_extension
---

## Summary

A skew polynomial ring $R[x; \sigma]$ is a ring of polynomials over a [[ring|0B1261B5ED]] $R$ in which the variable twists the coefficients.
The rule is $x a = \sigma(a) x$ for a fixed endomorphism $\sigma$ of $R$.
It is the [[Ore extension|VF3PV13BA1]] with zero derivation.
Some authors use the name skew polynomial ring for every Ore extension $R[x; \sigma, \delta]$.
Skew polynomial rings over finite fields are used in coding theory, and quantum planes are skew polynomial rings.

## Explanations

### L1 human

Polynomials are added as usual, but multiplying $x$ past a coefficient $a$ replaces it with $\sigma(a)$.
Over the complex numbers with $\sigma$ the complex conjugation, $x \cdot i = -i \cdot x$.
So $x$ anticommutes with $i$ but commutes with real numbers.
The order of factors now matters, while every element is still a sum $a_0 + a_1 x + \cdots + a_n x^n$.
