---
tag: 9G1XS1XZ1F
kind: concept
name: Monoid object
msc: [18M05, 18C40]
sources:
  - url: https://en.wikipedia.org/wiki/Monoid_(category_theory)
same_as:
  wikidata: Q2785361
  wikipedia: Monoid (category theory)
---

## Summary

A monoid object in a [[monoidal category|M3MSQ3NKAE]] is an object $M$ with a multiplication $M \otimes M \to M$ and a unit $I \to M$.
These must satisfy the associativity and unit laws, written as equations between morphisms.
It generalizes the notion of a [[monoid|0N6R902FG1]] to any monoidal category.
Monoids in sets are ordinary monoids, monoids in abelian groups are [[rings|0B1261B5ED]], monoids in vector spaces are associative algebras, and monoids among endofunctors are [[monads|FF6XXA6D1A]].
Many algebraic structures are thus one notion read in different monoidal categories.

## Explanations

### L1 human

A monoid is a set with an associative multiplication and a unit, like the whole numbers under addition.
A monoid object asks for the same thing, but the "set" may be any object of a monoidal category and the multiplication is a morphism.
The laws are written as equalities of composite morphisms instead of equations between elements.
For example, a ring is an abelian group $R$ with a multiplication map $R \otimes R \to R$ that is associative and has a unit $1$: a monoid object in abelian groups.
