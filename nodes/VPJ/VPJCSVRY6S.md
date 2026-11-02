---
tag: VPJCSVRY6S
kind: concept
name: Associated Legendre polynomials
msc: [33C45, 33C55]
specializes: [69XMERM6KJ]
sources:
  - url: https://en.wikipedia.org/wiki/Associated_Legendre_polynomials
same_as:
  wikidata: Q228376
  wikipedia: Associated Legendre polynomials
---

## Summary

The associated Legendre polynomials $P_\ell^m$ are the [[Legendre functions|69XMERM6KJ]] of integer degree $\ell$ and integer order $m$ on the interval $[-1, 1]$.
They are obtained from the [[Legendre polynomials|QFYGJVA996]] by differentiating $m$ times and multiplying by $(1 - x^2)^{m/2}$.
They give the dependence on the polar angle of the [[spherical harmonics|3F32Y21HP4]] on the sphere in $\R^3$.

## Explanations

### L1 human

Spherical harmonics describe patterns on a sphere, such as the shapes of atomic orbitals.
Each pattern splits into a wave around the equator and a profile from the north pole to the south pole.
The associated Legendre polynomials are these north-to-south profiles.
For example, $P_1^1(\cos \theta) = -\sin \theta$ for $0 \le \theta \le \pi$, a profile that is zero at both poles and largest in size at the equator.
Despite the name, they are not polynomials when $m$ is odd, because of the square root $(1 - x^2)^{1/2}$.
