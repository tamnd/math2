---
tag: G6GMSEZDB1
kind: concept
name: Affine group
msc: [51N10, 20H15, 15A04]
sources:
  - url: https://en.wikipedia.org/wiki/Affine_group
same_as:
  wikidata: Q686291
  wikipedia: Affine group
---

## Summary

The affine group of an [[affine space|09XNAPTJQ7]] is the group of all its invertible [[affine maps|0JF0TVYGWT]].
On $F^n$ these are the maps $x \mapsto Ax + b$ with $A$ an invertible matrix and $b$ a vector.
It is the [[semidirect product|0H3WZXCZNF]] of the [[translations|087VJM5Q77]] and the [[general linear group|0FCHE902D7]].
In the [[Erlangen program|9QW65PGEPW]], it is the group that defines affine geometry.

## Explanations

### L1 human

An affine map moves the plane so that straight lines stay straight and parallel lines stay parallel.
It may stretch, shear, rotate, reflect and shift, but it may not bend.
For example, $(x, y) \mapsto (2x + y + 1, \, y - 3)$ is an invertible affine map of the plane.
The affine group collects all such maps, with composition as the operation.
