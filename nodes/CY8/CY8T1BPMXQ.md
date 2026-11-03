---
tag: CY8T1BPMXQ
kind: concept
name: Lie conformal algebra
msc: [17B69, 17B65, 81R10]
sources:
  - url: https://en.wikipedia.org/wiki/Lie_conformal_algebra
same_as:
  wikidata: Q6543817
  wikipedia: Lie conformal algebra
---

## Summary

A Lie conformal algebra is a module over the polynomial ring $\C[\partial]$ with a $\lambda$-bracket.
The values of this bracket are polynomials in a formal variable $\lambda$.
It encodes the singular part of the operator product expansion of fields in a [[vertex operator algebra|GHRPQAJY43]].
Many infinite-dimensional [[Lie algebras|5JJYBJ6A8K]], such as the [[Virasoro algebra|R9WFXME6GC]] and affine Lie algebras, arise from Lie conformal algebras that are finitely generated over $\C[\partial]$.
The notion was introduced by Victor Kac.

## Explanations

### L1 human

Some infinite-dimensional Lie algebras have bases indexed by integers, like $L_n$ for $n \in \Z$, and their brackets follow a pattern in $n$.
A Lie conformal algebra packs the whole pattern into a finite amount of data.
The formal variable $\lambda$ plays the role of the index, and the operator $\partial$ plays the role of a derivative.
For example, the single generator $L$ with $[L_\lambda L] = (\partial + 2\lambda) L$ encodes the Witt algebra, the Virasoro algebra without its central term.
