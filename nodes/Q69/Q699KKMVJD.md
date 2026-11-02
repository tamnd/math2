---
tag: Q699KKMVJD
kind: concept
name: Pushout
msc: [18A30]
specializes: [BJS1CGTKQ5]
sources:
  - url: https://en.wikipedia.org/wiki/Pushout_(category_theory)
same_as:
  wikidata: Q1633079
  wikipedia: Pushout (category theory)
---

## Summary

A pushout is the [[colimit|BJS1CGTKQ5]] of a diagram made of two morphisms with a common source.
It glues two objects together along the images of a third object.
Pushouts give gluing of spaces, amalgamated free products of groups and tensor products of commutative rings.
It is the dual notion of a [[pullback|Q05K04QJ71]].

## Explanations

### L1 human

Take two objects $X$ and $Y$ and a common piece $Z$ that maps into both.
The pushout is the smallest object in which $X$ and $Y$ sit side by side and the two copies of $Z$ are glued into one.
For sets, take the disjoint union of $X$ and $Y$ and identify $f(z)$ with $g(z)$ for each $z$ in $Z$.
For example, gluing two closed intervals at one end point gives a longer interval.
In the same way, gluing two discs along their boundary circles gives a sphere.
