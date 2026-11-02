---
tag: Q0KB9QDH8V
kind: definition
name: Category theory
msc: [18A05]
defines: Q1RZT7DV0F
uses: [A2DE66937D, 28NQ0KRHD3, KYCPCC57FT]
sources:
  - url: https://en.wikipedia.org/wiki/Category_theory
---

## Definition

*Category theory* is the branch of mathematics whose objects of study are:

1. [[categories|A2DE66937D]], made of objects, morphisms between objects, and an associative composition of morphisms with identities;
2. [[functors|28NQ0KRHD3]], the maps between categories that preserve composition and identities;
3. [[natural transformations|KYCPCC57FT]], the maps between two functors with the same source and target.

## Remarks

The three levels are tied together: small categories and functors form a category, and functors from one category to another with natural transformations between them form a category again.
Example: the statement "a functor sends isomorphisms to isomorphisms" belongs to category theory, since it only uses composition and identities.
Indeed, if $g \circ f$ and $f \circ g$ are identities, then so are $F(g) \circ F(f)$ and $F(f) \circ F(g)$.
Non-example: the statement "every finite group of prime order is cyclic" is not a categorical statement, since it refers to the elements of a group.
Its main constructions are limits and colimits, adjoint functors, and the Yoneda lemma.
