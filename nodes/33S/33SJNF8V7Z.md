---
tag: 33SJNF8V7Z
kind: concept
name: Mortar methods
msc: [65N30, 65N55]
sources:
  - url: https://en.wikipedia.org/wiki/Mortar_methods
same_as:
  wikidata: Q17099078
  wikipedia: Mortar methods
---

## Summary

Mortar methods are finite element discretizations on a domain cut into subdomains whose meshes need not match across the interfaces.
Continuity across an interface is not imposed point by point but weakly.
The jump must be orthogonal to a space of multiplier functions, the mortar space.
They let each subdomain use its own mesh and polynomial degree while keeping optimal error estimates.
This makes them a standard tool of [[domain decomposition methods|AN054RHT1K]].

## Explanations

### L1 human

Imagine two brick walls built by different masons with bricks of different sizes, which must meet along a seam.
The bricks do not line up, so the mortar between them has to absorb the mismatch.
A mortar method does the same with meshes: two regions are meshed independently, and along their common edge the two sides are glued "on average" rather than at every node.
For example, a fine mesh around a corner singularity can meet a coarse mesh elsewhere without any transition layer.
