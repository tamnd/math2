---
tag: 6QF83CFK2G
kind: concept
name: Dual matroid
msc: [05B35]
sources:
  - url: https://en.wikipedia.org/wiki/Dual_matroid
same_as:
  wikidata: Q5310216
  wikipedia: Dual matroid
---

## Summary

The dual of a [[matroid|PX31ZNYS3Z]] $M$ is the matroid $M^*$ on the same ground set whose [[bases|QTSQR7130G]] are the complements of the bases of $M$.
Duality is an involution, $M^{**} = M$, and it exchanges deletion and contraction of [[minors|4WCYBSH1P6]].
For a planar graph, the dual of its graphic matroid is the graphic matroid of the [[dual graph|1QHTD1DS5J]].
So matroid duality extends planar graph duality to all matroids.

## Explanations

### L1 human

In a matroid, a basis is a largest independent set.
Taking the complement of every basis gives the bases of a new matroid, the dual.
For a connected planar graph, the edges outside a spanning tree correspond to a spanning tree of the dual graph, and this is the same idea.
For the uniform matroid in which bases are the $k$-element subsets of an $n$-element set, the dual has the $(n-k)$-element subsets as bases.
