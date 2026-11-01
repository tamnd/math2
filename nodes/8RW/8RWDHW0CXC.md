---
tag: 8RWDHW0CXC
kind: concept
name: Bergman kernel
msc: [30C40, "46E22", 32A25]
sources:
  - url: https://en.wikipedia.org/wiki/Bergman_kernel
same_as:
  wikidata: Q3345664
  wikipedia: Bergman kernel
---

## Summary

The Bergman kernel of a domain is the reproducing kernel of its [[Bergman space|2D619WTPYC]] $A^2$ of square-integrable [[holomorphic functions|0NAHXR1FRH]].
It is a function $K(z, w)$, holomorphic in $z$ and antiholomorphic in $w$, such that every $f \in A^2$ satisfies $f(w) = \int f(z)\overline{K(z, w)}\, dA(z)$.
For the unit disc it is $K(z, w) = \frac{1}{\pi (1 - z\bar w)^2}$.
It gives the orthogonal projection from $L^2$ onto $A^2$, it transforms simply under biholomorphic maps, and in several variables it defines the Bergman metric.

## Explanations

### L1 human

In the Bergman space, the value of a function at a point is an inner product with one special function attached to that point.
The Bergman kernel collects all these special functions into one formula.
On the unit disc the kernel at the point $w = 0$ is the constant $1/\pi$, which says that $f(0)$ is the average of $f$ over the disc.
The kernel encodes the shape of the domain, which is why it is used to study conformal and biholomorphic maps.
