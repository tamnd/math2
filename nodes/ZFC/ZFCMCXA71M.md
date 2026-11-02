---
tag: ZFCMCXA71M
kind: concept
name: Δ-complex
msc: [55U10, 57Q05]
sources:
  - url: https://en.wikipedia.org/wiki/Delta_set
---

## Summary

A $\Delta$-complex is a space built by gluing simplices along their faces.
Each face of a simplex is identified with another simplex by the order-preserving linear map.
It is more flexible than a [[simplicial complex|V8GZ0W1ZZ5]].
A simplex may have several of its faces glued together, and two simplices may share all their vertices.
$\Delta$-complexes are the geometric realizations of semi-simplicial sets, also called $\Delta$-sets, and they are the setting of simplicial homology in Hatcher's textbook.

## Explanations

### L1 human

Take some triangles, some edges and some points, and label the corners of every triangle and edge by $0, 1, 2, \dots$ in order.
Glue edges of triangles to edges, and ends of edges to points, always matching the labels in increasing order.
The torus is obtained from two triangles in this way, with only three edges and one vertex in total.
A simplicial complex would need many more triangles for the torus, since in a simplicial complex distinct triangles cannot share all three corners.
