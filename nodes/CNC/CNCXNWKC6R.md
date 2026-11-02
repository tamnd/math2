---
tag: CNCXNWKC6R
kind: concept
name: Sieve
msc: [18F10, 18F20]
sources:
  - url: https://en.wikipedia.org/wiki/Sieve_(category_theory)
same_as:
  wikidata: Q7511782
  wikipedia: Sieve (category theory)
---

## Summary

A sieve on an object $c$ of a [[category|A2DE66937D]] is a collection of morphisms with codomain $c$ that is closed under composition on the right.
Equivalently, it is a subfunctor of the [[representable functor|KCCHH87H6E]] $\Hom(-, c)$.
Sieves are the building blocks of [[Grothendieck topologies|GDRFSJ8E2B]]: a Grothendieck topology chooses which sieves count as coverings.
They play the role of open covers in a topological space.

## Explanations

### L1 human

Think of $c$ as an open set and of morphisms $d \to c$ as smaller open sets inside it.
A sieve on $c$ is a family of such smaller sets that is closed under shrinking.
If $V$ is in the family and $W \subseteq V$ is open, then $W$ is in the family too.
For example, for an open cover $\set{U_i}$ of $U$, all open sets contained in some $U_i$ form a sieve on $U$.
Working with sieves rather than covers removes the choice of a particular list of sets.
