---
tag: GGDSF85JPD
kind: concept
name: Partial isometry
msc: [47B02, 47A05]
sources:
  - url: https://en.wikipedia.org/wiki/Partial_isometry
same_as:
  wikidata: Q904849
  wikipedia: Partial isometry
---

## Summary

A partial isometry is a bounded operator on a Hilbert space that is isometric on the orthogonal complement of its kernel.
It maps an initial subspace isometrically onto a final subspace and kills everything orthogonal to the initial subspace.
Partial isometries appear in the [[polar decomposition|0J2C7BDJQA]] $T = V\abs{T}$ of an operator and in the comparison of projections in von Neumann algebras.

## Explanations

### L1 human

A partial isometry first throws away part of a vector and then moves the rest rigidly.
On $\C^2$, the map $(x_1, x_2) \mapsto (0, x_1)$ is an example: it forgets $x_2$ and moves $x_1$ to the second slot without changing its size.
Isometries, unitary operators and orthogonal projections are all partial isometries.
