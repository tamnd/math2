---
tag: G0XVRV6QT5
kind: concept
name: Barycentric coordinates
msc: [51N10, 51A05]
sources:
  - url: https://en.wikipedia.org/wiki/Barycentric_coordinate_system
same_as:
  wikidata: Q738422
  wikipedia: Barycentric coordinate system
---

## Summary

Barycentric coordinates describe a point of an [[affine space|09XNAPTJQ7]] by weights attached to the vertices of a fixed reference simplex.
The weights add up to $1$, and the point is the [[affine combination|0KJH6SRFZK]] of the vertices with these weights.
They need no origin and no basis, so they are the natural coordinates of affine geometry.
They are widely used for triangles, in computer graphics, and in finite element methods.

## Explanations

### L1 human

Put masses on the three corners of a triangle; their balance point is a point of the plane.
The masses, scaled so that they add up to $1$, are the barycentric coordinates of that point.
The centroid gets the equal weights $(1/3, 1/3, 1/3)$, and each corner gets weight $1$ on itself and $0$ on the others.
A point lies inside the triangle exactly when all three weights are positive.
Negative weights are allowed and give the points outside the triangle.
