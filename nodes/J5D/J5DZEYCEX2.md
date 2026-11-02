---
tag: J5DZEYCEX2
kind: concept
name: Barycentric subdivision
msc: [55U10, 57Q05]
sources:
  - url: https://en.wikipedia.org/wiki/Barycentric_subdivision
same_as:
  wikidata: Q4078260
  wikipedia: Barycentric subdivision
---

## Summary

The barycentric subdivision of a [[simplicial complex|V8GZ0W1ZZ5]] cuts every simplex into smaller simplices whose vertices are barycentres of faces.
It does not change the underlying space, but it makes the simplices smaller: repeated subdivision makes their diameters tend to $0$.
This is the key step in the simplicial approximation theorem and in the proof of excision for singular homology.

## Explanations

### L1 human

Take a triangle and mark the midpoint of each edge and the centre of the triangle.
Join the centre to the three corners and the three midpoints.
The triangle is now cut into six smaller triangles, and each small triangle has one corner, one midpoint and the centre as its vertices.
An interval is cut at its midpoint into two halves in the same way.
