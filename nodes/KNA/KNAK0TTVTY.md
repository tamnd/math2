---
tag: KNAK0TTVTY
kind: concept
name: Reciprocal lattice
msc: [82D25, 11H06]
sources:
  - url: https://en.wikipedia.org/wiki/Reciprocal_lattice
same_as:
  wikidata: Q164129
  wikipedia: Reciprocal lattice
---

## Summary

Let $\Lambda$ be a [[Bravais lattice|2ASPT0SP6Z]].
Its reciprocal lattice is the set of wave vectors $k$ for which the plane wave $e^{i k \cdot x}$ has every period in $\Lambda$.
It is again a lattice, and it is the dual lattice of $\Lambda$ scaled by $2\pi$.
Functions with the periodicity of the crystal expand as Fourier series over the reciprocal lattice.
In diffraction experiments the sharp peaks occur at points of the reciprocal lattice.

## Explanations

### L1 human

A crystal repeats in space, and a wave that fits the crystal must repeat with it.
The reciprocal lattice lists all wave vectors of such waves.
A long spacing in the crystal gives a short spacing in the reciprocal lattice, and the other way round.
For a chain of atoms at spacing $a$, the waves $e^{ikx}$ that repeat with period $a$ are those with $k$ a multiple of $2\pi/a$.
So the reciprocal lattice of $a\Z$ is $(2\pi/a)\Z$.
