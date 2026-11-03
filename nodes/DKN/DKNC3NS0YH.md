---
tag: DKNC3NS0YH
kind: concept
name: Polyhedral combinatorics
msc: [90C57, 52B05, 90C27]
sources:
  - url: https://en.wikipedia.org/wiki/Polyhedral_combinatorics
same_as:
  wikidata: Q8348314
  wikipedia: Polyhedral combinatorics
---

## Summary

Polyhedral combinatorics studies [[combinatorial optimization|FJPER80BJC]] problems through the [[convex polytopes|300K6CB1KH]] spanned by the incidence vectors of their feasible solutions.
A linear description of such a polytope by inequalities turns the combinatorial problem into a [[linear program|VNMXB0J2KA]], and linear programming duality then yields min-max theorems.
Classical results are the Birkhoff–von Neumann theorem for the assignment polytope and [[Edmonds' matching polytope theorem|K7JT5SBZFX]].
The same name is used for the study of the faces of polytopes, counted by $f$-vectors, which is the subject of [[polytope combinatorics|879SBTVE7V]].

## Explanations

### L1 human

Each feasible solution of a combinatorial problem, such as a matching in a graph, can be written as a vector of zeros and ones.
These vectors are corners of a geometric shape, their convex hull.
If one can describe this shape by a list of linear inequalities, the combinatorial problem becomes a linear program, which is much easier to solve.
For example, the shape whose corners are the $n \times n$ permutation matrices consists exactly of the matrices with nonnegative entries whose rows and columns each add up to $1$.
