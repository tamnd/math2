---
tag: VDF7CGPC0P
kind: concept
name: Geometric lattice
msc: [06C10, 05B35]
specializes: [C1NET23GG0]
sources:
  - url: https://en.wikipedia.org/wiki/Geometric_lattice
same_as:
  wikidata: Q5535493
  wikipedia: Geometric lattice
---

## Summary

A geometric lattice is a finite lattice that is [[atomistic|99DVVV7BH2]] and [[semimodular|C1NET23GG0]].
These lattices are exactly the lattices of flats of finite [[matroids|PX31ZNYS3Z]].
So they give an order-theoretic description of matroids, in which the atoms are the points and the rank function measures dimension.
Lattices of subspaces of a finite vector space, Boolean lattices of subsets of a finite set and lattices of partitions are geometric.

## Explanations

### L1 human

Take finitely many points in space and consider the "flats" they span: the points, the lines through two of them, the planes through three, and so on.
Ordered by inclusion, these flats form a geometric lattice.
Every flat is the join of the points it contains, and joining one more point raises the dimension by at most one.
For three points in general position in the plane, the lattice has the empty flat, three points, three lines and the whole plane.
