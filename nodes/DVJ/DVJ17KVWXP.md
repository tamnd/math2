---
tag: DVJ17KVWXP
kind: concept
name: Morrey quasiconvexity
msc: [49J45, 26B25]
sources:
  - url: https://en.wikipedia.org/wiki/Quasiconvexity_(calculus_of_variations)
same_as:
  wikidata: Q113635253
  wikipedia: Quasiconvexity (calculus of variations)
---

## Summary

A function $f$ on $m \times n$ matrices is quasiconvex in the sense of Morrey if perturbations with zero boundary values never help.
That is, the average of $f(\xi + \nabla \varphi)$ is never below $f(\xi)$.
Under suitable growth conditions on $f$, it is exactly the condition under which $\int_\Omega f(\nabla u) \, dx$ is weakly lower semicontinuous on Sobolev spaces of vector-valued maps.
It lies between polyconvexity and [[rank-one convexity|GK4P8G0PB2]].
It coincides with convexity when $m = 1$ or $n = 1$.
It is a different notion from the [[quasiconvex functions|S4RMH7JQB8]] of optimisation, which are defined by convex sublevel sets.

## Explanations

### L1 human

Take a linear map with constant gradient $\xi$ on a region, and wiggle it inside while keeping its boundary values.
Quasiconvexity says that the wiggled map always has at least as much energy as the linear one.
So, on average, an affine map is the cheapest way to achieve given affine boundary values.
Convex functions have this property by Jensen's inequality, because the average of $\nabla \varphi$ over the region is zero.
The condition is hard to check in general, because it is not local in $\xi$: it involves all test maps $\varphi$.
