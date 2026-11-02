---
tag: 9328WEVJEK
kind: concept
name: Quasi-category
msc: [18N60, 18N50]
specializes: [WW81ARB8K9]
sources:
  - url: https://en.wikipedia.org/wiki/Quasi-category
same_as:
  wikidata: Q7269442
  wikipedia: Quasi-category
---

## Summary

A quasi-category is a [[simplicial set|WW81ARB8K9]] in which every inner horn has a filler.
Quasi-categories are the most used model of [[(∞,1)-categories|YFY1FWA1MY]], developed by Joyal and Lurie.
They include both ordinary categories, through their [[nerves|RV0MKJ3CQ6]], and [[Kan complexes|FDFYCM3YYC]], which model $\infty$-groupoids.
Much of ordinary category theory, including limits, adjunctions and the Yoneda lemma, extends to quasi-categories.

## Explanations

### L1 human

A simplicial set has points, arrows between points, triangles, tetrahedra and so on.
Think of points as objects and arrows as morphisms; a triangle with edges $f$, $g$ and $h$ says that $h$ is a composite of $f$ and $g$.
In a quasi-category, any two arrows that meet end to start can be composed: there is a triangle that fills them in.
The composite is not unique, but any two choices are linked by higher simplices, so it is unique up to a contractible space of choices.
