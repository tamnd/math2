---
tag: M0Q5CFJ7ZH
kind: concept
name: Singular homology
msc: [55N10]
sources:
  - url: https://en.wikipedia.org/wiki/Singular_homology
same_as:
  wikidata: Q1095056
  wikipedia: Singular homology
---

## Summary

Singular homology assigns to every topological space $X$ a sequence of abelian groups $H_n(X)$, built from all continuous maps of simplices into $X$.
It is defined for every space without any choice, it is functorial, and it is invariant under homotopy equivalence.
It satisfies the Eilenberg–Steenrod axioms, and on CW complexes and simplicial complexes it agrees with cellular and simplicial homology, which makes it computable.

## Explanations

### L1 human

Singular homology looks at all the ways of placing points, paths, triangles and higher simplices into a space, however crumpled.
It forms formal sums of them and keeps those sums that have no boundary, modulo those that bound something bigger.
What remains counts holes: $H_0$ counts path components, $H_1$ detects loops that do not bound, and so on.
For example, the circle has $H_0 \cong \Z$, $H_1 \cong \Z$ and all higher groups zero.
