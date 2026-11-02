---
tag: BB7S4NTZ6V
kind: concept
name: Bergman metric
msc: [32F45, 32A36]
specializes: [CK1DCPC3D3]
sources:
  - url: https://en.wikipedia.org/wiki/Bergman_metric
same_as:
  wikidata: Q4891698
  wikipedia: Bergman metric
---

## Summary

The Bergman metric of a bounded domain $\Omega \subseteq \C^n$ is the Kähler metric whose potential is the logarithm of the [[Bergman kernel|8RWDHW0CXC]] on the diagonal.
It is defined from the Hilbert space of square-integrable holomorphic functions, the [[Bergman space|2D619WTPYC]].
Hence every biholomorphic map between bounded domains is an isometry for it.
Stefan Bergman introduced it, and on the unit disc it is the hyperbolic metric up to a constant factor.
It is a basic tool for the study of biholomorphic maps, for example in Fefferman's theorem on their boundary extension.

## Explanations

### L1 human

A bounded domain has a natural Hilbert space of holomorphic functions, those whose squared modulus has finite integral.
From this space one builds a kernel $K(z, w)$, and the logarithm of $K(z, z)$ serves as a potential for a Riemannian metric, the Bergman metric.
Because the construction uses only holomorphic functions and the integral, any biholomorphic map carries the metric of one domain to that of the other.
For the unit disc the Bergman metric is $\frac{2 \abs{dz}^2}{(1 - \abs{z}^2)^2}$, a multiple of the hyperbolic metric.
