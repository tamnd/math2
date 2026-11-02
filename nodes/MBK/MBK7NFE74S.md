---
tag: MBK7NFE74S
kind: concept
name: Rng
msc: [16B99]
sources:
  - url: https://en.wikipedia.org/wiki/Rng_(algebra)
same_as:
  wikidata: Q17102802
  wikipedia: Rng (algebra)
---

## Summary

A rng, also called a non-unital ring, is a structure with all the axioms of a [[ring|0B1261B5ED]] except the existence of a multiplicative identity.
The name is "ring" without the letter "i", for "identity".
Rngs arise naturally: ideals, rings of functions with compact support, and many algebras in analysis have no unit element.
Every rng embeds as an ideal in a ring with identity, so much of ring theory still applies.

## Explanations

### L1 human

A rng has addition and multiplication with the usual rules, but there may be no number $1$ that leaves every element unchanged.
The even integers $2\Z$ are the standard example: they are closed under addition and multiplication, but $1$ is not even.
No even integer $e$ satisfies $e \cdot 2 = 2$, so $2\Z$ has no identity.
