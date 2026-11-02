---
tag: 811NW2WEJH
kind: problem
name: Hauptvermutung
msc: [57Q25, 57Q15]
uses: [V8GZ0W1ZZ5, 0QT00PB5G2, YH170WBQ6M, C9X05EDS5F, SV0816DJP9, E4NJER1RFQ]
about: [YH170WBQ6M]
sources:
  - url: https://en.wikipedia.org/wiki/Hauptvermutung
same_as:
  wikidata: Q5682772
  wikipedia: Hauptvermutung
history:
  posed_by: "Ernst Steinitz and Heinrich Tietze"
  first_stated: "1908"
---

## Problem

Let $K$ and $L$ be [[simplicial complexes|V8GZ0W1ZZ5]] whose geometric realizations $\abs{K}$ and $\abs{L}$ are [[homeomorphic|0QT00PB5G2]].
Do $K$ and $L$ always have subdivisions $K'$ and $L'$ that are isomorphic as simplicial complexes?

Equivalently: are any two [[triangulations|YH170WBQ6M]] of the same space related by a piecewise linear homeomorphism?

## Remarks

The name is German for "main conjecture".
A positive answer would make the combinatorial invariants of a triangulation, such as simplicial homology, automatically topological invariants; homology was later shown to be a topological invariant by other means.
The answer is yes for complexes of dimension at most $2$, and for $3$-manifolds by [[Moise's theorem|SV0816DJP9]]; for surfaces it goes with [[Radó's theorem|C9X05EDS5F]].
The answer is no in general: John Milnor gave counterexamples in 1961 among finite simplicial complexes that are not manifolds.
For manifolds the answer is also no.
In dimensions at least $5$, the theory behind the [[Kirby–Siebenmann class|E4NJER1RFQ]] gives topological manifolds with several PL structures.
The corresponding triangulations are not related by any piecewise linear homeomorphism.

## Explanations

### L1 human

The same shape can be cut into triangles, or into higher-dimensional simplices, in many ways.
The question is whether any two such cuttings can be refined until they become the same cutting.
For shapes of dimension up to three this works, but in higher dimensions there are shapes where it fails.
