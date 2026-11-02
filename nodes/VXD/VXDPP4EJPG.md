---
tag: VXDPP4EJPG
kind: concept
name: Exact couple
msc: [55T05, 18G40]
sources:
  - url: https://en.wikipedia.org/wiki/Exact_couple
same_as:
  wikidata: Q25098609
  wikipedia: Exact couple
---

## Summary

An exact couple is a pair of abelian groups with three maps between them that form an exact triangle.
From it one builds a derived exact couple, and repeating this gives a spectral sequence.
Many spectral sequences of algebraic topology arise in this way.
Examples are the spectral sequence of a filtered space, the Bockstein spectral sequence and the Adams spectral sequence.

## Explanations

### L1 human

Long exact sequences in topology often come in families, one for each step of a filtration.
An exact couple packages such a family into a triangle of two groups and three maps, exact at each corner.
The composite of two of the maps squares to zero, so one can take its homology.
Doing this again and again produces the pages of a spectral sequence.
For example, multiplication by a prime $p$ on integral homology and the reduction to mod $p$ homology form an exact couple that gives the Bockstein spectral sequence.
