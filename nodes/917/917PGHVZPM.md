---
tag: 917PGHVZPM
kind: concept
name: Henselization
msc: [13J15, 13B40]
specializes: [MZ02BKPHJA]
sources:
  - url: https://en.wikipedia.org/wiki/Henselian_ring
---

## Summary

The Henselization of a [[local ring|MZ02BKPHJA]] $R$ is the smallest [[Henselian local ring|RNXPV3KC5J]] that receives a local map from $R$.
It is characterized by a universal property among local homomorphisms from $R$ to Henselian local rings.
It keeps the residue field of $R$ and, for a Noetherian $R$, it has the same completion as $R$.
It is a substitute for the completion that stays algebraic over $R$, and it is used in étale cohomology and in approximation theorems.

## Explanations

### L1 human

[[Hensel's lemma|010QVB71T2]] lets one lift a simple root of a polynomial modulo the maximal ideal to a true root.
Many local rings do not have this property, and the Henselization adds just enough elements to get it.
The completion also has the property, but it adds far more elements, most of them transcendental.
For the ring $\Z_{(p)}$ of fractions with denominator prime to $p$, the Henselization is the ring of $p$-adic integers that are algebraic over $\Q$.
So it lies between $\Z_{(p)}$ and the full ring of $p$-adic integers.
