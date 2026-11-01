---
tag: JJP4JFH3C6
kind: concept
name: Induced representation
msc: [20C15]
specializes: [WYGRXCG2RN]
sources:
  - url: https://en.wikipedia.org/wiki/Induced_representation
same_as:
  wikidata: Q3427423
  wikipedia: Induced representation
---

## Summary

Induction builds a [[representation|WYGRXCG2RN]] of a group $G$ from a representation of a [[subgroup|0X1JXT47GA]] $H$.
The induced representation is a sum of copies of the given space, one for each left coset of $H$, which $G$ permutes.
Induction is adjoint to restriction, by [[Frobenius reciprocity|PAP76H0ND9]].
Many representations of finite groups are constructed this way.

## Explanations

### L1 human

Suppose you know how a subgroup $H$ acts on a space $W$.
Take one copy of $W$ for each coset of $H$ in $G$, and let $G$ shuffle the copies while acting inside them through $H$.
The result is a representation of the whole group.
For instance, inducing the trivial representation of $H$ gives the permutation representation of $G$ on the cosets $G/H$.
Inducing from the trivial subgroup gives the regular representation, where $G$ acts on its own group algebra.
