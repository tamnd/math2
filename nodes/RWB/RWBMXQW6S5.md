---
tag: RWBMXQW6S5
kind: concept
name: Singular simplicial set
msc: [55U10, 18N50, 55N10]
sources:
  - url: https://en.wikipedia.org/wiki/Simplicial_set
---

## Summary

The singular simplicial set $\operatorname{Sing} X$ of a topological space $X$ is a simplicial set.
Its $n$-simplices are the continuous maps from the standard topological $n$-simplex into $X$.
It turns a space into combinatorial data without losing its weak homotopy type.
Its chains give singular homology, and it is a Kan complex, so its simplicial homotopy groups are the homotopy groups of $X$.

## Explanations

### L1 human

Look at all the ways of drawing a point, a path, a triangle, a tetrahedron, and so on, inside a space $X$.
The drawings may be crumpled or collapsed; they only have to be continuous.
Restricting a drawn triangle to one of its edges gives a drawn path, and this is the face operation.
The collection of all these drawings, with the face and degeneracy operations, is $\operatorname{Sing} X$.
When $X$ is a single point, there is exactly one drawing in each dimension.
