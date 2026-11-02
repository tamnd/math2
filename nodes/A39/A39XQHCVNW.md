---
tag: A39XQHCVNW
kind: concept
name: Proj construction
msc: [14A15, 13A02]
sources:
  - url: https://en.wikipedia.org/wiki/Proj_construction
same_as:
  wikidata: Q7248935
  wikipedia: Proj construction
---

## Summary

The Proj construction makes a [[scheme|5A35TYZD02]] $\operatorname{Proj} S$ out of a [[graded ring|8KB4SQGC0C]] $S$.
Its points are the homogeneous prime ideals that do not contain all elements of positive degree.
It plays for projective geometry the role that $\operatorname{Spec}$ plays for affine geometry: $\operatorname{Proj}$ of a polynomial ring is projective space.

## Explanations

### L1 human

A point of projective space is given by coordinates $[x_0 : \cdots : x_n]$ that matter only up to a common factor.
So only homogeneous polynomials, whose zero sets do not depend on the factor, make sense on projective space.
The Proj construction turns this into algebra: it uses the homogeneous prime ideals of a graded ring.
It is covered by affine pieces, one for each homogeneous element $f$ of positive degree, on which $f \ne 0$.
For $S = k[x_0, \ldots, x_n]$ and $f = x_0$, that piece is the affine space with coordinates $x_1/x_0, \ldots, x_n/x_0$.
