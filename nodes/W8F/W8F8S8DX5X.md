---
tag: W8F8S8DX5X
kind: concept
name: Tension field
msc: ["58E20", 53C43]
sources:
  - url: https://en.wikipedia.org/wiki/Harmonic_map
---

## Summary

The tension field of a smooth map between [[Riemannian manifolds|7CBT4SM83Y]] is a vector field along the map.
It is the trace of the covariant derivative of the differential of the map.
It generalizes the Laplacian of a function and the acceleration of a curve.
Minus the tension field is the gradient of the [[energy|E6HDE1DFXD]], so a map is [[harmonic|KZJYG9DS3M]] exactly when its tension field vanishes.
The [[harmonic map heat flow|MD99PYBCE6]] moves a map in the direction of its tension field.

## Explanations

### L1 human

The tension field tells, at each point, in which direction the map is pulled if one wants to lower its energy.
For a curve, it is the acceleration as seen from inside the target, the part of the bending that is not forced by the curvature of the target.
For a real function on a domain, it is the Laplacian, which compares the value at a point with the average of nearby values.
For example, the map $t \mapsto (\cos t, \sin t)$ into the plane has tension $(-\cos t, -\sin t)$, pointing inward, but the same circle seen as a map into the unit circle has tension $0$.
