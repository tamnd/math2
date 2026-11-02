---
tag: 1BCJ7A73KS
kind: concept
name: Euclidean distance matrix
msc: [51K05, 15B48]
sources:
  - url: https://en.wikipedia.org/wiki/Euclidean_distance_matrix
same_as:
  wikidata: Q5406122
  wikipedia: Euclidean distance matrix
---

## Summary

A Euclidean distance matrix is a square matrix whose entries are the squared distances between some points of a Euclidean space.
It records the whole shape of a finite point set up to isometry.
[[Schoenberg's criterion|4B0R70F4VE]] recognizes these matrices through a [[positive semidefinite|01MMVW8CKC]] condition, which links [[distance geometry|HPW5F0GQ4B]] with linear algebra.
They are used in multidimensional scaling, molecular conformation and sensor localization.

## Explanations

### L1 human

Take a few points, number them, and write the square of the distance from point $i$ to point $j$ in row $i$ and column $j$.
The table you get is a Euclidean distance matrix.
It is symmetric with zeros on the diagonal.
For the points $0$, $1$ and $3$ on a line, the table has rows $(0, 1, 9)$, $(1, 0, 4)$ and $(9, 4, 0)$.
The hard question is the reverse one: given such a table, do points exist that produce it?
