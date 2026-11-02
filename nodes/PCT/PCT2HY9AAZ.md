---
tag: PCT2HY9AAZ
kind: concept
name: Generalized polygon
msc: ["51E12", "51E24"]
sources:
  - url: https://en.wikipedia.org/wiki/Generalized_polygon
same_as:
  wikidata: Q5532502
  wikipedia: Generalized polygon
---

## Summary

A generalized $n$-gon is an incidence structure of points and lines whose incidence graph has diameter $n$ and girth $2n$.
Ordinary $n$-gons are the trivial examples, [[projective planes|DANFNN8C4Y]] are the generalized $3$-gons, and the [[generalized quadrangles|GQJCPFSYVK]] are the generalized $4$-gons.
Jacques Tits introduced them as the [[buildings|6BQJ50NEJ0]] of rank $2$, and the [[Feit–Higman theorem|P2V0XS4F63]] limits the finite thick ones to $n \in \set{2, 3, 4, 6, 8}$.

## Explanations

### L1 human

Draw a triangle: three points, three sides, each side with two points and each point on two sides.
Make a graph whose vertices are the points and the sides, with an edge when a point lies on a side.
This graph is a cycle of length $6$: any two vertices are at distance at most $3$, and the shortest cycle has length $6 = 2 \cdot 3$.
A generalized $3$-gon keeps these two numbers but allows many more points on each line and many more lines through each point.
That is exactly a projective plane: two points always share a line, and two lines always share a point.
