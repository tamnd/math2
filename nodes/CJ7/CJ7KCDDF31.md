---
tag: CJ7KCDDF31
kind: statement
role: theorem
name: Cauchy's rigidity theorem
msc: [52B10, 52C25, 51M20]
uses: [0325SGSJAR, 02AS45T3H9, 02HPP5VCZH]
about: [0325SGSJAR, V5YS9BZX0N]
sources:
  - url: https://en.wikipedia.org/wiki/Cauchy%27s_theorem_(geometry)
same_as:
  wikidata: Q3527034
  wikipedia: Cauchy's theorem (geometry)
---

## Statement

Let $P$ and $P'$ be convex [[polyhedra|0325SGSJAR]] in $\R^3$.
Suppose there is a bijection between their faces that preserves the incidences of faces, edges and vertices.
Suppose also that each face of $P$ is congruent to the corresponding face of $P'$.
Then there is an [[isometry|02HPP5VCZH]] of $\R^3$ that maps $P$ onto $P'$.

## Remarks

The proof compares the dihedral angles at corresponding edges and marks each edge $+$, $-$ or $0$ according to the change.
Cauchy's arm lemma shows that around each vertex with a marked edge, the signs change at least four times.
A count of sign changes with Euler's formula $V - E + F = 2$ then shows that no edge can be marked, so all dihedral angles agree.
Cauchy's original proof of the arm lemma had a gap, which was later repaired.

Convexity is needed.
Take a convex polyhedron with a vertex whose neighbours all lie in one plane.
Reflect the small pyramid at that vertex inward through that plane.
The new nonconvex polyhedron has the same combinatorics and congruent faces, but it is not congruent to the old one.
Flexible polyhedra show that even a single nonconvex polyhedron can deform continuously with rigid faces.

## Explanations

### L1 human

Make a convex solid from rigid cardboard faces joined by hinges at the edges.
Cauchy's theorem says the solid cannot wobble: the faces alone fix its whole shape.
In particular, a convex polyhedron is determined by its net of faces and the way they are glued.

### L2 human

The theorem is a statement of global rigidity for convex polyhedral surfaces among all convex realizations.
It implies that a convex polyhedron cannot be deformed continuously with rigid faces.
Dehn later proved the stronger infinitesimal rigidity of convex polyhedra.
For nonconvex polyhedra rigidity can fail, as Connelly's flexible polyhedron shows, but the bellows conjecture says the volume is still preserved.
