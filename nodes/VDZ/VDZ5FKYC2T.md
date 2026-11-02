---
tag: VDZ5FKYC2T
kind: concept
name: Logarithmic kernel
msc: [31A15]
sources:
  - url: https://en.wikipedia.org/wiki/Fundamental_solution
---

## Summary

The logarithmic kernel is the function $k(z, w) = \log(1/\abs{z - w})$ of two points of the plane.
It is the planar counterpart of the [[Newtonian kernel|6TJTWQ5HCR]].
It equals $2\pi$ times the [[fundamental solution of the Laplacian|BSJ8X2XRN9]] of the plane, translated to the pole $w$.
Integrating it against a measure gives the logarithmic potential, which links potential theory with complex analysis, polynomial approximation and the distribution of zeros of polynomials.
Unlike the Newtonian kernel, it takes negative values when the two points are more than one unit apart.

## Explanations

### L1 human

In the plane, the potential of a point charge does not decay like one over the distance.
It changes like the logarithm of the distance, which grows without bound but very slowly.
The logarithmic kernel is $\log(1/\abs{z - w})$: it is large and positive near $w$, zero on the unit circle around $w$, and negative farther out.
For example, at distance $e$ from the pole its value is $-1$.
