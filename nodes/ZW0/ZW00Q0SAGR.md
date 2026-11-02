---
tag: ZW00Q0SAGR
kind: concept
name: Kodaira dimension
msc: ["14E30", 14J10]
sources:
  - url: https://en.wikipedia.org/wiki/Kodaira_dimension
same_as:
  wikidata: Q6425087
  wikipedia: Kodaira dimension
---

## Summary

The Kodaira dimension of a smooth projective variety measures how fast the spaces of sections of the powers of its [[canonical bundle|W05VYY4HBR]] grow.
It takes one of the values $-\infty, 0, 1, \dots, n$, where $n$ is the dimension of the variety.
It is a birational invariant, and it is the first coarse invariant in the classification of varieties, as in the [[Enriques–Kodaira classification|1GVF19KFAK]] of surfaces.
Varieties of maximal Kodaira dimension are said to be of general type.

## Explanations

### L1 human

The canonical bundle of a variety is built from its top-degree differential forms.
Count how many independent sections the $m$-th power of this bundle has, and watch how this number grows with $m$.
If it is always zero, the Kodaira dimension is $-\infty$; if it grows like $m^\kappa$, the Kodaira dimension is $\kappa$.
For curves, this gives three classes: the projective line has $-\infty$, elliptic curves have $0$, and curves of genus at least $2$ have $1$.
These three classes match the three geometries: spherical, flat and hyperbolic.
