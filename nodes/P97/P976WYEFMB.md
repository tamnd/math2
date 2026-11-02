---
tag: P976WYEFMB
kind: concept
name: Homotopy group
msc: [55Q05]
sources:
  - url: https://en.wikipedia.org/wiki/Homotopy_group
same_as:
  wikidata: Q1626416
  wikipedia: Homotopy group
---

## Summary

The $n$-th homotopy group $\pi_n(X, x_0)$ of a pointed space consists of the homotopy classes of based maps from the $n$-sphere to $(X, x_0)$.
For $n = 1$ it is the [[fundamental group|S1XK3HXHFX]], and for $n \ge 2$ it is abelian.
Homotopy groups are invariants of homotopy type, and on CW complexes they detect homotopy equivalences, by the [[Whitehead theorem|6P1E2FJPSD]].
They are easy to define and very hard to compute, even for spheres.

## Explanations

### L1 human

The group $\pi_n(X)$ records the ways an $n$-dimensional sphere can be placed in a space, where two placements count as the same if one can be deformed into the other.
A balloon inside a solid ball can always be shrunk to a point, so $\pi_2$ of a ball is trivial.
A balloon wrapped once around the surface of a sphere cannot be shrunk on that surface, and $\pi_2(S^2) \cong \Z$ counts how many times it wraps.
