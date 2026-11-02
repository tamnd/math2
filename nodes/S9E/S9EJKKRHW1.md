---
tag: S9EJKKRHW1
kind: concept
name: Category of elements
msc: [18A25]
sources:
  - url: https://en.wikipedia.org/wiki/Category_of_elements
same_as:
  wikidata: Q5051844
  wikipedia: Category of elements
---

## Summary

The category of elements of a [[functor|28NQ0KRHD3]] $F \colon \mathcal{C} \to \mathbf{Set}$ has as objects the pairs $(A, x)$ with $x \in F(A)$.
Its morphisms are the morphisms of $\mathcal{C}$ that carry one chosen element to the other.
It turns a set-valued functor into a category lying over $\mathcal{C}$, and it is a special [[comma category|PC6HG1JEGM]].
It is used to write every [[presheaf|AND2WHZC8P]] as a colimit of representable functors, and it is the simplest case of the [[Grothendieck construction|272T16NWZ9]].

## Explanations

### L1 human

A set-valued functor gives a set $F(A)$ for each object $A$, and functions between these sets for each arrow.
The category of elements spreads all these sets out: each element of each set becomes a point.
There is an arrow from $(A, x)$ to $(B, y)$ for each arrow $f \colon A \to B$ whose function sends $x$ to $y$.
For a group acting on a set, this gives a picture with one point per element of the set and one arrow per group element moving one point to another.
