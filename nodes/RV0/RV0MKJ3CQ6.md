---
tag: RV0MKJ3CQ6
kind: concept
name: Nerve of a category
msc: [18N50, 55U10]
specializes: [WW81ARB8K9]
sources:
  - url: https://en.wikipedia.org/wiki/Nerve_(category_theory)
same_as:
  wikidata: Q17099363
  wikipedia: Nerve (category theory)
---

## Summary

The nerve of a small [[category|A2DE66937D]] $\mathcal{C}$ is the [[simplicial set|WW81ARB8K9]] whose $n$-simplices are the strings of $n$ composable morphisms of $\mathcal{C}$.
The construction is a fully faithful [[functor|28NQ0KRHD3]] from small categories to simplicial sets, so no information about $\mathcal{C}$ is lost.
Its geometric realization is the classifying space of $\mathcal{C}$; for a group $G$ viewed as a one-object category it gives the classifying space $BG$.
Nerves are the basic examples of [[quasi-categories|9328WEVJEK]] and, for groupoids, of [[Kan complexes|FDFYCM3YYC]].

## Explanations

### L1 human

Draw a point for each object of the category and an edge for each arrow.
Fill in a triangle for each pair of arrows that can be composed, with the composite as the third side.
Then fill in a tetrahedron for each string of three composable arrows, and so on.
The resulting shape is the nerve.
For example, the category $0 \to 1$ with one non-identity arrow has as nerve a single edge, the standard $1$-simplex $\Delta^1$, plus its degenerate simplices.
