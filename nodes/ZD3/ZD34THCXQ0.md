---
tag: ZD34THCXQ0
kind: concept
name: Primary decomposition
msc: ["13A15", "13C05"]
sources:
  - url: https://en.wikipedia.org/wiki/Primary_decomposition
same_as:
  wikidata: Q172298
  wikipedia: Primary decomposition
---

## Summary

A primary decomposition of an ideal writes it as a finite intersection of [[primary ideals|TMTPWVETQK]].
It generalises the factorisation of an integer into prime powers, since $(n) = (p_1^{e_1}) \cap \cdots \cap (p_k^{e_k})$ in $\Z$ when $n = p_1^{e_1} \cdots p_k^{e_k}$.
By the [[Lasker–Noether theorem|5H8Z56KXMS]], every ideal of a Noetherian ring has one, and its [[associated primes|ERFZ6S8X0X]] are unique.
Geometrically, it splits an algebraic set into irreducible components, with extra embedded components that record finer structure.

## Explanations

### L1 human

In rings without unique factorisation of elements, one can still split ideals into simple pieces.
The pieces are primary ideals, and the ideal is their intersection.
For example, in $\Z$ the ideal $(12)$ is $(4) \cap (3)$.
In the polynomial ring $k[x, y]$ the ideal $(x^2, xy)$ is $(x) \cap (x^2, y)$: the line $x = 0$ together with extra structure at the origin.
