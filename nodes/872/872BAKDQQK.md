---
tag: 872BAKDQQK
kind: concept
name: f-vector
msc: [52B05, "05E45"]
sources:
  - url: https://en.wikipedia.org/wiki/Simplicial_complex
---

## Summary

The f-vector of a [[convex polytope|300K6CB1KH]] lists how many faces it has in each dimension.
For a $d$-polytope it is $(f_0, f_1, \dots, f_{d-1})$, where $f_i$ is the number of $i$-dimensional faces.
The same notion applies to [[simplicial complexes|V8GZ0W1ZZ5]], and it is the starting point for the h-vector; see [[f-vector and h-vector|DCK64GFPD7]].
Describing which vectors are f-vectors is a main problem of [[polytope combinatorics|879SBTVE7V]].

## Explanations

### L1 human

Count the corners, edges, faces and so on of a shape, and write the counts in a row.
That row is the f-vector.
A cube gives $(8, 12, 6)$: $8$ corners, $12$ edges and $6$ square faces.
The numbers in an f-vector are not arbitrary; for solids in space the corners minus edges plus faces is always $2$.
