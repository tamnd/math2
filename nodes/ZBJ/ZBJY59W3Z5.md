---
tag: ZBJY59W3Z5
kind: concept
name: Lattice gauge theory
msc: [81T25, 81T13, 82B20]
specializes: [2GKJQNQMVN]
sources:
  - url: https://en.wikipedia.org/wiki/Lattice_gauge_theory
same_as:
  wikidata: Q386769
  wikipedia: Lattice gauge theory
---

## Summary

Lattice gauge theory replaces spacetime by a grid of points and puts the gauge field on the edges of the grid.
Each edge carries a group element that describes [[parallel transport|TVAGN3D6W5]] from one point to the next.
Kenneth Wilson introduced it in 1974 to study the confinement of quarks.
The theory is a finite-dimensional integral over copies of a compact group, so it is mathematically well defined, and it is exactly gauge invariant.
Physicists compute low-energy properties of [[quantum chromodynamics|SEE8XD0APW]] through its continuum limit, as the lattice spacing goes to $0$.
Making that limit rigorous is a central open problem.

## Explanations

### L1 human

Instead of a field at every point of space and time, one keeps only a field on a fine checkerboard of points.
Between two neighbouring points one stores a small rotation, which says how to compare the internal state at one point with the internal state at the next.
Going around a small square of the grid and composing the four rotations gives the field strength in that square.
The theory weighs each configuration by how close these square loops are to doing nothing, and computers then average over random configurations.
Such simulations have computed the masses of the proton and other hadrons from first principles.
