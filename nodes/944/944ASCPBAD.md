---
tag: 944ASCPBAD
kind: concept
name: Geopotential model in spherical harmonics
msc: [86A20, 33C55, 86A30]
sources:
  - url: https://en.wikipedia.org/wiki/Geopotential_spherical_harmonic_model
same_as:
  wikidata: Q5535591
  wikipedia: Geopotential spherical harmonic model
---

## Summary

A geopotential model expands the gravitational potential of the Earth in [[spherical harmonics|3F32Y21HP4]].
Outside the Earth the potential is a [[harmonic function|0DEB0JMN0W]] that tends to $0$ at infinity.
So it is a series of terms $r^{-n-1}$ times surface spherical harmonics of degree $n$.
The model is a table of coefficients $\bar C_{nm}, \bar S_{nm}$, estimated from satellite orbits and gravity data.
The largest term after the central one is $J_2$, which describes the Earth's flattening.

## Explanations

### L1 human

Seen from far away, the Earth pulls like a point mass, and the potential is just $GM/r$.
Closer up, the bulge at the equator and the uneven mass inside add small corrections.
Spherical harmonics are wave patterns on the sphere, and the corrections are sums of such patterns, finer and finer as the degree grows.
A modern model has thousands of degrees, describing details of about ten kilometres.
The first correction, from the equatorial bulge, is about a thousand times smaller than the main term.
