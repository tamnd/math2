---
tag: F79NNVV0B1
kind: concept
name: Mori–Tanaka method
msc: [74Q15, "74E30", 74A60]
specializes: [VSBFY8EN2H]
sources:
  - url: https://en.wikipedia.org/wiki/Effective_medium_approximations
---

## Summary

The Mori–Tanaka method is an [[effective medium approximation|VSBFY8EN2H]] for the stiffness of a composite made of a matrix with embedded inclusions.
It assumes that each inclusion behaves like a single ellipsoidal inclusion in an infinite matrix.
This matrix is loaded by the average strain of the real matrix, not by the applied strain.
The single-inclusion problem is solved by [[Eshelby's inclusion problem|X2N1EA2JGT]], so the method yields explicit formulas.
It is widely used for fibre and particle reinforced materials at moderate volume fractions.

## Explanations

### L1 human

Imagine glass beads in an epoxy resin.
Each bead feels the stretching of the resin around it, and that stretching is already changed by all the other beads.
The Mori–Tanaka method takes this into account in the simplest way.
It puts each bead alone in an infinite block of resin, stretched by the average stretch of the real resin.
For spherical beads in a softer resin, its estimate of the bulk modulus equals the lower [[Hashin–Shtrikman bound|FZGYFV69HK]].
