---
tag: Y2SPPSQ5D4
kind: concept
name: Iwasawa theory
msc: [11R23]
sources:
  - url: https://en.wikipedia.org/wiki/Iwasawa_theory
same_as:
  wikidata: Q1392559
  wikipedia: Iwasawa theory
---

## Summary

Iwasawa theory studies arithmetic objects, such as [[ideal class groups|WQ46BD3ARY]], along an infinite tower of number fields $K = K_0 \subset K_1 \subset K_2 \subset \cdots$.
The union of the tower has Galois group isomorphic to the additive group of [[p-adic integers|V6TJAFZ4MD]] $\Z_p$.
Such a tower is a $\Z_p$-extension, and the main example is obtained from the fields $\Q(\zeta_{p^n})$ of $p$-power roots of unity.
The objects attached to the whole tower are modules over the Iwasawa algebra $\Z_p[\![T]\!]$, whose structure theory gives regular growth formulas.
The [[Iwasawa main conjecture|67A4D4FAYJ]] links these modules to $p$-adic $L$-functions.

## Explanations

### L1 human

Instead of studying one number field at a time, Iwasawa theory looks at an infinite tower of fields, each of degree $p$ over the one below.
The class numbers along the tower grow in a very regular way.
Iwasawa proved that the power of $p$ dividing the $n$-th class number is $p^{e_n}$ with $e_n = \mu p^n + \lambda n + \nu$ for all large $n$, for some fixed integers $\lambda, \mu, \nu$.
For example, if $p$ divides no class number in the tower $\Q(\zeta_{p^{n+1}})$, all three of these numbers are $0$.
Studying the whole tower at once reveals structure that is hidden in each single field.
