---
tag: GRG8WEBSH5
kind: concept
name: Full and faithful functors
msc: [18A22]
sources:
  - url: https://en.wikipedia.org/wiki/Full_and_faithful_functors
same_as:
  wikidata: Q1064276
  wikipedia: Full and faithful functors
---

## Summary

A [[functor|28NQ0KRHD3]] is faithful when it is injective on each set of morphisms between two fixed objects.
It is full when it is surjective on each such set, and fully faithful when it is both.
A faithful functor loses no information about morphisms, and a fully faithful one identifies the morphisms of its source with those between the images.
Forgetful functors such as groups to sets are faithful but not full.
Fully faithful functors are the embeddings of category theory, and the Yoneda embedding is the main example.
Together with [[essential surjectivity|6ERBSBVF14]] they characterize [[equivalences of categories|K7A04ZBD92]].

## Explanations

### L1 human

Look at all the arrows between two objects, and at all the arrows between their images.
A functor gives a map from the first collection to the second.
It is faithful if different arrows stay different, and full if every arrow between the images comes from some arrow.
Forgetting that a group is a group is faithful, since a homomorphism is determined by its underlying function.
It is not full, because most functions between two groups are not homomorphisms.
