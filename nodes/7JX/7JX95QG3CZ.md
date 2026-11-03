---
tag: 7JX95QG3CZ
kind: concept
name: Yee lattice
msc: [78M20, 65M06]
sources:
  - url: https://en.wikipedia.org/wiki/Finite-difference_time-domain_method
---

## Summary

The Yee lattice, or Yee cell, is a staggered grid.
The [[finite-difference time-domain method|57XRW2119C]] stores the electromagnetic field on it.
The components of the electric field sit at the midpoints of the edges of a cubic grid.
Those of the magnetic field sit at the centres of its faces.
With this placement every curl in [[Maxwell's equations|9BWWD4QK8Y]] becomes a [[central difference|8HSQHDNFEF]] around a small loop.
The discrete divergence of a discrete curl is then exactly zero, so the scheme keeps Gauss's laws.

## Explanations

### L1 human

Picture a grid of small cubes.
Put one arrow of the electric field on the middle of each edge, pointing along the edge.
Put one arrow of the magnetic field in the middle of each face, pointing across the face.
Then each magnetic arrow is circled by four electric arrows, and each electric arrow by four magnetic arrows, just as Faraday's and Ampère's laws ask.
