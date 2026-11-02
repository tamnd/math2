---
tag: VEB7J3C74F
kind: concept
name: Clenshaw–Curtis quadrature
msc: [65D32, 41A55]
specializes: [ADSVMCY77A]
sources:
  - url: https://en.wikipedia.org/wiki/Clenshaw–Curtis_quadrature
same_as:
  wikidata: Q5131618
  wikipedia: Clenshaw–Curtis quadrature
---

## Summary

Clenshaw–Curtis quadrature integrates a function on $[-1, 1]$ by interpolating it at the points $\cos(k\pi/N)$ and integrating the interpolating polynomial exactly.
The substitution $x = \cos\theta$ turns the problem into a cosine series, so the weights can be computed fast with the discrete cosine transform.
Its nodes for $N$ are contained in its nodes for $2N$, so doubling $N$ reuses all earlier function values.
For many smooth functions it is about as accurate as [[Gauss–Legendre quadrature|RGGXDRCJVE]] with the same number of points.

## Explanations

### L1 human

Sample the function at points that are the shadows on the $x$-axis of equally spaced points on a half circle.
These points crowd towards the ends of the interval, which avoids the wild oscillations of interpolation at equally spaced points.
Fit the polynomial through the samples and integrate that polynomial exactly.
For example, with $N = 2$ the points are $-1, 0, 1$, and the result is [[Simpson's rule|MNXC26G3BQ]].
