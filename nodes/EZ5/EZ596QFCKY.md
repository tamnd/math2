---
tag: EZ596QFCKY
kind: concept
name: Multidimensional scaling
msc: [62H25, 62H30]
sources:
  - url: https://en.wikipedia.org/wiki/Multidimensional_scaling
same_as:
  wikidata: Q620538
  wikipedia: Multidimensional scaling
---

## Summary

Multidimensional scaling places objects as points in a low-dimensional space so that their distances match given dissimilarities as well as possible.
Its input is only a table of pairwise dissimilarities, not coordinates.
Classical multidimensional scaling does this exactly when the dissimilarities are [[Euclidean distances|0NPPGHQNXQ]], using the [[eigenvectors|0N6960W0BV]] of a centred matrix.
It is used to visualise similarity data in two or three dimensions.

## Explanations

### L1 human

Given only the road distances between cities, one can try to redraw the map.
Multidimensional scaling does exactly this: it finds points in the plane whose distances are close to the given ones.
The map comes out correct up to shifting, turning and mirroring, since these do not change distances.
For three points with distances $1$, $1$ and $2$, it puts them on a line at $-1$, $0$ and $1$.
