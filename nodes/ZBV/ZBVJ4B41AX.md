---
tag: ZBVJ4B41AX
kind: counterexample
name: Hirsch conjecture
msc: [52B05, 90C05, 52B11]
uses: [300K6CB1KH, DPDXN2FJC4, 0QV9VNNB4Z, VNMXB0J2KA]
sources:
  - url: https://en.wikipedia.org/wiki/Hirsch_conjecture
same_as:
  wikidata: Q2993326
  wikipedia: Hirsch conjecture
---

## Counterexample

For a [[convex polytope|300K6CB1KH]] $P$, the graph of $P$ has the vertices of $P$ as vertices and the edges of $P$ as edges.
The diameter of $P$ is the largest [[distance|0QV9VNNB4Z]] in this graph between two vertices.
The Hirsch conjecture asserted: if $d \ge 2$ and $P$ is a $d$-dimensional polytope with $n$ [[facets|DPDXN2FJC4]], then the diameter of $P$ is at most $n - d$.
The conjecture is false: in 2010 Francisco Santos constructed a $43$-dimensional polytope with $86$ facets whose diameter is at least $44$, while $n - d = 43$.

## Remarks

Santos's construction first builds a spindle: a polytope with two special vertices whose distance exceeds the dimension.
A known reduction, which adds facets and dimensions in step, then turns it into a counterexample.
For unbounded polyhedra the analogous statement had already been disproved by Victor Klee and David Walkup in 1967.
The bound $n - d$ is attained by the $d$-cubes, which have $n = 2d$ facets and diameter $d$.

The question matters for [[linear programming|VNMXB0J2KA]], since the simplex method walks along edges of the feasible polytope.
So the diameter bounds from below the worst number of steps of any edge-following pivot rule.
Whether the diameter is bounded by a polynomial in $n$ and $d$ remains open.
The best general bound known is quasi-polynomial, of the form $n^{\log_2 d + 2}$, due to Gil Kalai and Daniel Kleitman.

## Explanations

### L1 human

Walk from corner to corner along the edges of a polytope.
The Hirsch conjecture claimed that any two corners are joined by a short walk: at most the number of walls minus the dimension.
For half a century nobody could prove or refute it.
Santos found a polytope in $43$ dimensions where some walk must be longer, so the conjecture is false, though only by a little.
