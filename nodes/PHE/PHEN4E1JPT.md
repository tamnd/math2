---
tag: PHEN4E1JPT
kind: concept
name: Hopfian group
msc: ["20E26", "20E36"]
specializes: [G5S1M9]
sources:
  - url: https://en.wikipedia.org/wiki/Hopfian_group
same_as:
  wikidata: Q5900529
  wikipedia: Hopfian group
---

## Summary

A [[group|G5S1M9]] is Hopfian if every surjective homomorphism from the group to itself is an isomorphism.
Equivalently, the group is not isomorphic to any of its proper quotients.
Finite groups, $\Z$ and every finitely generated [[residually finite group|HEE922EHQ8]] are Hopfian.
The [[Baumslag–Solitar group|429JJ5ZNBY]] $BS(2, 3)$ is a finitely presented group that is not Hopfian.

## Explanations

### L1 human

A homomorphism can collapse parts of a group.
A Hopfian group cannot collapse a part and still look like the whole group afterwards.
For finite groups this is clear by counting: a map from a finite set onto itself is a bijection.
An infinite group can fail.
Take the group of all sequences $(x_1, x_2, \ldots)$ of elements of $\Z/2$ that are $0$ from some point on.
Deleting the first term is onto, but it kills the sequence $(1, 0, 0, \ldots)$.
