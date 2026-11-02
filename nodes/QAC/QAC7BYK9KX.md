---
tag: QAC7BYK9KX
kind: concept
name: Holomorphic line bundle
msc: [32L05, 14C22]
specializes: [TKA958Z4KZ]
sources:
  - url: https://en.wikipedia.org/wiki/Holomorphic_vector_bundle
---

## Summary

A holomorphic line bundle is a [[holomorphic vector bundle|TKA958Z4KZ]] of rank one.
Its transition functions are nowhere vanishing holomorphic functions.
So the isomorphism classes of holomorphic line bundles on a complex manifold $X$ form the [[Picard group|3Z9DCWYXQZ]] $H^1(X, \mathcal{O}_X^*)$ under tensor product.
Line bundles encode divisors, maps to projective space and positivity, as with the [[canonical bundle|W05VYY4HBR]] and the bundles $\mathcal{O}(k)$ on $\mathbb{P}^n$.

## Explanations

### L1 human

A holomorphic line bundle attaches a complex line to each point of a complex manifold, in a holomorphic way.
Locally it is just $U \times \C$, and two local pictures are related by multiplying by a nowhere zero holomorphic function.
A section is then like a holomorphic function, except that its values are only defined up to these gluing factors.
For example, the homogeneous polynomials of degree $k$ in $z_0, z_1$ are not functions on the Riemann sphere, but they are exactly the holomorphic sections of the line bundle $\mathcal{O}(k)$.
