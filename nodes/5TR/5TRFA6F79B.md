---
tag: 5TRFA6F79B
kind: concept
name: Gegenbauer polynomials
msc: [33C45, 33C55]
sources:
  - url: https://en.wikipedia.org/wiki/Gegenbauer_polynomials
same_as:
  wikidata: Q1498246
  wikipedia: Gegenbauer polynomials
---

## Summary

The Gegenbauer polynomials $C_n^{(\lambda)}$, also called ultraspherical polynomials, are orthogonal on $[-1, 1]$ for the weight $(1 - x^2)^{\lambda - 1/2}$.
Up to constant factors they are the [[Jacobi polynomials|TRD7DSF2KR]] with $\alpha = \beta = \lambda - \frac12$.
They generalize the [[Legendre polynomials|QFYGJVA996]] ($\lambda = \frac12$) and give the [[zonal spherical harmonics|Q5D54R3RGE]] on spheres of every dimension at least $2$.

## Explanations

### L1 human

The Legendre polynomials are tied to the ordinary sphere in space.
On a sphere in a space of another dimension, the same role is played by a related family, the Gegenbauer polynomials.
They all come from one formula: expand $(1 - 2xt + t^2)^{-\lambda}$ in powers of $t$, and the coefficients are the $C_n^{(\lambda)}(x)$.
For $\lambda = \frac12$ this is the generating function of the Legendre polynomials.
