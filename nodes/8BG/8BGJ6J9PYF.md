---
tag: 8BGJ6J9PYF
kind: concept
name: Bar resolution
msc: [20J06, 18G10, "16E40"]
specializes: [HK2AA1YSQ2]
sources:
  - url: https://en.wikipedia.org/wiki/Bar_complex
---

## Summary

The bar resolution of a group $G$ is an explicit free resolution of the trivial module $\Z$ over the [[group ring|MNP2HBWB5Q]] $\Z[G]$.
Its basis elements in degree $n$ are the symbols $[g_1 | \cdots | g_n]$, one for each list of $n$ elements of $G$.
It turns [[group cohomology|YXJXA0Q52R]] into a concrete computation with functions of $n$ group elements, which gives the classical cocycle descriptions of $H^1$ and $H^2$.
The same construction exists for augmented algebras, where it computes Hochschild homology and Tor.

## Explanations

### L1 human

To compute group cohomology one needs a resolution, and the bar resolution is one that works for every group without any choices.
Its pieces are free modules with a basis vector for every list of group elements.
The boundary map multiplies neighbouring entries of the list, with alternating signs, and drops the first or last entry at the ends.
It is large and wasteful for computing, but its uniformity makes it the right tool for proofs and for writing down cocycles.
