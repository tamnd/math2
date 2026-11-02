---
tag: 28NQ0KRHD3
kind: concept
name: Functor
msc: [18A05, 18A22]
sources:
  - url: https://en.wikipedia.org/wiki/Functor
same_as:
  wikidata: Q864475
  wikipedia: Functor
---

## Summary

A functor is a map between two [[categories|A2DE66937D]]: it sends objects to objects and [[morphisms|859F0TFVA3]] to morphisms, and it respects composition and identities.
Functors are how one field of mathematics is translated into another, as when the [[fundamental group|S1XK3HXHFX]] turns spaces and continuous maps into groups and homomorphisms.
Because functors preserve composition, they send isomorphisms to isomorphisms, which makes them a source of invariants.
Functors between two categories are compared by [[natural transformations|KYCPCC57FT]].

## Explanations

### L1 human

A functor takes every object of one category to an object of another, and every arrow to an arrow between the images.
It must send a chain of arrows to the chain of the images, and an identity arrow to an identity arrow.
A simple example forgets structure: send each group to its underlying set and each homomorphism to the same map seen as a function.
A deeper one sends each space to its fundamental group.
If two spaces are homeomorphic, their fundamental groups are isomorphic, so different groups prove that two spaces are different.
