---
tag: KGC5CYDF53
kind: concept
name: Cayley–Menger determinant
msc: [51K05, 51M25]
sources:
  - url: https://en.wikipedia.org/wiki/Cayley%E2%80%93Menger_determinant
same_as:
  wikidata: Q60790093
  wikipedia: Cayley–Menger determinant
---

## Summary

The Cayley–Menger determinant of $n + 1$ points is a [[determinant|00KDZRW4C0]] built only from the squares of their pairwise distances.
Up to a constant factor, it equals the square of the $n$-dimensional volume of the [[simplex|YX1DJK2QAG]] with these points as vertices.
It lets one compute volumes, and test whether given distances fit points of Euclidean space, without coordinates.
[[Heron's formula|0FRBZ2X4HJ]] for the area of a triangle is its case $n = 2$.

## Explanations

### L1 human

If you know the six edge lengths of a tetrahedron, you know its shape, so you should be able to compute its volume.
The Cayley–Menger determinant does exactly this.
Put the squared distances in a table, add a border of ones, and take the determinant.
A suitable constant times this number is the squared volume.
For three points on a line the determinant is zero, since the flat triangle they form has area zero.
