---
tag: 9DNFN8M83X
kind: concept
name: Incidence matrix
msc: [05C50]
sources:
  - url: https://en.wikipedia.org/wiki/Incidence_matrix
same_as:
  wikidata: Q939272
  wikipedia: Incidence matrix
---

## Summary

The incidence matrix of a graph records which vertices lie on which edges.
It has a row for each vertex, a column for each edge, and a nonzero entry where the vertex is an end of the edge.
In the oriented version the two ends get opposite signs, and the product of the matrix with its transpose is the [[Laplacian matrix|TN6M6DVZRP]].
More generally, an incidence matrix describes any incidence relation between two finite sets, such as points and blocks of a design.

## Explanations

### L1 human

Make a table with the vertices of a graph down the side and the edges across the top.
Put a $1$ in a cell when the vertex is an end of the edge, and $0$ otherwise.
Each column then has exactly two $1$s, one for each end of the edge, and the row of a vertex has as many $1$s as the vertex has edges.
This table is the incidence matrix.
