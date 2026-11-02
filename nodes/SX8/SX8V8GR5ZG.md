---
tag: SX8V8GR5ZG
kind: concept
name: Cartan–Eilenberg resolution
msc: [18G10, 18G35]
specializes: [N80ABTQHEQ]
sources:
  - url: https://en.wikipedia.org/wiki/Cartan%E2%80%93Eilenberg_resolution
same_as:
  wikidata: Q5047047
  wikipedia: Cartan–Eilenberg resolution
---

## Summary

A Cartan–Eilenberg resolution of a chain complex $C$ is a [[double complex|N80ABTQHEQ]] of projective objects.
It resolves not only each term of $C$ but also its boundaries, cycles and homology, all at once.
It is the tool for defining derived functors of complexes, called hyperderived functors.
It is also the main step in the proof of the [[Grothendieck spectral sequence|ZV7VGE2SQ2]].

## Explanations

### L1 human

A projective resolution replaces one object by a chain of simple objects.
For a whole chain complex one wants to do this term by term, but in a way that respects the structure of the complex.
A Cartan–Eilenberg resolution is a grid of projective objects, and each column resolves one term of the complex.
The rows are arranged so that the homology of the complex is resolved as well.
For a complex with a single nonzero term $M$, it is just a projective resolution of $M$ placed in one column.
