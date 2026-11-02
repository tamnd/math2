---
tag: 6ERBSBVF14
kind: concept
name: Essentially surjective functor
msc: [18A22]
sources:
  - url: https://en.wikipedia.org/wiki/Essentially_surjective_functor
same_as:
  wikidata: Q140283
  wikipedia: Essentially surjective functor
---

## Summary

A [[functor|28NQ0KRHD3]] $F \colon \mathcal{C} \to \mathcal{D}$ is essentially surjective when every object of $\mathcal{D}$ is isomorphic to $F(A)$ for some object $A$ of $\mathcal{C}$.
It is surjectivity on objects up to isomorphism, which is the right notion in category theory, where isomorphic objects are interchangeable.
A [[fully faithful|GRG8WEBSH5]] and essentially surjective functor is an [[equivalence of categories|K7A04ZBD92]].

## Explanations

### L1 human

A functor might not hit every object of its target, but it can still reach every object up to isomorphism.
For example, the vector spaces $\R^n$ for $n = 0, 1, 2, \dots$ are only a few of all finite-dimensional real vector spaces.
Yet each finite-dimensional real vector space is isomorphic to one of them.
So including the spaces $\R^n$ into all finite-dimensional spaces is essentially surjective, though far from surjective on objects.
