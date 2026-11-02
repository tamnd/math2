---
tag: SDTZVZ6B4Q
kind: concept
name: Model category
msc: [18N40, 55U35]
sources:
  - url: https://en.wikipedia.org/wiki/Model_category
same_as:
  wikidata: Q1941896
  wikipedia: Model category
---

## Summary

A model category is a [[category|A2DE66937D]] with three chosen classes of morphisms, called weak equivalences, fibrations and cofibrations, that satisfy axioms modelled on topological spaces.
Quillen introduced model categories in 1967 to do homotopy theory in settings such as simplicial sets and chain complexes.
The weak equivalences are the maps to be treated as isomorphisms, and the fibrations and cofibrations give the tools to compute with them.
The homotopy category of a model category, obtained by inverting the weak equivalences, has a concrete description in terms of homotopy classes of maps.

## Explanations

### L1 human

In topology one often wants to regard two spaces as the same when one can be deformed into the other.
Making such deformations into honest isomorphisms is easy to say but hard to compute with.
A model category adds two kinds of well-behaved maps, fibrations and cofibrations, which play the roles of nice projections and nice inclusions.
With them one can replace any object by a good one and compute maps up to homotopy as in topology.
Topological spaces, simplicial sets and chain complexes of modules all carry standard model structures.
