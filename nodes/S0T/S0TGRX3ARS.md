---
tag: S0TGRX3ARS
kind: concept
name: Dehn invariant
msc: [52B45, 51M20]
sources:
  - url: https://en.wikipedia.org/wiki/Dehn_invariant
same_as:
  wikidata: Q30587580
  wikipedia: Dehn invariant
---

## Summary

The Dehn invariant of a [[polyhedron|0325SGSJAR]] combines the lengths of its edges with their [[dihedral angles|05HN08ZSRJ]] in a tensor product of abelian groups.
It does not change when a polyhedron is cut into pieces and the pieces are reassembled.
Max Dehn used it in 1900 to solve [[Hilbert's third problem|81035XQ5HE]].
A cube and a regular tetrahedron of the same volume have different Dehn invariants, so neither can be cut into the other.

## Explanations

### L1 human

When you cut a solid into pieces, new edges appear.
Around a new edge inside the solid, the angles of the pieces add up to a full turn or a half turn.
The Dehn invariant adds up "edge length times angle" over all edges, but counts angles only up to rational multiples of $\pi$.
With this rule the new edges contribute nothing.
A cube has only right angles, which are rational multiples of $\pi$, so its invariant is $0$.
A regular tetrahedron has the angle $\arccos(1/3)$, which is not, so its invariant is not $0$.
