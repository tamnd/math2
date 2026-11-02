---
tag: NT6WDN07RC
kind: concept
name: Fibred category
msc: [18D30]
sources:
  - url: https://en.wikipedia.org/wiki/Fibred_category
same_as:
  wikidata: Q5446431
  wikipedia: Fibred category
---

## Summary

A fibred category is a functor $p \colon \mathcal{E} \to \mathcal{B}$ along which objects can be pulled back.
For every object $y$ of $\mathcal{E}$ and every morphism $f$ into $p(y)$, there is a universal, or cartesian, morphism over $f$ ending at $y$.
Fibred categories describe families of categories indexed by the objects of $\mathcal{B}$, such as sheaves or vector bundles over varying spaces.
They are the setting of Grothendieck's descent theory and of stacks.

## Explanations

### L1 human

Think of $\mathcal{B}$ as a category of spaces and of the objects of $\mathcal{E}$ over a space $b$ as structures on $b$, for example vector bundles on $b$.
Given a map of spaces $f \colon b' \to b$ and a bundle on $b$, one can pull the bundle back to $b'$.
A fibred category is the abstract form of this pullback operation.
The pulled-back object is determined up to unique isomorphism by a universal property, not chosen once and for all.
