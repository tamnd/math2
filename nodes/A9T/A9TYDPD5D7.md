---
tag: A9TYDPD5D7
kind: concept
name: Thom–Boardman singularities
msc: [57R45, 58K30, 58K05]
specializes: [1JG3HFWX3T]
sources:
  - url: https://en.wikipedia.org/wiki/Singularity_theory
---

## Summary

The Thom–Boardman singularities sort the [[singular points|1JG3HFWX3T]] of a smooth map by a sequence of numbers $(i_1, i_2, \ldots)$.
The first number is the dimension of the kernel of the differential.
The second is the same dimension for the restriction of the map to the set of points with that first number, and so on.
Thom introduced the first steps, and Boardman made the construction work in general by defining the corresponding subsets of jet space.
For a generic map the sets $\Sigma^{i_1, i_2, \ldots}(f)$ are submanifolds of known codimension, and they give a first coarse classification of singularities.

## Explanations

### L1 human

For a typical map between manifolds, first look at how many directions the map crushes at each point; that number is $i_1$.
The points where exactly $i_1$ directions are crushed form a curve, a surface, or some other smaller manifold.
Now restrict the map to this smaller manifold and ask again how many directions it crushes there; that number is $i_2$.
For a map of the plane to the plane, a fold point has symbol $(1, 0)$: one direction is crushed, but the map is regular along the fold curve.
A cusp point has symbol $(1, 1, 0)$: the map also crushes the direction along the fold curve at that point.
