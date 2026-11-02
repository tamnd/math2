---
tag: 6P5MCRDD9Q
kind: concept
name: Discontinuous Galerkin method
msc: [65M60, 65N30, 35L65]
specializes: [Y5B0PEBKE8]
sources:
  - url: https://en.wikipedia.org/wiki/Discontinuous_Galerkin_method
same_as:
  wikidata: Q428273
  wikipedia: Discontinuous Galerkin method
---

## Summary

A discontinuous Galerkin method is a [[Galerkin method|Y5B0PEBKE8]] whose trial and test functions are polynomials on each element of a mesh.
No continuity is required between elements.
Elements are coupled only through numerical fluxes on their common faces, as in a [[finite volume method|HGKN8E09RS]].
It combines the high order of [[finite element methods|98GZ9DVHTA]] with the local conservation and upwinding of finite volume schemes.
It was introduced by Reed and Hill for the neutron transport equation, and is widely used for [[conservation laws|8RA7AMWSAF]].
See the [[definition|J332CQ8SPB]].

## Explanations

### L1 human

Cut the domain into pieces and, on each piece, approximate the solution by its own polynomial.
The polynomials of neighbouring pieces need not agree at the boundary, so the approximation may jump there.
The pieces talk to each other only through a flux at their common boundary, chosen so that what leaves one piece enters the next.
With polynomials of degree zero, each piece holds one number, and the method is a finite volume scheme.
