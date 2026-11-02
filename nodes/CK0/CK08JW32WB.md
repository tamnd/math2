---
tag: CK08JW32WB
kind: concept
name: Generator
msc: [18A05, 18A20]
sources:
  - url: https://en.wikipedia.org/wiki/Generator_(category_theory)
same_as:
  wikidata: Q17000267
  wikipedia: Generator (category theory)
---

## Summary

A generator, also called a separator, of a [[category|A2DE66937D]] is an object $G$ with the following property.
Its morphisms into other objects are enough to tell any two different parallel morphisms apart.
Equivalently, the [[hom functor|VJXS8AK67E]] $\Hom(G, -)$ is faithful.
Generators and the dual cogenerators appear as hypotheses in the special adjoint functor theorem, and generators are part of the definition of a Grothendieck category.

## Explanations

### L1 human

Two functions $f, g \colon X \to Y$ are different exactly when they differ at some point $x$ of $X$.
In the category of sets, a point of $X$ is the same as a map from the one-point set $\{*\}$ to $X$.
So $\{*\}$ can "probe" every difference between maps: it is a generator.
In the category of abelian groups, the group $\Z$ plays the same role, since a homomorphism $\Z \to A$ is the same as an element of $A$.
A generator is an object whose probes see everything.
