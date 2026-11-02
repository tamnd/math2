---
tag: WW81ARB8K9
kind: concept
name: Simplicial set
msc: [18N50, 55U10]
specializes: [WK0A32TZHB, AND2WHZC8P]
sources:
  - url: https://en.wikipedia.org/wiki/Simplicial_set
same_as:
  wikidata: Q1467124
  wikipedia: Simplicial set
---

## Summary

A simplicial set is a [[presheaf|AND2WHZC8P]] on the [[simplex category|FRFYHJGAN3]], that is, a [[simplicial object|WK0A32TZHB]] in the category of sets.
It records a set $X_n$ of $n$-simplices for each $n$, together with face and degeneracy maps.
Simplicial sets are a combinatorial model for topological spaces up to homotopy, and they extend [[simplicial complexes|V8GZ0W1ZZ5]] by allowing degenerate and repeated simplices.
Through the [[nerve|RV0MKJ3CQ6]] they also contain all small categories, which makes them the basis of [[quasi-categories|9328WEVJEK]].

## Explanations

### L1 human

Imagine building a shape from points, edges, triangles and higher-dimensional triangles, glued along their faces.
A simplicial set lists the pieces of each dimension and says which pieces are faces of which.
It also keeps "flattened" copies of lower pieces, such as an edge whose two ends are the same point, which makes the bookkeeping uniform.
The [[singular simplicial set|RWBMXQW6S5]] of a space $Y$ is an example: its $n$-simplices are the continuous maps from the standard $n$-simplex into $Y$.
The simplest example is the standard $n$-simplex $\Delta^n$, whose $m$-simplices are the order-preserving maps $[m] \to [n]$.
