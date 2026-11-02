---
tag: GJAYCVYZYF
kind: concept
name: Lattice of subvarieties
msc: [08B15]
sources:
  - url: https://en.wikipedia.org/wiki/Variety_(universal_algebra)
---

## Summary

The lattice of subvarieties of a variety $\mathcal{V}$ is the set of all [[subvarieties|4YSCK1DF26]] of $\mathcal{V}$, ordered by inclusion.
It is a complete lattice, and it is dually isomorphic to the lattice of equational theories that contain the theory of $\mathcal{V}$.
Its shape records how $\mathcal{V}$ can be cut down by further identities, and its study is a large part of the theory of varieties.

## Explanations

### L1 human

Put all the subvarieties of a variety in a diagram, with smaller ones lower down.
The bottom is the trivial variety, of one-element algebras, and the top is the whole variety.
For abelian groups, the subvarieties other than the top are the classes defined by $nx = 0$ for $n \ge 1$.
The class for $n$ lies inside the class for $m$ exactly when $n$ divides $m$.
So this lattice is the divisibility order on the positive integers, with an extra top element.
