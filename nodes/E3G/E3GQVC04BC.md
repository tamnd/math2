---
tag: E3GQVC04BC
kind: concept
name: Fréchet mean
msc: [62R20, 62R30]
sources:
  - url: https://en.wikipedia.org/wiki/Fréchet_mean
same_as:
  wikidata: Q5506662
  wikipedia: Fréchet mean
---

## Summary

The Fréchet mean generalises the average to data in a [[metric space|0VKD1TP7F3]]: it is a point that minimises the expected squared distance to the data.
In Euclidean space it is the usual mean.
It also makes sense for points on a sphere, on a [[Riemannian manifold|7CBT4SM83Y]], or in spaces of trees, shapes or covariance matrices.
In these spaces adding and dividing points is not defined.
It need not exist or be unique, and the conditions for uniqueness involve the curvature of the space.
It is named after Maurice Fréchet; local minimisers on Riemannian manifolds are also called Karcher means.

## Explanations

### L1 human

To average two cities on the globe, you cannot average their coordinates in 3D space, since the result lies inside the Earth.
Instead, look for the place on the surface that minimises the sum of squared distances, measured along the surface, to the two cities.
That place is the midpoint of the shortest route between them.
The same recipe works for averaging directions, rotations or shapes.
For two exactly opposite points on a sphere, every point of the great circle halfway between them is a Fréchet mean, so the mean is not unique.
