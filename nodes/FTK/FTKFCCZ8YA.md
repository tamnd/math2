---
tag: FTKFCCZ8YA
kind: concept
name: Koszul algebra
msc: [16S37]
specializes: [3CTW1P4HBP]
sources:
  - url: https://en.wikipedia.org/wiki/Koszul_algebra
same_as:
  wikidata: Q6433697
  wikipedia: Koszul algebra
---

## Summary

A Koszul algebra is a graded [[associative algebra|3CTW1P4HBP]] over a field whose trivial module has a linear projective resolution.
This means that the $i$-th term of the resolution is generated in degree $i$.
Polynomial algebras and [[exterior algebras|0MDMZ965VE]] are the basic examples, resolved by the [[Koszul complex|YZY11W08SD]].
Koszul algebras are quadratic, and they are the setting of [[Koszul duality|6AW49BZ8TM]].

## Explanations

### L1 human

To understand a graded algebra one often resolves its simplest module, the field $k$, by free modules.
For most algebras the generators of these free modules sit in irregular degrees.
A Koszul algebra is one where the $i$-th step is generated exactly in degree $i$, as tidy as possible.
For the polynomial ring $k[x]$ the resolution is $0 \to k[x] \xrightarrow{x} k[x] \to k \to 0$, with generators in degrees $0$ and $1$.
This tidiness makes many invariants of a Koszul algebra computable from its quadratic relations.
