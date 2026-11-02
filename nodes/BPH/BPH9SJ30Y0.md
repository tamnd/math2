---
tag: BPH9SJ30Y0
kind: concept
name: Enriched category
msc: [18D20]
sources:
  - url: https://en.wikipedia.org/wiki/Enriched_category
same_as:
  wikidata: Q5379515
  wikipedia: Enriched category
---

## Summary

A category enriched over a [[monoidal category|M3MSQ3NKAE]] $\mathcal{V}$ has, instead of a set of morphisms between two objects, an object of $\mathcal{V}$.
Composition and identities are morphisms of $\mathcal{V}$ that satisfy associativity and unit laws.
Ordinary locally small [[categories|A2DE66937D]] are the case $\mathcal{V} = \mathbf{Set}$; [[preadditive categories|SC6FD5F4J0]] are the case of abelian groups; strict 2-categories are the case of small categories.
Lawvere observed that [[metric spaces|0VKD1TP7F3]] are categories enriched over the non-negative reals.

## Explanations

### L1 human

In many categories the morphisms between two objects carry extra structure.
Linear maps between vector spaces can be added, continuous maps between spaces form a space, and so on.
An enriched category builds this structure into the definition: the "hom-set" is replaced by a hom-object of some fixed kind.
A surprising example: a metric space is a category whose objects are points and whose "hom-object" from $x$ to $y$ is the number $d(x, y)$.
Composition becomes the triangle inequality.
