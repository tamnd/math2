---
tag: VF3PV13BA1
kind: concept
name: Ore extension
msc: [16S36, 16W20, 16W25]
specializes: [D1SA8CHJV0]
sources:
  - url: https://en.wikipedia.org/wiki/Ore_extension
same_as:
  wikidata: Q7100975
  wikipedia: Ore extension
---

## Summary

An Ore extension $R[x; \sigma, \delta]$ of a [[ring|0B1261B5ED]] $R$ is a ring of polynomials $\sum a_i x^i$ in which the variable does not commute with the coefficients.
Instead, $x a = \sigma(a) x + \delta(a)$ for an endomorphism $\sigma$ of $R$ and a twisted [[derivation|3J89REV9WQ]] $\delta$.
Ore extensions give many of the basic examples of [[noncommutative rings|D1SA8CHJV0]], such as the [[Weyl algebras|98QE7KY55W]] and quantum planes.
They keep good properties of $R$, such as being a domain or being Noetherian, under mild conditions.

## Explanations

### L1 human

In an ordinary polynomial ring the variable $x$ commutes with every coefficient.
In an Ore extension, moving $x$ past a coefficient $a$ changes $a$ to $\sigma(a)$ and adds a correction term $\delta(a)$.
Every element can still be written uniquely as $a_0 + a_1 x + \cdots + a_n x^n$, so the ring looks like a polynomial ring, only with a new rule of multiplication.
For example, with $R = k[y]$, $\sigma$ the identity and $\delta = d/dy$, the rule $xy = yx + 1$ gives the first Weyl algebra.
