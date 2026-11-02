---
tag: A7W468BQSM
kind: concept
name: Grothendieck category
msc: ["18E10"]
specializes: [Y9CZ3MTNF1]
sources:
  - url: https://en.wikipedia.org/wiki/Grothendieck_category
same_as:
  wikidata: Q5610721
  wikipedia: Grothendieck category
---

## Summary

A Grothendieck category is an [[abelian category|Y9CZ3MTNF1]] with all small colimits, in which filtered colimits are exact, and which has a generator.
Grothendieck introduced these conditions in his 1957 Tôhoku paper and proved that such categories have enough injective objects.
This made it possible to define sheaf cohomology as a derived functor.
Module categories and categories of sheaves of abelian groups are Grothendieck categories.
By the [[Gabriel–Popescu theorem|3MP41FQHZ5]], every Grothendieck category is a localization of a module category.

## Explanations

### L1 human

Abelian categories are a good setting for homological algebra, but some need extra properties to construct resolutions.
A Grothendieck category asks for three things that modules have.
One can glue infinitely many objects together, and gluing along a directed system does not destroy exactness.
There is also one object, like the ring itself, from which all others can be probed.
With these, every object embeds in an injective object, so derived functors such as sheaf cohomology can be defined.
